import cv2
cap = cv2.VideoCapture(0);
fourcc= cv2.VideoWriter_fourcc(*'XVID') # class
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) # capture the video and save it with given file name

while cap.isOpened() : #if camera index is true then program enters to while loop otherwise go to else condition
   ret,frame = cap.read()

   if ret == True :
       out.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xFF == ord ('q'):
           break
   else:
       break
cap.release()# release resouces
out.release()
cv2.destroyAllWindows()