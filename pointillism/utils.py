import numpy as np 
import cv2


def limit_size(img,max_x,max_y=0):
    # If the maximum width is 0 return the original img without resizing
    if max_x == 0:
        return img
    # if height is not provided it takes the width's size constraining it to a square
    if max_y == 0:
        max_y = max_x
    
    # computation to get the ratios
    ratio = min(1.0,float(max_x) / img.shape[1], float(max_y) / img.shape[0])

    if ratio != 1.0:
        shape = (int(img.shape[1] * ratio), int(img.shape[0] * ratio ))
        return cv2.resize(img,shape,interpolation=cv2.INTER_AREA)
    
    else:
        return img

def clipped_addition(img, x, _max=255, _min=0):
    # Brightening the image
    if x > 0:
        mask = img > (_max - x)
        img += x
        np.putmask(img, mask, _max)

    # Darken the image
    if x < 0:
        mask = img < (_min - x)
        img += x
        np.putmask(img, mask, _min)

def regulate(img, hue=0, saturation=0, luminosity=0):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
    if hue < 0:
        hue = 255 + hue
    hsv[:, :, 0] += hue
    clipped_addition(hsv[:, :, 1], saturation)
    clipped_addition(hsv[:,:, 2], luminosity)
    return cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR_FULL)


