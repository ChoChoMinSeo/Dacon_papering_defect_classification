import os
import cv2
from math import floor
import data_augment_fns as fn
import numpy as np
from PIL import Image, ImageEnhance

IMAGEPATH = 'C:/dob/open/train'
class_list = os.listdir(IMAGEPATH)
save_path = 'C:/dob/aug_br_rgb'
    
def mul3(img, class_path,imagepath):
    img1 = fn.brightness_dec(img,25)
    img2 = fn.brightness_inc(img,25)
    img3 = fn.brightness_dec(img,50)
    path1 = class_path+'/'+'br0_'+imagepath
    extension = os.path.splitext(path1)[1] # 이미지 확장자   
    result, encoded_img = cv2.imencode(extension, img1)
    if result:
        with open(path1, mode='w+b') as f:
            encoded_img.tofile(f)
    path2 = class_path+'/'+'br1_'+imagepath
    extension = os.path.splitext(path2)[1] # 이미지 확장자   
    result, encoded_img = cv2.imencode(extension, img2)
    if result:
        with open(path2, mode='w+b') as f:
            encoded_img.tofile(f)
    path3 = class_path+'/'+'br2_'+imagepath
    extension = os.path.splitext(path3)[1] # 이미지 확장자   
    result, encoded_img = cv2.imencode(extension, img3)
    if result:
        with open(path3, mode='w+b') as f:
            encoded_img.tofile(f)
# def mul2_rot(img, class_path,imagepath):
#     img1 = fn.rotate90(img)
#     img2 = fn.horizontal_flip(img)
#     path1 = class_path+'/'+'rot_'+imagepath
#     extension = os.path.splitext(path1)[1] # 이미지 확장자   
#     result, encoded_img = cv2.imencode(extension, img1)
#     if result:
#         with open(path1, mode='w+b') as f:
#             encoded_img.tofile(f)
#     path2 = class_path+'/'+'flip_'+imagepath
#     extension = os.path.splitext(path2)[1] # 이미지 확장자   
#     result, encoded_img = cv2.imencode(extension, img2)
#     if result:
#         with open(path2, mode='w+b') as f:
#             encoded_img.tofile(f)
# def mul2_cont(pil_img):
#     return fn.contrast(pil_img) 
def mul7(img, class_path,imagepath):
    img_list = [fn.r_control(img,4),fn.g_control(img,8),fn.g_control(fn.b_control(img,16),16)]
    path_list=[]
    for i in range(4):
        path_list.append(class_path+'/'+'rgb'+str(i)+'_'+imagepath)
    for i in range(len(img_list)):
        extension = os.path.splitext(path_list[i])[1] # 이미지 확장자   
        result, encoded_img = cv2.imencode(extension, img_list[i])
        if result:
            with open(path_list[i], mode='w+b') as f:
                encoded_img.tofile(f)
for i in class_list:
    print(i, len(os.listdir(IMAGEPATH+'/'+i)))
for i in range(len(class_list)):#len(class_list)
    class_path = IMAGEPATH+'/'+class_list[i]
    img_list = os.listdir(class_path)
    for j in img_list: 
        img_path = class_path+'/'+j
        img_array = np.fromfile(img_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        extension = os.path.splitext(class_path+'/'+j)[1] # 이미지 확장자   
        result, encoded_img = cv2.imencode(extension, img)
        if result:
            with open(save_path+'/'+class_list[i]+'/'+j, mode='w+b') as f:
                encoded_img.tofile(f)#원본 저장
    img_list = os.listdir(save_path+'/'+class_list[i])
    if len(img_list)<99:
        for j in img_list:
            img_path = save_path+'/'+class_list[i]+'/'+j
            img_array = np.fromfile(img_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            mul3(img,save_path+'/'+class_list[i],j)
        img_list = os.listdir(save_path+'/'+class_list[i])
        for k in img_list:
            img_path = save_path+'/'+class_list[i]+'/'+k
            img_array = np.fromfile(img_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            mul7(img,save_path+'/'+class_list[i],k)
    elif len(img_list)<200:
        for j in img_list:
            img_path = class_path+'/'+j
            img_array = np.fromfile(img_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            mul7(img,save_path+'/'+class_list[i],j)


   