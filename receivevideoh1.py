#!/bin/python3

# This is client code to receive video frames over UDP
import cv2, imutils, socket
import numpy as np
import time
import base64
import os

BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_ip = '10.0.2.2'
print(host_ip)
port = 9998

message = b'Hello'
client_socket.sendto(message,(host_ip,port))
fps,st,frames_to_count,cnt = (0,time.time_ns(),20,0)

cnttt = 0
file = open("./timeReceiveVideoPacket_H1.csv", "w")
file.write('FrameId;ReceivingTime;Fps\n')

while True:
	print("we are waiting...")
	packet,_ = client_socket.recvfrom(BUFF_SIZE)

	print("We got packet "+str(cnttt))
	print("FPS : "+str(fps))

	# data = packet
	f = open("./pictureReceived.jpg", "wb")
	f.write(packet)
	# os.system("/bin/time -f \"%P\" -o /home/p4/tutorials/exercises/results/CPUResults/mogrify.log -a mogrify -resize 10% ./pictureReceived.jpg") #resizing the frame size
	f.close()
	os.system("mogrify -resize 55% ./pictureReceived.jpg") #resizing the frame size

	f = open("./pictureReceived.jpg", "rb")
	data = f.read()
	f.close()

	#save the time when we receive the packet and after doing transcoding
	file.write(str(cnttt) + ';' + str(time.time_ns()) +';' +str(fps) +'\n')
	print("Size of the frame after transcoding: "+str(len(data)))
	npdata = np.fromstring(data,dtype=np.uint8)
	frame = cv2.imdecode(npdata,1)
	cv2.imshow("RECEIVING VIDEO (Without INC)",frame)

	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		client_socket.close()
		break

	try:
		interval = (time.time_ns()-st)
		st = time.time_ns()
		fps = round( (1/interval)*1000000000)
	except:
		pass

	cnttt+=1
	if cnttt == 3600 :
		print('we are closing the file end receiving!')
		file.close()
		break
