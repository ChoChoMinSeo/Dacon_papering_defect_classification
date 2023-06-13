import cv2
import numpy as np
from PIL import Image, ImageEnhance

def horizontal_flip(img):
    return cv2.flip(img, 1)
def vertical_flip(img):
    return cv2.flip(img, 0)
def brightness_inc(img, val):
    hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsvimg) # hue 색, saturation 채도, value 명도 
    lim = 255 - val
    v[v > lim] = 255
    v[v <= lim] += val
    final_hsv = cv2.merge((h, s, v))
    res = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return res
def brightness_dec(img, val):
    hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsvimg)
    lim = val
    v[v < lim] = 0
    v[v >= lim] -= val
    final_hsv = cv2.merge((h, s, v))
    res = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return res
def rotate90(img):
    return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
def rotate_anti90(img):
    return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
def b_control(img, val):
    b,g,r = cv2.split(img)
    if val<0:
      lim = -val
      b[b<lim] = 0
      b[b>=lim]-=-val
    else:
      lim = 255-val
      b[b>lim] = 255
      b[b<=lim]+=val
    res = cv2.merge((b,g,r))
    return res
def g_control(img, val):
    b,g,r = cv2.split(img)
    if val<0:
      lim = -val
      g[g<lim] = 0
      g[g>=lim]-=-val
    else:
      lim = 255-val
      g[g>lim] = 255
      g[g<=lim]+=val
    res = cv2.merge((b,g,r))
    return res
def r_control(img, val):
    b,g,r = cv2.split(img)
    if val<0:
      lim = -val
      r[r<lim] = 0
      r[r>=lim]-=-val
    else:
      lim = 255-val
      r[r>lim] = 255
      r[r<=lim]+=val
    res = cv2.merge((b,g,r))
    return res
def contrast(image):
    # image = Image.open(img_path)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    return image
    