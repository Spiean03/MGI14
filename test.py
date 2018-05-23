# -*- coding: utf-8 -*-

"""
Created on Mon May 30 11:24:11 2016

@author: Administrator
"""
import FileManagement

f=FileManagement.FileManagement('C:\\Users\\Administrator\\Desktop','lol','lol')
#print f

f._newline()
"""
for i in range(10):
    f._newline()
    for j in range(5):
        f._writefile(str(j)+'\t')
    print i
"""
k=[1,2,3,4,5,6]
g=[7,8,9,10,11,12]

for p in range(len(k)):
    f._writefile(str(k[p]))
    f._tab()
    f._writefile(str(g[p]))
    f._newline()


    
"""   
f._writelist(k)
f._newline()
f._writelist(g)
"""

print 'Finished'

"""
c=raw_input('Nom de fichier: ')

g=open(c+'.txt','w')

g.close()
"""