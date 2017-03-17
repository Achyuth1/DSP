from os import listdir
from os.path import isfile, join
import numpy
import cv2

for i in xrange(0,9):	
	inp = i #digit folder
	mypath='./'+str(inp)
	output = numpy.zeros(10)
	output[inp] = 1
	training_data = []
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	images = numpy.empty(len(onlyfiles), dtype=object)
	for n in range(0, len(onlyfiles)):
	  images[n] = cv2.imread( join(mypath,onlyfiles[n]))
	  img2 = numpy.resize(images[n],(784,1))
	  img2 = img2/255.0
	  training_data = training_data + [(img2,output)]

	#print training_data  


	############### Saving the training data #######################
	import pickle
	outfile = 'out_'+str(i)
	with open(outfile, 'wb') as fp:
	    pickle.dump(training_data, fp)

	############### Loading the data -- checking ###################
	#with open ('outfile', 'rb') as fp:
	#    itemlist = pickle.load(fp) 
	    
	#print(itemlist)      