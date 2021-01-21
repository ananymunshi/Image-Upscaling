#modified
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img1 = cv2.imread('720.png',1)
img2 = cv2.imread('1080.png',1)


img = cv2.resize(img1,(1920,1080), fx = 0, fy = 0, interpolation = cv2.INTER_LANCZOS4)

#cv2.imshow("img",img)
k = (img + img2)/2
ss = 0
#print("First Pixel of 720p image: ",img1[0][0])
#print("First Pixel of 1080p image: ",img2[0][0])
k = img2 - img
#print("Error in pixel Value: ",k[0][0][1])
#print(len(k))
i = 0
j = 0

while j < len(img2):
	while i < len(img2[0]):
		ss = ss + math.sqrt(((k[j][i][0]*k[j][i][0])+(k[j][i][1]*k[j][i][1])+(k[j][i][2]+k[j][i][2]))/3)
		#print(math.sqrt(((k[j][i][0]*k[j][i][0])+(k[j][i][1]*k[j][i][1])+(k[j][i][2]+k[j][i][2]))/3))
		i += 1
	j+=1

i = 0
j = 0

"""
while j < 1080:
	while i < 1920:
		#print("Hello")
		if img[j][i][1] == img2[j][i][1]:
			print("(",j,", ",i,")") 
		i += 1
	j+=1
"""

#print(img2[0][0])
#print(img[0][0])
#print(k[0][0])
bwk = cv2.cvtColor(k, cv2.COLOR_BGR2GRAY)
cv2.imshow("img",bwk)
ssa = (ss*100)/(1920*1080)
print("Pixel Error ",ss)

cv2.waitKey(0) 
cv2.destroyAllWindows()