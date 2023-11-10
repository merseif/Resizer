from resize import Resize
from getway import Getway
import cv2
import matplotlib.pyplot as plt

class Opencv_resizer(Resize):
    def __init__ (self, height, width, image_path):
        super().__init__( height, width,image_path)
    

    
    def resize(self):
        pic = cv2.imread(self.image_path)
        pic_resized = cv2.resize(pic, (self.height, self.width))
        return pic_resized
            



#for trying the code
image=Getway.getimage()
image_resized=Opencv_resizer(200,200,image).resize()
plt.imshow(image_resized, cmap='gray')
plt.show()


    



        


