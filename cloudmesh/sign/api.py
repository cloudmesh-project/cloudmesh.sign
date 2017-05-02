from __future__ import print_function
#import cv2

class Sign(object):

    def __init__(self):
        # not your location will not work easily / is not writeable
        self.classifier = '/street-signal/classifier/stopsign_classifier.xml'
        
    def hello(self, msg):
        print ("Hello Sign", msg)

    def detect(self, image):
        '''
        stop_cascade = cv2.CascadeClassifier(self.classifier)
        test = cv2.imread(image)
        gray = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
        stops = stop_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
        for (x,y,w,h) in stops:
            cv2.rectangle(test,(x,y),(x+w,y+h),(255,0,0),2)
        return test
        '''
        return image  # remove once you fix the above

    def cp(self, image, server): 

	return image 
