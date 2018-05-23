# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:42:06 2016

@author: Administrator
"""
import matplotlib.pyplot as plt
import numpy as np

F=open('2016628_MappingTest2.txt','r')
lines=F.readlines()
result=[]
for x in lines:
    result.append(x.split('\t'))
F.close()

for i in range(len(result)):
    print result[i]

r=[]
c=[]

for i in range(len(result)):
    try:
        r.append(float(result[i][4]))
        c.append(result[i][5])
    
    except (IndexError,ValueError):
        print 'Cannot be Converted'
    

print r,c

size=(3,3)
v=np.zeros(size)
print 'Done'

z=0
for i in range(3):
     for j in range(3):
         #print r[z]
         #print v[i][j]
         v[i][j]=r[z]
         #print v[i][j]
         z+=1
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
im=ax.imshow(v,extent=(0,3,0,3),interpolation='nearest')
cb=plt.colorbar(im)
plt.setp(cb.ax.get_yticklabels(),visible=True)
plt.show()

size=(3,3)
v=np.zeros(size)
print 'Done'

k=0
for i in range(3):
       for j in range(3):
           print c[k]
           print v[i][j]
           v[i][j]=c[k]
           print v[i][j]
           k+=1
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
im=ax.imshow(v,extent=(0,3,0,3),interpolation='nearest')
cb=plt.colorbar(im)
plt.setp(cb.ax.get_yticklabels(),visible=True)
plt.show()
