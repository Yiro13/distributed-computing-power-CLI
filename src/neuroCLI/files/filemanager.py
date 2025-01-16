import os
from neuroCLI.com.serverCom.tokenManager import sendToken


def verifyToken() -> bool:
    file_path = os.path.expanduser("~") + "/Documents/neuroToken.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            token = file.readline().strip()

        user = sendToken.verifyUserToken(token)

        if user:
            return user

    else:
        return False
