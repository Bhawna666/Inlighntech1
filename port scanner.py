import socket
import threading

def scan_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

target = input("Enter target IP or domain: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(target, port))
    thread.start()