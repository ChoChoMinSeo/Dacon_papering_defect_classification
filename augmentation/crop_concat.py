import os
import cv2
import numpy as np
IMAGEPATH = 'C:/dob/train_images'
class_list = os.listdir(IMAGEPATH)
img_path = IMAGEPATH+'/'+class_list[0]+'/'+'0.png'
img_array = np.fromfile(img_path, np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
h,w,_ = img.shape
print(h,w)
resized_list=[]
img_list = [img[0:h//3,0:w//3],img[h//3:h//3*2,0:w//3],img[h//3*2:h,0:w//3],img[0:h//3,w//3:w//3*2],img[h//3:h//3*2,w//3:w//3*2],img[h//3*2:h,w//3:w//3*2],img[0:h//3,w//3*2:w],img[h//3:h//3*2,w//3*2:w],img[h//3*2:h,w//3*2:w]]
for i in range(len(img_list)):
    resized_list.append(cv2.resize(img_list[i],(224,224),cv2.INTER_AREA))
res= np.concatenate(resized_list,axis=2)
print(res.shape)
res = res/255
print(res)