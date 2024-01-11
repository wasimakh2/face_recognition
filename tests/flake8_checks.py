import os
import subprocess
import sys

import flake8.api


class Flake8Checker:
    def run_checks(self, file_paths):
        # Convert file paths to a space-separated string
        file_paths_str = " ".join(file_paths)

        # Execute flake8 checks using subprocess
        result = subprocess.run(
            f"flake8 {file_paths_str}",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Print the flake8 output
        print(result.stdout)

        # Return the flake8 exit code
        return result.returncode
