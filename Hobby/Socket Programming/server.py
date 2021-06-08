import socket
import concurrent.futures
import json
import time 
import os

localtime = time.localtime()

# intiialise server information
server_signit = f"[{time.strftime('%x %X', time.localtime())}] [SERVER]"
FORMAT = "utf-8"
HEADER_LEN = 1024
PORT = 1010
HOST = socket.gethostbyname(socket.gethostname())
DISCONNECT = "!DISCONNECT"


exit_code = os.system('cmd /c "netstat -an > netstat.txt"')
print("[EXECUTED] netstat -an")
if exit_code == 0:
    print("EXECUTION SUCCESSFUL")

with open("netstat.txt", "r") as netsat_extract:
    lines = netsat_extract.readlines()
    for i in range(4,len(lines)):
        if str(PORT) == lines[i].split()[1].split(":")[-1]:
            raise OSError("PORT taken")
            break

# add to json for client import
server_info = {}
server_info["ADDR"] = {"HOST" : HOST, "PORT": PORT}
server_info["CONNECTION"] = {"AF":"AF_INET", "soc_type":"SOCK_STREAM"}
server_info["HEADER"] = {"FORMAT":FORMAT, "HEADER_LEN":HEADER_LEN, "DISCONNECT_MSG":DISCONNECT}

with open("server_info.json", "w") as out_file:
    json.dump(server_info, out_file)

# server init
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


def handle_client(conn, addr):
    with conn:
        print(f"{server_signit} NEW CONNECTION ")
        bad_header = 0
        while True and bad_header < 1000:
            try:
                msg_len = conn.recv(HEADER_LEN).decode(FORMAT)
                if msg_len:
                    msg_len = int(msg_len)
            except ValueError:
                print(f"{server_signit} [ERROR] INVALID HEADER")
                bad_header += 1
            else:
                msg = conn.recv(msg_len).decode(FORMAT)
                
                if msg == DISCONNECT:
                    break
                else:
                    print(f"{server_signit} received: {msg}")
                    conn.sendall(msg)
    
    # conn.close()

def start():
    """
    init thread pool and listen, add accepted connections to thread pool 
    """
    with concurrent.futures.ThreadPoolExecutor() as executor: 
        socs = []
        print(f"{server_signit} STARTING...")
        server.listen()
        print(f"{server_signit} LISTENING ON {HOST}")
        while True:
            conn, addr = server.accept()
            socs.append(executor.submit(handle_client, args=(conn, addr)))
            print(f"{server_signit} ACTIVE CONNECTIONS {len(socs)}") 

if __name__ == "__main__":
    start()
