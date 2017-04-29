from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class FindImageCommand(PluginCommand):

    @command
    def do_findimage(self, args, arguments):
        """
        ::

          Usage:
                command -f IMAGE
                command IMAGE
                command list

          This command does some useful things.

          Arguments:
              IMAGE  testimage 

          Options:
              -f      specify the test image to be searched for stop sign

        """
        print(arguments)
	
#	import cv2
#        stop_cascade = cv2.CascadeClassifier('/street-signal/classifier/stopsign_classifier.xml')
#        test = cv2.imread(image)
#        gray = cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
#        stops = stop_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
#        for (x,y,w,h) in stops:
#            cv2.rectangle(test,(x,y),(x+w,y+h),(255,0,0),2)
#        return test

