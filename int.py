#lanczos4

import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

sum1 = 0
cnt = 0

while cnt < 100:

	img1 = cv2.imread('Data/LR/'+str(cnt)+'.png',1)
	img2 = cv2.imread('Data/HR/'+str(cnt)+'.png',1)
	img = cv2.resize(img1,(len(img2),len(img2[0])), fx = 0, fy = 0, interpolation = cv2.INTER_LANCZOS4)
	#cv2.imshow("img",img)
	k = (img + img2)/2
	ss = 0
	k = img2 - img
	i = 0
	j = 0
	el = []


	while j < len(img2):
		while i < len(img2[0]):
			ss = ss + math.sqrt(((k[j][i][0]*k[j][i][0])+(k[j][i][1]*k[j][i][1])+(k[j][i][2]+k[j][i][2]))/3)
			#print(math.sqrt(((k[j][i][0]*k[j][i][0])+(k[j][i][1]*k[j][i][1])+(k[j][i][2]+k[j][i][2]))/3))
			
			i += 1
		j+=1


	ssa = (ss*100)/(len(k)*len(k[0]))
	i = 0
	j = 0
	bwk = cv2.cvtColor(k, cv2.COLOR_BGR2GRAY)
	#cv2.imshow("img",bwk)
	ssa = (ss*100)/(len(k)*len(k[0]))
	#print("Pixel Error ",ssa)
	sum1 = sum1 + ssa
	print(cnt,".png : ",ssa)

	cv2.waitKey(0) 
	cv2.destroyAllWindows()
	cnt += 1

print("Total Error Percentage Average :",sum1/100)
#cv2.imshow("img",bwk)

cv2.waitKey(0) 
cv2.destroyAllWindows()