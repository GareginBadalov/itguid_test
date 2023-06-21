import websockets
import asyncio

from src.core.app import marco_polo

clients = []


async def send_message(message: str):
    for client in clients:
        await client.send(message=message)


async def new_client_connected(client_socket: websockets.WebSocketClientProtocol, path: str):
    print("new")
    clients.append(client_socket)

    while True:
        new_message = await client_socket.recv()
        func_type, value = new_message.split(" ")
        match func_type:
            case "solo":
                marco_polo(value)
            case "array":
                values = value.split(",")
                [marco_polo(int(val)) for val in values]
            case "range":
                values = value.split(",")
                [marco_polo(value) for value in range(int(values[0]), int(values[1]) + 1)]
        await send_message(new_message)


async def start_server():
    await websockets.serve(new_client_connected, "localhost", 2000)


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()

