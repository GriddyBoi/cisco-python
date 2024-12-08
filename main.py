#!usr/bin/python
import paramiko
import config

# Define your Cisco device credentials
ip_address = config.HOST
username = config.USERNAME
password = config.PASSWORD

# Create an SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the device
ssh_client.connect(ip_address, username=username, password=password)

# Execute commands
stdin, stdout, stderr = ssh_client.exec_command("sh int status")
print(stdout.read().decode())

# Close the connection
ssh_client.close()