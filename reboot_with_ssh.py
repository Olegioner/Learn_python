import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('ip-адрес', username='имя', password='*******')

client.exec_command('sudo reboot')

