from runner import run_subprocess


def compile(openapi_directory: str):
    # You can put the parts of your command in the list below or just use a string directly.

    command_to_execute = ["./restler/restler/Restler",
                          "compile", "--api_spec", f"{openapi_directory}/spec.json"]

    run_subprocess(command_to_execute)
