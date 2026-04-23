import paramiko
import re

def connect_ssh(hostname, username, password):
    SSH_client = paramiko.SSHClient()
    SSH_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SSH_client.connect(hostname=hostname, username=username, password=password)
    return SSH_client

def log_errors(SSH_client, log_path, error_path):
    sftp = SSH_client.open_sftp()
    error_lines = []
    log_file = sftp.open(log_path, "r")
    pattern = re.compile(r"\bERROR\b", re.IGNORECASE)

    for line in log_file:
        if pattern.search(line):
            print(line, end='')
            error_lines.append(line)

    log_file.close()

    error_file = sftp.open(error_path, "w")
    for line in error_lines:
        error_file.write(line)
    error_file.close()
    sftp.close()

ssh = connect_ssh(
    "192.168.88.7",
    "uniserver",
    "123"
)
log_errors(
    ssh,
    "/home/uniserver/Dona/python practice/log.txt",
    "/home/uniserver/Dona/python practice/error.txt"
)
ssh.close()