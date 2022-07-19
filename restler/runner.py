import subprocess


def run_subprocess(command_to_execute: list[str]):
    # You can put the parts of your command in the list below or just use a string directly.

    # command_to_execute = ["ls", "-l"]
    run = subprocess.run(command_to_execute, capture_output=True)

    print(run.stdout, flush=True)  # the output "Test"
    print(run.stderr, flush=True)  # the error part of the output
