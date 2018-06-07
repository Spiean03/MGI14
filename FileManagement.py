# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:13:01 2016

@author:    Andreas Spielhofer
            Ph.D. Candidate
            Physics Departement
            McGill University
            Montreal, Canada
@contact:   andreas.spielhofer@mail.mcgill.ca
"""

import os.path
import datetime as _dt

class FileManagement():
    def __init__(self,directory,text,description):
        self.d=_dt.datetime.now()
        self.i=text
        self.g=directory
        
#        self.l=pox.find(str(self.d.year)+str(self.d.month)+str(self.d.day)+'_'+self.i+'.txt')
#        print self.l
        j=0
        i=True
        if os.path.isfile(self.g+'\\'+str(self.d.year)+str(self.d.month)+str(self.d.day)+'_'+self.i+'.txt'):
            print 'File exists'
            while i==True:
                
                if os.path.isfile(self.g+'\\'+str(self.d.year)+str(self.d.month)+str(self.d.day)+'_'+self.i+'('+str(j+1)+').txt'):
                    print 'File exists'
                    j+=1
                else:
                    self.f=open(self.g+'\\'+str(self.d.year)+str(self.d.month)+str(self.d.day)+'_'+self.i+'('+str(j+1)+').txt','w')
                    self.n=self.g+'\\'+str(self.d.year)+str(self.d.month)+str(self.d.day)+'_'+self.i+'('+str(j+1)+').txt'
                    i=False
                    
        else:
            self.f=open(self.g+str(self.d.year)+str(self.d.month)+str(self.d.day)+'_'+self.i+'.txt','a')
            self.n=self.g+'\\'+str(self.d.year)+str(self.d.month)+str(self.d.day)+'_'+self.i+'.txt'
            
                    
                    
            
            
        self.f.write('Description: '+ description)
        self.f.close()
        
        return 
    
    
    def _newline(self):
        self.f=open(self.n,mode='a')
        self.f.write('\n')
        self.f.close()
        return
	
    def _writefile(self,text):
        self.f=open(self.n,mode='a')
        self.f.write(text)
        self.f.close()
        return

    def _tab(self):
        self.f=open(self.n,mode='a')
        self.f.write('\t')
        self.f.close()
        return
    def _readlines(self):
        self.f=open(self.n,mode='r')
        lines=self.f.readlines()
        result=[]
        #result2=[]
        for x in lines:
            result.append(x.split('\t'))
        self.f.close
        return result
    
    
        
        
        
        
            


        
        
        
