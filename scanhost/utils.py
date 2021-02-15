def get_acctive_host(hosts):
    import nmap
    nm = nmap.PortScanner()
    result = nm.scan(hosts=hosts, arguments='-n -sP')
    hosts = nm.all_hosts()
    return hosts


def is_ssh_up(host, port=22, timeout=5):
    import telnetlib
    import re
    try:
        tn = telnetlib.Telnet(host=host, port=port, timeout=timeout)
        tn_reult = tn.read_until(b'\n', timeout=timeout).decode('utf-8')
        ssh_result = re.search('SSH', tn_reult)
    except:
        return False
    else:
        return True


def login_ssh_password(host, port=22, username='root', password=None, command='hostname'):
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, port=port, username=username, password=password)
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode('utf-8')
