import numpy as np
from conv_num import *

NUM_MAX = 100
TEST_NUM = 2 #the number of test data is 10
MAX_QUIZ_NUM = 30

username = ['inusan', 'kumasan', 'nekosan', 'test119', 'test120', 'test121', 'tomato', 'torisan', 'usagisan']

for i_name in username:
  print(i_name)
  tag_number = conv_num(i_name)
  print(tag_number)

  xdata_b = "./data/" + str(tag_number) + "_new/factor_before.csv"
  x2data_b = "./data/" + str(tag_number) + "_new/kibun_before.csv"
  ydata_b = "./data/" + str(tag_number) + "_new/signal_before.csv"

  factor= np.loadtxt(xdata_b,delimiter='\t')
  mood = np.loadtxt(x2data_b,delimiter='\t')
  face= np.loadtxt(ydata_b,delimiter='\t')

  test_index = np.zeros(TEST_NUM,dtype='int')

  SAVE_DIR = "/home/kazumi/prog/quiz_check2023/sep_data/"

  EACH_RANDOM_COMB_NUM = 5

  for set_num in (5,10,15,20,25):
    for i in range(MAX_QUIZ_NUM-1):
      test_index[0] = i
      test_index[1] = i+1
      
      numbers = np.linspace(0,MAX_QUIZ_NUM-1,MAX_QUIZ_NUM,dtype='int')
      not_test_index = np.ones(len(numbers),dtype=bool)
      not_test_index[test_index] = False

      last_index = numbers[not_test_index]
      for comb_t in range(EACH_RANDOM_COMB_NUM):
        train_index = np.random.choice(last_index,set_num,replace=False)

        comb_way_num = i*EACH_RANDOM_COMB_NUM+comb_t

        ####################
        factor_train= factor[train_index,:]
        mood_train= mood[train_index]
        face_train= face[train_index,:]

        factor_test= factor[test_index,:]
        mood_test= mood[test_index]
        face_test= face[test_index,:]

        save_factor_train = SAVE_DIR +str(tag_number)+"/factor_train"+str(set_num) + "-" +str(comb_way_num)+".csv"
        save_mood_train = SAVE_DIR +str(tag_number)+"/mood_train"+str(set_num) + "-" +str(comb_way_num)+".csv"
        save_face_train = SAVE_DIR +str(tag_number)+"/face_train"+str(set_num) + "-" +str(comb_way_num)+".csv"
        #save_mood_train = "/home/kazumi/prog/quiz_check2016/jrm_test/"+str(tag_number)+"/mood_train"+str(set_num) + "-" +str(i)+".csv"
        #save_face_train = "/home/kazumi/prog/quiz_check2016/jrm_test/"+str(tag_number)+"/face_train"+str(set_num) + "-" +str(i)+".csv"
        np.savetxt(save_factor_train,factor_train,fmt='%.4f',delimiter=",")
        np.savetxt(save_mood_train,mood_train,fmt='%.4f',delimiter=",")
        np.savetxt(save_face_train,face_train,fmt='%.4f',delimiter=",")

        save_factor_test = SAVE_DIR +str(tag_number)+"/factor_test"+str(set_num) + "-" +str(comb_way_num)+".csv"
        save_mood_test = SAVE_DIR +str(tag_number)+"/mood_test"+str(set_num) + "-" +str(comb_way_num)+".csv"
        save_face_test = SAVE_DIR +str(tag_number)+"/face_test"+str(set_num) + "-" +str(comb_way_num)+".csv"

        np.savetxt(save_factor_test,factor_test,fmt='%.4f',delimiter=",")
        np.savetxt(save_mood_test,mood_test,fmt='%.4f',delimiter=",")
        np.savetxt(save_face_test,face_test,fmt='%.4f',delimiter=",")

        selected_test = SAVE_DIR +str(tag_number) + "/selected_num_test"+str(set_num) + "-"+ str(comb_way_num) + ".csv"
        #selected_test = "/home/kazumi/prog/quiz_check2016/jrm_test/" +str(tag_number) + "/selected_num_test"+str(set_num) + "-"+ str(i) + ".csv"
        selected_train = SAVE_DIR +str(tag_number) + "/selected_num_train"+str(set_num) + "-"+ str(comb_way_num) + ".csv"
        #selected_train = "/home/kazumi/prog/quiz_check2016/jrm_test/" +str(tag_number) + "/selected_num_train"+str(set_num) + "-"+ str(i) + ".csv"
        np.savetxt(selected_test,test_index,fmt='%2d',delimiter=",") 
        np.savetxt(selected_train,train_index,fmt='%2d',delimiter=",") 
