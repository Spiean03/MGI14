# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 18:18:26 2017

@author:    Andreas Spielhofer
            Ph.D. Candidate
            Physics Departement
            McGill University
            Montreal, Canada
@contact:   andreas.spielhofer@mail.mcgill.ca
"""


import serial
import time

class Arduino():
    def __init__(self, port=None):
        try:
            if port is None:
                s= serial.Serial(
                                    port='COM26',
                                    baudrate=9600,
                                    timeout=1
                                    )
                self.s = s
                self.port = port
                print self.s.name
            else:
                print "Problems with Connecting"
        except:
            self.s.close()
            raise RuntimeError('Could not open Serial Connection')
        if self.s is None:
            raise RuntimeError('Could not open Serial Connection')
            print "Did not work"
        print('Arduino initialized on Port %s' %self.s.name)
        self.s.write("Connected to Arduino Micro\n")
        time.sleep(0.1)
        self.firmware = self.s.readline()
        print(self.firmware)
        
    def switch(self,pin,status):
        """
        status = 0 : turn all LEDs off
        status = 1 : turn all LEDs on
        Digital pins available: 2-13
        Analog pins available: 14(A0)-19(A5)
        """
        if pin ==14:    #Analog Output A0
            pin = "A0"
        if pin == 15:    #Analog Output A1
            pin = "A1"
        if pin == 16:    #Analog Output A2
            pin = "A2"
        if pin == 17:    #Analog Output A3
            pin = "A3"
        if pin == 18:    #Analog Output A4
            pin = "A4"
        if pin == 19:    #Analog Output A5
            pin = "A5"
        
        if status == 1: #Turn on
            self.message = str(pin)+str("on\n")
        if status == 0: #Turn off
            self.message = str(pin)+str("off\n")
        self.send()    

    def send(self):
        #print self.message
        self.s.write(self.message)
        #print self.s.readline()
        #self.msg = self.s.readline()
        #print "Message from arduino: "+ str(msg)
        
    def close(self):
        self.s.close()        
           
    def switch_all(self,status): 
        '''
        status = 0 : turn all LEDs off
        status = 1 : turn all LEDs on
        '''
        for i in range (2,20):
            print i
            self.switch(i,status) 

    def LED_on(self,pin):
        if pin ==14:
            pin = "A0"
        if pin == 15:
            pin = "A1"
        if pin == 16:
            pin = "A2"
        if pin == 17:
            pin = "A3"
        if pin == 18:
            pin = "A4"
        if pin == 19:
            pin = "A5"

        self.message = str(pin)+str("on\n")
        self.send()
    
    def LED_off(self,pin):
        if pin ==14:
            pin = "A0"
        if pin == 15:
            pin = "A1"
        if pin == 16:
            pin = "A2"
        if pin == 17:
            pin = "A3"
        if pin == 18:
            pin = "A4"
        if pin == 19:
            pin = "A5"
        self.message = str(pin)+str("off\n")
        self.send()


        