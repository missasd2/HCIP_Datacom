"""

5.3.3 服务器端完整代码
"""
import time
from concurrent import futures

import grpc
import paramiko.client

import get_config_pb2
import get_config_pb2_grpc


class Display_Config(get_config_pb2_grpc.get_configServicer):
     # 调用paramiko登录设备获取当前配置
    def Login_info(self, request, context):
        ssh = paramiko.client.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=request.host, port=22, username=request.username, password=request.password)
        cli = ssh.invoke_shell()
        time.sleep(0.5)
        cli.send("screen-length 0 temporaay\n")
        time.sleep(0.5)
        cli.send("display cu\n")
        time.sleep(3)
        data = cli.recv(999999).decode()
        ssh.close()
        # 返回回显的配置信息
        return get_config_pb2.Reply(message=data)


def serve():
    # 创建RPC服务
    server = grpc.Server(futures.ThreadPoolExecutor(max_workers=10))
    # 从定义的服务中部署gRPC servicer
    get_config_pb2_grpc.add_get_configServicer_to_server(Display_Config(), server)
