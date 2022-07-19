from runner import run_subprocess


def test_api(openapi_directory: str):
    # You can put the parts of your command in the list below or just use a string directly.

    command_to_execute = ["./restler/restler/Restler", "fuzz",
                          "--grammar_file", "Compile/grammar.py",
                          "--dictionary_file", "Compile/dict.json",
                          "--settings", "Compile/engine_settings.py"]
                        #   "--token_refresh_interval", "3",
                        #   "--token_refresh_command", "<command>",
                        #   "--time_budget", "1"]

    run_subprocess(command_to_execute)

# restler.exe fuzz --grammar_file <RESTLer grammar.py file> --dictionary_file <RESTler fuzzing-dictionary.json file> --token_refresh_interval <time in seconds> --token_refresh_command <command> --time_budget <max number of hours (default 1)
