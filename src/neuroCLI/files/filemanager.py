import os


def verifyToken() -> bool:
    file_path = os.path.expanduser("~") + "/Documents/neuroToken.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            token = file.readline().strip()

        """
            Database validation of token
        """

        if token == "TEST_TOKEN":
            return True

    else:
        return False
