import paramiko
import time

SWITCH_IP = "" #Enter IP of Switch
USERNAME = "" #Enter IP of Switch
PASSWORD = "" #Enter Switch Password
PORT_NUMBER7 = "0/7" #Enter Port of Switch in the following format "0/PortNumber" Example is Port 7


# Connect to the EdgeSwitch
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(SWITCH_IP, username=USERNAME, password=PASSWORD, look_for_keys=False)
    channel = client.invoke_shell()

    # Send commands
    channel.send("enable\n")
    time.sleep(1)  # Wait for the 'Password:' prompt
    channel.send(PASSWORD + "\n")
    time.sleep(1)  # Wait for the prompt
    channel.send("configure\n")
    time.sleep(1)  # Wait for the prompt

    # Turn Off Port 7 
    channel.send(f"interface {PORT_NUMBER7}\n")
    time.sleep(1)  # Wait for the prompt
    channel.send("no shutdown\n")
    time.sleep(1)  # Wait for the prompt
    channel.send("exit\n")

    time.sleep(1)  # Wait for the prompt
    channel.send("exit\n")
    time.sleep(1)  # Wait for the prompt

    # Receive and print output
    output = channel.recv(4096).decode("utf-8")
    print(output)

finally:
    client.close()