"""
Created on Tue Mar 08 14:45:27 2015
@author:    Andreas Spielhofer
            Ph.D. Candidate
            Physics Departement
            McGill University
            Montreal, Canada
@contact:   andreas.spielhofer@mail.mcgill.ca
"""

from spinmob import egg
import spinmob
import Keithley as _k
import _base as _b
import _coordinates as _c
import _calibration as _d
import time
import numpy as _np
import FileManagement as _f
import matplotlib.pyplot as plt
import sys
import subprocess
import arduino_test_class as _a

#import CameraAndreas as _a

#creating a window w/ tabs

w=egg.gui.Window('Micromanipulator Graphical Interface', autosettings_path='wa.txt')#The window is created
w.set_column_stretch(1,100)
tabs1=w.place_object(egg.gui.TabArea(autosettings_path='tabs1a.txt'))#Tab area containing manipulator, 4-point probe and connection tabs
tabs2=w.place_object(egg.gui.TabArea(autosettings_path='tabs2a.txt'))#Tab area containing measurment and mapping tabs
tabs3=w.place_object(egg.gui.TabArea(autosettings_path='tabs3a.txt'))#Tab area containing file tab

#adding tabs
t_manipulator=tabs1.add_tab('Manipulator')#Tab containing manipulator controllings buttons and functions
t_point_probe=tabs1.add_tab("4 Point-Probe")#Tab containing parameters needed for measure and measure making measures
t_connect=tabs1.add_tab('Connect')#Tab containing connections of different measure instruments

t_approach=tabs2.add_tab("Approach") #Tab containing the I and V measured while approaching
t_measurments=tabs2.add_tab("Measurements")

t_mapping=tabs2.add_tab('Mapping')#Tab containing results of the measurments in a map format
t_textfile=tabs3.add_tab('File') #Tab containing file creation widgets 
t_plot=tabs3.add_tab('Plot')#Tab containing functions to make pop up plots wanted

#load previous settings if present

tabs1.load_gui_settings()
tabs2.load_gui_settings()
tabs3.load_gui_settings()


class Arduino():
    def Connect_Arduino(self):
        self.arduino = _a.Arduino()
        return

class Manipulator():
    """
    This class has all the methods used to move the manipulator and set its speed. 
    """
    
    def Connect_Manipulator(self):
        """
        Connects Manipulator and make it an object so its methods can be used.
        """
        self.n=_b.NanoControl()
        self.d=_d.CalibrationDummy()
        self.d._configuration(1)
        self.n._coarse_reset()
        return
    
    def Counterread(self):
        """
        This function takes the counterread and put it in a list
        """
        A=self.n.position0
        B=self.n.position1
        C=self.n.position2
        P=[A,B,C]
        return P
    
    def Counterreset(self):
        """
        This function resets the counterread
        """
        self.n._coarse_reset()
    
    def set_speed(self,speed):
        """
        This function takes an integer and sets the speed
        """
        self.n._speed(speed)
        
    
    def speed_value(self):
        """
        This function get the value in the number box and assigns it to the speed
        """
        spd_value=int(nb_speed.get_value())#Integer speed value
        self.n._speed(spd_value)
        return
    
    def b_move_right(self):
        """
        Makes the manipulator moves right by a number of steps inputed into  the steps numberbox when the proper button is pushed
        """
        if int(self.n.speed0) <= 3:
            print 'fine'        
            self.n._fine('A',int(steps_value()))
            print 'fine checked'
            self.n._get_fine_counter()
            m.update_box_fine()
        if int(self.n.speed0) > 3:
            print 'coarse'
            self.n._coarse('A',int(steps_value()))
            print 'coarse checked'
            #P=m.Counterread()
            #m.update_box_coarse(P)
        else:
            print 'Error'
        print 'Moving right!'
    def b_move_left(self):
        """
        Makes the manipulator moves left by a number of steps inputed into  the steps numberbox when the proper button is pushed
        """
        if int(self.n.speed0) <= 3:
            print 'fine'        
            self.n._fine('A',-int(steps_value()))
            print 'fine checked'
            self.n._get_fine_counter()
        if int(self.n.speed0) > 3:
            print 'coarse'
            self.n._coarse('A',-int(steps_value()))
            print 'coarse checked'
            #P=m.Counterread()
            #m.update_box_coarse(P)
        else:
            print 'Error'
        print 'Moving left!'

    def b_move_up(self):
        """
        Makes the manipulator moves up by a number of steps inputed into  the steps numberbox when the proper button is pushed
        """
    
        if int(self.n.speed0) <= 3:
            print 'fine'        
            self.n._fine('B',-int(steps_value()))
            print 'fine checked'
            self.n._get_fine_counter()
            m.update_box_fine()
        if int(self.n.speed0) > 3:
            print 'coarse'
            self.n._coarse('B',-int(steps_value()))
            print 'coarse checked'
            #P=m.Counterread()
            #m.update_box_coarse(P)
        else:
            print 'Error'
        print 'Moving up!'
    
    def b_move_down(self):
        """
        Makes the manipulator moves down by a number of steps inputed into  the steps numberbox when the proper button is pushed
        """
        if int(self.n.speed0) <= 3:
            print 'fine'        
            self.n._fine('B',int(steps_value()))
            print 'fine checked'
            self.n._get_fine_counter()
            m.update_box_fine()
        if int(self.n.speed0) > 3:
            print 'coarse'
            self.n._coarse('B',int(steps_value()))
            print 'coarse checked'
            #P=m.Counterread()
            #m.update_box_coarse(P)
        else:
            print 'Error'
        print 'Moving down!'
    def b_move_extend(self):
        """
        Makes the manipulator extends by a number of steps inputed into  the steps numberbox when the proper button is pushed
        """
        if int(self.n.speed0) <= 3:
            print 'fine'        
            self.n._fine('C',-int(steps_value()))
            print 'fine checked'
            self.n._get_fine_counter()
            m.update_box_fine()
        if int(self.n.speed0) > 3:
            print 'coarse'
            self.n._coarse('C',-int(steps_value()))
            print 'coarse checked'
            #P=m.Counterread()
            #m.update_box_coarse(P)
        else:
            print 'Error'
        print 'Extending!'
    def b_move_retract(self):
        """
        Makes the manipulator retracts by a number of steps inputed into  the steps numberbox when the proper button is pushed
        """
        if int(self.n.speed0) <= 3:
            print 'fine'        
            self.n._fine('C',int(steps_value()))
            print 'fine checked'
            self.n._get_fine_counter()
            m.update_box_fine()
        if int(self.n.speed0) > 3:
            print 'coarse'
            self.n._coarse('C',int(steps_value()))
            print 'coarse checked'
            #P=m.Counterread()
            #m.update_box_coarse(P)
        else:
            print 'Error'
        print 'Retracting!'
        
    def update_box_fine(self,P):
        """
        Updates the number boxes in front of the fine counter label
        """
        
        A = P[0]
        B = P[1]
        C = P[2]
        nb_A_fine.set_value(A)
        nb_B_fine.set_value(B)
        nb_C_fine.set_value(C)    
        return
    def update_box_coarse(self):
        """
        Updates the number boxes in front of the coarse counter label
        """
        A = int(self.n.position0)
        B = int(self.n.position1)
        C = int(self.n.position2)
        nb_A_coarse.set_value(A)
        nb_B_coarse.set_value(B)
        nb_C_coarse.set_value(C)    
        return
    def distancetotravel(self,x,y,z,x2,y2,z2):
        """
        This function calculates the differrence in each coordinate from point A to point B    
        """
        speed = nb_speed.get_value()
        
        Xsteps = (x2-x)
        Ysteps = (y2-y)
        Zsteps = (z2-z)
        
        if speed == 1:
            if Xsteps < 0:
                xsteps=Xsteps*self.d.X[0]
            else:
                xsteps=Xsteps*self.d.X[1]
            if Ysteps < 0:
                ysteps=Ysteps*self.d.Y[0]
            else:
                ysteps=Ysteps*self.d.Y[1]
            if Zsteps < 0:
                zsteps=Zsteps*self.d.Z[0]
            else:
                zsteps=Zsteps*self.d.Z[1]
        if speed == 2:
           if Xsteps < 0:
                xsteps=Xsteps*self.d.X[2]
           else:
                xsteps=Xsteps*self.d.X[3]
           if Ysteps < 0:
                ysteps=Ysteps*self.d.Y[2]
           else:
                ysteps=Ysteps*self.d.Y[3]
           if Zsteps < 0:
                zsteps=Zsteps*self.d.Z[2]
           else:
                zsteps=Zsteps*self.d.Z[3]
        if speed == 3:
            if Xsteps < 0:
                xsteps=Xsteps*self.d.X[4]
            else:
                xsteps=Xsteps*self.d.X[5]
            if Ysteps < 0:
                ysteps=Ysteps*self.d.Y[4]
            else:
                ysteps=Ysteps*self.d.Y[5]
            if Zsteps < 0:
                zsteps=Zsteps*self.d.Z[4]
            else:
                zsteps=Zsteps*self.d.Z[5]
        if speed == 4:
            if Xsteps <= 0:
                xsteps=Xsteps*self.d.X[6]
            else:
                xsteps=Xsteps*self.d.X[7]
            if Ysteps <= 0:
                ysteps=Ysteps*self.d.Y[6]
            else:
                ysteps=Ysteps*self.d.Y[7]
            if Zsteps <= 0:
                zsteps=Zsteps*self.d.Z[6]
            else:
                zsteps=Zsteps*self.d.Z[7]
        if speed == 5:
            if Xsteps <= 0:
                xsteps=Xsteps*self.d.X[8]
            if Xsteps > 0:
                xsteps=Xsteps*self.d.X[9]
            if Ysteps <= 0:
                ysteps=Ysteps*self.d.Y[8]
            if Ysteps > 0:
                ysteps=Ysteps*self.d.Y[9]
            if Zsteps <= 0:
                zsteps=Zsteps*self.d.Z[8]
            if Zsteps > 0:
                zsteps=Zsteps*self.d.Z[9]
        if speed == 6 :
            if Xsteps <= 0:
                print 'asdf'
                xsteps=Xsteps*self.d.X[10]
            if Xsteps > 0:
                xsteps=Xsteps*self.d.X[11]
            if Ysteps <= 0:
                print'xD'
                ysteps=Ysteps*self.d.Y[10]
            if Ysteps > 0:
                ysteps=Ysteps*self.d.Y[11]
            if Zsteps <= 0:
                print 'lel'
                zsteps=Zsteps*self.d.Z[10]
            if Zsteps > 0:
                zsteps=Zsteps*self.d.Z[11]
        
        d=[xsteps,ysteps,zsteps]
        print d
        return d


    def move_up(self,steps):
        """
        Makes the manipulator extends by a number of steps inputed into  the steps numberbox when called by different functions
        """
           
        if int(self.n.speed0) <= 3:
            print 'fine'        
            self.n._fine('B',int(-steps))
            print 'fine checked'
            #self.n._get_fine_counter()
        elif int(self.n.speed0) > 3:
            print 'coarse'
            self.n._coarse('B',int(-steps))
            print 'coarse checked'
            self.n._get_coarse_counter()
        else:
            print 'Error'
        print 'Moving up!'
    
    def move_down(self,steps):
        """
        Makes the manipulator extends by a number of steps inputed into  the steps numberbox when called by different functions
        """
        
        if int(self.n.speed0) <= 3:
            #print 'fine'        
            self.n._fine('B',int(steps))
            #print 'fine checked'
            #self.n._get_fine_counter()
        elif int(self.n.speed0) > 3:
            #print 'coarse'
            self.n._coarse('B',int(steps))
            #print 'coarse checked'
            self.n._get_coarse_counter()
        else:
            print 'Error'
        print 'Moving down!'


    def move_right(self, microns):
        m.set_speed(4)
        while microns >= 50:
            steps = 21
            self.n._coarse('A',steps)
            microns -= 50
            time.sleep(1)

        while microns >= 10:
            steps = 6
            self.n._coarse('A',steps)
            microns -= 10
            time.sleep(1)
            
        if microns > 0:
            steps = int((microns/10)*6)
            self.n._coarse('A', steps)
            
            
    def move_left(self, microns):
        m.set_speed(4)
        while microns >= 50:
            steps = 20
            self.n._coarse('A',-steps)
            microns -= 50
            time.sleep(1)

        while microns >= 10:
            steps = 5
            self.n._coarse('A',-steps)
            microns -= 10
            time.sleep(1)
            
        if microns > 0:
            steps = int((microns/10)*5)
            self.n._coarse('A',-steps)
            
        
    def move_extend(self, microns):
        m.set_speed(4)
        while microns >= 5:
            steps = 10
            self.n._coarse('C',-steps)
            microns -= 5
            time.sleep(1)
            
        if microns > 0:
            steps = int((microns/5)*10)
            self.n._coarse('C', -steps)
            
        
    def move_retract(self, microns):
        m.set_speed(4)
        while microns >= 30:
            steps = 100
            self.n._coarse('C',steps)
            microns -= 30
            time.sleep(1)
                    
        while microns >= 20:
            steps = 85
            self.n._coarse('C',steps)
            microns -= 20
            time.sleep(1)
                    
        while microns >= 5:
            steps = 10
            self.n._coarse('C',steps)
            microns -= 5
            time.sleep(1)
            
        if microns > 0:
            steps = int((microns/5)*10)
            self.n._coarse('C',steps)
            
class Keithley():
    """
    In this class, there is alle the methods
    """
    def Connect_Keithley(self):
        """
        Connects Keithley and make it an object so its methods can be used.
        """
        self.k=_k.Keithley()
        self.f_c=_c.FourPointProbeCoordinates()
        return
        
        
    def forward(self,p,y,x):
        """
        Converts pyx into XYZ coordinates
        """
        forward=self.f_c.forward(p,y,x)
        return forward
        
        
    def update_coordinates_XYZ(self):
        """
        Updates XYZ numberboxes
        """
        p=nb_p.get_value()
        y=nb_y.get_value()
        x=nb_x.get_value()
        forward=self.f_c.forward(p,y,x)
        a=forward[0]
        b=forward[1]
        c=forward[2]
        nb_X.set_value(a)
        nb_Y.set_value(b)
        nb_Z.set_value(c)    
        return
        
        
    def update_coordinates_pyx(self):
        """
        Updates pyx numberboxes
        """
        x=nb_X.get_value()
        y=nb_Y.get_value()
        z=nb_Z.get_value()
        reverse=self.f_c.reverse(x,y,z)
        a=reverse[0]
        b=reverse[1]
        c=reverse[2]
        nb_p.set_value(a)
        nb_y.set_value(b)
        nb_x.set_value(c)    
        return
        
        
    def sweep(self):
        """
        This function verify if the sweep is done in voltage or current mode to sweep samples
        """
        if s['Sweep/Source']=='Voltage':
            K.volt_sweep()
        elif s['Sweep/Source']=='Current':
            K.current_sweep()
        else:
            raise ValueError
    
    
    def sweep2(self):
        """
        This function verify if the sweep is done in voltage or current mode to map samples
        """
        if s['Mapping/Source']=='Voltage':
            data = K.map_voltage()
        elif s['Mapping/Source']=='Current':
            data = K.map_current()
        else:
            raise ValueError
        return data 
        
        
    def current_sweep(self):
        """
        This function does a current sweep on the sample and plots voltage/current and resistance/current 
        """
        value = s['Sweep/StartValue']
        stopvalue = s['Sweep/StopValue']
        voltage=[]
        current=[]
        resistance=[]
        
        
        self.k.ser.write("*RST"+'\r')
        self.k.ser.write("*RST"+'\r')
        self.k.ser.write(':SENS:FUNC:CONC:ON\r')
        
        if s['Sweep/Type'] == '2-Wire':  
            self.k.ser.write(":SYST:RSEN OFF \r")   # Set system to 2-Wire
        else:
            self.k.ser.write(":SYST:RSEN ON\r")     # Set system to 4-Wire
         
        self.k.ser.write(":SYST:AZER:CACH ON\r")    # Enable/disable NPLC caching
        if s['Sweep/Terminals'] == "Rear":
            self.k.ser.write(":ROUT:TERM REAR \r") # sets the output to the Rear Terminals
        else:
            self.k.ser.write(":ROUT:TERM FRON \r") # sets the output to the Front Terminals 
        self.k.ser.write(":SENS:RES:MODE MAN \r") #Select manual ohms mode.
        self.k.ser.write(":SENS:FUNC:OFF:ALL \r")
        self.k.ser.write(':SENS:FUNC "VOLT"\r')
        self.k.ser.write(':SENS:FUNC "RES"\r')
        self.k.ser.write(':SENS:FUNC "CURR"\r')
        self.k.ser.write(":SENS:VOLT:RANG:AUTO ON \r") # Enable auto volts range
        self.k.ser.write(":SENS:RES:RANG:AUTO ON \r") # Enable auto resistance range
        print str(s['Sweep/VoltProt_Level'])
        self.k.ser.write(":SENS:VOLT:PROT:LEV " + str(s['Sweep/VoltProt_Level']) + "\r") # set voltage protection level
        print str(s['Sweep/CurrProt_Level'])
        self.k.ser.write(":SENS:CURR:PROT:LEV " + str(s['Sweep/CurrProt_Level']) + "\r") # set current protection level

        self.k.ser.write(":SOUR:FUNC:MODE CURR\r") # Sets source to Current mode
        #self.k.ser.write(":SOUR:VOLT:RANG "+ str(0.01) +"\r")
        self.k.ser.write(":SOUR:CURR:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:CURR:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:VOLT:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:VOLT:PROT:LEV " + str(s['Sweep/VoltProt_Level']) + "\r") 
        self.k.ser.write(":SOUR:DEL:AUTO ON \r") # source delay auto on
        self.k.ser.write(":SOUR:CLE:AUTO OFF \r") #enable auto-clear for source
        self.k.ser.write(":SOUR:CURR:MODE FIX \r")
        self.k.ser.write(":TRIG:COUN 1" + "\r")
        self.k.ser.write(":SENS:AVER:TCON REP \r")  #look into this what this does. It has to do with filtering
        self.k.ser.write(":SENS:AVER:COUN "+ str(s['Sweep/Averaging']) +"\r") # read the same data point multiple times and average the measured values
        self.k.ser.write(":SENS:AVER:STAT ON \r")
        self.k.ser.write(":OUTP:STAT ON \r") # output on
        print s['Sweep/CurrProt_Level']
        if abs(stopvalue) <= s['Sweep/CurrProt_Level'] and abs(value) <= s['Sweep/CurrProt_Level']:
            while value <= s['Sweep/StopValue']+s['Sweep/StepSize']:
                w.process_events()
                data = self.k.currentread(value)
                #Append the lists of the data
                voltage.append(data[0])
                current.append(data[1])
                resistance.append(data[2])
                d_mapping.clear()
                d_mapping['voltage'] = voltage
                d_mapping['resistance'] = resistance
                d_mapping['current'] = current
                d_mapping.plot()
                value += s['Sweep/StepSize']
                print "Value = %s" %value     
                print data
                time.sleep(0.1)

        else:
            print "Start- and/or StopValue above Current Protection Level"
            raise ValueError
        
        b_sweep.set_checked(False)
        self.k.ser.write(":OUTP:STAT OFF \r") # output on
        self.k.ser.write(":SENS:AVER:STAT OFF \r") # output on
        my_fitter = spinmob.data.fitter(f = 'a*x +b',p='a=1000, b=0')
        my_fitter.set_data(xdata = d_mapping['current'], ydata =d_mapping['voltage'], eydata= 40e-6)
        my_fitter.set(xlabel="Current [A]",ylabel="Voltage [V]")
        
        my_fitter.fit()
        my_fitter.autoscale_eydata_and_fit
        self.fitted_resistance = my_fitter.results[0]

        
        for p in range(len(voltage)):
            F._write((voltage[p]))
            F._tab()
            F._write(resistance[p])
            F._tab()
            F._write(current[p])
            F._newline()

    def current_sweep2(self):
        """
        This function does a current sweep on the sample for mapping
        """
        value = s['Mapping/StartValue']
        
        voltage=[]
        current=[]
        resistance=[]
        self.k.ser.write("*RST"+'\r')
        self.k.ser.write(':SENS:FUNC:CONC:ON\r')
        
        if s['Mapping/Type'] == '2-Wire':  
            self.k.ser.write(":SYST:RSEN OFF \r")   # Set system to 2-Wire
        else:
            self.k.ser.write(":SYST:RSEN ON\r")     # Set system to 4-Wire
         
        self.k.ser.write(":SYST:AZER:CACH ON\r")    # Enable/disable NPLC caching
        if s['Mapping/Terminals'] == "Rear":
            self.k.ser.write(":ROUT:TERM REAR \r") # sets the output to the Rear Terminals
        else:
            self.k.ser.write(":ROUT:TERM FRON \r") # sets the output to the Front Terminals 
        self.k.ser.write(":SENS:RES:MODE MAN \r") #Select manual ohms mode.
        self.k.ser.write(":SENS:FUNC:OFF:ALL \r")
        self.k.ser.write(':SENS:FUNC "VOLT"\r')
        self.k.ser.write(':SENS:FUNC "RES"\r')
        self.k.ser.write(':SENS:FUNC "CURR"\r')
        self.k.ser.write(":SENS:VOLT:RANG:AUTO ON \r") # Enable auto volts range
        self.k.ser.write(":SENS:RES:RANG:AUTO ON \r") # Enable auto resistance range
        self.k.ser.write(":SENS:VOLT:PROT:LEV " + str(s['Mapping/VoltProt_Level']) + "\r") # set voltage protection level
        self.k.ser.write(":SENS:CURR:PROT:LEV " + str(s['Mapping/CurrProt_Level']) + "\r") # set current protection level
        self.k.ser.write(":SOUR:FUNC:MODE CURR\r") # Sets source to Current mode
        self.k.ser.write(":SOUR:VOLT:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:CURR:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:VOLT:PROT:LEV " + str(s['Mapping/VoltProt_Level']) + "\r") 
        self.k.ser.write(":SOUR:DEL:AUTO ON \r") # source delay auto on
        self.k.ser.write(":SOUR:CLE:AUTO OFF \r") #enable auto-clear for source
        self.k.ser.write(":SOUR:CURR:MODE FIX \r")
        self.k.ser.write(":TRIG:COUN 1" + "\r")
        self.k.ser.write(":SENS:AVER:TCON REP \r")  #look into this what this does. It has to do with filtering
        self.k.ser.write(":SENS:AVER:COUN "+ str(s['Mapping/Averaging']) +"\r") # read the same data point multiple times and average the measured values
        self.k.ser.write(":SENS:AVER:STAT ON \r")
        self.k.ser.write(":OUTP:STAT ON \r") # output on
        
        
        
        if -1e-3 <= value <= 1e-3:
                data = self.k.currentread(value)
                #Append the lists of the data
                print(data)
                voltage.append(data[0])
                current.append(data[1])
                resistance.append(data[2])
        self.k.ser.write(":OUTP:STAT OFF \r") # output off
        self.k.ser.write(":SENS:AVER:STAT OFF \r") # output off
        for p in range(len(voltage)):
            F._write((voltage[p]))
            F._tab()
            F._write(resistance[p])
            F._tab()
            F._write(current[p])
            F._newline()
        return data
            
    
    def volt_sweep(self):
        """
        This function does a volt sweep on the sample and plots resistance/voltage and current/voltage in the measurment tab
        """
        value = s['Sweep/StartValue']
        voltage = []
        current = []
        resistance = []
        self.k.ser.write("*RST" + "\r")
        self.k.ser.write(":SENS:FUNC:CONC ON\r") # Concurrent on
        if s['Sweep/Type'] == '2-Wire':  
            self.k.ser.write(":SYST:RSEN OFF \r")   # Set system to 2-Wire
        else:
            self.k.ser.write(":SYST:RSEN ON\r")     # Set system to 4-Wire
         
            self.k.ser.write(":SYST:AZER:CACH ON\r")    # Enable/disable NPLC caching
         
        if s['Sweep/Terminals'] == "Rear":
            self.k.ser.write(":ROUT:TERM REAR \r") # sets the output to the Rear Terminals
        else:
            self.k.ser.write(":ROUT:TERM FRON \r") # sets the output to the Front Terminals 
        self.k.ser.write(":SENS:RES:MODE MAN \r") #Select manual ohms mode.
        self.k.ser.write(":SENS:FUNC:OFF:ALL \r")
        self.k.ser.write(':SENS:FUNC "VOLT"\r')
        self.k.ser.write(':SENS:FUNC "RES"\r')
        self.k.ser.write(':SENS:FUNC "CURR"\r')
        self.k.ser.write(":SENS:VOLT:RANG:AUTO ON \r") # Enable auto volts range
        self.k.ser.write(":SENS:RES:RANG:AUTO ON \r") # Enable auto resistance range
        self.k.ser.write(":SENS:VOLT:PROT:LEV " + str(s['Sweep/VoltProt_Level']) + "\r") # set voltage protection level
        self.k.ser.write(":SENS:CURR:PROT:LEV " + str(s['Sweep/CurrProt_Level']) + "\r") # set current protection level

        self.k.ser.write(":SOUR:FUNC:MODE VOLT\r") # Sets source to Volt mode
        self.k.ser.write(":SOUR:VOLT:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:CURR:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:VOLT:PROT:LEV " + str(s['Sweep/VoltProt_Level']) + "\r") 
        self.k.ser.write(":SOUR:DEL:AUTO ON \r") # source delay auto on
        self.k.ser.write(":SOUR:CLE:AUTO OFF \r") #enable auto-clear for source
        self.k.ser.write(":SOUR:VOLT:MODE FIX \r")
        self.k.ser.write(":TRIG:COUN 1" + "\r")
        self.k.ser.write(":SENS:AVER:TCON REP \r")  #look into this what this does. It has to do with filtering
        self.k.ser.write(":SENS:AVER:COUN "+ str(s['Sweep/Averaging']) +"\r") # read the same data point multiple times and average the measured values
        self.k.ser.write(":SENS:AVER:STAT ON \r")
        self.k.ser.write(":OUTP:STAT ON \r") # output on
     
        while value <= s['Sweep/StopValue']+s['Sweep/StepSize']:
            w.process_events()
            data = self.k.voltread(value)
            print value
            print(data)
            voltage.append(data[0])
            current.append(data[1])
            resistance.append(data[2])
            d_mapping.clear()   
            d_mapping['voltage'] = voltage
            d_mapping['current'] = current
            d_mapping['resistance'] = resistance
            d_mapping.plot()
            value += s['Sweep/StepSize']
     
        b_sweep.set_checked(False)
        self.k.ser.write(":OUTP:STAT OFF \r") # output on
        self.k.ser.write(":SENS:AVER:STAT OFF \r") # output on
        my_fitter = spinmob.data.fitter(f = 'a*x +b', p='a=1000, b=0')
#        my_fitter = spinmob.data.fitter(f = 'a*(exp((x)*b)-1)', p='a=1E-12, b=38.46,')
#        my_fitter = spinmob.data.fitter(f ='a*(1.602*10^(-19))/(300*1.38*10^(-23))*exp(1.602*10^(-19)*x/(300*1.38*10^(-23)))')
        my_fitter.set_data(xdata = d_mapping['voltage'], ydata =d_mapping['current'], eydata = 0.002)
        my_fitter.fit()
        for p in range(len(voltage)):
            F._write((voltage[p]))
            F._tab()
            F._write(resistance[p])
            F._tab()
            F._write(current[p])
            F._newline()


    def map_voltage(self):
        """
        This function map the sample using "Voltage" mode
        """
        value = s['Mapping/StartValue']
        voltage = []
        current = []
        resistance = []
        self.k.ser.write("*RST" + "\r")
        self.k.ser.write(":SENS:FUNC:CONC ON\r") # Concurrent on
        if s['Mapping/Type'] == '2-Wire':  
            self.k.ser.write(":SYST:RSEN OFF \r")   # Set system to 2-Wire
        else:
            self.k.ser.write(":SYST:RSEN ON\r")     # Set system to 4-Wire
         
        self.k.ser.write(":SYST:AZER:CACH ON\r")    # Enable/disable NPLC caching
         
        if s['Mapping/Terminals'] == "Rear":
            self.k.ser.write(":ROUT:TERM REAR \r") # sets the output to the Rear Terminals
        else:
            self.k.ser.write(":ROUT:TERM FRON \r") # sets the output to the Front Terminals 
        self.k.ser.write(":SENS:RES:MODE MAN \r") #Select manual ohms mode.
        self.k.ser.write(":SENS:FUNC:OFF:ALL \r")
        self.k.ser.write(':SENS:FUNC "VOLT"\r')
        self.k.ser.write(':SENS:FUNC "RES"\r')
        self.k.ser.write(':SENS:FUNC "CURR"\r')
        self.k.ser.write(":SENS:VOLT:RANG:AUTO ON \r") # Enable auto volts range
        self.k.ser.write(":SENS:RES:RANG:AUTO ON \r") # Enable auto resistance range
        self.k.ser.write(":SENS:VOLT:PROT:LEV " + str(s['Mapping/VoltProt_Level']) + "\r") # set voltage protection level
        self.k.ser.write(":SENS:CURR:PROT:LEV " + str(s['Mapping/CurrProt_Level']) + "\r") # set current protection level
        self.k.ser.write(":SOUR:FUNC:MODE VOLT\r") # Sets source to Volt mode
        self.k.ser.write(":SOUR:VOLT:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:CURR:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:VOLT:PROT:LEV " + str(s['Mapping/VoltProt_Level']) + "\r") 
        self.k.ser.write(":SOUR:DEL:AUTO ON \r") # source delay auto on
        self.k.ser.write(":SOUR:CLE:AUTO OFF \r") #enable auto-clear for source
        self.k.ser.write(":SOUR:VOLT:MODE FIX \r")
        self.k.ser.write(":TRIG:COUN 1" + "\r")
        self.k.ser.write(":SENS:AVER:TCON REP \r")  #look into this what this does. It has to do with filtering
        self.k.ser.write(":SENS:AVER:COUN "+ str(s['Mapping/Averaging']) +"\r") # read the same data point multiple times and average the measured values
        self.k.ser.write(":SENS:AVER:STAT ON \r")
        self.k.ser.write(":OUTP:STAT ON \r") # output on

        data = self.k.voltread(value)
        print value
         #Append the lists of the data
        print(data)
        voltage.append(data[0])
        current.append(data[1])
        resistance.append(data[2])
        b_sweep.set_checked(False)
        self.k.ser.write(":OUTP:STAT OFF \r") # output off
        self.k.ser.write(":SENS:AVER:STAT OFF \r") # output on
        
        for p in range(len(voltage)):
            F._newline()
            F._write((voltage[p]))
            F._tab()
            F._write(resistance[p])
            F._tab()
            F._write(current[p])
            
        return data
        
        
    def test_sweep(self):
        self.k.ser.write("*RST\r")
        self.k.ser.write(':SENS:FUNC "CURR"\r') #Reset the Instrument
        self.k.ser.write(":SENS:CURR:RANG:AUTO ON\r") #Set to measure Current
        self.k.ser.write(":ROUT:TERM FRON\r") # Set the output to the front terminals
        self.k.ser.write(":SYST:RSEN ON\r") #4-wire on
        self.k.ser.write(":SOUR:FUNC VOLT\r") #set to source voltage
        self.k.ser.write(":SOUR:VOLT:ILIM 300e-3\r") #Set the limit level to 300mA
        self.k.ser.write(":SOUR:SWE:VOLT:LIN 0, 0.9, 181, 0.1\r") # set up sweep from 0 to 0.9 V in 181 steps with 100ms delay
        self.k.ser.write(":INIT\r")
        self.k.ser.write("*WAI\r") #Wait for sweep to complete
        self.k.ser.write(':TRAC:DATA? 1, 181, "defbuffer1", READ,SOUR, REL' + "\r")  #Select ohms measurement function
        print self.k.ser.readline()
        
        
    def approach(self):
        """
        Approaches the sample by verifying if voltage is under 5V
        """
        print self.k.ser.readline()
        self.k.ser.write(":SENS:FUNC:CONC ON\r") # Concurrent on
        self.k.ser.write(":SYST:RSEN OFF\r")     # Set system to 2-Wire  
        self.k.ser.write(":SYST:AZER:CACH ON\r")    # Enable/disable NPLC caching
        self.k.ser.write(":ROUT:TERM FRON \r") # sets the output to the Front Terminals 
        self.k.ser.write(":SENS:RES:MODE MAN \r") #Select manual ohms mode.
        self.k.ser.write(":SENS:FUNC:OFF:ALL \r")
        self.k.ser.write(':SENS:FUNC "VOLT"\r')
        self.k.ser.write(':SENS:FUNC "RES"\r')
        self.k.ser.write(':SENS:FUNC "CURR"\r')
        self.k.ser.write(":SENS:VOLT:RANG:AUTO ON \r") # Enable auto volts range
        self.k.ser.write(":SENS:RES:RANG:AUTO ON \r") # Enable auto resistance range
        self.k.ser.write(":SENS:VOLT:PROT:LEV " + str(s['Sweep/VoltProt_Level']) + "\r") # set voltage protection level
        self.k.ser.write(":SENS:CURR:PROT:LEV " + str(s['Sweep/CurrProt_Level']) + "\r") # set current protection level
        self.k.ser.write(":SOUR:FUNC:MODE VOLT\r") # Sets source to Volt mode
        self.k.ser.write(":SOUR:VOLT:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:CURR:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:VOLT:PROT:LEV " + str(11) + "\r") 
        self.k.ser.write(":SOUR:DEL:AUTO ON \r") # source delay auto on
        self.k.ser.write(":SOUR:CLE:AUTO OFF \r") #enable auto-clear for source
        self.k.ser.write(":SOUR:VOLT:MODE FIX \r")
        self.k.ser.write(":TRIG:COUN 1" + "\r")
        self.k.ser.write(":SENS:AVER:TCON REP \r")  #look into this what this does. It has to do with filtering
        self.k.ser.write(":SENS:AVER:COUN "+ str(1) +"\r") # read the same data point multiple times and average the measured values
        self.k.ser.write(":SENS:AVER:STAT ON \r")
        self.k.ser.write(":OUTP:STAT ON \r") # output on
        self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
        self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
        time.sleep(0.2)
        print self.k.ser.readline()
        approachvalue = self.k.ser.readline()
        print approachvalue
        self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
        time.sleep(0.2)
        self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
        time.sleep(0.2)
        approachvalue = self.k.ser.readline()
        print approachvalue
        approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
        print approachvalue
        voltageapproach = approachvalue[0]
        currentdetected  = approachvalue[1]
        #resistancedetected = approachvalue[2]
        print voltageapproach
        m.set_speed(s['Manipulator/Approach_Speed'])
        steps = s['Manipulator/Approach_Steps']
        #while 4.5 <= voltageapproach <= 5.5:
        #while resistancedetected >= 1e7 or resistancedetected < 1:
        
        approachvoltage = []
        approachcurrent = []
        approachsteps = []
        approach = 0
        
        while abs(currentdetected) <= 1e-7:
            print self.k.ser.readline()
            if b_stop.is_checked():
                m.speed_value()
                self.k.ser.write(":OUTP:STAT OFF \r") # output off
                self.k.ser.write(":SENS:AVER:STAT OFF \r") # output off               
                return
            try:
                time.sleep(0.2)
                self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
                time.sleep(0.2)
                self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
                time.sleep(0.2)
                print approachvalue
                approachvalue = self.k.ser.readline()
                print approachvalue
                approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
                voltageapproach = approachvalue[0]
                #resistancedetected = approachvalue[2]
                currentdetected  = approachvalue[1]
                time.sleep(0.2)
                #print voltageapproach
                #print resistancedetected
                print currentdetected
                steps = s['Manipulator/Approach_Steps']
                m.move_down(steps)
                w.process_events()  
            except ValueError:
                try:
                    self.k.ser.readline()
                    print "Approached due to error"
                    self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
                    time.sleep(0.2)
                    self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
                    time.sleep(0.3)
                    approachvalue = self.k.ser.readline()
                    print approachvalue
                    approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
                    voltageapproach = approachvalue[0]
                    currentdetected  = approachvalue[1]
                    #resistancedetected = approachvalue[2]
                except ValueError:
                    self.k.ser.readline()
                    print "Approached due to error"
                    self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
                    time.sleep(0.2)
                    self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
                    time.sleep(0.3)
                    approachvalue = self.k.ser.readline()
                    print approachvalue
                    approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
                    voltageapproach = approachvalue[0]
                    currentdetected  = approachvalue[1]
            approach = approach + steps 
            approachvoltage.append(voltageapproach)
            approachcurrent.append(currentdetected)
            approachsteps.append(approach)
            d_approach.clear()
            d_approach['steps'] = approachsteps
            d_approach['current'] = approachcurrent
            d_approach['voltage'] = approachvoltage
            d_approach.plot()

        print("Approached :-). I = " + str(currentdetected))  
        self.k.ser.write(":SYST:BEEP 200,1 \r") # makes a beep sound
        self.k.ser.write(":OUTP:STAT OFF \r") # output off
        self.k.ser.write(":SENS:AVER:STAT OFF \r") # output off   
        m.speed_value()


    def unapproach(self):
        """
        Unapproaches the sample by verifying if voltage is 5V
        """
        print self.k.ser.readline()
        self.k.ser.write(":SENS:FUNC:CONC ON\r") # Concurrent on
        self.k.ser.write(":SYST:RSEN OFF\r")     # Set system to 2-Wire
        self.k.ser.write(":SYST:AZER:CACH ON\r")    # Enable/disable NPLC caching  
        self.k.ser.write(":ROUT:TERM FRON \r") # sets the output to the Front Terminals 
        self.k.ser.write(":SENS:RES:MODE MAN \r") #Select manual ohms mode.
        self.k.ser.write(":SENS:FUNC:OFF:ALL \r")
        self.k.ser.write(':SENS:FUNC "VOLT"\r')
        self.k.ser.write(':SENS:FUNC "RES"\r')
        self.k.ser.write(':SENS:FUNC "CURR"\r')
        self.k.ser.write(":SENS:VOLT:RANG:AUTO ON \r") # Enable auto volts range
        self.k.ser.write(":SENS:RES:RANG:AUTO ON \r") # Enable auto resistance range
        self.k.ser.write(":SENS:VOLT:PROT:LEV " + str(s['Sweep/VoltProt_Level']) + "\r") # set voltage protection level
        self.k.ser.write(":SENS:CURR:PROT:LEV " + str(s['Sweep/CurrProt_Level']) + "\r") # set current protection level
        self.k.ser.write(":SOUR:FUNC:MODE VOLT\r") # Sets source to Volt mode
        self.k.ser.write(":SOUR:VOLT:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:CURR:RANG:AUTO ON \r")
        self.k.ser.write(":SOUR:VOLT:PROT:LEV " + str(s['Sweep/VoltProt_Level']) + "\r") 
        self.k.ser.write(":SOUR:DEL:AUTO ON \r") # source delay auto on
        self.k.ser.write(":SOUR:CLE:AUTO OFF \r") #enable auto-clear for source
        self.k.ser.write(":SOUR:VOLT:MODE FIX \r")
        self.k.ser.write(":TRIG:COUN 1" + "\r")
        self.k.ser.write(":SENS:AVER:TCON REP \r")  #look into this what this does. It has to do with filtering
        self.k.ser.write(":SENS:AVER:COUN "+ str(s['Sweep/Averaging']) +"\r") # read the same data point multiple times and average the measured values
        self.k.ser.write(":SENS:AVER:STAT ON \r")
        self.k.ser.write(":OUTP:STAT ON \r") # output on
        self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
        self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
        time.sleep(0.2)
        self.k.ser.readline()
        approachvalue = self.k.ser.readline()
        print approachvalue
        self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
        time.sleep(0.2)
        self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
        time.sleep(0.2)
        print approachvalue
        approachvalue = self.k.ser.readline()
        print approachvalue
        approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
        voltageapproach = approachvalue[0]
        currentdetected = approachvalue[1]
        print voltageapproach
        m.set_speed(s['Manipulator/Approach_Speed']+1)
        
        #while  0 <= voltageapproach <= 1:
        while abs(currentdetected) >= 1e-7:
            w.process_events()
            print self.k.ser.readline()
            if b_stop.is_checked():
                m.speed_value()
                self.k.ser.write(":OUTP:STAT OFF \r") # output off
                self.k.ser.write(":SENS:AVER:STAT OFF \r") # output off   
                return
            try:
                time.sleep(0.2)
                self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
                time.sleep(0.2)
                self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
                time.sleep(0.2)
                print approachvalue
                approachvalue = self.k.ser.readline()
                print approachvalue
                approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
                voltageapproach = approachvalue[0]
                #resistancedetected = approachvalue[2]
                currentdetected  = approachvalue[1]
                time.sleep(0.2)
                #print voltageapproach
                #print resistancedetected
                print currentdetected
                m.move_up(s['Manipulator/Approach_Steps'])
                w.process_events()
            except ValueError:
                try:             
                    print "Approached due to error"
                    self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
                    time.sleep(0.2)
                    self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
                    time.sleep(0.3)
                    approachvalue = self.k.ser.readline()
                    print approachvalue
                    approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
                    voltageapproach = approachvalue[0]
                    currentdetected = approachvalue[1]
                    w.process_events()
                
                except ValueError:
                    print "Approached due to error"
                    self.k.ser.write(':SOUR1:VOLT:LEV:IMM:AMPL '+str(s['Manipulator/V_Sense']) +'\r')
                    time.sleep(0.2)
                    self.k.ser.write(":READ?" + "\r")  #Select ohms measurement function
                    time.sleep(0.3)
                    approachvalue = self.k.ser.readline()
                    print approachvalue
                    approachvalue = _np.array([float(item) for item in approachvalue.split(',')])
                    voltageapproach = approachvalue[0]
                    currentdetected = approachvalue[1]
                    w.process_events()
        time.sleep(0.1)
        self.k.ser.readline()
        print("Un-approached :-). V = " + str(currentdetected))   
        self.k.ser.write(":SYST:BEEP 200,1 \r") # makes a beep sound
        self.k.ser.write(":OUTP:STAT OFF \r") # output off
        self.k.ser.write(":SENS:AVER:STAT OFF \r") # output off        
        time.sleep(1)
        lift = s['Manipulator/Lift_Steps']
        print lift
        m.move_up(lift)
        time.sleep(0.2)
        m.speed_value()
        
class CreateFile():
    """
    This class is used to create a file and to into the created file. 
    """
    def create_file(self):
        """
        When the function is called, it creates a file.
        """
        h=f_p['File/Directory']#Take the input in the Directory text box
        i=f_p['File/Filename'] #Take the input in File name text box
        j=f_p['File/Description']+s['Sweep/Source']#Take the input in Description text box
        self.f=_f.FileManagement(h,i,j) #Creating the file
        self.f._newline()
        if b_temperature.is_checked(): #If the temperature button is checked it creates a column for it
            self.f._writefile('Temperature'+'\t')
        if b_pressure.is_checked(): #If the pressure button is checked it creates a column for it
            self.f._writefile('Pressure'+'\t')
        self.f._writefile('Voltage\tResistance\tCurrent\tX\tY\tX[um]\tY[um]') #position 
        self.f._newline()
        return 

    def _write(self,text):
        """
        When the function is called, it writes in the text file created sooner
        """
        self.f._writefile(str(text))
        return
        
    def _tab(self):
        """
        When the function is called, it makes a tab in the text file created sooner
        """
        self.f._tab()
        return

    def _newline(self):
        """
        When the function is called, it makes a newline in the text file created sooner
        """
        self.f._newline()
        return
    
    def _readline(self):
        """
        When the function is called, it reads the line in the text file created sooner and creates lists with the columns
        """
        l=self.f._readlines() #Creates a list wtih the lines in the file
        
        if b_voltage.is_checked(): #If the voltage button is checked it creates a list containing voltage data
            self.v=[]
        if b_resistance.is_checked(): #If the resistance button is checked it creates list containing resistance data
            self.r=[]
        if b_current.is_checked(): #If the current button is checked it creates a list containing current data
            self.c=[]
        if b_temperature.is_checked(): #If the temperature button is checked it creates a list containing temperature data
            self.t=[]
        if b_pressure.is_checked(): #If the pressure button is checked it creates a list containing pressure data
            self.p=[]
        columns=[]
        for i in range(len(l)):#assign the values to the list situtated in the position i and the number of the column if they can be converted to a float
            try:
                if b_voltage.is_checked():
                    self.v.append(float(l[i][0]))
                    columns.append(self.v)
                if b_resistance.is_checked():    
                    self.r.append(float(l[i][2]))
                    columns.append(self.r)
                if b_current.is_checked():    
                    self.c.append(float(l[i][1]))
                    columns.append(self.c)
                if b_temperature.is_checked():
                    self.t.append(float(l[i][3]))
                    columns.append(self.t)
                if b_pressure.is_checked():
                    self.p.append(float(l[i][4]))
                    columns.append(self.p)
                
            except (IndexError,ValueError): #if they cannot be converted, they are not appended
                print 'Cannot be Converted'
        
        return columns
        
    def _loadfile(self):
        filename=t_loadfile.get_text()
        nf=open(filename,mode='r')
        
        lines=nf.readlines() #Creates a list wtih the lines in the file
        result=[]
#        if b_voltage.is_checked(): #If the voltage button is checked it creates a list containing voltage data
        self.v=[]
#        if b_resistance.is_checked(): #If the resistance button is checked it creates list containing resistance data
        self.r=[]
#        if b_current.is_checked(): #If the current button is checked it creates a list containing current data
        self.c=[]
        self.x=[]
        self.y=[]
        if b_temperature.is_checked(): #If the temperature button is checked it creates a list containing temperature data
            self.t=[]
        if b_pressure.is_checked(): #If the pressure button is checked it creates a list containing pressure data
            self.p=[]
        for x in lines:#assign the values to the list situtated in the position i and the number of the column if they can be converted to a float
            result.append(x.split('\t'))
        for i in range(len (result)):
            try:
                #if b_voltage.is_checked(): #If the voltage button is checked it creates a list containing voltage data
                self.v.append(float(result[i][0]))
                #if b_resistance.is_checked(): #If the resistance button is checked it creates list containing resistance data
                self.r.append(float(result[i][1]))
                #if b_current.is_checked(): #If the current button is checked it creates a list containing current data
                self.c.append(float(result[i][2]))
                self.x.append(float(result[i][3]))
                self.y.append(float(result[i][4]))
                if b_temperature.is_checked(): #If the temperature button is checked it creates a list containing temperature data
                    self.t.append(float(result[i][3]))
                if b_pressure.is_checked(): #If the pressure button is checked it creates a list containing pressure data    
                    self.p.append(float(result[i][4]))
                
            except (IndexError,ValueError): #if they cannot be converted, they are not appended
                pass
                #print 'Cannot be Converted'
        
    def _plotfile(self):
        """
        This function pops up a plot once Plot! button is hit. (ONLY CHECK TWO BUTTONS!)
        """
        
        g=(2,len(self.v)) #Size of the matrix containning the two list that will be plotted
        self.plot=_np.zeros(g) #Matrix ontainning the two list that will be plotted 
        self.title=[]#List containning name of the parameters that will be plotted
        
        if b_x.is_checked() : #If 'X' button in front of voltage is checked, plot matrix append the list of data in the first spot and title list appends 'Voltage'in the first spot
            self.plot[0]=self.v
            self.title.append('Voltage')
        if b_x2.is_checked() :#If 'X' button in front of current is checked, plot matrix append the list of data in the first spot and title list appends 'Current'in the first spot
            self.plot[0]=self.c
            self.title.append('Current')
        if b_x3.is_checked() :#If 'X' button in front of resistance is checked, plot matrix append the list of data in the first spot and title list appends 'Resistance'in the first spot
            self.plot[0]=self.r
            self.title.append('Resistance')
        if b_x4.is_checked() :#If 'X' button in front of temperature is checked, plot matrix append the list of data in the first spot and title list appends 'Temperature'in the first spot
            self.plot[0]=self.t
            self.title.append('Temperature')
        if b_x5.is_checked() :#If 'X' button in front of pressure is checked, plot matrix append the list of data in the first spot and title list appends 'Pressure'in the first spot
            self.plot[0]=self.p
            self.title.append('Pressure')
        if b_time2.is_checked() :#If 'Time' button is checked, plot matrix append the list of data in the first spot and title list appends 'Time'in the first spot
            
            time=_np.linspace(0,len(self.v),len(self.v))#creates a linear space that has the same size of the other lists
            self.plot[0]=time
            self.title.append('Time')
        if b_y.is_checked() :#If 'X' button in front of voltage is checked, plot matrix append the list of data in the second spot and title list appends 'Voltage'in the second spot
            self.plot[1]=self.v
            self.title.append('Voltage')
        if b_y2.is_checked() :#If 'X' button in front of current is checked, plot matrix append the list of data in the second spot and title list appends 'Current'in the second spot
            self.plot[1]=self.c
            self.title.append('Current')
        if b_y3.is_checked() :#If 'X' button in front of resistance is checked, plot matrix append the list of data in the second spot and title list appends 'Resistance'in the second spot
            self.plot[1]=self.r
            self.title.append('Resistance')
        if b_y4.is_checked() :#If 'X' button in front of temperature is checked, plot matrix append the list of data in the second spot and title list appends 'Temperature'in the second spot
            self.plot[1]=self.t
            self.title.append('temperature')
        if b_y5.is_checked() :#If 'Y' button in front of pressure is checked, plot matrix append the list of data in the second spot and title list appends 'Pressure'in the second spot
            self.plot[1]=self.p
            self.title.append('Pressure')

        print self.title
        print len(self.plot),len(self.title)
        if len(self.plot) != 2 or len(self.title) != 2:#If either the plot matrix does not have a size of 2 and title list does not have  
                                                                   #a size of 2, there is no plot that will be done
            print 'Wrong choice!'
            return
        plt.plot(self.plot[0],self.plot[1]) #plots the two lists accordig to what has been appended
        plt.title(self.title[1]+' against '+self.title[0]) #adds a title to the plot accordingly to what has been appended 
        plt.xlabel(self.title[0])
        plt.ylabel(self.title[1])
        plt.show()
        
    def _plotlive(self):
        F._readline()
        F._plotfile()
        return
        
    def _map_plotfile(self):
        """
        This function pops up a grid of the chosen data when Map! button is hit. (ONLY CHECK ONE BUTTON!)
        """
        sx,sy=int(s['Mapping\Points_X']),int(s['Mapping\Points_Y'])
        self.g=[[0 for i in range(sx)] for j in range(sy)]
        
        if b_voltage3.is_checked(): #When Voltage button is checked an Map! button is hit, it pops us a grid with voltage data on the sample
            k=0
            for i in range(len(self.x)):

                    self.g[self.x[i]][self.y[i]]=self.v[i]
            print self.g
            fig=plt.figure()
            ax=fig.add_subplot(1,1,1)
            im=ax.imshow(self.g,extent=(0,sx,0,sy),interpolation='nearest')
            cb=plt.colorbar(im)
            plt.setp(cb.ax.get_yticklabels(),visible=True)
            squareX= int(s['Mapping\Size_X']/s['Mapping\Points_X'])
            squareY= int(s['Mapping\Size_Y']/s['Mapping\Points_Y'])
            plt.title('Voltage on the sample( Every square is ' + str(squareX) +' X ' + str(squareY) +' um )')
            plt.show()
        elif b_current3.is_checked(): #When Current button is checked an Map! button is hit, it pops us a grid with current data on the sample
            k=0
            for i in range(len(self.x)):

                    self.g[self.x[i]][self.y[i]]=self.c[i]
                    
            print self.g
            fig=plt.figure()
            ax=fig.add_subplot(1,1,1)
            im=ax.imshow(self.g,extent=(0,sx,0,sy),interpolation='nearest')
            cb=plt.colorbar(im)
            plt.setp(cb.ax.get_yticklabels(),visible=True)
            squareX= int(s['Mapping\Size_X']/s['Mapping\Points_X'])
            squareY= int(s['Mapping\Size_Y']/s['Mapping\Points_Y'])
            plt.title('Current on the sample( Every square is ' + str(squareX)+ ' X ' + str(squareY)+' um )' )
            plt.show()
        elif b_resistance3.is_checked(): #When Resistance button is checked an Map! button is hit, it pops us a grid with resistance data on the sample
            k=0
            for i in range(len(self.x)):
                self.g[self.x[i]][self.y[i]]=self.r[i]
                k+=1
            print self.g
            fig=plt.figure()
            ax=fig.add_subplot(1,1,1)
            im=ax.imshow(self.g,extent=(0,sx,0,sy),interpolation='nearest')
            cb=plt.colorbar(im)
            plt.setp(cb.ax.get_yticklabels(),visible=True)
            squareX= int(s['Mapping\Size_X']/s['Mapping\Points_X'])
            squareY= int(s['Mapping\Size_Y']/s['Mapping\Points_Y'])
            plt.title('Resistance on the sample ( Every square is ' + str(squareX) +' X ' + str(squareY)+' um )' )
            plt.show()
        elif b_temperature3.is_checked(): #When Temperature button is checked an Map! button is hit, it pops us a grid with temperature data on the sample
            k=0
            for i in range(len(self.y)):

                self.g[self.x[i]][self.y[i]]=self.t[k]
                k+=1
            fig=plt.figure()
            ax=fig.add_subplot(1,1,1)
            im=ax.imshow(self.g,extent=(0,sx,0,sy),interpolation='nearest')
            cb=plt.colorbar(im)
            plt.setp(cb.ax.get_yticklabels(),visible=True)
            squareX= int(s['Mapping\Size_X']/s['Mapping\Points_X'])
            squareY= int(s['Mapping\Size_Y']/s['Mapping\Points_Y'])
            plt.title('Temperature on the sample( Every square is ' + str(squareX) +' X ' + str(squareY)+' um )' )
            plt.show()
        elif b_pressure3.is_checked(): #When Pressure button is checked and Map! button is hit, it pops us a grid with pressure data on the sample
           
            for i in range(len(self.y)):
                self.g[self.x[i]][self.y[i]]=self.p[k]
                
            fig=plt.figure()
            ax=fig.add_subplot(1,1,1)
            im=ax.imshow(self.g,extent=(0,sx,0,sy),interpolation='nearest')
            cb=plt.colorbar(im)
            plt.setp(cb.ax.get_yticklabels(),visible=True)
            squareX= int(s['Mapping\Size_X']/s['Mapping\Points_X'])
            squareY= int(s['Mapping\Size_Y']/s['Mapping\Points_Y'])
            plt.title('Pressure on the sample ( Every square is ' + str(squareX)+ ' X ' + str(squareY) )
            plt.show()
        else:
            print 'Wrong choice!'
        return 
    def _map_plotlive(self):
        F._readline()
        F._map_plotfile()
    
F=CreateFile() #Create a file object, that will be manipulated. To create a file, call the create_file function 
m=Manipulator()#Create the manipulator object, that will be manipulated. To manipulate it, call the Connect_Manipulator function 
K=Keithley() #Create the Keithley object, that will be manipulated. To manipulate it, call the Connect_Keithley function 
A = Arduino()
"""
Manipulator tab

In this tab, there is everything needed to manually move the manipulator(Top grid) and by coordinates(Mid and bottom grid).
g_top begin
"""


g_top=t_manipulator.place_object(egg.gui.GridLayout(False),0,0) #grid containing buttons that moves the manipulator
g_top.set_height(150)
g_mid=t_manipulator.place_object(egg.gui.GridLayout(False),0,6)#grid containing fine and coarse counterread numberboxes
g_mid.set_height(75)
g_bottom=t_manipulator.place_object(egg.gui.GridLayout(False),0,11)#grid containing coordinates where the manipulator is in XYZ and pyx coordinate systems
g_bottom.set_height(125)
g_bottom2=t_manipulator.place_object(egg.gui.GridLayout(False),0,14)#grid containing coordinate inputs for go_to_XYZ and go_to_pyz functions
g_bottom2.set_height(125)


#chosing the speed
L_speed=g_top.place_object(egg.gui.Label('Speed'),0,0)#when you click on this button, it sends the number
L_speed.set_width(70)

nb_speed=g_top.place_object(egg.gui.NumberBox(bounds=(1,6)),2,0)#speed's number box
nb_speed.set_width(70)

#w.connect(b_speed.signal_clicked,speed_value)#Get the value in the number box and asign it to the speed function of NanoControl 

#input the steps
L_step=g_top.place_object(egg.gui.Label('Steps'),0,1)#when you click on this button, it sends the number
L_step.set_width(70)

nb_steps=g_top.place_object(egg.gui.NumberBox(),2,1)#steps' number box
nb_steps.set_width(70)


def steps_value():
    """
    This function take the value written in the steps number box and creates an integer.
    """
    step_value=int(nb_steps.get_value())
    
    print step_value
    return step_value

#w.connect(.signal_clicked,steps_value) "To connect with direction buttons"
    

#adding buttons

b_extend=g_top.place_object(egg.gui.Button("Ext"),0,5)#Extend Button
b_up=g_top.place_object(egg.gui.Button("Up"),1,5,alignment=1.5) #Up button
b_up.set_width(70)
b_reset=g_top.place_object(egg.gui.Button("Reset"),2,5) #Stop button

b_left=g_top.place_object(egg.gui.Button("Left"),0,6)#Left button
b_right=g_top.place_object(egg.gui.Button("Right"),2,6)#Right button
b_retract=g_top.place_object(egg.gui.Button("Ret"),0,7)#Retract button
b_down=g_top.place_object(egg.gui.Button("Down"),1,7,alignment=1)#Down button
b_down.set_width(70)
b_approach=g_top.place_object(egg.gui.Button("Approach"),0,8)#Approach button
b_stop=g_top.place_object(egg.gui.Button("Stop"),1,8)
b_stop.set_checkable()
b_unapproach=g_top.place_object(egg.gui.Button("Unapproach"),2,8)#Unapproach button

w.connect(b_up.signal_clicked,m.speed_value) #Up button speed intake
w.connect(b_down.signal_clicked,m.speed_value)#Down button speed intake
w.connect(b_right.signal_clicked,m.speed_value)#Right button speed intake
w.connect(b_left.signal_clicked,m.speed_value)#Left button speed intake
w.connect(b_extend.signal_clicked,m.speed_value)#Extend button speed intake
w.connect(b_retract.signal_clicked,m.speed_value)#Retract button speed intake

w.connect(b_reset.signal_clicked,m.Counterreset)#Reset button assignation

w.connect(b_left.signal_clicked,m.b_move_left)#Left button assignation
w.connect(b_right.signal_clicked,m.b_move_right) #Right button assignation
w.connect(b_up.signal_clicked,m.b_move_up)#Up button assignation
w.connect(b_down.signal_clicked,m.b_move_down) #Down button assignation           
w.connect(b_extend.signal_clicked,m.b_move_extend)#Extend button assignation
w.connect(b_retract.signal_clicked,m.b_move_retract)#Retract button assignation 
w.connect(b_approach.signal_clicked,K.approach) #Approach button assignation
w.connect(b_unapproach.signal_clicked,K.unapproach) #Unapproach button assignation









"""
g_mid begins

These number boxes in manipulator is according to the counterread
"""

L_channels=g_mid.place_object(egg.gui.Label('Channels'),0,0) #Channels label
L_channel_A=g_mid.place_object(egg.gui.Label('A'),1,1)# A channel label
L_channel_B=g_mid.place_object(egg.gui.Label('B'),2,1)#B channel label
L_channel_C=g_mid.place_object(egg.gui.Label('C'),3,1)#C channel label
L_fine=g_mid.place_object(egg.gui.Label('Fine'),0,2)#Fine couterread number boxes label
L_coarse=g_mid.place_object(egg.gui.Label('Coarse'),0,3)#Coarse counterread number boxes label

nb_A_fine=g_mid.place_object(egg.gui.NumberBox(),1,2)# Fine 'A' channel number box
nb_B_fine=g_mid.place_object(egg.gui.NumberBox(),2,2)# Fine 'B' channel number box
nb_C_fine=g_mid.place_object(egg.gui.NumberBox(),3,2)# Fine 'C' channel number box
nb_A_coarse=g_mid.place_object(egg.gui.NumberBox(),1,3)# Coarse 'A' channel number box
nb_B_coarse=g_mid.place_object(egg.gui.NumberBox(),2,3)# Coarse 'B' channel number box
nb_C_coarse=g_mid.place_object(egg.gui.NumberBox(),3,3)# Coarse 'C' channel number box

#block events is preventing the numberboxes to be changed manually. To change them, see update_box_fine and update_box_coarse

nb_A_fine.set_step(0,block_events=True)
nb_B_fine.set_step(0,block_events=True)
nb_C_fine.set_step(0,block_events=True)
nb_A_coarse.set_step(0,block_events=True)
nb_B_coarse.set_step(0,block_events=True)
nb_C_coarse.set_step(0,block_events=True)

"""
g_bottom begins

These number boxes indicate where the manipulator in each coordinate system
"""
L_coordinates=g_bottom.place_object(egg.gui.Label('Coordinates'),0,0) #Coordinates label
L_XYZ=g_bottom.place_object(egg.gui.Label('X Y Z'),0,1)#'X Y Z' Coordinate system label
L_pyx=g_bottom.place_object(egg.gui.Label('p y x'),0,2)#'p y x' Coordinate system label

nb_X=g_bottom.place_object(egg.gui.NumberBox(),1,1)#X Numbers box
nb_Y=g_bottom.place_object(egg.gui.NumberBox(),2,1)#Y Numbers box
nb_Z=g_bottom.place_object(egg.gui.NumberBox(),3,1)#Z Numbers box
nb_p=g_bottom.place_object(egg.gui.NumberBox(),1,2)#p Numbers box
nb_y=g_bottom.place_object(egg.gui.NumberBox(),2,2)#y Numbers box
nb_x=g_bottom.place_object(egg.gui.NumberBox(),3,2)#x Numbers box

#block events is preventing the numberboxes to be changed manually. To change them, see update_coordinates_XYZ and update_coordinates_pyx 

nb_X.set_step(0,block_events=True)
nb_Y.set_step(0,block_events=True)
nb_Z.set_step(0,block_events=True)
nb_p.set_step(0,block_events=True)
nb_y.set_step(0,block_events=True)
nb_x.set_step(0,block_events=True)

"""
g_bottom2 begins

These numberboxes are the input of the go_to_XYZ and go_to_pyx functions
"""
L_go_to=g_bottom2.place_object(egg.gui.Label('Go to: '),0,0) #Label of the grid
b_go_to_XYZ=g_bottom2.place_object(egg.gui.Button('Go to (X,Y,Z)'),0,1) #Actions the go_to_XYZ when pressed
b_go_to_pyx=g_bottom2.place_object(egg.gui.Button('Go to (p,y,x)'),0,2) #Actions the go_to_pyx when pressed

nb_X2=g_bottom2.place_object(egg.gui.NumberBox(),1,1)#X Numbers box of where the manipulator should go
nb_Y2=g_bottom2.place_object(egg.gui.NumberBox(),2,1)#Y Numbers box of where the manipulator should go
nb_Z2=g_bottom2.place_object(egg.gui.NumberBox(),3,1)#Z Numbers box of where the manipulator should go
nb_p2=g_bottom2.place_object(egg.gui.NumberBox(),1,2)#p Numbers box of where the manipulator should go
nb_y2=g_bottom2.place_object(egg.gui.NumberBox(),2,2)#y Numbers box of where the manipulator should go
nb_x2=g_bottom2.place_object(egg.gui.NumberBox(),3,2)#x Numbers box of where the manipulator should go

def go_to_XYZ():
    """
    This function determines how many steps there is to make in order to reach the given point(X,Y,Z) and moves there.
    """
    X2=nb_X2.get_value()
    Y2=nb_Y2.get_value()
    Z2=nb_Z2.get_value()
    reverse=K.reverse(X2,Y2,Z2)
    p2=reverse[0]
    y2=reverse[1]
    x2=reverse[2]
    p=nb_p.get_value()
    y=nb_y.get_value()
    x=nb_x.get_value()
    d=m.distancetotravel(p,y,x,p2,y2,x2)
    if d[0]<0:
        m.move_left(d[0])
    if d[0]>0:
        m.move_right(d[0])
    if d[1]<0:
        m.move_up(d[1])
    if d[1]>0:
        m.move_down(d[1])
    if d[2]<0:
        m.move_extend(d[2])
    if d[2]>0:
        m.move_retract(d[2])
    nb_X.set_value(X2)
    nb_Y.set_value(Y2)
    nb_Z.set_value(Z2)
    #K.update_coordinates_pyx()
    return

def go_to_pyx():
    """
    This function determines how many steps there is to make in order to reach the given point(p,y,z) and moves there.
    """
    p2=nb_p2.get_value()
    y2=nb_y2.get_value()
    x2=nb_x2.get_value()
    p=nb_p.get_value()
    y=nb_y.get_value()
    x=nb_x.get_value()
    d=m.distancetotravel(p,y,x,p2,y2,x2)
    
    if d[1]>0:
        m.move_up(d[1])
    if d[1]<0:
        m.move_down(d[1])
    if d[0]>0:
        m.move_left(d[0])
    if d[0]<0:
        m.move_right(d[0])
    if d[2]>0:
        m.move_extend(d[2])
    if d[2]<0:
        m.move_retract(d[2])
        
    nb_p.set_value(p2)
    nb_y.set_value(y2)
    nb_x.set_value(x2)
    
    #K.update_coordinates_XYZ()
    return
w.connect(b_go_to_XYZ.signal_clicked,m.speed_value)#go_to_XYZ speed intake
w.connect(b_go_to_pyx.signal_clicked,m.speed_value)#go_to_pyx speed intake

w.connect(b_go_to_XYZ.signal_clicked,go_to_XYZ)#go_to_XYZ button assignation
w.connect(b_go_to_pyx.signal_clicked,go_to_pyx)#go_to_pyx button assignation



"""
Constructing the 4 point probe tab

On this tab, all parameters and functions associated with measuring the sample in the chamber is located here. 
First, there is a tree dictionary that shows the parameters of the last measuring session (Last time the software was ran)
Then, the functions to do different types of measures
"""


s = t_point_probe.place_object(egg.gui.TreeDictionary(default_save_path='parameters.txt'),0,0) #Where the parameters are saved
s.set_height(580)
s.set_width(300)

s.add_parameter('Sweep/Source', "Voltage", type ='list', values =['Current','Voltage']) #Switching between Current or Voltage mode
s.add_parameter('Sweep/Type', "4-Wire", type ='list', values =['2-Wire', '4-Wire']) #Switching between 2-Wire and 4-Wire mode
s.add_parameter('Sweep/StartValue', -5.0,  type='float', limits=(-11, 11)) #Starting value when sweeping
s.add_parameter('Sweep/StopValue', 5.0,  type='float', limits=(-11, 11)) #Stopping value when sweeping
s.add_parameter('Sweep/StepSize', 0.1, type='float', limits=(0, 5.0)) #Step between each mesured value
s.add_parameter('Sweep/Averaging', 3, type='int') #
s.add_parameter('Sweep/Terminals', "Front", type ='list', values = ["Front", "Rear"]) #Switching between Front and rear connections
s.add_parameter('Sweep/VoltProt_Level', 5, type='float', limits=(0, 25)) #Voltage protection level
s.add_parameter('Sweep/CurrProt_Level', 0.100, type='float', limits=(0, 1))#Current protection level

s.add_parameter('Mapping/Size_X',0.0,type='float') #Sample size in X
s.add_parameter('Mapping/Size_Y',0.0,type='float') #Sample size in Y
s.add_parameter('Mapping/Points_X',0,type='int') #Number of points mesured in X
s.add_parameter('Mapping/Points_Y',0,type='int') #Number of point mesured in Y
s.add_parameter('Mapping/Source', "Voltage", type ='list', values =['Current','Voltage']) #Switching between Current or Voltage mode
s.add_parameter('Mapping/Type', "4-Wire", type ='list', values =['2-Wire', '4-Wire']) #Switching between 2-Wire and 4-Wire mode
s.add_parameter('Mapping/StartValue', -5.0,  type='float', limits=(-11, 11)) #Starting value when sweeping
s.add_parameter('Mapping/Averaging', 3, type='int') #
s.add_parameter('Mapping/Terminals', "Front", type ='list', values = ["Front", "Rear"]) #Switching between Front and rear connections
s.add_parameter('Mapping/VoltProt_Level', 5, type='float', limits=(0, 25)) #Voltage protection level
s.add_parameter('Mapping/CurrProt_Level', 0.100, type='float', limits=(0, 1))#Current protection level

s.add_parameter('Manipulator/Approach_Speed',1,type='int',limits=(1,6)) #Speed when using the Approach function
s.add_parameter('Manipulator/Approach_Steps',0,type='int') #Steps done in one movement when using the Approach function
s.add_parameter('Manipulator/Lift_Steps',0,type='int') #Steps done after using the Unapproach function
s.add_parameter('Manipulator/V_Sense',5,type='int')
s.load('parameters.txt') #Load the parameters used last time in the software

def save():
    """
    This function saves the parameters each time they are changed
    """
    s.save('parameters.txt')
    return


s_top=t_point_probe.place_object(egg.gui.GridLayout(False),0,1)
s_top.set_height(120)
s.connect_any_signal_changed(save) #save the parameter are changed


'''
4 Point-Probe Tab:
Multiplexer Buttons and Functions
'''

def multiplexer_off():   
    '''
    this sets all buttons to off
    '''
    
    I_minus_1.set_checked(False)
    I_minus_2.set_checked(False)
    I_minus_3.set_checked(False)
    I_minus_4.set_checked(False)
    
    V_minus_1.set_checked(False)
    V_minus_2.set_checked(False)
    V_minus_3.set_checked(False)
    V_minus_4.set_checked(False)
    
    V_plus_1.set_checked(False)
    V_plus_2.set_checked(False)
    V_plus_3.set_checked(False)
    V_plus_4.set_checked(False)    
    
    I_plus_1.set_checked(False)
    I_plus_2.set_checked(False)
    I_plus_3.set_checked(False)
    I_plus_4.set_checked(False)
    
    multiplexer_status()
    
def multiplexer_reset():      
    multiplexer_off()
    I_plus_1.set_checked(True)
    V_plus_2.set_checked(True)
    V_minus_3.set_checked(True)
    I_minus_4.set_checked(True)
    
    multiplexer_status()
    
def multiplexer_rcontact():
    contact_resistance = []
    contact_uncertanty = []
    for i in range(1,6):
        multiplexer_off()
        print i
        if i == 1:
            I_minus_1.set_checked(True)
            V_minus_1.set_checked(True)
            V_plus_2.set_checked(True)
            I_plus_2.set_checked(True)
        if i == 2:
            I_minus_2.set_checked(True)
            V_minus_2.set_checked(True)
            V_plus_3.set_checked(True)
            I_plus_3.set_checked(True)
        if i == 3:
            I_minus_3.set_checked(True)
            V_minus_3.set_checked(True)
            V_plus_4.set_checked(True)
            I_plus_4.set_checked(True)                    
        if i == 4:
            I_minus_1.set_checked(True)
            V_minus_1.set_checked(True)
            V_plus_3.set_checked(True)
            I_plus_3.set_checked(True)
        if i == 5:
            I_minus_1.set_checked(True)
            V_minus_1.set_checked(True)
            V_plus_3.set_checked(True)
            I_plus_3.set_checked(True)
        if i == 6:
            I_minus_1.set_checked(True)
            V_minus_1.set_checked(True)
            V_plus_4.set_checked(True)
            I_plus_4.set_checked(True)    
            
        time.sleep(0.2)
        K.current_sweep()
        contact_resistance.append(K.fitted_resistance[0])
        contact_uncertanty.append(K.fitted_resistance[1])
        print contact_resistance
        print contact_uncertanty
    multiplexer_reset()
    
def multiplexer_status(*a):
    '''
    Checks the button status of each Multiplexer button and sets
    the Arduino/Multiplexer in the right mode
    '''
#    if I_minus_1.is_checked() == True:
#        print "hello"
#    else:
#        print "go"
#        

        
#I- Row:
    if I_minus_1.is_checked():
        A.arduino.switch(5,1)
        print "P1: I-"            
    else:
        #print "Button 0,0 Released"
        A.arduino.switch(5,0)      
    if  I_minus_2.is_checked():
        #print "Button 0,1 Pressed"
        print "P2: I-"   
        A.arduino.switch(4,0)
    else:
        #print "Button 0,1 Released"
        A.arduino.switch(4,1)
    if  I_minus_3.is_checked():
        print "P3: I-"   
        #print "Button 0,2 Pressed"
        A.arduino.switch(3,0) 
    else:
        #print "Button 0,2 Released"
        A.arduino.switch(3,1)
    if  I_minus_4.is_checked():
        print "P4: I-"   
        #print "Button 0,2 Pressed"
        A.arduino.switch(2,1) 
    else:
        #print "Button 0,2 Released"
        A.arduino.switch(2,0)
#V- Row:
    if  V_minus_1.is_checked():
        print "P1: V-"
        #print "Button 0,0 Pressed"            
        A.arduino.switch(9,1)            
    else:
        #print "Button 0,0 Released"
        A.arduino.switch(9,0)      
    if V_minus_2.is_checked():
        print "P2: V-"
        #print "Button 0,1 Pressed"
        A.arduino.switch(8,0)
    else:
        #print "Button 0,1 Released"
        A.arduino.switch(8,1)
    if V_minus_3.is_checked():
        print "P3: V-"
        #print "Button 0,2 Pressed"
        A.arduino.switch(7,0) 
    else:
        #print "Button 0,2 Released"
        A.arduino.switch(7,1)
    if V_minus_4.is_checked():
        print "P4: V-"
        #print "Button 0,2 Pressed"
        A.arduino.switch(6,1) 
    else:
        #print "Button 0,2 Released"
        A.arduino.switch(6,0)            
#V+ Row:
    if V_plus_1.is_checked():
        print "P1: V+"            
        #print "Button 0,0 Pressed"            
        A.arduino.switch(18,1)            
    else:
        #print "Button 0,0 Released"
        A.arduino.switch(18,0)      
    if V_plus_2.is_checked():
        print "P2: V+"             
        #print "Button 0,1 Pressed"
        A.arduino.switch(19,0)
    else:
        #print "Button 0,1 Released"
        A.arduino.switch(19,1)
    if V_plus_3.is_checked():
        print "P3: V+"             
        #print "Button 0,2 Pressed"
        A.arduino.switch(11,0) 
    else:
        #print "Button 0,2 Released"
        A.arduino.switch(11,1)
    if V_plus_4.is_checked():
        print "P4: V+"             
        #print "Button 0,2 Pressed"
        A.arduino.switch(10,1) 
    else:
        #print "Button 0,2 Released"
        A.arduino.switch(10,0)
#I+ Row:
    if I_plus_1.is_checked():
        print "P1: I+"             
        #print "Button 0,0 Pressed"            
        A.arduino.switch(14,1)            
    else:
        #print "Button 0,0 Released"
        A.arduino.switch(14,0)      
    if I_plus_2.is_checked():
        print "P2: I+"              
        #print "Button 0,1 Pressed"
        A.arduino.switch(15,0)
    else:
        #print "Button 0,1 Released"
        A.arduino.switch(15,1)
    if I_plus_3.is_checked():
        print "P3: I+"              
        #print "Button 0,2 Pressed"
        A.arduino.switch(16,0) 
    else:
        #print "Button 0,2 Released"
        A.arduino.switch(16,1)
    if I_plus_4.is_checked():
        print "P4: I+"  
        #print "Button 0,2 Pressed"
        A.arduino.switch(17,1) 
    else:
        #print "Button 0,2 Released"
        A.arduino.switch(17,0)




# Multiplexer Buttons with all connections to the multiplexer_status function
I_plus_1=s_top.place_object(egg.gui.Button("I+"),0,1)
I_plus_1.set_checkable(True)
w.connect(I_plus_1.signal_clicked,multiplexer_status)

I_plus_2=s_top.place_object(egg.gui.Button("I+"),1,1)
I_plus_2.set_checkable(True)
w.connect(I_plus_2.signal_clicked,multiplexer_status)

I_plus_3=s_top.place_object(egg.gui.Button("I+"),2,1)
I_plus_3.set_checkable(True)
w.connect(I_plus_3.signal_clicked,multiplexer_status)

I_plus_4=s_top.place_object(egg.gui.Button("I+"),3,1)
I_plus_4.set_checkable(True)
w.connect(I_plus_4.signal_clicked,multiplexer_status)

V_plus_1=s_top.place_object(egg.gui.Button("V+"),0,2)
V_plus_1.set_checkable(True)
w.connect(V_plus_1.signal_clicked,multiplexer_status)

V_plus_2=s_top.place_object(egg.gui.Button("V+"),1,2)
V_plus_2.set_checkable(True)
w.connect(V_plus_2.signal_clicked,multiplexer_status)

V_plus_3=s_top.place_object(egg.gui.Button("V+"),2,2)
V_plus_3.set_checkable(True)
w.connect(V_plus_3.signal_clicked,multiplexer_status)

V_plus_4=s_top.place_object(egg.gui.Button("V+"),3,2)
V_plus_4.set_checkable(True)
w.connect(V_plus_4.signal_clicked,multiplexer_status)

V_minus_1=s_top.place_object(egg.gui.Button("V-"),0,3)
V_minus_1.set_checkable(True)
w.connect(V_minus_1.signal_clicked,multiplexer_status)

V_minus_2=s_top.place_object(egg.gui.Button("V-"),1,3)
V_minus_2.set_checkable(True)
w.connect(V_minus_2.signal_clicked,multiplexer_status)

V_minus_3=s_top.place_object(egg.gui.Button("V-"),2,3)
V_minus_3.set_checkable(True)
w.connect(V_minus_3.signal_clicked,multiplexer_status)

V_minus_4=s_top.place_object(egg.gui.Button("V-"),3,3)
V_minus_4.set_checkable(True)
w.connect(V_minus_4.signal_clicked,multiplexer_status)

I_minus_1=s_top.place_object(egg.gui.Button("I-"),0,4)
I_minus_1.set_checkable(True)
w.connect(I_minus_1.signal_clicked,multiplexer_status)

I_minus_2=s_top.place_object(egg.gui.Button("I-"),1,4)
I_minus_2.set_checkable(True)
w.connect(I_minus_2.signal_clicked,multiplexer_status)

I_minus_3=s_top.place_object(egg.gui.Button("I-"),2,4)
I_minus_3.set_checkable(True)
w.connect(I_minus_3.signal_clicked,multiplexer_status)

I_minus_4=s_top.place_object(egg.gui.Button("I-"),3,4)
I_minus_4.set_checkable(True)
w.connect(I_minus_4.signal_clicked,multiplexer_status)

b_multiplexer_reset = s_top.place_object(egg.gui.Button("Reset"),0,5)
w.connect(b_multiplexer_reset.signal_clicked,multiplexer_reset)
b_multiplexer_alloff = s_top.place_object(egg.gui.Button("All Off"),1,5)
w.connect(b_multiplexer_alloff.signal_clicked,multiplexer_off)
b_multiplexer_contactresistance = s_top.place_object(egg.gui.Button("R_cont"),2,5)
w.connect(b_multiplexer_contactresistance.signal_clicked, multiplexer_rcontact)





'''
4-Point Probe Tab:
Sweep, Contact Resistance and Mapping Buttons
'''

b_sweep=t_point_probe.place_object(egg.gui.Button("Sweep"),0,6) #Plotting
b_sweep.set_width(300)
w.connect(b_sweep.signal_clicked,F.create_file)
w.connect(b_sweep.signal_clicked,K.sweep) #Sweep button assignation

b_contactresistance=t_point_probe.place_object(egg.gui.Button("Contact Resistance"),0,7)
b_contactresistance.set_width(300)


b_Mapping=t_point_probe.place_object(egg.gui.Button('Mapping'),0,8) #Mapping
b_Mapping.set_width(300)
w.connect(b_Mapping.signal_clicked,F.create_file)
w.connect(b_Mapping.signal_clicked,K.sweep2)


"""
Connect tab

This tab contains connection buttons for the different measuring instruments
"""
gri=t_connect.place_object(egg.gui.GridLayout(),0,0) #Grid into the tab

l_manipulator=gri.place_object(egg.gui.Label('Manipulator'),0,0) #Label before the manipulator connection button
b_connect_manipulator=gri.place_object(egg.gui.Button('Connect'),1,0) #manipulator connection button

l_fourpointprobe=gri.place_object(egg.gui.Label('Four Point Probe'),0,1)#Label before the four-point probe connection button
b_connect_4pp=gri.place_object(egg.gui.Button('Connect'),1,1) #four-point probe connection button

l_arduino = gri.place_object(egg.gui.Label('Four Point-Probe Multiplexer'),0,2)
b_connect_arduino=gri.place_object(egg.gui.Button('Connect'),1,2) #four-point probe connection button
b_connect_arduino.set_checkable(True)


#l_temperaturegauge=gri.place_object(egg.gui.Label('Temperature Gauge'),0,2)
#b_connect_temperaturegauge=gri.place_object(egg.gui.Button('Connect'),1,2)
#
#l_pressuregauge=gri.place_object(egg.gui.Label('Pressure Gauge'),0,3)
#b_connect_pressuregauge=gri.place_object(egg.gui.Button('Connect'),1,3)

w.connect(b_connect_manipulator.signal_clicked,m.Connect_Manipulator) #manipulator connection button assignation
w.connect(b_connect_4pp.signal_clicked,K.Connect_Keithley) #four-point probe connection button assignation
w.connect(b_connect_arduino.signal_clicked,A.Connect_Arduino)



"""
Approach Tab
"""
d_approach = t_approach.place_object(egg.gui.DataboxPlot())



"""
Measurement Tab
"""
d_mapping=t_measurments.place_object(egg.gui.DataboxPlot('*.raw','auto.cfg')) #Where the plots appears when sweeping
"""
Mapping tab
"""
ib_voltage= t_mapping.place_object(egg.gui.Button('Voltage'),0,0)
ib_voltage.set_checkable()

ib_resistance= t_mapping.place_object(egg.gui.Button('Resistance'),1,0)
ib_resistance.set_checkable()

ib_current= t_mapping.place_object(egg.gui.Button('Current'),2,0)
ib_current.set_checkable()

ib_temperature= t_mapping.place_object(egg.gui.Button('Temperature'),0,2)
ib_temperature.set_checkable()

ib_pressure= t_mapping.place_object(egg.gui.Button('Pressure'),1,2)
ib_pressure.set_checkable()

ib_makeimage= t_mapping.place_object(egg.gui.Button('Make Image appear'),3,0)

image=[]

def make_imageview():
    global image
    if ib_voltage.is_checked():
        p_mapping_voltage=t_mapping.place_object(egg.pyqtgraph.ImageView(),0,1)
        image.append(p_mapping_voltage)
    if ib_resistance.is_checked():
        p_mapping_resistance=t_mapping.place_object(egg.pyqtgraph.ImageView(),1,1) #Where the resistance mapping should appear 
        image.append(p_mapping_resistance)
    if ib_current.is_checked():
        p_mapping_current=t_mapping.place_object(egg.pyqtgraph.ImageView(),2,1) #Where the current mapping should appear 
        image.append(p_mapping_current)
    if ib_temperature.is_checked():
        p_mapping_temperature=t_mapping.place_object(egg.pyqtgraph.ImageView(),0,3)
        image.append(p_mapping_temperature)
    if ib_pressure.is_checked():
        p_mapping_pressure=t_mapping.place_object(egg.pyqtgraph.ImageView(),1,3)
        image.append(p_mapping_pressure)
    
    return image

w.connect(ib_makeimage.signal_clicked,make_imageview)


class Mapping():
#    def axes(self):
#        """
#        This function initialises the map, and shows it, that will be used during the experiment. 
#        It takes its value from the tree dictionary in th 4PP tab.
#        """
 #      size=(s['Sample/Points_Y'],s['Sample/Points_X'])
#        
#        self.n_array=[] #List that appends matrixes created and will be used to know how many subplots we have to add in the figure       
#        
#        if b_resistance.is_checked(): 
#            self.r=_np.zeros(size) #resistance matrix
#            self.n_array.append(self.r) #append the matrix if value is measured
#        
#        if b_current.is_checked():
#            self.c=_np.zeros(size) #current matrix
#            self.n_array.append(self.c) #append the matrix if value is measured
#        
#        if b_temperature.is_checked():
#            self.t=_np.zeros(size) #temprature matrix
#            self.n_array.append(self.t) #append the matrix if value is measured
#        
#        if b_pressure.is_checked():
#            self.p=_np.zeros(size) #pressure matrix
#            self.n_array.append(self.p) #append the matrix if value is measured
#        
#        if b_voltage.is_checked():
#            self.v=_np.zeros(size) #voltage matrix
#            self.n_array.append(self.v) #append the matrix if value is measured
#        
#        
#        sidex = _np.linspace(0,s['Sample/Size_X'],s['Sample/Points_X']+1) 
#        sidey = _np.linspace(0,s['Sample/Size_Y'],s['Sample/Points_X']+1)
#        self.X,self.Y = _np.meshgrid(sidex,sidey)
#        
#        print 'Done'
    
#    def _map(self):
#        """
#        This function is creating a map depending on the number of values that is measured.
#        """
#        i=1 #Map counter
#        for a in self.n_array:
#            
#            if len(self.n_array == 1):
#                    plt.figure()
#                    plt.subplot(111)
#                    plt.pcolormesh(self.X,self.Y,a)
#                    
#            if len(self.n_array == 2):
#                if i==1:
#                    plt.figure()
#                    plt.subplot(210+i)
#                    plt.pcolormesh(self.X,self.Y,a)
#                else:
#                    plt.subplot(210+i)
#                    plt.pcolormesh(self.X,self.Y,a)
#                    
#            if len(self.n_array == 3):
#                if i==1:
#                    plt.figure()
#                    plt.subplot(310+i)
#                    plt.pcolormesh(self.X,self.Y,a)
#                    
#                else:
#                    plt.subplot(310+i)
#                    plt.pcolormesh(self.X,self.Y,a)
#                    
#            if len(self.n_array == 4):
#                if i==1:
#                    plt.figure()
#                    plt.subplot(410+i)
#                    plt.pcolormesh(self.X,self.Y,a)
#                    
#                else:
#                    plt.subplot(410+i)
#                    plt.pcolormesh(self.X,self.Y,a)
#                    
#            if len(self.n_array == 5):
#                if i==1:
#                    plt.figure()
#                    plt.subplot(510+i)
#                    plt.pcolormesh(self.X,self.Y,a)
#                    
#                else:
#                    plt.subplot(510+i)
#                    plt.pcolormesh(self.X,self.Y,a)
#                    
    def _measure(self):
        """
        This function is collecting data point and update the map created when the class is initialised, when a data is taken on the sample. 
        It has two counters, one for mesuring going right or left and one for the while loop. It stops by itself when all the sample is measured.
        """
        global p_mapping_current, p_mapping_resistance
        size=(s['Mapping/Points_Y'],s['Mapping/Points_X'])
        if b_resistance.is_checked(): 
            self.r=_np.zeros(size) #resistance matrix
        
        if b_current.is_checked():
            self.c=_np.zeros(size) #current matrix
        """
        This section is about trying to start the measurment where it stopped if an error happenned
        """
#        lists = F._readline()
#        if len(lists) != 0: #things are done for resistance only! Do the same for every variables
#            f=0
#            g=0
#            h=0
#            r=lists[1]
#            while f < len(r):
#                if h< s['Mapping/Points_Y']:
#                    self.r[-g][h] = r[f]
#                    h+=1
#                else:
#                    g+=0
#                    h=0
#                    self.r[-g][h] = r[f]  
#            f+=1
#        for i in range(len(self.r)):
#               if (i//2)==0:
#                    self.r[i]==self.r[i][::-1]
#               else:
#                   pass                   
#        else:
#            pass
#        
        microns_x = int(float(s['Mapping/Size_X'])/float(s["Mapping/Points_X"]))
        microns_y = int(float(s['Mapping/Size_Y'])/float(s["Mapping/Points_Y"]))

        print microns_x,microns_y
        
        k=0 #left-right counter
        l=0 #maps counter
        y=0 #y-axis counter
        K.unapproach()
        while y < s['Mapping/Points_Y']:
            if k==0: 
                for j in range(0,s['Mapping/Points_X']):
                    
                    time.sleep(0.3)
                    K.approach()
                    print "Approached"
                    
                    time.sleep(0.3)
                    d=K.sweep2()
                    print d
                    self.r[j][y]=d[2]
                    self.c[j][y]=d[1]

                    image[1].setImage(self.c)
                    image[2].setImage(self.r)
                    
                    w.process_events()
                    time.sleep(1)
                    print "Measured"
                    
                    time.sleep(0.3)
                    #Write_Counterread()
                    F._write(str(j)+'\t'+ str(y)+'\t'+str(j*microns_x)+'\t'+str(y*microns_y)+'\n')
                    print "Position marked"
                    
                    K.unapproach()
                    print "Unapproached"
                    
                    time.sleep(0.3)
                    if j < s['Mapping/Points_X']-1:
                        
                        m.move_right(microns_x)
            
                    
                    w.process_events()
                    l+=1
                print "Row Finished"
                k+=1
                
                
            elif k==1:
                for j in range(1,s['Mapping/Points_X']+1):
                    time.sleep(0.3)
                    K.approach()
                    print "Approached"
                   
                    time.sleep(0.3)
                    d=K.sweep2()
                    
                    self.r[-j][y]=d[2]
                    self.c[-j][y]=d[1]
                    
                    image[1].setImage(self.c)
                    image[2].setImage(self.r)
                    
                    time.sleep(1)
                    w.process_events()
                    print "Measured"
                    
                    #Write_Counterread()
                    F._write(str(4-j)+'\t'+ str(y)+str((4-j)*microns_x)+'\t'+str(y*microns_y)+'\n')
                    print "Position marked"
                    
                    time.sleep(0.3)
                    K.unapproach()
                    time.sleep(0.3)
                    print "Unapproached"
                    
                    time.sleep(0.3)
                    if j < s['Mapping/Points_X'] :
                        m.move_left(microns_x)
                        
                    w.process_events()
                    l+=1
                    
                print "Row Finished"
                k-=1
                
                
            else:
                print "Error"
            if y < s['Mapping/Points_Y']-1:
                m.move_retract(microns_y)
                
            y+=1
        print 'Finished'
        return
    

_m=Mapping() #Creates the mapping object to be manipulated later.
#w.connect(b_Mapping.signal_clicked,_m.axes) #creates the intial map #Not needed anymore
w.connect(b_Mapping.signal_clicked,_m._measure) #Mapping button assignation



"""
Text file tab

This tab is the creation file tab. There is two textboxes, one for the filename and one for the description. The buttons in the second row act like
checkboxes and designate what will be in the file. The last one creates the file. See the class FileManagement for further details on file creation. 

"""

grid=t_textfile.place_object(egg.gui.GridLayout(),0,0) #grid layout containing text boxes for file name and description
grid.set_height(100)
grid2=t_textfile.place_object(egg.gui.GridLayout(),0,4) #grid layout containing checkboxes and creation file button
grid2.set_height(100)

f_p=grid.place_object(egg.gui.TreeDictionary(default_save_path='File_parameters.txt')) #file parameters(f_p) to be saved after closing the software
f_p.set_width(400)
f_p.set_height(90)

f_p.add_parameter('File/Directory',type='str') #Write the directory here
f_p.add_parameter('File/Filename',type='str') #Write the filename here
f_p.add_parameter('File/Description',type='str') #Write the description here
f_p.load('File_parameters.txt')

def save2():
    """
    This function saves the parameters each time they are changed
    """
    f_p.save('File_parameters.txt')
    return

f_p.connect_any_signal_changed(save2)



b_voltage=grid2.place_object(egg.gui.Button('Voltage'),0,0) #Voltage checkbox
b_voltage.set_checkable()

b_resistance=grid2.place_object(egg.gui.Button('Resistance'),1,0) #Resistance checkbox
b_resistance.set_checkable()

b_current=grid2.place_object(egg.gui.Button('Current'),2,0) #Current checkbox
b_current.set_checkable()

b_temperature=grid2.place_object(egg.gui.Button('Temperature'),3,0) #Temperature checkbox
b_temperature.set_checkable()

b_pressure=grid2.place_object(egg.gui.Button('Pressure'),4,0) #Pressure textbox
b_pressure.set_checkable()


b_createfile=grid2.place_object(egg.gui.Button('Create the file'),2,2) #Creating file button

def Write_Counterread():
    """
    This function writes the counterread into the file.
    """
    P=m.Counterread() #See Couterread in Manipulator class
    for i in range(len(P)):
        F._write(P[i])
        F._tab()
    return
    
w.connect(b_createfile.signal_clicked,F.create_file) #Create File assignation


"""
Plot tab 

In this tab, this is where you can push the proper button and pop up the plot or map you want.
"""

grid=t_plot.place_object(egg.gui.GridLayout(),0,0) #GridLayout containig Plotting checkboxes and button
grid.set_height(300)
grid2=t_plot.place_object(egg.gui.GridLayout(),0,8) #GridLayout containig Mapping checkboxes and button
grid2.set_height(100)
grid3=t_plot.place_object(egg.gui.GridLayout(),0,11)
grid3.set_height(75)

l_plot=grid.place_object(egg.gui.Label("Plot:"),0,0) #Label on top of plotting checkboxes

l_voltage2=grid.place_object(egg.gui.Label('Voltage'),0,1) #Voltage checkbox for plotting
b_x=grid.place_object(egg.gui.Button('X'),1,1)
b_x.set_checkable()
b_y=grid.place_object(egg.gui.Button('Y'),2,1)
b_y.set_checkable()

l_current2=grid.place_object(egg.gui.Label('Current'),0,2) #Current checkbox for plotting
b_x2=grid.place_object(egg.gui.Button('X'),1,2)
b_x2.set_checkable()
b_y2=grid.place_object(egg.gui.Button('Y'),2,2)
b_y2.set_checkable()

l_resistance2=grid.place_object(egg.gui.Label('Resistance'),0,3) #Resistance checkbox for plotting
b_x3=grid.place_object(egg.gui.Button('X'),1,3)
b_x3.set_checkable()
b_y3=grid.place_object(egg.gui.Button('Y'),2,3)
b_y3.set_checkable()

l_temperature2=grid.place_object(egg.gui.Label('Temperature'),0,4) #Temperature checkbox for plotting
b_x4=grid.place_object(egg.gui.Button('X'),1,4)
b_x4.set_checkable()
b_y4=grid.place_object(egg.gui.Button('Y'),2,4)
b_y4.set_checkable()

l_pressure2=grid.place_object(egg.gui.Label('Pressure'),0,5) #Pressure checkbox for plotting
b_x5=grid.place_object(egg.gui.Button('X'),1,5)
b_x5.set_checkable()
b_y5=grid.place_object(egg.gui.Button('Y'),2,5)
b_y5.set_checkable()

b_time2=grid.place_object(egg.gui.Button('Time'),0,6) #Time checkbox for plotting
b_time2.set_checkable()

b_plot=grid.place_object(egg.gui.Button('Plot working file!'),0,7) #When this button is hit, a plot pops up depending on what is checked in the working file
b_plot2=grid.place_object(egg.gui.Button('Plot loaded file!'),1,7) #When this button is hit, a plot pops up depending on what is checked in the loaded file

w.connect(b_plot.signal_clicked,F._plotlive) 
w.connect(b_plot2.signal_clicked,F._loadfile)
w.connect(b_plot2.signal_clicked,F._plotfile)
"""
Mapping buttons
"""

l_mapping=grid2.place_object(egg.gui.Label('Mapping:'),0,0) #Label on top of mapping checkboxes

b_voltage3=grid2.place_object(egg.gui.Button('Voltage'),0,1) #Voltage checkbox for mapping
b_voltage3.set_checkable()

b_current3=grid2.place_object(egg.gui.Button('Current'),1,1) #Current checkbox for mapping
b_current3.set_checkable()

b_resistance3=grid2.place_object(egg.gui.Button('Resistance'),2,1) #Resistance checkbox for mapping
b_resistance3.set_checkable()

b_temperature3=grid2.place_object(egg.gui.Button('Temperature'),3,1) #Temperature checkbox for mapping

b_pressure3=grid2.place_object(egg.gui.Button('Pressure'),4,1) #Pressure checkbox for mapping
b_pressure3.set_checkable()

b_mapping=grid2.place_object(egg.gui.Button("Map working file!"),0,2) #When this button is hit, a map pops up depending on what is checked
b_mapping2=grid2.place_object(egg.gui.Button("Map loaded file!"),1,2)

w.connect(b_mapping.signal_clicked,F._map_plotlive)
w.connect(b_mapping2.signal_clicked,F._loadfile)
w.connect(b_mapping2.signal_clicked,F._map_plotfile)

"""
Load File

Use this to read files created before
"""

b_loadfile=grid3.place_object(egg.gui.Button('Load File'),0,0)#Button you push to load the file in the text box

t_loadfile=grid3.place_object(egg.gui.TextBox('File name you want to load'),1,0)# this is where you pout the name of the file 
t_loadfile.set_width(200)                                                       #(same directory as in the parameter tree in file tab)



w.connect(b_loadfile.signal_clicked, F._loadfile)#The function assignated to the "Load File" Button


"""
Console tab
"""

#showing the thing    
w.show()
