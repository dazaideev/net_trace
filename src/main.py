import sys

sys.path.append('packages')
from packages import network as ntn

if __name__ == "__main__":
    print(f"\n[+] Your public IP address: {ntn.get_public_ip()}")
    print(f"[+] Your local IP address: {ntn.get_local_ip()}")
    ntn.show_connections()
    input()
