import socket
import requests
import smtplib
import psutil
import datetime

def get_local_ip() -> str:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip() -> str:
    try:
        response = requests.get("https://api.ipify.org")
        return response.text
    except requests.RequestException:
        return "The IP address could not be retrieved from the Internet."

def geolocate_ip(ip_address):
    try:
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            print(f"[+] IP Address: {ip_address}")
            print(f"[+] Country: {data['country']}")
            print(f"[+] Region: {data['regionName']}")
            print(f"[+] City: {data['city']}")
            print(f"[+] ISP: {data['isp']}")
            print(f"[+] Coordinates: {data['lat']}, {data['lon']}")
        else:
            print(f"[-] Error: {data['message']}")
    except Exception as e:
        print(f"[-] Exception occurred: {e}")
    print()

def show_connections():
    connections = psutil.net_connections(kind='tcp')
    seen_connections = set()

    print(f"\n{'PROTO':>5}  {'LOCAL ADDR':<22}  {'REMOTE ADDR':<22}  STATUS")

    for conn in connections:
        if not conn.laddr or not conn.raddr:
            continue

        if conn.laddr.ip == '127.0.0.1' or conn.raddr.ip == '127.0.0.1':
            continue
        if get_local_ip() in (conn.laddr.ip, conn.raddr.ip):
            pass

        if conn.status != 'ESTABLISHED':
            continue

        proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}"

        key = (proto, laddr, raddr)
        if key in seen_connections:
            continue
        seen_connections.add(key)

        if get_local_ip() in laddr:
            print(f"> {proto:>5}  {"lip.lip.lip.lip":<22}  {raddr:<22}  {conn.status}")
        else:
            print(f"> {proto:>5}  {laddr:<22}  {raddr:<22}  {conn.status}")
        with open("data.txt", "a") as file:
            file.write(f"{str(datetime.datetime.now()).replace(' ', '-')}|{proto}|MY_IP|{raddr}|{conn.status}\n")

        geolocate_ip(raddr.split(':')[0])