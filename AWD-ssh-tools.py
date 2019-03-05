# -*- coding: utf-8 -*- 
import paramiko

transport = paramiko.Transport(('10.211.55.11',22))
m = transport.connect(username='parallels', password='woaini123')
# 将sshclient的对象的transport指定为以上的transport
ssh = paramiko.SSHClient()
ssh._transport = transport
# 执行命令，和传统方法一样
stdin, stdout, stderr = ssh.exec_command('ls')
stdin, stdout, stderr = ssh.exec_command('cd /bin')
stdin, stdout, stderr = ssh.exec_command('ls')
print (stdout.read())
# 关闭连接
transport.close()