from fabric import Connection

user_pass = {'password' : 'fgvBQ205'}
with Connection('172.16.10.131', user='user', connect_kwargs=user_pass) as conn:
    conn.run('sudo lprm -')
    conn.run('sudo service cups restart')





