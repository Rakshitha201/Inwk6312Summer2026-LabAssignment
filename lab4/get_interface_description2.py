from netmiko import ConnectHandler

r1 = {"device_type": "cisco_ios", "ip": "192.168.1.101", "username": "student", "password": "Meilab123", "port": "22"}
r2 = {"device_type": "cisco_ios", "ip": "192.168.1.102", "username": "student", "password": "Meilab123", "port": "22"}
r3 = {"device_type": "cisco_ios", "ip": "192.168.1.103", "username": "student", "password": "Meilab123", "port": "22"}
r4 = {"device_type": "cisco_ios", "ip": "192.168.1.104", "username": "student", "password": "Meilab123", "port": "22"}

commands = [
    "show ip interface brief",
    "show ip route",
    "show version"
]

for device in (r1, r2, r3, r4):

    net_connect = ConnectHandler(**device)

    print("\n" + "=" * 100)
    print(f"Device: {device['ip']}")

    for cmd in commands:
        output = net_connect.send_command(cmd)

        print("\n" + "-" * 40)
        print(f"Command: {cmd}")
        print(output)

    net_connect.disconnect()

    print("=" * 100)
