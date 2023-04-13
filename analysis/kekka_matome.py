import numpy as np
import scipy as sp
from scipy.stats import pearsonr
from scipy.stats import wilcoxon
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import iqr

print("input slope or cos")
flg = input()

#EACH_RANDOM_COMB_NUM = 5
TEST_DATA_PATTERN = 145

test_len = TEST_DATA_PATTERN
hito_num = 9

set_list = (5, 10, 15, 20, 25)

nn_ave = np.zeros((len(set_list),hito_num))
phi_ave = np.zeros((len(set_list),hito_num))

nn_all = np.zeros((len(set_list),hito_num,test_len))
phi_all = np.zeros((len(set_list),hito_num,test_len))

phi_minmax = np.zeros((2,len(set_list),hito_num))

for name_num in range(hito_num):
  dir_name = "../sep_data/" + str(name_num+1)+"/output/"

  for set_num in set_list:

    if(flg == "slope"):

      nn_cos = 50*np.loadtxt(dir_name + "/nn_slope-" + str(set_num) + ".csv", delimiter=",")
      phi_cos = np.loadtxt(dir_name + "/phi_slope-" + str(set_num) + ".csv", delimiter=",")
      str_label = 'the value of katamuki similarity \n between estimated mood and self-assessed mood'

    elif(flg == "cos"):
      nn_cos = np.loadtxt(dir_name + "/nn_cos-" + str(set_num) + ".csv", delimiter=",")
      phi_cos = np.loadtxt(dir_name + "/phi_cos-" + str(set_num) + ".csv", delimiter=",")
      str_label = 'the value of cosine similarity \n between estimated mood and self-assessed mood'

    phi_cos[np.isinf(nn_cos)] = 0
    nn_cos[np.isnan(nn_cos)] = 0

    set_num_id = int(set_num/5-1)
    nn_all[set_num_id,name_num,:]= nn_cos
    phi_all[set_num_id,name_num,:]= phi_cos

    nn_ave[set_num_id,name_num]= np.average(abs(nn_cos))
    phi_ave[set_num_id,name_num]= np.average(abs(phi_cos))

    left = np.arange(test_len)
    width = 0.3

zero_wil   = nn_all[1,:,:]
for set_num in (5,10,15,20,25):
  set_num_id = int(set_num/5-1)
  phi_wil  = nn_all[set_num_id,:,:]
  print('set_num',set_num)
  print('wilcoxon check',wilcoxon(zero_wil.reshape(-1),phi_wil.reshape(-1)))

#for i in range(len(set_list)):
#  val = phi_all[i,:,:]
#  val = nn_all[i,:,:]

columns = ['phi','nn']
index = np.zeros((len(set_list),1))
index[:,0] = np.linspace(5,25,len(set_list),dtype='int')

nn_way_list = ["Neural network"] * 145
phi_way_list = ["Proposed method"] * 145

for setnum in range(5):
  set_list = [str((setnum+1)*5)]
  for hitonum in range(9):

    nn_pdall=pd.DataFrame(nn_all[setnum,hitonum,:])
    phi_pdall=pd.DataFrame(phi_all[setnum,hitonum,:])

    df_phi_in = pd.DataFrame(data=set_list*145,columns=["the number of supervisor data"],dtype='int')
    df_nn_way = pd.DataFrame({'way':nn_way_list},columns=["way"],dtype='object',index=range(145))
    df_phi_way = pd.DataFrame({'way':phi_way_list},columns=["way"],dtype='object',index=range(145))

    df_nn_data = pd.DataFrame(data=nn_pdall,dtype='float',index=range(145))
    df_phi_data = pd.DataFrame(data=phi_pdall,dtype='float',index=range(145))
    df_nn_data.columns = [str(hitonum)]
    df_phi_data.columns = [str(hitonum)]
#df_nn_data = pd.DataFrame(data=nn_ave,columns=["0","1","2","3","4","5","6","7","8"],dtype='float',index=[0,1,2,3,4])
#df_phi_data = pd.DataFrame(data=phi_ave,columns=["0","1","2","3","4","5","6","7","8"],dtype='float',index=[0,1,2,3,4])

    df_nn = pd.concat([df_phi_in,df_nn_way,df_nn_data],axis=1)
    df_phi= pd.concat([df_phi_in,df_phi_way,df_phi_data],axis=1)

    nn_melt = pd.melt(df_nn, id_vars=['the number of supervisor data','way'],var_name='hito')
    phi_melt = pd.melt(df_phi, id_vars=['the number of supervisor data','way'],var_name='hito')

    if((setnum == 0)and(hitonum==0)):
      df_nn_all = nn_melt
      df_phi_all = phi_melt

    else:
      df_nn_all = pd.concat([df_nn_all,nn_melt],axis=0)
      df_phi_all = pd.concat([df_phi_all,phi_melt],axis=0)

data = pd.concat([df_nn_all,df_phi_all])
data_new = data.rename(columns={'value':str_label})
#data_new = data.rename(columns={'value':'correlation between estimated mood and self-assessed mood'})
print(data)

plt.figure(figsize=(8,6))
sns.set(style='whitegrid',palette='bright')
sns.set_context(font_scale=10)
#sns_plot = sns.boxplot(x='the number of supervisor data',y=str_label,hue='way',data=data_new)
sns_plot = sns.pointplot(x='the number of supervisor data',y=str_label,hue='way',data=data_new,capsize=.2)

#sns_plot = sns.pointplot(x='the number of supervisor data',y='correlation between estimated mood and self-assessed mood',hue='way',data=data_new,capsize=.2)

#plt.ylim([0,0.3])

fig = sns_plot.get_figure()
plt.show()
#plt.savefig('5-30_compare_'+flag+'.eps')
