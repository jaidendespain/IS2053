import socket
import time


# Getting target IP address.
def get_address():
    while True:
        identifier = input("Would you like to enter an IP address or hostname: ")
        
        # If IP address entered.
        if identifier.lower() == "ip address":
            address = input("Enter target IP address: ")
            return address
        
        # If hostname entered.
        elif identifier.lower() == "hostname":
            host_name = input("Enter target hostname: ")
            address = socket.gethostbyname(host_name)
            return address
        
        else:
            print("Enter 'IP address' or 'hostname'")


# Scanning for open ports.
def port_scanner(address):
    # Recording start time.
    start_time = time.time()

    open_ports = []

    # Scanning ports 1-500.
    for port in range(1, 500 + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Setting a timeout to speed up scanning.
        sock.settimeout(0.1) 

        # Determining whether OPEN or CLOSED.
        result = sock.connect_ex((address, port))
        if result == 0:
            print(f"Port {port}: OPEN")
            open_ports.append(port)
        else:
            print(f"Port {port}: CLOSED")
        
        sock.close()

    # Printing all open ports.
    open_ports = "{}".format(", ".join(str(num) for num in open_ports))
    print(f"\nOpen ports: {open_ports}")

    # Printing total scan time.
    print(f"Time taken: {round(time.time() - start_time, 3)} seconds")


def main():
    print("==============================================================")

    # Getting user's IP address. / Starting scanner.
    port_scanner(get_address())

    print("==============================================================")


if __name__ == "__main__":
    main()
