#!/usr/bin/env python3
from netmiko import ConnectHandler

def configure_router(hostname, ip):
    username = input(f"Enter username for {hostname}:\n>")
    secret = input(f"Enter secret for {hostname}:\n>")
    device0 = {
                "device_type": "cisco_ios",
                "host": ip,
                "username": username,
                "password": secret,
                "secret": secret,
            }

    with ConnectHandler(**device0) as connection:
        output = connection.send_command('show ip int brief')
        print(output)
        connection.enable()

        output = connection.send_config_from_file(f"{hostname}.txt")
        print(output)

def main():
    #print("This is working!")
    configure_router("R3", '198.51.100.5')
    configure_router("R2", '198.51.100.4')
    configure_router("R1", '198.51.100.3')

if __name__ == "__main__":
    main()
