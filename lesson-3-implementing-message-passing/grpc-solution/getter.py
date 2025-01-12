import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

if __name__ == "__main__":
    response = stub.Get(order_pb2.Empty())
    print(response)
    for order in response.orders:
        print(order.id)

