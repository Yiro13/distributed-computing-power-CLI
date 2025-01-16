import grpc

"""from neuroCLI.com.serverCom.generated import service_pb2
from neuroCLI.com.serverCom.generated import service_pb2_grpc
import time


def generate_client_status(clientID: str):
    while True:
        yield service_pb2.ClientStatus(client_id=clientID, status="active")
        time.sleep(60)


def run(clientID: str) -> None:
    channel = grpc.insecure_channel("localhost:50051")
    stub = service_pb2_grpc.ClientServerCommStub(channel)

    responses = stub.KeepAlive(generate_client_status(clientID))

    for response in responses:
        print(f"Server response: {response.message}")
"""
