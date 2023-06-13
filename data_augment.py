import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        value = 128 + factor * (c - 128)
        return max(0, min(255, value))
    return img.point(contrast)
train_path = 'C:/dob/open/train'
class_list = os.listdir(train_path)
save_path = 'C:/dob/augmented'
sum=0
for i in range(len(class_list)):
    class_path = train_path+'/'+class_list[i]
    img_list = os.listdir(class_path)
    sum+=len(img_list)
    print(class_list[i],len(img_list))
print(sum)
train_path = 'C:/dob/open/train'
class_list = os.listdir(train_path)   
for i in range(len(class_list)):
    class_path = train_path+'/'+class_list[i]
    img_list = os.listdir(class_path)
    print(len(img_list))
    
# for i in range(len(class_list)):
#     class_path = train_path+'/'+class_list[i]
#     img_list = os.listdir(class_path)
#     for j in img_list:
#         img_path = class_path+'/'+j
#         image = Image.open(img_path)
#         enhancer = ImageEnhance.Contrast(image)
#         image = enhancer.enhance(3)
#         # image = np.array(image)
#         # img = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
#         path = save_path+'/'+class_list[i]+'/'+j
#         # extension = os.path.splitext(path)[1] # 이미지 확장자
#         # result, encoded_img = cv2.imencode(extension, img)
#         image.save(path, dpi=dpi)
#         # if result:
#         #     with open(path, mode='w+b') as f:
#         #         encoded_img.tofile(f)
#         # cv2.imwrite(save_path+'/'+class_list[i]+'/'+j,img)
#     print(class_list[i],'fin')
		

        