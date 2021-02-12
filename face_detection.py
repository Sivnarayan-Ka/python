### to do fcae_recognition library is not getting installed pip error similarly to do detect face.py 
###
from PIL import Image
import face_detection

image = face_detection.loa(faces1.jpg)

face_locations = face_detection.face_locations(image)

for face_location in face_locations:
    top,rght,bottom,left = face_location
    
    face_image = image[top:bottom , left:right]
    pill_image = image.fromaarray(face_image)
    pill_image.show()