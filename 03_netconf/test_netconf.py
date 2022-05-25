from ncclient import manager
from ncclient import operations
import paramiko
import time

# 设备参数
ip = '192.168.56.100'
ssh_user = "python"
ssh_password = "Huawei12#$"
netconf_port = "830"
netconf_user = "netconf"
netconf_password = "Huawei12#$"
filename = "netconf.txt"

# 定义类ssh,用于配置设备netconf
class ssh():
    def ssh_connect(self, ip, username, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username, password=password)
        print(ip + " login successfully")
        return ssh

    def ssh_config(self, file, ip, username, password):
        a = ssh.ssh_connect(ip, username, password)
        cli = a.invoke_shell()
        cli.send("N\n")
        time.sleep(0.5)
        cli.send("screen-length 0 temporary \n")
        time.sleep(0.5)

        f = open(file, 'r')
        config_list = f.readlines()
        for i in config_list:
            cli.send(i)
            time.sleep(0.5)

        dis_this = cli.recv(999999).decode()
        print(dis_this)
        a.close()


