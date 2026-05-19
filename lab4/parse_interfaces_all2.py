from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"},
]

for device in devices:

    print("\n==============================")
    print(f"Device: {device['ip']}")

    net_connect = Netmiko(**device)

    # IMPORTANT: TextFSM parsing enabled
    output = net_connect.send_command("show ip route", use_textfsm=True)

    net_connect.disconnect()

    # Loop through parsed routes
    for route in output:

        protocol = route.get("protocol", "N/A")
        network = route.get("network", "N/A")
        distance = route.get("distance", "N/A")
        metric = route.get("metric", "N/A")

        print(
            f"Protocol: {protocol} | "
            f"Network: {network} | "
            f"Distance: {distance} | "
            f"Metric: {metric}"
        )
