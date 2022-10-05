from email.mime import base
import cv2
import os
# import cv2.cv as cv/

# vid1 = 'spirial/Motion2-1 - 2of4.avi'
# vid2 = 'camel/Motion2-1 - 1of2.avi'

# if not os.path.exists(vid1.replace('.avi','')):
#     os.makedirs(vid1.replace('.avi',''))
    
# if not os.path.exists(vid2.replace('.avi','')):
#     os.makedirs(vid2.replace('.avi',''))
    
CAM = '../ALPHA_EXP/CAMEL'
SPR = '../ALPHA_EXP/SPIRIAL'

def address(base_path):
    files = os.listdir(base_path)
    for file in files:
        avi_path = base_path + '/' + file
        output_path = avi_path.replace('.avi','')
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        video_capture(avi_path)

def video_capture(path):
    
    output_p = path.replace('.avi','')
    output_path= './'+ output_p
    
    print(output_path)
    
    cap = cv2.VideoCapture(path)

    if cap.isOpened() == False:
        print("Can\'t open the video: ", path)
        a=1
        exit()

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(width, height, fps)
    # fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    # out = cv2.VideoWriter(output_path, fourcc, fps, (int(width), int(height)))
    
    count = 0 
    while True:

        cur_list = []
        ret, frame = cap.read()

        img = frame
        
        if frame is None:
            print("Video Conversion Completed")
            a=1
            break


        cv2.imwrite(output_path +'/' + str(count) +'.jpg', img)

        count += 1
        
    cap.release()
    # out.release()
    cv2.destroyAllWindows()
    
    

address(CAM)
print('cam done')
address(SPR)