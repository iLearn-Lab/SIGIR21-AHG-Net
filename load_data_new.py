import numpy as np
import os

path_twitter = '/home/share/chenxiaolin/UIL2/Model/dataset/Content_vec/Twitter_padding/'
path_foursquare = '/home/share/chenxiaolin/UIL2/Model/dataset/Content_vec/Fq_padding/'

path_tw_img = '/home/share/chenxiaolin/UIL2/Model/dataset/Img/v1/TW/'
path_fq_img = '/home/share/chenxiaolin/UIL2/Model/dataset/Img/v1/FQ/' 

path_tw_tl = '/home/share/chenxiaolin/data/twitter/Generation/Time_location_matrix/'
path_fq_tl = '/home/share/chenxiaolin/data/foursquare/Generation/Time_location_matrix/'

tl_tw_exist_list = os.listdir(path_tw_tl)
tl_fq_exist_list = os.listdir(path_fq_tl)

num_time = 77
num_city = 947
zero_list_tl = [[0 for i in range(num_city)] for j in range(num_time) ]

def load_img(x_index): 
    x_batch_TW1 = []
    x_batch_FQ1 = []
    x_batch_FQ2 = []

    for pair in x_index:
        pair_list1 = []
        pair_list2 = []
        pair_list3 = []

        TW_1 = path_tw_img + pair[0] + '.npy'
        FQ_1 = path_fq_img + pair[1] + '.npy'  
        FQ_2 = path_fq_img + pair[2] + '.npy'            

        data_TW1 = np.load(TW_1)
        data_FQ1 = np.load(FQ_1)
        data_FQ2 = np.load(FQ_2)

        pair_list1.extend(data_TW1)
        pair_list2.extend(data_FQ1)
        pair_list3.extend(data_FQ2)

        x_batch_TW1.append(pair_list1)
        x_batch_FQ1.append(pair_list2)
        x_batch_FQ2.append(pair_list3)

    return np.array(x_batch_TW1), np.array(x_batch_FQ1), np.array(x_batch_FQ2)


def load_content(x_index):
    x_batch_TW1 = []
    x_batch_FQ1 = []
    x_batch_FQ2 = []

    for pair in x_index:
        pair_list1 = []
        pair_list2 = []
        pair_list3 = []

        TW_1 = path_twitter + pair[0] + '.npy'
        FQ_1 = path_foursquare + pair[1] + '.npy' 
        FQ_2 = path_foursquare + pair[2] + '.npy'            

        data_TW1 = np.load(TW_1)
        data_FQ1 = np.load(FQ_1)
        data_FQ2 = np.load(FQ_2)

        pair_list1.extend(data_TW1)
        pair_list2.extend(data_FQ1)
        pair_list3.extend(data_FQ2)

        x_batch_TW1.append(pair_list1)
        x_batch_FQ1.append(pair_list2)
        x_batch_FQ2.append(pair_list3)


    return np.array(x_batch_TW1), np.array(x_batch_FQ1), np.array(x_batch_FQ2)

def load_tl(x_index):
    x_batch_TW1 = []
    x_batch_FQ1 = []
    x_batch_FQ2 = []


    for pair in x_index:
        pair_list1 = []
        pair_list2 = []
        pair_list3 = []

        TW_1_ = pair[0] + '.npy'
        FQ_1_ = pair[1] + '.npy' 
        FQ_2_ = pair[2] + '.npy'   

        if TW_1_ in tl_tw_exist_list:
            TW_1 = path_tw_tl + TW_1_
            data_TW1 = np.load(TW_1)
        else:
            data_TW1 = zero_list_tl

        if FQ_1_ in tl_fq_exist_list:
            FQ_1 = path_fq_tl + FQ_1_
            data_FQ1 = np.load(FQ_1)
        else:
            data_FQ1 = zero_list_tl

        if FQ_2_ in tl_fq_exist_list:
            FQ_2 = path_fq_tl + FQ_2_
            data_FQ2 = np.load(FQ_2)
        else:
            data_FQ2 = zero_list_tl

        pair_list1.extend(data_TW1)
        pair_list2.extend(data_FQ1)
        pair_list3.extend(data_FQ2)

        x_batch_TW1.append(pair_list1)
        x_batch_FQ1.append(pair_list2)  
        x_batch_FQ2.append(pair_list3)        

    return np.array(x_batch_TW1), np.array(x_batch_FQ1), np.array(x_batch_FQ2)
