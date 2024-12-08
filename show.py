from netmiko import ConnectHandler
import config
from getpass import getpass


net_connect = ConnectHandler(
    device_type="cisco_ios",
    host = config.HOST,
    username = input("Enter Username: "),
    password = getpass(),
)


output = net_connect.send_command('show ip int brief')
print(output)