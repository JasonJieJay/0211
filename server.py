#coding=utf-8
import socket
#导入socket模块
ip_port=('127.0.0.1',9999)
#以元组形式定一个IP和端口
sk=socket.socket()
#创建对象并且进行绑定IP进行监听
sk.bind(ip_port)
#开始监听传入链接(可以挂起最大连接数)
sk.listen(5)
while True:
	print('welcome to my server!!!')
	#conn代表客户端和服务端建立连接的通信链路
	conn,addr=sk.accept()
	#acccept代表阻塞方式，没有收到请求就不会向下执行
	client_date=conn.recv(1024)
	print(client_date)
	#回复消息
	conn.sendall(('server recieved your msg!').encode())
	conn.close()

