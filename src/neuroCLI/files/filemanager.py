import os
from neuroCLI.com.serverCom.tokenManager import sendToken
from neuroCLI.com.serverCom.tokenManager import sendCredentials


def verifyToken() -> bool:
    filePath = os.path.expanduser("~") + "/Documents/neuroToken.txt"

    if os.path.exists(filePath):
        with open(filePath, "r") as file:
            token = file.readline().strip()

        user = sendToken.verifyUserToken(token)

        if user:
            return user

    else:
        return False


def writeToken(email: str, password: str) -> bool:
    filePath = os.path.expanduser("~") + "/Documents/neurotoken.txt"

    token = sendCredentials.verifyUserCredentials(email, password)

    if token:
        if os.path.exists(filePath):
            with open(filePath, "w") as file:
                file.write(token + "\n")

                return True

    else:
        return False
