import grpc
import threading
import time
from neuroCLI.com.serverCom.tokenManager.generated import status_pb2
from neuroCLI.com.serverCom.tokenManager.generated import status_pb2_grpc


def status(user: str) -> None:
    channel = grpc.insecure_channel("localhost:50051")
    stub = status_pb2_grpc.StatusStub(channel)

    request = status_pb2.SendUser(user)
    response = stub.status(request)

    print(f"Response: {response.message}")


def sendStatus(user: str) -> None:
    while True:
        status(user)
        time.sleep(60)


def startStatusPing(user: str) -> None:
    thread = threading.Thread(target=sendStatus, args=(user,))
    thread.daemon = True
    thread.start()
