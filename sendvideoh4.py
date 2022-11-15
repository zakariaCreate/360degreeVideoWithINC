#!/bin/python3

# This is server code to send video frames over UDP
import cv2, imutils, socket
import numpy as np
import time
import base64

print(cv2.__version__)

BUFF_SIZE = 65536

server_socket8 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket8.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
socket_address8 = ('10.0.4.4',19998)
server_socket8.bind(socket_address8)
msg8,client_addr8 = server_socket8.recvfrom(BUFF_SIZE)
print('Message received : ',msg8 )
print('GOT connection from ',client_addr8)

vid = cv2.VideoCapture('video.mp4')

fps,st,frames_to_count,cnt = (0,time.time_ns(),20,0)
cnttt = 0
timeToSleep = 0

while True:

	WIDTH=400

	if (vid.isOpened() == False):
		print("Error opening video file")
		break

	f = open("./timeSendVideoPacket_H4.csv", "w")
	f.write('FrameId;SendingTime;Fps\n')

	while(vid.isOpened()):
		ret,frame = vid.read()
		if not ret:
			print("Can't receive frame (stream end?). Exiting ...")
			break

		print("let us wait "+str(timeToSleep)+" seconds")
		time.sleep(timeToSleep) #we add delay to fix fps at 20 FPS
		print("Go ahead ! frame Number : " + str(cnttt))
		print("FPS : "+str(fps))

		frame = imutils.resize(frame,width=WIDTH)
		encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,10])

		message = buffer
		#message = base64.b64encode(buffer) #we desabled the B64encoder

		#save the time when we sent the packet
		f.write(str(cnttt) + ';' + str(time.time_ns()) +';' +str(fps) + '\n')

		server_socket8.sendto(message.tobytes(),client_addr8)

		cv2.imshow('SENDING VIDEO (With INC)',frame)

		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			server_socket1.close()
			break

		#fixing the FPS
		interval = time.time_ns() - st
		st = time.time_ns()
		if interval < 100000000 : #to fix fps to 20 fps we need to send a frame every 5e+7 nano second
			newTimeToSleep = (100000000 - interval)/1000000000 + timeToSleep
			if newTimeToSleep < 0 :
				timeToSleep = timeToSleep - newTimeToSleep
			else :
				timeToSleep = newTimeToSleep
		fps = round((1/interval)*1000000000)

		cnttt+=1

		if cnttt == 3600 :
			print('we are closing the file end sending!')
			f.close()
			# When everything done, release
			# the video capture object
			vid.release()

			# Closes all the frames
			cv2.destroyAllWindows()
			break
