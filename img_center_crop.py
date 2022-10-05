import cv2
import os

def center_crop(img, set_size):

    h, w, c = img.shape

    if set_size > min(h, w):
        return img

    crop_width = set_size
    crop_height = set_size

    mid_x, mid_y = w//2, h//2
    offset_x, offset_y = crop_width//2, crop_height//2
       
    crop_img = img[mid_y - offset_y:mid_y + offset_y, mid_x - offset_x:mid_x + offset_x]
    return crop_img

folder_path = '../ALPHA_EXP/camel_center_crop'

files = os.listdir(folder_path)

for file in files:
    input_path = folder_path+'/' +file
    output_path = folder_path+'/' +file
    
    img = cv2.imread(input_path)

    # print(img.shape)

    img = center_crop(img, 800)
    
    cv2.imwrite(output_path,img)
    