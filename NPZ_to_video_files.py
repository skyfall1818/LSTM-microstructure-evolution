from PIL import Image
import os, shutil, sys
import numpy as np

VIDEO_ROOT_DIR = os.path.join('data', 'dataset_I')

def make_dir(dir_name): # making sub_path. deletes path if already exist
    try:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
        os.mkdir(dir_name)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (dir_name, e))
        sys.exit()


if __name__ == '__main__':
    video_root = os.path.join(os.getcwd(), VIDEO_ROOT_DIR)
    dir_list = os.listdir(video_root)
    for item in dir_list:
        # look for an .npz file to unzip
        if '.npz' in item:
            # making new directory
            filename = item.replace('.npz', '')

            # Loads all .npz files and converts it to a Jpeg
            # Each Jpeg represents 1 frame of the data 
            print('loading ' + os.path.join(video_root , item))
            data = np.load( os.path.join(video_root , item), allow_pickle=True)
            for key in data.keys(): # np load creates a dictionary. Ussually there is only one key.
                npset = data[key]
                s_count = 1 # squence counter
                for seq in npset: #each video in the data
                    name_path = filename + '_' + key + '_S-' + str(s_count)
                    seq_path = os.path.join(video_root  , name_path)
                    make_dir(seq_path) # making a new directory for each video
                    s_count += 1
                    f_count = 1 # frame counter
                    for frame in seq: # each image framge of the data
                        im = Image.fromarray((frame * 255).astype(np.uint8))
                        frame_name = 'Frame-' + str(f_count) + '.jpeg'
                        frame_path = os.path.join(seq_path, frame_name)
                        im.save ( frame_path ) # converts the the frame into a JPEG
                        f_count +=1
