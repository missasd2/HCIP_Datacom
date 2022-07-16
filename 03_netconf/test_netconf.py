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
netconf_password = "Origin@159357"
filename = "netconf1.txt"


# 定义类ssh,用于配置设备netconf
class ssh():
    def ssh_connect(sip, username, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username, password=password)
        print(ip + " login successfully")
        return ssh

    def ssh_config(file, ip, username, password):
        a = ssh.ssh_connect(ip, username, password)
        cli = a.invoke_shell()
        # cli.send("N\n")
        time.sleep(0.5)
        cli.send("screen-length 0 temporary \n")
        time.sleep(0.5)

        # f = open(file, 'r')
        # config_list = f.readlines()
        # for i in config_list:
        #     cli.send(i)
        #     time.sleep(0.5)

        dis_this = cli.recv(999999).decode()
        print(dis_this)
        a.close()


# 定义函数huawei_connect, 用于建立NETCONF连接
def huawei_connnect(host, port, user, password):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           hostkey_verify=False,
                           device_params={"name": "huawei"},
                           allow_agent=False,
                           look_for_keys=False
                           )

# NETCONF 发送XML数据，配置设备接口IP地址
CREATE_INTERFACE = """<config>

    <ethernet xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <ethernetIfs>
            <ethernetIf operation="merge">
                <ifName>GE1/0/2</ifName>
                <l2Enable>disable</l2Enable>
            </ethernetIf>
        </ethernetIfs>
    </ethernet>

    <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
        <interfaces>
            <interface operation="merge">
                <ifName>GE1/0/2</ifName>
                <ifDescr>Config by NETCONF</ifDescr>
                <ifmAm4>
                    <am4CfgAddrs>
                        <am4CfgAddr operation="create">
                            <subnetMask>255.255.255.0</subnetMask>
                            <addrType>main</addrType>
                            <ifIpAddr>192.168.2.1</ifIpAddr>
                        </am4CfgAddr>
                    </am4CfgAddrs>
                </ifmAm4>
            </interface>
        </interfaces>
    </ifm>
</config>"""


if __name__ == '__main__':
    ssh.ssh_config(filename, ip, ssh_user, ssh_password)
    m = huawei_connnect(ip, netconf_port, netconf_user, netconf_password)
    m.edit_config(target="running", config=CREATE_INTERFACE)




