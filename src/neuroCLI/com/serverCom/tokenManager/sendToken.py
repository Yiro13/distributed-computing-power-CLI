import grpc
from neuroCLI.com.serverCom.tokenManager.generated import sendToken_pb2
from neuroCLI.com.serverCom.tokenManager.generated import sendToken_pb2_grpc


def sendUserToken(token: str):
    return sendToken_pb2.SendToken(token=token)


def verifyUserToken(token: str):
    channel = grpc.insecure_channel("localhost:50051")
    stub = sendToken_pb2_grpc.VerifyTokenServiceStub(channel)

    request = sendUserToken(token)
    response = stub.verifyToken(request)

    if response.success:
        return response.user
    else:
        print("Invalid token.")

        return False
