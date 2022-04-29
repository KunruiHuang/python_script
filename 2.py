import os
import sys
import functools

def compare_filepath(x, y):
    x_val, y_val = int(x.split('/')[-1]), int(y.split('/')[-1])
    return x_val - y_val

def list_files(input_path,flag):
    # print(input_path, flag)
    filepath_list = []
    for filepath, dirs, filenames in os.walk(input_path):
        if flag in filenames:
            filepath_list.append(filepath)
    filepath_list.sort(key=functools.cmp_to_key(compare_filepath))
    res_path = []
    for path in filepath_list:
        thermal_file = os.path.join(path, flag)
        res_path.append(thermal_file)
    return res_path

if __name__ == '__main__':
    # input_path = sys.argv[1]
    input_path_bin =  '/home/kerwin/Data/20210705111700'
    input_path_json = '/home/kerwin/Data/20210705111700'
    bin_path_list = list_files(input_path_bin, 'thermal.bin')
    json_path_list = list_files(input_path_json, 'frame_detail.json')
    for sub_list in zip(bin_path_list, json_path_list):
        for per_path in sub_list:
            print(per_path)
