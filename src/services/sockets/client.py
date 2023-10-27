import socket
import threading
from ip import get_ip

CONN_DETAILS = {
    "server_addr": ('192.168.0.103', 5000),
    "client_ip": get_ip(),
    "client_port": int(input("Port: ")),
    "target_port": int(input("Target port: "))
}
CONN_ADDR = (CONN_DETAILS["client_ip"], CONN_DETAILS["client_port"])

DATA_DETAILS = {
    "header_len": 64,
    "format": "utf-8",
    "disconnect_message": "QUIT"
}


def get_data(sock: socket.socket) -> None:
    while True:
        addr_len = sock.recv(DATA_DETAILS["header_len"]).decode(
            DATA_DETAILS["format"])
        if not addr_len:
            continue
        addr_len = int(addr_len[2:-1])

        addr = sock.recv(addr_len).decode(
            DATA_DETAILS["format"])

        data_len = sock.recv(DATA_DETAILS["header_len"]).decode(
            DATA_DETAILS["format"])
        data_len = int(data_len[2:-1])

        data = sock.recv(data_len).decode(
            DATA_DETAILS["format"])

        print(f"\n{addr}: {data}")


def pad_len(length: str) -> str:
    data = length.encode(DATA_DETAILS["format"])
    data_len = len(data)
    out_len = str(data_len).encode(DATA_DETAILS["format"])
    out_len += b' ' * (DATA_DETAILS["header_len"] - len(out_len) - 3)

    return out_len


def send_data(sock: socket.socket) -> None:
    while True:
        data = input(f"{CONN_ADDR}: ")
        if data == DATA_DETAILS["disconnect_message"]:
            port = int(input("Target port: "))
            if port == 0:
                break
            CONN_DETAILS["target_port"] = port
            continue

        sock.send(f"{pad_len(str(CONN_ADDR))}".encode(DATA_DETAILS["format"]))
        sock.send(f"{CONN_ADDR}".encode(DATA_DETAILS["format"]))

        sock.send(f"{pad_len(str(CONN_DETAILS['target_port']))}".encode(
            DATA_DETAILS["format"]))
        sock.send(f'{CONN_DETAILS["target_port"]}'.encode(
            DATA_DETAILS["format"]
        ))

        sock.send(f"{pad_len(str(data))}".encode(DATA_DETAILS["format"]))
        sock.send(f"{data}".encode(DATA_DETAILS["format"]))


def start() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client_sock.bind(CONN_ADDR)
        client_sock.connect(CONN_DETAILS["server_addr"])

        in_thread = threading.Thread(target=get_data, args=(client_sock,))
        out_thread = threading.Thread(target=send_data, args=(
            client_sock,)
        )

        in_thread.start()
        out_thread.start()

        in_thread.join()
        out_thread.join()


if __name__ == '__main__':
    start()
