from asyncio import base_events
import cv2
import os
import numpy as np
from tqdm import tqdm
import shutil

def increase_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    return img

# folder_path = '../ALPHA_EXP/sp_br'

# files = os.listdir(folder_path)

def change_img(input_path, output_path):
    img = cv2.imread(input_path)
    file_name = input_path.split('/')[-1]
    # print(file_name)

    alpha2 = 0.8 # 명암 조정값
    val = 60
    array = np.full(img.shape, (val, val, val), dtype=np.uint8)
    img2 = cv2.add(img, array)
    
    img3 = np.clip((1+alpha2) * img2 - 128 * alpha2, 0, 255).astype(np.uint8)   
    
    cv2.imwrite(output_path+'/'+ file_name, img3)

    
CAM = '../ALPHA_EXP/CAMEL'
SPR = '../ALPHA_EXP/SPIRIAL'

def address_each_avi(base_path):
    files = os.listdir(base_path)
    folders =[j for j in files if '.avi' not in j]

    for folder in tqdm(folders):
        output_folder = base_path+'/'+folder+'_modified'
        imgs = os.listdir(base_path+'/'+folder)
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        for i in imgs:
            input_i = base_path+'/'+folder+'/'+i
            change_img(input_i, output_folder)
        
        shutil.make_archive(output_folder, 'tar', output_folder)

address_each_avi(CAM)
address_each_avi(SPR) 
        














# for file in files:
#     input_path = folder_path +'/' + file
#     img = cv2.imread(input_path)
    
#     output_path = '../ALPHA_EXP/sp_br_result'
#     if not os.path.exists(output_path):
#         os.makedirs(output_path)
  
#     alpha1 = -0.5 # 명암 조정값
#     alpha2 = 0.8 # 명암 조정값

#     # dst1 = np.clip((1+alpha1) * img - 128 * alpha1, 0, 255).astype(np.uint8)

        
#     val = 60
#     array = np.full(img.shape, (val, val, val), dtype=np.uint8)
#     # img2 = increase_brightness(img, 30)
#     img2 = cv2.add(img, array)
    
#     img3 = np.clip((1+alpha2) * img2 - 128 * alpha2, 0, 255).astype(np.uint8)    
    
#     cv2.imwrite(output_path+'/'+file, img3)