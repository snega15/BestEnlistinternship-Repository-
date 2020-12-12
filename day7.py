import sys,os
file=sys.argv[0]
pathname=os.path.dirname(file)
print(pathname)


#
import numpy as np
k=np.random.randint(1,100)
print(k)

#
import pandas as pd
k=pd.array([1,2,3])
m=pd.datatime(2020,4,1)
print(pd._version)
print(k,m)
k=['e1','e2']
pd.set_option('display.max_rows',2)
pd.set_option('display.max_columns',2)
df=pd.read_csv('3.csv')
df.e4.value_counts().plot(kind='bar')

#
from listc import "
for i in range(len(11)):
    l1[i]=l1[i]+20
print(11)
'''
second method:
import listc as li
k=[]
k=li.l1
for i in range(len(k)):
   k[i]=k[i]+10
print(k)'''   

