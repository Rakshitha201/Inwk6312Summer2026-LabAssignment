from netmiko import Netmiko

devices = [
    {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"},
    {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"},
]

for device in devices:

    print("\n==============================")
    print(f"Configuring device: {device['ip']}")

    net_connect = Netmiko(**device)

    loopback_config = [
        "interface Loopback0",
        "description Loopback created with Netmiko",
        "ip address 10.10.10.1 255.255.255.0"
    ]

    output = net_connect.send_config_set(loopback_config)

    print(output)

    net_connect.disconnect()
