from netmiko import ConnectHandler
import config

net_connect = ConnectHandler(
    device_type="cisco_ios",
    host = config.HOST,
    username = config.USERNAME,
    password = config.PASSWORD,
)



config_commands = [ 'spanning-tree vlan 1,2,11,17,45,167,200 priority 36864' ]
output = net_connect.send_config_set(config_commands)


print(output)