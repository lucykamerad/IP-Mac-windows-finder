import socket
import uuid
import re

def get_ip_address():
    try:
        # Connect to a public DNS server to get the local IP used for external traffic
        # This is more reliable than gethostbyname(gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return socket.gethostbyname(socket.gethostname())

def get_mac_address():
    try:
        # Get MAC address using uuid
        mac_num = hex(uuid.getnode()).replace('0x', '').upper()
        # Ensure it's 12 characters long (padding with zeros if necessary)
        mac_num = mac_num.zfill(12)
        # Format it as XX:XX:XX:XX:XX:XX
        mac = ":".join(re.findall('..', mac_num))
        return mac
    except Exception:
        return "Unknown"

def main():
    print("-" * 30)
    print(" Network Information Finder")
    print("-" * 30)
    
    ip = get_ip_address()
    mac = get_mac_address()
    
    print(f" Current IP Address:  {ip}")
    print(f" Current MAC Address: {mac}")
    print("-" * 30)
    
    # Keep the window open if run via double-click
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
