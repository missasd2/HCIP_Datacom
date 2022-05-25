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


