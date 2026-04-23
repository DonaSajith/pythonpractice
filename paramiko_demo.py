import paramiko
import re
error_lines = []

SSH_client = paramiko.SSHClient()
SSH_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SSH_client.connect(hostname="192.168.88.7", username="uniserver", password="123")
sftp = SSH_client.open_sftp()

log_file = sftp.open("/home/uniserver/Dona/python practice/log.txt", "r")
for line in log_file:
    if re.search(r'ERROR', line):
        print(line, end='')
        error_lines.append(line)
log_file.close()

error_file = sftp.open("/home/uniserver/Dona/python practice/error.txt", "w")
for line in error_lines:
    error_file.write(line)
error_file.close()

sftp.close()
SSH_client.close()
