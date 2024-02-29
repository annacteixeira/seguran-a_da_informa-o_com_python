import ipaddress

ip = '192.168.0.0/4'

# address = ipaddress.ip_address(ip)

network = ipaddress.ip_network(ip, strict=False)

# print(address)
for ip in network:
    print(ip)