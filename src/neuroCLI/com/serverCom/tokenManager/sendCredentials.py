import grpc
from neuroCLI.com.serverCom.tokenManager.generated import sendCredentials_pb2
from neuroCLI.com.serverCom.tokenManager.generated import sendCredentials_pb2_grpc


def sendUserCredentials(email: str, password: str):
    return sendCredentials_pb2.sendCredentials(email=email, password=password)


def verifyUserCredentials(email: str, password: str):
    channel = grpc.insecure_channel("localhost:50051")
    stub = sendCredentials_pb2_grpc.VerifyCredentialsServiceStub(channel)

    request = sendUserCredentials(email, password)
    response = stub.verifyCredentials(request)

    if response.success:
        return response.token
    else:
        print("Invalid credentials.")

        return False
