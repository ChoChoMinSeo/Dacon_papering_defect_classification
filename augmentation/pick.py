import os
import random
from PIL import Image

IMAGEPATH = 'C:/dob/train_images'
class_list = os.listdir(IMAGEPATH)
save_path = "C:/dob/train_data_balanced"
for i in range(len(class_list)):
    class_path = IMAGEPATH+'/'+class_list[i]
    image_list = os.listdir(class_path)
    cur_num = len(image_list)
    if i == 2 or i== 4 or i==8 or i==10:
        #class0
        goal = 210
        print('class0',class_list[i], cur_num, goal)
    elif i == 0 or i==1 or i==3 or i==5 or i== 7 or i== 14 or i== 16:
        #class1
        goal = 120
        print('class1',class_list[i], cur_num, goal)
    elif i== 6 or i== 12 or i==13 or i==15 or i== 18:
        #class2
        goal = 168
        print('class2',class_list[i], cur_num, goal)
    elif i == 9 or i==11 or i==17:
        goal = 280
        print('class3',class_list[i], cur_num, goal)
    sampled_list = random.sample(image_list,goal)
    for j in range(len(sampled_list)):
        img = Image.open(class_path+'/'+sampled_list[j])
        img.save(save_path+'/'+class_list[i]+'/'+str(j)+'.png')