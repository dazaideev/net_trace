# NET TRACE
`net_trace` is a lightweight command-line tool for monitoring active TCP connections, retrieving your local and public IP addresses, and geolocating remote IPs.

## The current version of `net_trace` is designed to display and geolocate current connections. If you wish to modify the program for your own needs, here are the available functions:
```python
#  Returns your public IP address
network.get_public_ip()

# Returns your local IP address
network.get_local_ip()

# shows the following information about the IP address: Country, Region, City, ISP, Coordinates
network.geolocate_ip(IP_YOU_WANT_TO_GEOLOCATE)

# shows and writes to a .txt file all current connections
network.show_connections()
```

## Example:
```python
import sys

sys.path.append('packages')
from packages import network as network

if __name__ == "__main__":
    print(f"\n[+] Your public IP address: {network.get_public_ip()}")
    print(f"[+] Your local IP address: {network.get_local_ip()}")
    network.show_connections()

```