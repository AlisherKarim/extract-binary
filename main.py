import sys
import os

paths = []

def search(path, filename):
    for dirName in os.listdir(os.path.abspath(path)):
        if os.path.isdir(os.path.join(path, dirName)):
            search(os.path.join(path, dirName), filename)
        if os.path.isfile(os.path.join(path, dirName)):
            # if os.access(dirName, os.X_OK):
            if filename in dirName:
                paths.append(os.path.join(path, dirName))
        

def main(argv):
    if len(argv) < 3:
        print('>>> [ERROR] Please, use the following format:')
        print('>>>  python main.py path_to_firmware target_binary_name')
        return
    
    firmware_path = argv[1]
    target_binary_name = argv[2]
    firmware_path_directory, firmware_name = os.path.split(firmware_path)
    # run extraction script
    os.system('binwalk -e ' + firmware_path)
    # the extracted firmware is stored in the same directory
    target_directory = None
    for dirName in os.listdir(firmware_path_directory):
        if os.path.isdir(os.path.join(firmware_path_directory, dirName)):
            if firmware_name in dirName:
                target_directory = dirName
                break
    
    if target_directory is None:
        print('>>> [ERROR] Could\'t find extracted files')
        return

    target_path = os.path.abspath(firmware_path_directory + '/' + target_directory)
    print(">>> The extracted files are stored in: " + target_path)


    # check if target extracted folder contains bin folder
    # if os.path.isdir(target_path + '/squashfs-root/bin'):
    #     for binary in os.listdir(target_path + '/squashfs-root/bin'):
    #         if target_binary_name in binary:
    #             print(">>> Binary is found in: " + target_path + '/squashfs-root/bin/' + target_binary_name)
    #             # paths.append(target_path + '/squashfs-root/bin/' + target_binary_name)
                

    # # check in usr/bin folder
    # if os.path.isdir(target_path + '/squashfs-root/usr/bin'):
    #     for binary in os.listdir(target_path + '/squashfs-root/usr/bin'):
    #         if target_binary_name in binary:
    #             print(">>> Binary is found in: " + target_path + '/squashfs-root/usr/bin/' + target_binary_name)
                

    search(target_path, target_binary_name)

    if len(paths) == 0:
        print(">>> Binary not found in the given firmware")
        return
    
    print(">>> Binary found in the following paths:")
    for path in paths:
        print(">>> [PATH] " + path)

if __name__ == "__main__":
    main(sys.argv)
    
