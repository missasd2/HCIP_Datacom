
import paramiko

import time

user = "python"
pw = "Huawei123#$"
ip = "192.168.56.10"


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip, username=user , password=pw,  look_for_keys=False, allow_agent=False)




#连接成功后，调用invoke_shell（）方法来唤醒shell，也就是华为系统命令行，同时把它赋值给command，方便后续调用。

command = ssh.invoke_shell()



#向设备发送命令，需要执行的命令。

# command.send("dis ip int bri\n")

command.send("dis cur conf | no-more\n")
command.send("quit")


#使用sleep函数，让脚步执行后休息2s，再回显内容。65535是回显多少个字符

time.sleep(2)

output = command.recv(65535)

print(output.decode("ascii"))



#配置完后，用close方法退出ssh 欢迎关注网络工程师阿龙

ssh.close()