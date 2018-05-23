# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 16:03:27 2016

@author: Andreas Spielhofer
"""
import serial
import time
import numpy as _np


# configure the serial connections (the parameters differs on the device you are connecting to)

class Keithley():
    def __init__(self, port=None):
        print "Now initializing"
        try:
            print "Trying hard"
            if port is None:
                ser = serial.Serial(
                                    port='COM4',
                                    baudrate=9600,
                                    parity=serial.PARITY_NONE,
                                    stopbits=serial.STOPBITS_ONE,
                                    bytesize=serial.EIGHTBITS,
                                    xonxoff=0,
                                    rtscts=1,
                                    timeout=0.15
                                    )
                self.ser = ser
                self.port = port
                print self.ser.name
                print "Hallo"
            else:
                print "tried"
        except:
            self.ser.close()
            raise RuntimeError('Could not open serial connection')

        if self.ser is None:
            raise RuntimeError('Could not open serial connection')
            print "did not work"
        print('Keithley initialized on port %s' %self.ser.name)
        self.ser.write('*IDN?' + '\r')
        time.sleep(0.1)
        self.firmware = self.ser.readline()
        print('Firmware Version:'+ self.firmware)
#        print "Hallo."

        
    def _close_connection(self):
        self.ser.close()
        print('Connection closed')
        
    def _open_connection(self):
        self.ser.open()
        
    
    # Set the Keithley to measure current.
    def _current_mode(self):
        self.ser.write("SOUR:FUNC VOLT"+ '\r')
        time.sleep(0.2)
        self.ser.write("SOUR:VOLT 0"+ '\r')
        time.sleep(0.2)
        self.ser.write("CONF:CURR"+ '\r')
        time.sleep(0.2)
        self.ser.write("FORM:ELEM CURR"+ '\r')

        time.sleep(1)
    
    
    # Open the connection to the Prologix USB/GPIB interface and configure
    # it to communicate with the Keithley 2400.

        
    
    # Set up the Keithley 2400 to provide live readings.
    def _enable_live_readings(self):
        self.ser.write("ARM:COUN INF")  # infinite arm count
        self.ser.write("TRIG:DEL 0")    # zero trigger delay
        self.ser.write("INIT")          # start measurements
    
    
    # This function is a placeholder to maintain compatibility with the 
    # keithley617 module.
    def _enable_voltage_source(self):
        pass
    
    
    # This function is primarily a placeholder to maintain compatibility 
    # with the keithley617 module, it sets the output of the Keithley's 
    # internal voltage source to zero Volts.
    def _disable_voltage_source(self):
        self.ser.write("SOUR:VOLT 0")
    
    
    # This function is the default value of the function parameter for the
    # read function below.
    def _do_nothing(self, *dummy):
        pass
    
    
#    # Read a specified number of measurement samples from the keithley at a
#     #specified sample period.
#    def _read(self, interval = 0, samples = 1, update_graph = _do_nothing, *args):
#      self.ser.write("ARM:COUN 1")              # arm instrument
#      self.ser.write("TRIG:COUN %d" % samples)  # setup trigger count
#      elf.ser.write("TRIG:DEL %f" % interval)  # setup trigger delay
#      Time = []
#      Data = []
#      CurrentSample = 0
#      self.ser.write("READ?")          # start measurement
#      while len(Data) < samples:
#        while CurrentSample < len(Data):
#          update_graph(Time[CurrentSample], Data[CurrentSample], figure)
#          CurrentSample = CurrentSample + 1
#        time.sleep(interval)
#        DataString = self.ser.readline()
#        DataString = DataString.split(',')
#        for i in range(len(DataString)):
#          if len(DataString[i]) > 0:
#            #print DataString[i]
#            if DataString[i] != '\x00\x00\x00':  # some 2400s return this if no data
#              Time.append(float(len(Data) * interval))
#              Data.append(float(DataString[i]))
#      while CurrentSample < len(Data):
#        update_graph(Time[CurrentSample], Data[CurrentSample], *args)
#        CurrentSample = CurrentSample + 1
#    
#      if samples > 1:
#        return Time, Data
#      else:
#        return Data[0]
#    
        
    # Set the Keithley to measure resistance.
    def _resistance_mode(self):
        self.ser.write("CONF:RES" + '\r')
        time.sleep(0.1)
        self.ser.write("FORM:ELEM RES"+ '\r')
    
    
    # Set the value of the Keithley's internal voltage source.
    def _set_voltage_source(self, voltage):
        if abs((voltage / 5e-6) - round(voltage / 5e-6)) > 1e-10:
            print 'Warning: The voltage source in the Keithley 2400 has a ' \
            'maximum resolution of 5 uV.'
        self.ser.write("SOUR:VOLT " + str(voltage)+ '\r')
    
    
    # This function sets the Keithley to measure voltage.
    def _voltage_mode(self):
        self.ser.write("SOUR:FUNC CURR"+ '\r')
        time.sleep(0.1)
        self.ser.write("SOUR:CURR 0"+ '\r')
        time.sleep(0.1)
        self.ser.write("CONF:VOLT"+ '\r')
        time.sleep(0.1)
        self.ser.write("FORM:ELEM VOLT"+ '\r')
        time.sleep(1)
        
    def _output(self, status):
        if status == "ON":
            self.output = "ON"
            self.ser.write("OUTP ON" +'\r')
        elif status == "OFF":
            self.output = "OFF"
            self.ser.write("OUTP OFF" +'\r')
        else:
            print('Input not vaild. Write as argument "OFF" or "ON"')
    
    def _measure(self):
        self.ser.write("TRIG:COUN 1" + '\r')
        self.ser.write("INIT" + "\r")
        self.ser.write("read?" + '\r')
        meas = self.ser.readline()
        print(meas)
    
    
    
#    def _voltswipe(self,minimum, maximum, stepsize):
#
#            if minimum in range(-11,11) and maximum in range(-11,11):
#                if minimum <= maximum:
#                    self.minimum = float(minimum)  
#                    self.maximum = float(maximum)
#                    self.stepsize = float(stepsize)
#  
#                    newvalue = self.minimum
#                                
#                    while newvalue <= maximum:
#                        self.newvalue = newvalue
#                        if self.newvalue < stepsize :
#                            self.newvalue = float(-stepsize/2)
#                            print self.newvalue
#                            self.ser.write(':SOUR:VOLT:LEV:IMM:AMPL ' +str(self.newvalue)+ "\r")
#                        #time.sleep(3)
#                        #self.ser.write("*RST" + "\r")  # Reset instrument to default parameters.
#                        #self.ser.write(":SENS:FUNC 'RES'" + "\r")  #Select ohms measurement function#k.ser.write(":SENS:RES:NPLC 1" + "\r")  #Set measurement speed to 1 PLC
#                        #self.ser.write(":SENS:RES:MODE MAN" + "\r")  #Select manual ohms mode.
#                        #self.ser.write(":SOUR:FUNC VOLT" + "\r")  #Select voltage source function.
#                        #self.ser.write(":SOUR:VOLT " +str(self.newvalue) + "\r")     #Set source to output 10mA.
#                        #self.ser.write(":SOUR:CLE:AUTO ON" + "\r")  #Enable source auto output-off.
#                        #self.ser.write(":SENS:VOLT:PROT 10" + "\r")  #Set 10V compliance limit.
#                        #self.ser.write(":TRIG:COUN 10" + "\r")  #Set to perform one measurement.
#                        
#                        self.ser.write(':SOUR:VOLT:LEV:IMM:AMPL ' +str(self.newvalue)+ "\r")
#                        #self.ser.write(":SENS:FUNC 'RES'" + "\r")  #Select ohms measurement function
#                        #time.sleep(2)
#                        self.ser.write(":READ?" + "\r")  #Select ohms measurement function
#                        time.sleep(0.1)
#                        data = self.ser.readline()
#                 
#                        print self.newvalue
#                        #print data
#                        newvalue = self.newvalue + self.stepsize
#                        time.sleep(0.5)
#                        
#                                                
#                else:
#                    print('Error: maximum has to be greater than minimum')
#            else:
#                print("voltage out of range -10,10")
#                
    #def voltread(self, voltage, sampling):
    def voltread(self, voltage):           
        
        """
        This function reads the votlage.
        """
        #self.ser.write("*RST" + "\r")  # Reset instrument to default parameters.
        #time.sleep(0.1)
        #self.ser.write(":SENS:FUNC 'RES'" + "\r")  #Select ohms measurement function#k.ser.write(":SENS:RES:NPLC 1" + "\r")  #Set measurement speed to 1 PLC
        #time.sleep(0.1)        
        #self.ser.write(":SENS:RES:MODE MAN" + "\r")  #Select manual ohms mode.
        #time.sleep(0.1)        
        #self.ser.write(":SOUR:FUNC VOLT" + "\r")  #Select voltage source function.
        #time.sleep(0.1)
        #self.ser.write(":SOUR:CLE:AUTO ON" + "\r")  #Enable source auto output-off.
        #time.sleep(0.1)
        #self.ser.write(":SENS:VOLT:PROT 10" + "\r")  #Set 10V compliance limit.
        #time.sleep(0.1)
        #self.ser.write(":TRIG:COUN " +str(sampling) + "\r")  #Set to perform one measurement.
        #time.sleep(0.1)
        #self.ser.write(":SENS:FUNC 'RES'" + "\r")  #Select ohms measurement function  
        #time.sleep(0.1)
        #self.ser.write(":SYST:RSEN ON" + "\r")  #Select ohms measurement function  
        if -11.0 <= voltage <=  11.0:
           
           
            #self.ser.write(":SOUR:VOLT " +str(voltage) + "\r")     #Set source to output 10mA.
            if voltage == 0.0:
                voltage = 0.1
            time.sleep(0.1)
            self.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(voltage) +'\r')
            self.ser.write(":READ?" + "\r")  #Select ohms measurement function
            time.sleep(0.3)
            data = self.ser.readline()

            data = _np.array([float(item) for item in data.split(',')])

            #data.reshape(int(sampling),5)
            #print data
            #data = data.reshape(int(sampling),5)
            #print data
            return data
            
        else:
            print "The voltage is out of the range"
            return
            
        
    def currentread(self,current):
        """
        This function reads the current
        """
        if -0.1 <= current <= 0.1:
            
            if current == 0.0:
                current=1e-8
            self.ser.readline()
            self.ser.write(':SOUR1:CURR:LEV:IMM:AMPL '+str(current)+'\r')
            self.ser.write(':READ?'+'\r')
            time.sleep(0.2)
            data=self.ser.readline()
            #print data
            data=_np.array([float(item) for item in data.split(',')])
            #print data
            return data
        
    def _format(self):
        self.ser.write('format:elements?' +'\r')
        print self.ser.readline()
        
   

#                         
            
#            k.ser.write(":READ?" + "\r")  #Select ohms measurement function
#            time.sleep(0.1)
#            data = k.ser.read(80)
            
#    def approach(self):
#        self.ser.write(":SENS:FUNC:CONC ON\r") # Concurrent on
#
#        self.ser.write(":SYST:RSEN ON\r")     # Set system to 4-Wire
#         
#        self.ser.write(":SYST:AZER:CACH ON\r")    # Enable/disable NPLC caching
#         
#        self.ser.write(":ROUT:TERM FRON \r") # sets the output to the Front Terminals 
#        self.ser.write(":SENS:RES:MODE MAN \r") #Select manual ohms mode.
#        self.ser.write(":SENS:FUNC:OFF:ALL \r")
#        self.ser.write(':SENS:FUNC "VOLT"\r')
#        self.ser.write(':SENS:FUNC "RES"\r')
#        self.ser.write(':SENS:FUNC "CURR"\r')
#        self.ser.write(":SENS:VOLT:RANG:AUTO ON \r") # Enable auto volts range
#        self.ser.write(":SENS:RES:RANG:AUTO ON \r") # Enable auto resistance range
#        self.ser.write(":SENS:VOLT:PROT:LEV " + str(11) + "\r") # set voltage protection level
#        self.ser.write(":SENS:CURR:PROT:LEV " + str(0.1) + "\r") # set current protection level
#
#        self.ser.write(":SOUR:FUNC:MODE VOLT\r") # Sets source to Volt mode
#        self.ser.write(":SOUR:VOLT:RANG:AUTO ON \r")
#        self.ser.write(":SOUR:CURR:RANG:AUTO ON \r")
#        self.ser.write(":SOUR:VOLT:PROT:LEV " + str(11) + "\r") 
#        self.ser.write(":SOUR:DEL:AUTO ON \r") # source delay auto on
#        self.ser.write(":SOUR:CLE:AUTO OFF \r") #enable auto-clear for source
#        self.ser.write(":SOUR:VOLT:MODE FIX \r")
#        self.ser.write(":TRIG:COUN 1" + "\r")
#        self.ser.write(":SENS:AVER:TCON REP \r")  #look into this what this does. It has to do with filtering
#        self.ser.write(":SENS:AVER:COUN "+ str(1) +"\r") # read the same data point multiple times and average the measured values
#        self.ser.write(":SENS:AVER:STAT ON \r")
#        self.ser.write(":OUTP:STAT ON \r") # output on
#        
#        voltage = 5.0
#        
#        while True:
#            try:
#                self.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(5) +'\r')
#                time.sleep(0.2)
#                self.ser.write(":READ?" + "\r")  #Select ohms measurement function
#                time.sleep(0.3)
#                approachvalue = self.ser.readline()
#                print approachvalue
#                approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
#                voltage = approachvalue[0]
#            
#                time.sleep(0.2)
#                print voltage
#                return
#                
#            except ValueError:
#                print "Approached due to error"
#                self.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(5) +'\r')
#                time.sleep(0.2)
#                self.ser.write(":READ?" + "\r")  #Select ohms measurement function
#                time.sleep(0.3)
#                approachvalue = self.ser.readline()
#                print approachvalue
#                approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
#                voltage = approachvalue[0]
#                
#                return
#    
    def beep(self):
        self.ser.write(":SYST:BEEP 200,1 \r") # makes a beep sound
#        
#    def sweeper(self,start,stop,step):
#        self.ser.write("*RST" + "\r")
#        self.ser.write(":SYST:RSEN ON\r")     # Set system to 4-Wire
#        self.ser.write(":ROUT:TERM FRON \r") # sets the output to the Front Terminals 
#        self.ser.write(":SENS:RES:MODE MAN \r") #Select manual ohms mode.
#        self.ser.write(":SENS:FUNC:OFF:ALL \r")
#        self.ser.write(':SENS:FUNC "VOLT"\r')
#        self.ser.write(':SENS:FUNC "RES"\r')
#        self.ser.write(':SENS:FUNC "CURR"\r')
#        self.ser.write(":SENS:VOLT:RANG:AUTO ON \r") # Enable auto volts range
#        self.ser.write(":SENS:RES:RANG:AUTO ON \r") # Enable auto resistance range
#        self.ser.write(":SENS:VOLT:PROT:LEV " + str(11) + "\r") # set voltage protection level
#        self.ser.write(":SENS:CURR:PROT:LEV " + str(0.1) + "\r") # set current protection level
#        
#        self.ser.write(":SOUR:FUNC:MODE VOLT\r")
#
#        self.ser.write(":SOUR:VOLT:PROT:LEV " + str(11) + "\r") 
#        self.ser.write(":SOUR:SWE:SPAC LIN\r")
#        self.ser.write(":SOUR:VOLT:STAR " + str(start) +"\r")
#        self.ser.write(":SOUR:VOLT:STOP " + str(stop) +"\r")
#        self.ser.write(":SOUR:VOLT:STEP " + str(step) +"\r")
#        self.ser.write(":SOUR:SWE:POIN?\r")
#        points = int(self.ser.readline())
#        print points
#        self.ser.write(":TRIG:COUN " + str(points) +"\r")
#        self.ser.write(":TRIG:DEL 0\r")        
#        self.ser.write(":SENS:AVER:COUN "+ str(1) +"\r") # read the same data point multiple times and average the measured values
#        self.ser.write(":SOUR:VOLT:MODE SWE\r")
#        self.ser.write(":SOUR:DEL:AUTO OFF\r")
#        self.ser.write(":SOUR:DEL 0\r")          
#        self.ser.write(":OUTP ON\r") # output on
#        self.ser.write(":INIT"+"\r")
#        self.ser.readline()
#        
#
#        if points <10:
#            time.sleep(5)
#        elif points <50:
#            time.sleep(5)
#        elif points <100:
#            time.sleep(5)
#        elif points <150:
#            time.sleep(5)
#        else:
#            time.sleep(5)
#            
#        self.ser.write(":READ?" + "\r")
#        data1 = self.ser.readline()
#
#        data1 = _np.array([float(item) for item in data1.split(',')])
#        print data1
#        data2 = self.ser.readline()
#        data2 = _np.array([float(item) for item in data2.split(',')])
#        print data2
#        
#        
#        self.ser.write(":OUTP OFF\r") # output on
    
    
#    ################# OLD STUFF BELOW ######################
#    
#    # This function is called by the read function in the event that 
#    # samples > 1.
#    def _read_old(self, interval = 0, samples = 1, update_graph = _do_nothing):
#      RAV = 1 << 6
#      ser.write("TRIG:COUN 1")      # setup trigger count
#      ser.write("TRIG:DEL %f" % interval)  # setup trigger delay
#      Time = []
#      Data = []
#      CurrentSample = 1
#      Datum = ser.readline()
#      ser.write("INIT")          # start measurement
#      while CurrentSample <= samples:
#        reading_available = 0
#        while not reading_available:
#          #print str(measurement_event) + ", " + str(reading_available)
#          time.sleep(interval)
#          ser.write("STAT:MEAS?")    # read measurement event register
#          ser.write("++read 10")
#          measurement_event = int(ser.readline())
#          reading_available = measurement_event & RAV
#        ser.write("FETC?")
#        ser.write("++read 10")
#        ser.write("INIT")          # start measurement
#        Datum = ser.readline()
#        #print Datum
#        #Data = Data + [float(Datum[4:Datum.find(',')])]
#        Data = Data + [float(Datum)]
#        Time = Time + [(CurrentSample - 1) * interval]
#        CurrentSample = CurrentSample + 1
#        update_graph(Time[-1], Data[-1])     # call graph update function 
#      ser.write("ARM:COUN INF")      # return instrument to live mode
#      ser.write("TRIG:DEL 0")
#      ser.write("INIT")          # start measurements
#      if samples > 1:
#        return Time, Data
#      else:
#        return float(Datum)
#    
#    
#    # This function is called by the read function in the event that 
#    # samples = 1.
#    def _read_one(self, interval = 0):
#      #gpib.write("ARM:COUN 1")
#      #gpib.write("ARM:SOUR BUS")
#      ser.write("TRIG:COUN 1")      # setup trigger count
#      ser.write("TRIG:DEL %f" % interval)  # setup trigger delay
#      ser.write("INIT")          # start measurement
#      #gpib.write("*TRG")
#    
#      ser.write("STAT:MEAS?")        # read measurement event register
#      ser.write("++read 10")
#      measurement_event = int(ser.readline())
#      RAV = 1 << 6
#      reading_available = measurement_event & RAV
#      while not reading_available:
#        #print str(measurement_event) + ", " + str(reading_available)
#        time.sleep(interval)
#        ser.write("STAT:MEAS?")      # read measurement event register
#        ser.write("++read 10")
#        measurement_event = int(ser.readline())
#        reading_available = measurement_event & RAV
#      #gpib.write("*CLS")          # clear event registers
#      #time.sleep(interval)
#      ser.write("FETC?")
#      ser.write("++read 10")
#      Datum = ser.readline()
#      print "reading: " + Datum
#      return Datum


# This function reads values from the Keithley at a specified sample interval
# (in seconds). All timing is controlled by the Keithley. If only one sample is 
# requested the function returns the second sample taken by the Keithley, 
# otherwise it returns the first n samples.
# For example, Read(10) returns one sample that is taken 10 seconds after the
# function is called while Read(10, 2) returns two samples, the first one is 
# taken immediately when the function is called and the second sample is taken
# 10 seconds later.
# If more than one sample is requested, the allowed values of the interval 
# parameter are 0, 1, 10, 60, 600, and 3600. If only one sample is requested,
# the allowed values of interval are 0 through 99.
# The allowed values of the samples parameter are 1 to 100.
#    def read_old(interval = 0, samples = 1, update_graph = _do_nothing):
#      if samples > 1:
#        return _read_multiple(interval, samples, update_graph)
#      else:
#        return _read_one(interval)

# examples:
# DISP:ENAB ON
# DISP:ENAB OFF
# DISP:ENAB?
# *IDN?

#k = Keithley()

# Example from Manual:
#k.ser.write("*RST" + "\r")  # Reset instrument to default parameters.
#k.ser.write(":SENS:FUNC 'RES'" + "\r")  #Select ohms measurement function
#k.ser.write(":SENS:RES:NPLC 1" + "\r")  #Set measurement speed to 1 PLC
#k.ser.write(":SENS:RES:MODE MAN" + "\r")  #Select manual ohms mode.
#k.ser.write(":SOUR:FUNC CURR" + "\r")  #Select current source function.
#k.ser.write(":SOUR:CURR 0.01" + "\r")     #Set source to output 10mA.
#k.ser.write(":SOUR:CLE:AUTO ON" + "\r")  #Enable source auto output-off.
#k.ser.write(":SENS:VOLT:PROT 10" + "\r")  #Set 10V compliance limit.
#k.ser.write(":TRIG:COUN 1" + "\r")  #Set to perform one measurement.
#k.ser.write(":SENS:FUNC 'RES'" + "\r")  #Select ohms measurement function
#k.ser.write(":READ?" + "\r")  #Select ohms measurement function
#time.sleep(0.1)
#data = k.ser.read(80)
#print data

#k = Keithley()
#time.sleep(1)
#k.ser.write(":FORM:ELEM?" + "\r")
#time.sleep(0.2)
#print(k.ser.readline())



