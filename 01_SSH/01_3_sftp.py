import  paramiko

tran = paramiko.Transport("192.168.56.10", 22)
tran.connect(username="python", password="Huawei123#$")
sftp = paramiko.SFTPClient.from_transport(tran)
local_path = r"D:\backup\project\pycharmProjects\HCIP_Datacom_Auto\01_SSH\vrptest.cfg"
remote_path = r"/vrpcfg.cfg"
sftp.get(remote_path, local_path)
sftp.put(local_path, "/test.cfg")
tran.close()
