import socket
import json

# import server and protocal info
with open("server_info.json", "r") as in_file:
    server_info = json.load(in_file)

# get protocol and connection variables
HOST, PORT = server_info["ADDR"]["HOST"], server_info["ADDR"]["PORT"]
FORMAT, HEADER_LEN = server_info["HEADER"]["FORMAT"], server_info["HEADER"]["HEADER_LEN"]
DISCONNECT = server_info["HEADER"]["DISCONNECT_MSG"]

# does the client socket address family and socket type have to match server??
AF, sock_type = server_info["CONNECTION"]["AF"], server_info["CONNECTION"]["soc_type"]

# client init
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def getresponse():
    return client.recv(HEADER_LEN).decode(FORMAT)


def send(msg):
    encoded_msg = msg.encode(FORMAT)
    # send header with length of message
    msg_len = str(len(encoded_msg)).encode(FORMAT)
    header = msg_len + b' ' * (HEADER_LEN - len(msg_len))
    client.send(header)

    # send message
    client.send(encoded_msg)

    # get response
    print(getresponse())


if __name__ == "__main__":
    while True:
        msg = input(f"[CLIENT] ")
        send(msg)
        if msg == DISCONNECT:
            break
        

        
