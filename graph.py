import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

data = pd.read_csv(r'C:/Users/Administrator/Desktop/file1.csv',encoding='gbk')
data = data.sort_values(by = ['单位缴存人数'],axis=0,ascending=True)
X = data['单位缴存人数'].values
yu_e = data['单位账户余额'].values
jiaocun_e = data['单位月缴存额'].values
ge_ren = data['个人缴存基数'].values


# for i in range(len(X)):
#     if X[i] > 100000:
#          print(X[i],i)

bili = jiaocun_e / ge_ren
            
# X = np.delete(X,49636)
# yu_e = np.delete(yu_e,49636)
# jiaocun_e =np.delete(jiaocun_e,49636)
# ge_ren = np.delete(ge_ren,49636)
# jiaocun_renshu = np.delete(jiaocun_renshu,49636)

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(6,4),dpi=144)
plt.xlabel('单位缴存人数')
plt.ylabel('单位账户余额')
plt.plot(X,yu_e,linewidth=2)


plt.show()

plt.figure(figsize=(6,4),dpi=144)
plt.plot(X,jiaocun_e,linewidth=2)
plt.xlabel('单位缴存人数')
plt.ylabel('单位月缴存额')
plt.show()
jiaocun_e.shape

plt.figure(figsize=(6,4),dpi=144)
plt.plot(X,ge_ren,linewidth=2)
plt.xlabel('单位缴存人数')
plt.ylabel('个人缴存基数')
plt.show()
jiaocun_e.shape

x= [5,6,7,8]
y= [10.0,6,7,8]
x=np.array(x)
y=np.array(y)
z = x/y
z

plt.figure(figsize=(6,4),dpi=144)
plt.plot(X,bili,linewidth=2)
plt.xlabel('单位缴存人数')
plt.ylabel('比例')
plt.show()