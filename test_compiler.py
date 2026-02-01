import os
import signal
import subprocess
from pathlib import Path
import sys
from types import FunctionType
import re

# ==== Compilation ====

OWN_COMPILE_CMD = (
    'java -cp antlr-4.13.2-complete.jar:. StupsCompiler -compile "{test_case}"'
)
FPC_COMPILE_CMD = 'fpc "{test_case}"'
JASMIN_COMPILE_CMD = 'java -jar jasmin.jar -d "{dir}" "{jasmin_file_path}"'

LIVENESS_CMD = (
    'java -cp antlr-4.13.2-complete.jar:. StupsCompiler -liveness "{test_case}"'
)

# ==== Directories ====

COMPILATION_TEST_DIR = Path("./test/")
"""Der Ordner, in dem die Test Cases liegen. Auch Unterordner werden betrachtet."""

COPY_TO = Path("./test/_build/sample.pas")
"""
Die .pas Datei wird in einen Kompilierungs-Ordner kopiert und dort kompiliert. 

Auf `None` setzen, um das auszuschalten
"""

EXCLUDE_FILES = [
    r"_.*",  # fängt mit "_" an
    r"-.*",  # fängt mit "-" an
    r"^(?!.*\.pas$).*$",  # hört nicht mit ".pas" auf
]
EXCLUDE_FOLDERS = [
    r"_.*",  # fängt mit "_" an
    r"-.*",  # fängt mit "-" an
]

LIVENESS_TEST_DIR = Path("./test/liveness")
"""Der Ordner, in dem die Liveness Test Cases liegen. Auch Unterordner werden betrachtet."""


# === Miscellaneous ===

DELETE_GENERATED_FILES_WHEN_RUNNING_ALL = True
DELETE_GENERATED_FILES_WHEN_RUNNING_ONE = True

# ==== Formatting =====

INDENT_SPACES = 2


# ansi color codes
RESET = "\033[0m"
DIM = "\033[2m"
BRIGHT = "\033[1m"
YELLOW = "\033[33m"
RED = "\033[31m"
GREEN = "\033[32m"


def frame(
    string: str, frame_char: str, format_inner: FunctionType = lambda x: x
) -> str:
    length = len(string)
    return (
        frame_char * length + "\n" + format_inner(string) + "\n" + frame_char * length
    )


def fmt_dim(string: str) -> str:
    return f"{DIM}{string}{RESET}"


def fmt_wrn(string: str) -> str:
    return f"{YELLOW}{BRIGHT}{string}{RESET}"


def fmt_err(string: str) -> str:
    return f"{RED}{BRIGHT}{string}{RESET}"


def fmt_suc(string: str) -> str:
    return f"{GREEN}{BRIGHT}{string}{RESET}"


def success_str(success: bool) -> str:
    if success:
        return fmt_suc("SUCCESS")
    return fmt_err("FAILED")


def indent(string: str, amount: int = 1) -> str:
    lines = []
    for line in string.splitlines():
        if line.strip() != "":
            lines.append(INDENT_SPACES * amount * " " + line + "")
        else:
            lines.append("")
    return "\n".join(lines)


class TestDetails:
    file_path: Path
    fpc_comp_out: str
    fpc_comp_success: bool
    own_comp_out: str
    own_comp_success: bool
    fpc_result_out: str
    own_result_out: str
    compilation_output: bool
    execution_output: bool

    def __init__(
        self, file_path: Path, compilation_output: bool, execution_output: bool
    ) -> None:
        self.file_path = file_path
        self.compilation_output = compilation_output
        self.execution_output = execution_output


def print_test_result(details: TestDetails, test_success: bool, test_message: str = ""):
    if details.compilation_output:
        print(
            f"⚙ fpc compilation ({success_str(details.fpc_comp_success)}):\n\n{indent(details.fpc_comp_out)}\n"
        )
        print(
            f"⚙ own compilation ({success_str(details.own_comp_success)}):\n\n{indent(details.own_comp_out)}\n",
        )
    if details.execution_output:
        print(f"‣ expected output:\n{indent(details.fpc_result_out)}\n")
        print(f"‣ actual output:\n{indent(details.own_result_out)}\n")
    if not details.compilation_output and not details.execution_output:
        if test_success:
            print(indent(f"{fmt_suc("test passed ✔")}  {fmt_dim(test_message)}"))
        else:
            print(indent(f"{fmt_err("test failed ✘")}  {fmt_dim(test_message)}"))
    else:
        if test_success:
            print(f"{fmt_suc("✔ test passed")}  {fmt_dim(test_message)}")
        else:
            print(f"{fmt_err("✘ test failed")}  {fmt_dim(test_message)}")


def assert_file_exists(file_path: Path) -> bool:
    if not file_path.exists():
        print(fmt_err(f"file {file_path} does not exist"))
        return False
    if not file_path.is_file():
        print(fmt_err(f"{file_path} is not a file"))
        return False
    return True


def test_compilation(
    file_path: Path,
    test_path: Path,
    compilation_output=True,
    execution_output=True,
    delete_gen_files=DELETE_GENERATED_FILES_WHEN_RUNNING_ONE,
) -> bool:
    if not assert_file_exists(file_path):
        return True

    if test_path is None:
        test_path = file_path

    class_name = file_path.name.removesuffix(".pas").title()
    # read class name from file
    with open(file_path, "r") as f:
        content = f.read()
        matches = re.search(r".*program +([a-zA-Z_][a-zA-Z0-9_]*);.*", content)
        if matches != None:
            class_name = matches.group(1)

    details = TestDetails(file_path, compilation_output, execution_output)
    print(f"▪ testing {details.file_path}")

    if file_path != test_path:
        os.system(f'cp "{file_path}" "{test_path}"')

    # compile with fpc
    details.fpc_comp_success = True
    try:
        details.fpc_comp_out = subprocess.check_output(
            FPC_COMPILE_CMD.replace("{test_case}", str(test_path)),
            shell=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        details.fpc_comp_out = e.output
        details.fpc_comp_success = False
    except UnicodeDecodeError as e:
        details.fpc_comp_out = str(e)

    if "invalid continuation byte" in details.fpc_comp_out:
        details.fpc_comp_success = False

    folder_hint = None
    if "shouldPass" in str(file_path.absolute()):
        folder_hint = True
    if "shouldFail" in str(file_path.absolute()):
        folder_hint = False
    if folder_hint is not None and folder_hint != details.fpc_comp_success:
        print(fmt_wrn(f"file {file_path} is in the wrong folder"))

    # compile with own compiler
    details.own_comp_success = True
    try:
        details.own_comp_out = subprocess.check_output(
            OWN_COMPILE_CMD.replace("{test_case}", str(test_path)),
            stderr=subprocess.STDOUT,
            shell=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        details.own_comp_out = e.output
        details.own_comp_success = False
    except UnicodeDecodeError as e:
        details.fpc_comp_out = str(e)
    if details.own_comp_success:
        jasmin_file_path = test_path.parent / (
            test_path.name.removesuffix(".pas") + ".j"
        )
        jasmin_comp_out = subprocess.check_output(
            JASMIN_COMPILE_CMD.replace("{dir}", str(test_path.parent)).replace(
                "{jasmin_file_path}", str(jasmin_file_path)
            ),
            stderr=subprocess.STDOUT,
            shell=True,
            text=True,
        )
        jasmin_comp_out = jasmin_comp_out.replace("Warning", fmt_wrn("Warning"))
        jasmin_comp_out = jasmin_comp_out.replace("Error", fmt_err("Error"))
        details.own_comp_out += "\n" + re.sub(
            r"(Found [0-9]+ errors?])", fmt_err("\\1"), jasmin_comp_out
        )
        if "Error" in jasmin_comp_out:
            details.own_comp_success = False

    fpc_timeout = False
    if details.fpc_comp_success:
        fpc_file_path = test_path.parent / test_path.name.removesuffix(".pas")
        proc = subprocess.Popen(
            [str(fpc_file_path)],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
        )
        try:
            details.fpc_result_out, _ = proc.communicate(timeout=1)
        except subprocess.TimeoutExpired as e:
            proc.kill()
            proc.wait()
            details.fpc_result_out = "[ timed out ]"
            fpc_timeout = True
        except subprocess.CalledProcessError as e:
            details.fpc_result_out = e.output
    else:
        details.fpc_result_out = "[ compilation failed ]"

    own_timeout = False
    if details.own_comp_success:
        proc = subprocess.Popen(
            [f'java -cp "{test_path.parent}" "{class_name}"'],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
            text=True,
            start_new_session=True,
        )
        try:
            details.own_result_out, _ = proc.communicate(timeout=1)
        except subprocess.TimeoutExpired as e:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
            proc.wait()
            details.own_result_out = "[ timed out ]"
            own_timeout = True
        except subprocess.CalledProcessError as e:
            details.own_result_out = e.output
    else:
        details.own_result_out = "[ compilation failed ]"

    # clean output
    details.fpc_result_out = (
        re.sub(r"([0-9]+\.[0-9])0+000E\+000", r"\1", details.fpc_result_out)
        .removeprefix(" ")
        .replace("FALSE", "false")
        .replace("TRUE", "true")
    )
    details.own_result_out = details.own_result_out.replace("FALSE", "false").replace(
        "TRUE", "true"
    )

    if delete_gen_files:
        base_name = test_path.name.removesuffix(".pas")
        junk_files_names = [
            base_name,
            base_name + ".j",
            base_name + ".o",
            class_name + ".class",
        ]
        for f in junk_files_names:
            file_path = test_path.parent / f
            if file_path.exists():
                Path.unlink(test_path.parent / f)

    # print test result
    if details.fpc_comp_success and not details.own_comp_success:
        print_test_result(
            details, False, "own compilation failed when it should have succeeded"
        )
        return False
    if not details.fpc_comp_success and details.own_comp_success:
        print_test_result(
            details, False, "own compilation succeeded when it should have failed"
        )
        return False
    if not details.fpc_comp_success and not details.own_comp_success:
        print_test_result(details, True, "successfully failed")
        return True

    if fpc_timeout and not own_timeout:
        print_test_result(details, False, "should have timed out but didn't")
        return False
    if not fpc_timeout and own_timeout:
        print_test_result(details, False, "timed out when it shouldn't have")
        return False
    if fpc_timeout and own_timeout:
        print_test_result(details, True, "correctly timed out")
        return True

    if "java.lang.VerifyError" in details.own_result_out:
        print_test_result(details, False, "verify error")
        return False

    matches = True
    for fpcl, ownl in zip(
        details.fpc_result_out.strip().splitlines(),
        details.own_result_out.strip().splitlines(),
    ):
        fpcl = fpcl.strip()
        ownl = ownl.strip()

        if fpcl == ownl:
            continue
        try:
            a = float(fpcl)
            b = float(ownl)
            if abs(a - b) < 0.00001:
                continue
        except:
            matches = False
            break

    if matches:
        print_test_result(details, True, "correct output")
        return True
    else:
        fpc_inline = details.fpc_result_out.strip().replace("\n", "↵")
        own_inline = details.own_result_out.strip().replace("\n", "↵")
        print_test_result(
            details,
            False,
            f"wrong output (expected: {fpc_inline} | got: {own_inline})",
        )
        return False


def get_files_in_subfolders(base_dir: Path) -> list[os.DirEntry[str]]:
    file_exclude_ptrn = [re.compile(p) for p in EXCLUDE_FILES]
    folder_exclude_ptrn = [re.compile(p) for p in EXCLUDE_FOLDERS]

    dirs = [base_dir]
    files: list[os.DirEntry[str]] = []
    while len(dirs) > 0:
        dir = dirs.pop()
        for f in os.scandir(dir):
            if f.is_file():
                if any(p.match(f.name) for p in file_exclude_ptrn):
                    continue
                files.append(f)
            else:
                if any(p.match(f.name) for p in folder_exclude_ptrn):
                    continue
                dirs.append(Path(f.path))
    return files


def test_compilation_all(
    base_dir: Path = Path("./test/jasmin/"),
    test_path: Path = Path("./test/sample.pas"),
    compilation_output: bool = False,
    execution_output: bool = False,
    delete_gen_files=DELETE_GENERATED_FILES_WHEN_RUNNING_ALL,
):
    files = get_files_in_subfolders(base_dir)

    successful = 0
    for f in files:
        if test_compilation(
            Path(f.path),
            test_path,
            compilation_output,
            execution_output,
            delete_gen_files,
        ):
            successful += 1

    total_tested = len(files)

    if successful == total_tested:
        print(frame(f"passed all {total_tested} tests", "=", fmt_suc))
    else:
        print(
            frame(
                f"failed {total_tested - successful} of {total_tested} tests",
                "=",
                fmt_err,
            )
        )


def test_liveness(file_path: Path):
    if not assert_file_exists(file_path):
        return True

    print(f"▪ testing {file_path}")

    expect_reg = None
    with open(file_path, "r") as f:
        content = f.read()
        matches = re.search(r"\[\[ *LIVENESS_REGISTERS: *([0-9]+) *\]\]", content)
        if matches != None:
            expect_reg = int(matches.group(1))

    if expect_reg is None:
        print(fmt_err(f"file {file_path} does not specify expected register count"))
        print(fmt_dim(f'add a comment with "[[LIVENESS_REGISTERS:<num_registers>]]"'))
        return

    # compile with own compiler
    actual_out = None
    try:
        actual_out = subprocess.check_output(
            LIVENESS_CMD.replace("{test_case}", str(file_path)),
            stderr=subprocess.STDOUT,
            shell=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        actual_out = e.output
    except UnicodeDecodeError as e:
        pass

    if actual_out == None:
        print(indent(f'{fmt_err("test failed")}  {fmt_dim("no output")}'))
        return False

    actual_reg = None
    matches = re.search(r"Registers: ([0-9]+)", actual_out)
    if matches != None:
        actual_reg = int(matches.group(1))

    if actual_reg is None:
        print(
            indent(
                f'{fmt_err("test failed")}  {fmt_dim("output: " + repr(actual_out))}'
            )
        )
        return False

    if actual_reg == expect_reg:
        print(
            indent(
                f'{fmt_suc("test passed")}  {fmt_dim(f"{actual_reg} registers is correct")}'
            )
        )
        return True

    print(
        indent(
            f'{fmt_err("test failed")}  {fmt_dim(f"expected: {expect_reg} | actual: {actual_reg}")}'
        )
    )
    return False


def test_liveness_all(
    base_dir: Path = Path("./test/jasmin/"),
):
    files = get_files_in_subfolders(base_dir)

    successful = 0
    for f in files:
        if test_liveness(
            Path(f.path),
        ):
            successful += 1

    total_tested = len(files)

    if successful == total_tested:
        print(frame(f"passed all {total_tested} liveness tests", "=", fmt_suc))
    else:
        print(
            frame(
                f"failed {total_tested - successful} of {total_tested} liveness tests",
                "=",
                fmt_err,
            )
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE:")
        print(
            "python3 test_compiler.py <test_case>         test compiler on <test_case> with verbose output"
        )
        print(
            "python3 test_compiler.py -a [<test_dir>]     test compiler on all .pas files in <test_dir>"
        )
        print(
            "python3 test_compiler.py -l <test_case>      test liveness on <test_case>"
        )
        print(
            "python3 test_compiler.py -l -a [<test_dir>]  test liveness on all files in <test_dir>"
        )
        sys.exit()

    if sys.argv[1] == "-a":
        test_dir = COMPILATION_TEST_DIR
        if len(sys.argv) > 2:
            test_dir = Path(sys.argv[2])
        test_compilation_all(test_dir, COPY_TO)
    elif sys.argv[1] == "-l":
        if sys.argv[2] == "-a":
            test_dir = LIVENESS_TEST_DIR
            if len(sys.argv) > 3:
                test_dir = Path(sys.argv[3])
            test_liveness_all(test_dir)
        else:
            test_liveness(Path(sys.argv[1]))
    else:
        delete_gen_files = DELETE_GENERATED_FILES_WHEN_RUNNING_ONE
        if len(sys.argv) > 2:
            if sys.argv[2] == "d":
                delete_gen_files = not delete_gen_files
        test_compilation(Path(sys.argv[1]), COPY_TO, delete_gen_files=delete_gen_files)
