from runner import run_subprocess


def test_api(openapi_directory: str):
    # You can put the parts of your command in the list below or just use a string directly.

    command_to_execute = ["./restler/restler/Restler", "fuzz-lean",
                          "--grammar_file", f"{openapi_directory}/spec.json",
                          "--dictionary_file", f"{openapi_directory}/spec.json",
                          "--token_refresh_interval", "3",
                          "--token_refresh_command", "<command>",
                          "--time_budget", "1"]

    run_subprocess(command_to_execute)

# C:\restler_bin\restler\restler.exe fuzz-lean --grammar_file <RESTLer grammar.py file> --dictionary_file <RESTler fuzzing-dictionary.json file> --token_refresh_interval <time in seconds> --token_refresh_command <command>
