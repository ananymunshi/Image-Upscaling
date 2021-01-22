#lanczos4
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

sum1 = 0
cnt = 0
li = []

while cnt < 100:

	img1 = cv2.imread('Data/LR/'+str(cnt)+'.png',1)
	img2 = cv2.imread('Data/HR/'+str(cnt)+'.png',1)
	img = cv2.resize(img1,(len(img2),len(img2[0])), fx = 0, fy = 0, interpolation = cv2.INTER_LANCZOS4)

	k = (img + img2)/2
	ss = 0
	k = img2 - img
	i = 0
	j = 0
	el = []


	while j < len(img2):
		while i < len(img2[0]):
			
			ss = ss + math.sqrt(int(k[j][i][0])**2 + int(k[j][i][1])**2 + int(k[j][i][0])**2)
			
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
	#if ssa >= 80:
	#	cv2.imshow("0%",k)
	print(cnt,".png : ",ssa)
	li.append(ssa)
	cv2.waitKey(0) 
	cv2.destroyAllWindows()
	cnt += 1

print("Total Error Percentage Average :",sum1/100)
#cv2.imshow("img",bwk)
#print(li)
li.sort()
plt.plot(li)
plt.show()


cv2.waitKey(0) 
cv2.destroyAllWindows()