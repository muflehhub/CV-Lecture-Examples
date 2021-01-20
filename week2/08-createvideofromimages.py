"""

Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.


Make video with different formate
"""

import cv2
import os
import re

image_folder = './w2data/Couple/img'


def get_file_names(search_path):
    for (dirpath, _, filenames) in os.walk(search_path):
        for filename in filenames:
            yield filename  # os.path.join(dirpath, filename)


def makevideo(i_videoname, i_codec, i_list_images, i_fps, i_width, i_height):
    # True for color BGR
    video = cv2.VideoWriter(i_videoname, i_codec, i_fps, (i_width, i_height), True)
    for image in i_list_images[0:150]:

        print("saving..." + image)
        frame = cv2.imread(os.path.join(image_folder, image))
        cv2.imshow("Frame", frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        video.write(frame)
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    print("Inside main..............")
    print("Start saving images to video")
    list_files = sorted(get_file_names(image_folder),
                        key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    print(list_files)
    frame = cv2.imread(os.path.join(image_folder, list_files[0]))
    height, width, layers = frame.shape
    print(frame.shape)
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    ################################
    # '''
    # 0: This option is an uncompressed raw video file. The file extension should be .avi.
    # '''
    # fourcc = 0
    # video_name = 'Woman.avi'
    ################################

    '''
    This option is an uncompressed YUV encoding, 4:2:0 chroma subsampled. 
    This encoding is widely compatible but produces large files. 
    The file extension should be .avi.
    '''
    # fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')
    # video_name = 'WomanYUV.avi'
    ################################
    '''
    This option is MPEG-1. The file extension should be .avi.
    '''
    # fourcc = cv2.VideoWriter_fourcc('P','I','M','1')
    # video_name = 'WomanPIM1.avi'
    ##########################################
    '''
    This option is a relatively old MPEG-4 encoding. It is a good option 
    if you want to limit the size of the resulting video. 
    The file extension should be .avi.
    '''
    # fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    # video_name = 'WomanXVID.avi'
    ##################################################
    '''
    This option is another relatively old MPEG-4 encoding. 
    It is a good option if you want to limit the size
    of the resulting video. The file extension should be .mp4.
    '''
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video_name = './w2output/CoupleMP4V.mp4'
    ##################################################
    # '''
    # This option is a Flash video.
    # The file extension should be .flv.
    # '''
    # fourcc = cv2.VideoWriter_fourcc('F','L','V','1')
    # video_name = 'WomanFLV1.flv'

    makevideo(i_videoname=video_name, i_codec=fourcc, i_list_images=list_files,
              i_fps=25, i_width=width, i_height=height)
