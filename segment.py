import cv2
import numpy as np

#1 for row
#0 for column

def extract_line(th,flag):
	r,c = np.shape(th)
	if flag==1:
		x = np.ones((c,1))
		y = np.dot(th,x)
	elif flag==0:
		x = np.ones((1,r))
		y = np.dot(x,th)
	y[y>254] = 1
	i=0
	g=0
	start_flag = 0
	start_y = 0
	end_y = 0
	line_count = 0
	start_loc = []
	end_loc = []
	if flag==0:#column
		while i<c:	
			if y[0][i]==1:
				if start_flag==0:
					print("started at")
					start_loc.insert(g,i)
					print(i)
				start_flag = 1
			if y[0][i]==0:
				if start_flag == 1:
					if i-start_loc[g]>5:
						end_loc.insert(g,i)
						print("char ended at")
						print(i)
						g=g+1
					else:
						start_loc.pop()
						print("char noise detected & removed")
				start_flag = 0
			i = i+1
		return start_loc, end_loc, g

	elif flag==1:#row
		while i<r:	
			if y[i]==1:
				if start_flag==0:
					print("started at")
					start_loc.insert(g,i)
					print(i)
				start_flag = 1
			if y[i]==0:
				if start_flag == 1:
					if i-start_loc[g]>10:
						end_loc.insert(g,i)
						print("ended at")
						print(i)
						g=g+1
					else:
						start_loc.pop()
						print("noise detected & removed")
				start_flag = 0
			i = i+1	
		return start_loc, end_loc

def save_char(line_in, a, b, j):
	line_in_t = line_in.transpose()
	i=0
	while i<np.size(a):
		char_t = line_in_t[a[i]:b[i]+1]
		char = char_t.transpose()
		y_up,y_down = extract_line(char,1)
		if (np.size(y_up) !=0) and (np.size(y_down) !=0):
			char = char[y_up[0]:y_down[0]+1]
			r,c = np.shape(char)
			char_res = cv2.resize(char,(28, 28), interpolation = cv2.INTER_CUBIC)
			cv2.imwrite('char_1_'+str(j+1)+'_'+str(i+1)+'.png',char_res)
		
		i = i+1

img = cv2.imread('1.jpg',0)
img1,th = cv2.threshold(img,160,255,cv2.THRESH_BINARY_INV)
cv2.imwrite('1_2.png',th)
start_loc, end_loc = extract_line(th,1)
line_count = np.size(start_loc)
char_line = np.zeros((1,1))
i=0
count = 0

while i<line_count:
	char_line = th[start_loc[i]:end_loc[i]+1]
	a,b,c = extract_line(char_line,0)
	save_char(char_line,a,b,i)
	i = i+1
	count = count+c	

print(count)

# import scipy
# from scipy import ndimage

# # # Convert BGR to HSV
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# # # define range of blue color in HSV
# lower_blue = np.array([0,0,0])
# upper_blue = np.array([110,255,255])

# # # Threshold the HSV image to get only blue colors
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
# cv2.imwrite('filtered.jpg',mask)

# #flatten to ensure greyscale.
# im = scipy.misc.imread('frame.jpg',flatten=0)
# objects, number_of_objects = ndimage.label(im)
# letters = ndimage.find_objects(objects)

# #to save the images for illustrative purposes only:
# cv2.imwrite('ob.png',objects)
# for i,j in enumerate(letters):
#     cv2.imwrite('ob'+str(i)+'.png',objects[j])
# def extract_char(line_in):
# 	r,c = np.shape(line_in)
# 	x = np.ones((1,r))
# 	y = np.dot(x,line_in)
# 	y[y>254] = 1
# 	i=0
# 	g=0
# 	start_flag = 0
# 	start_y = 0
# 	end_y = 0
# 	line_count = 0
# 	start_loc = []
# 	end_loc = []
# 	while i<c:	
# 		if y[0][i]==1:
# 			if start_flag==0:
# 				print("started at")
# 				start_loc.insert(g,i)
# 				print(i)
# 			start_flag = 1
# 		if y[0][i]==0:
# 			if start_flag == 1:
# 				if i-start_loc[g]>5:
# 					end_loc.insert(g,i)
# 					print("char ended at")
# 					print(i)
# 					g=g+1
# 				else:
# 					start_loc.pop()
# 					print("char noise detected & removed")
# 			start_flag = 0
# 		i = i+1
	
# 	return start_loc, end_loc, g
