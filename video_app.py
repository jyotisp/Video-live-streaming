import socket
import cv2
import numpy as np
import os
import threading

afn=socket.AF_INET
pn=socket.SOCK_DGRAM
s=socket.socket(afn,pn)
ip1="192.168.0.2"
port1=4321

ip2="192.168.0.16"
port2=1234

def reciever():
	
	s.bind((ip1,port1))
	while True:
		x=s.recvfrom(65530)
		img=np.asarray(bytearray(x[0]), dtype="uint8")
		img=img.reshape(-1,1)
		dec1=cv2.imdecode(img,cv2.IMREAD_COLOR)
		cv2.imshow("t",dec1)
		if cv2.waitKey(1)==13:
			break
	cv2.destroyAllWindows()

def sender():

	while True:
		cap=cv2.VideoCapture(0)
		ret,photo=cap.read()
		ret,photo1 = cv2.imencode(".jpg",photo[:400,:400])
		ds=photo1.tobytes()
		s.sendto(ds, (ip2, port2))
		if cv2.waitKey(1) == 13:
		    break

	cv2.destroyAllWindows()
	cap.release()
	
thread1=threading.Thread(target=reciever)
thread2=threading.Thread(target=sender)

thread1.start()
thread2.start()
