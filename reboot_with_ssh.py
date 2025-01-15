import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('172.16.10.115', username='pi', password='246249')

stdin, stdout, stderr = client.exec_command('sudo reboot')

client.close()