import subprocess


def compile(openapi: str):
    # You can put the parts of your command in the list below or just use a string directly.
    command_to_execute = ["restler", "compile", "--api_spec", openapi]

    run = subprocess.run(command_to_execute, capture_output=True)

    print(run.stdout, flush=True)  # the output "Test"
    print(run.stderr, flush=True)  # the error part of the output
