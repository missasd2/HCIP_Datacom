"""
4 配置对比实验
"""
import re
import sys

import paramiko
import time
import difflib

username = "python"
password = "Huawei12#$"
ip = "192.168.56.100"


# 获取某设备当前配置
def get_config(ip, username, password):
    dis_cu = ""
    ssh = paramiko.client.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=22, username=username, password=password)
    print(ip + "login successfully")
    print("获取当前配置")

    cli = ssh.invoke_shell()
    time.sleep(0.5)
    cli.send("screen-length 0 temporary\n")
    time.sleep(0.5)
    cli.send("display cur\n")
    time.sleep(2)

    dis_cu = cli.recv(999999).decode()
    ssh.close()
    return dis_cu


# 通过ssh根据配置文件下发配置
def ssh_config(filename, ip, username, password):
    ssh = paramiko.client.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=22, username=username, password=password)
    print(ip + "login successfully")
    print("开始下发配置")

    cli = ssh.invoke_shell()
    time.sleep(0.5)
    cli.send("screen-length 0 temporary\n")
    time.sleep(0.5)

    with open(filename, "r", encoding="utf-8") as f:
        config_list = f.readlines()
        for i in config_list:
            cli.send(i)
            time.sleep(0.5)
    dis_this = cli.recv(999999).decode()
    print(dis_this)
    ssh.close()


def save_config(config_str, filename):
    # filename += str(time.localtime())
    with open(filename , "w") as _file:
        _file.writelines(config_str[0])


def main():
    # 保存当前配置
    config1 = get_config(ip=ip, username=username, password=password)
    cur_config1 = re.findall(r"(<CE1>display cu[\d\D]+<CE1>$)", config1)
    save_config(cur_config1, "file1.txt")

    # 下发配置
    ssh_config("netconf1.txt", ip=ip, username=username, password=password)

    # 保存新的配置
    config2 = get_config(ip=ip, username=username, password=password)
    cur_config2 = re.findall(r"(<CE1>display cu[\d\D]+<CE1>$)", config2)
    save_config(cur_config2, "file2.txt")



# 前后配置文件比对
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf8") as f:
            return f.readlines()
    except IOError:
        print("%s 未找到该文件" %filename)
        sys.exit(1)


def compare_config(file1, file2):
    file1_content = read_file(str(file1))
    file2_content = read_file(str(file2))
    d = difflib.HtmlDiff()
    result = d.make_file(file1_content, file2_content)
    with open("result.html", "w") as w:
        w.writelines(result)
    print()


if __name__ == '__main__':
    main()
    compare_config("file1.txt", "file2.txt")
    print()