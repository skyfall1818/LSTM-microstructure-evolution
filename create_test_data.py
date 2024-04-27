import os, shutil, sys
import time
VIDEO_ROOT_DIR = os.path.join('data', 'dataset_I')
PERCENT=5
N_TOT_FRAMES=20

def make_dir(dir_name): # making sub_path. deletes path if already exist
    try:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
        os.mkdir(dir_name)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (dir_name, e))
        sys.exit()

def get_directory_list(root_path):
    dir_list = os.listdir(root_path)
    new_list = []
    for item in dir_list:
        item_dir = os.path.join(root_path, item)
        if os.path.isdir(item_dir):
            if 'test' in item:
                delete_directory(item_dir)
            else:
                new_list.append(item)
    new_list.sort(key=lambda x: int(x.split('-')[1]))
    return new_list

def get_image_list(path):
    global N_TOT_FRAMES
    
    path_list = os.listdir(path)
    path_list.sort(key=lambda x: int((x.split('-')[1]).split('.')[0]))
    return [path_list[i:i+ N_TOT_FRAMES] for i in range(0,len(path_list), N_TOT_FRAMES)]

def delete_directory(dir_name):
    try:
        if dir_name != "":
            shutil.rmtree(dir_name)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (dir_name, e))
        sys.exit()
    

if __name__ == '__main__':
    video_root = os.path.join(os.getcwd(), VIDEO_ROOT_DIR)
    
    dir_list = get_directory_list(video_root)
    dir_length = len(dir_list)
    num_training = int(dir_length * PERCENT // 100)
    print (num_training)
    print(dir_length)
    count = 1
    for item in dir_list[dir_length - num_training : dir_length]: # getting last n % of the directories
        current_dir = os.path.join(video_root, item)
        tot_images_in_subfolder = len(next(os.walk(current_dir))[2])

        video_list = get_image_list(current_dir)
        print("Creating test set with " + item)
        for lst in video_list:
            test_dir = os.path.join(video_root, "test_data-"+str(count))
            make_dir(test_dir)
            count +=1
            for i, name in enumerate(lst):
                src_path = os.path.join(current_dir, name)
                new_path = os.path.join(test_dir, "Frame-"+str(i+1)+".jpeg")
                os.rename(src_path, new_path)
        delete_directory(current_dir)
            
        
        
