import numpy as np
import scipy as sp
from scipy.stats import pearsonr

import matplotlib.pyplot as plt

ALL_SET_NUM = 145

#for name_num in range(9):
#for name_num in (6,7,8):
name_num = 5
dir_name = "../sep_data/" + str(name_num+1)
for set_num in (5,10,15,20,25):
  #set_num = 35
  r = np.zeros(ALL_SET_NUM)
  p = np.zeros(ALL_SET_NUM)
  for i in range(ALL_SET_NUM):#calculate the avelage value of estimated accuracy for datum in this loop
    i_csv = str(set_num) + "-" + str(i) + ".csv"

    mood_test = np.loadtxt(dir_name + "/mood_test" + i_csv ,delimiter=',')
    mood_est = np.loadtxt(dir_name + "/output/TRAINestimated_nn" + i_csv, delimiter=',')
    number = np.loadtxt(dir_name + "/selected_num_test" + i_csv, delimiter=',')

    #TESTestimated_10-0.csv
    #TRAINestimated_nn10-0.csv

    if(mood_test[0]==mood_test[1]):
      r[i] = None
      print("same")
    else:
      r[i] = (mood_est[1]-mood_est[0])/(mood_test[1]-mood_test[0])
      print(name_num,set_num,i,r[i])

  #test output
  np.savetxt(dir_name+"/output/nn_slope-"+str(set_num)+".csv",r,delimiter=',')

