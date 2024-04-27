import os

VIDEO_ROOT_DIR = os.path.join('data', 'dataset_I')
CONFIG_FILE = 'config_file'

if __name__ == '__main__':
    video_root = os.path.join(os.getcwd(), VIDEO_ROOT_DIR)
    config_f = os.path.join(video_root, CONFIG_FILE)

    dir_list = os.listdir(video_root)
    sect = {}
    print('editting ' + config_f)
    for item in sorted(dir_list):
        if os.path.isdir(os.path.join(video_root , item)):
            file, index = item.split('-')
            if file not in sect:
                sect[file] = [item]
            else:
                sect[file].append(item)
    with open(config_f, 'w') as file:
        file.write('') # reset file
    for lst in sect.values():
        lst.sort(key=lambda name: int(name.split('-')[1]))
        with open(config_f, 'a') as file:
            file.write('\n'.join(lst) + '\n')
    print('done')
