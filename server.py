import socket
import threading
from ip import get_ip

CONN_DETAILS = {
    "server_ip": get_ip(),
    "server_port": 5000,
}
CONN_ADDR = (CONN_DETAILS["server_ip"], CONN_DETAILS["server_port"])

DATA_DETAILS = {
    "header_len": 64,
    "format": "utf-8",
    "disconnect_message": "QUIT"
}

connected_clients: dict[int, socket.socket] = {}


def handle_client(conn_sock: socket.socket, conn_addr) -> None:
    with conn_sock:
        print(f"[CONNECTED] {conn_addr} connected....")
        while True:
            src_addr_len = conn_sock.recv(DATA_DETAILS["header_len"]).decode(
                DATA_DETAILS["format"])
            if not src_addr_len:
                continue
            addr_length = src_addr_len
            src_addr_len = int(src_addr_len[2:-1])

            src_addr = conn_sock.recv(src_addr_len).decode(
                DATA_DETAILS["format"])

            target_port_len = conn_sock.recv(
                DATA_DETAILS["header_len"]).decode(DATA_DETAILS["format"])
            target_port_len = int(target_port_len[2:-1])

            target_port = conn_sock.recv(
                target_port_len).decode(DATA_DETAILS["format"])

            src_data_len = conn_sock.recv(DATA_DETAILS["header_len"]).decode(
                DATA_DETAILS["format"])
            data_length = src_data_len
            src_data_len = int(src_data_len[2:-1])

            src_data = conn_sock.recv(src_data_len).decode(
                DATA_DETAILS["format"])

            target_client_socket = connected_clients[int(target_port)]
            if target_client_socket:
                target_client_socket.send(
                    addr_length.encode(DATA_DETAILS["format"]))
                target_client_socket.send(
                    src_addr.encode(DATA_DETAILS["format"]))
                target_client_socket.send(
                    data_length.encode(DATA_DETAILS["format"]))
                target_client_socket.send(
                    src_data.encode(DATA_DETAILS["format"]))


def start() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("[STARTING] Starting the server....")
        server_sock.bind(CONN_ADDR)

        print(f"[LISTENING] Server listening on {CONN_ADDR}")
        server_sock.listen()

        while True:
            conn_sock, conn_addr = server_sock.accept()
            conn_thread = threading.Thread(
                target=handle_client, args=(conn_sock, conn_addr)
            )
            conn_thread.start()

            connected_clients[conn_addr[1]] = conn_sock

            print(f"ACTIVE CONNECTIONS: {threading.active_count() - 1}")


if __name__ == '__main__':
    start()
