"""
Created on Tue Mar 08 14:45:27 2015
@author:    Andreas Spielhofer
            Ph.D. Candidate
            Physics Departement
            McGill University
            Montreal, Canada
@contact:   andreas.spielhofer@mail.mcgill.ca
"""

import cv2 as _cv2
import spinmob.egg   as egg
import time as _t
import numpy as _np

##########
# Window
##########
window = egg.gui.Window("Four Point-Probe Camera", autosettings_path="settings_new.cfg")

############################################
# Basic classes and functions for the camera
############################################

def image_to_rgb_data(image): 
    """
    Converts the array from cv2 to an array of data for our plotter.
    """
    return image.transpose((1,0,2)).astype(float)


def data_to_image(image, rescale=False):
    """
    Converts our plotty data to an image array for cv2.
    """    
    if rescale: 
        imax = max(image)
        imin = min(image)        
        return ((image.transpose((1,0)) - imin) * 256.0/(imax-imin)).astype(int) 
    else: 
        return image.transpose((1,0)).astype(int)

class ImageWithButtons(egg.gui.GridLayout):
    
    def __init__(self, window):
        """
        This object is a grid layout containing an image with save / load 
        buttons.
        
        You must supply a window object so that it can connect buttons to 
        actions, etc.
        """

        # initialize the grid layout
        egg.gui.GridLayout.__init__(self)    
        
        # no need for more margins
        self._layout.setContentsMargins(0,0,0,0)

        # store the window object
        self._window = window

        # add the save, load, and image
        self.button_save = self.place_object(egg.gui.Button("Save"))
        self.button_load = self.place_object(egg.gui.Button("Load"))
        self.image       = self.place_object(egg.pyqtgraph.ImageView(), 0,1, column_span=3, alignment=0)
       
        
        # sha-clacky the buttons together
        self.set_column_stretch(2,10)        
        
        # data
        self.data = 0.0
        

        # connect the buttons to the functionality
        self._window.connect(self.button_save.signal_clicked, self.button_save_clicked)
        self._window.connect(self.button_load.signal_clicked, self.button_load_clicked)
        
    def set_data(self, data, **kwargs):
        """
        Sets the image view data to the supplied array.
        """
        self.image.setImage(data, **kwargs)
        self.data = data
        
    def set_levels(self, minvalue, maxvalue, minlevel, maxlevel):
        """
        Sets the minimum and maximum values of the histogram as well as the levelbars. 
        """
        self.image.setLevels(minlevel, maxlevel)
        self.image.ui.histogram.setHistogramRange(minvalue, maxvalue)
    
    def save_image(self, path="ask"):
        """
        Saves the image.
        """
        # get a valid path
        if path=="ask": path = egg.dialogs.save("*.png")
        if not path: return

        # save the image
        _cv2.imwrite(path, data_to_image(self.image.image))
    
    def button_save_clicked(self, *a): self.save_image()

    def load_image(self, path="ask"):
        """
        Loads an image.
        """
        # get a path
        if path=="ask": path = egg.dialogs.open_single("*.png")
        if not path: return
        
        # load the image
        rgb = image_to_rgb_data(_cv2.imread(path))
    
        # assume r+g+b / 3 by default.
        self.set_data((rgb[:,:,0]+rgb[:,:,1]+rgb[:,:,2]) / 3.0)

    def button_load_clicked(self, *a): 
        self.load_image()

        
#########################
# Tabbed area for plots
#########################
tabs_plots = window.place_object(egg.gui.TabArea(False), 0,0, alignment=0)

# tabs
t_cam           = tabs_plots.add_tab("Camera Interfaces")
t_cam2 = tabs_plots.add_tab('Camera1')
t_cam3 = tabs_plots.add_tab('Camera2')

t_cam_row1      = t_cam.place_object(egg.gui.GridLayout())
t_cam_row1.set_column_stretch(2)
t_cam2_row1 = t_cam2.place_object(egg.gui.GridLayout())
t_cam2_row1.set_column_stretch(2)
#t_cam_row2 = t_cam.place_object(egg.gui.GridLayout())
#t_cam_row2.set_column_stretch(2)
video_input     = t_cam_row1.place_object(egg.gui.NumberBox(0, 1).set_width(40))
video_label     = t_cam_row1.place_object(egg.gui.Label('Input channel 1'))
button_stream   = t_cam_row1.place_object(egg.gui.Button('Stream').set_checkable(True))


video_input2     = t_cam_row1.place_object(egg.gui.NumberBox(0, 1).set_width(40))
video_label2     = t_cam_row1.place_object(egg.gui.Label('Input channel 2'))
button_stream2   = t_cam_row1.place_object(egg.gui.Button('Stream').set_checkable(True))

label_fps       = t_cam.place_object(egg.gui.Label("FPS = 0"), alignment=2       )
text_script     = t_cam.place_object(egg.gui.TextBox("(r+g+b)/3.0")              )

# second row: image
t_cam_row2 = t_cam.place_object(egg.gui.GridLayout(), 0,1, alignment=0)
image_raw = t_cam_row2.place_object(ImageWithButtons(window), alignment=0)


t_cam2_row3 = t_cam.place_object(egg.gui.GridLayout(), 1,1, alignment=0)
image_raw2 = t_cam_row2.place_object(ImageWithButtons(window), alignment=0)


#t_cam_CAMERA1 = t_cam2.place_object(egg.gui.GridLayout(), 0,1, alignment=0)
#image_raw_CAMERA1 = t_cam2_row.place_object(ImageWithButtons(window), alignment=0)

        
def button_stream_pressed(*a):
    '''
    Called whenever the stream button is pressed.
    '''

    # let the loop shut itself down
    #if not button_stream.is_checked(): 
        #return
    
    channel = int(video_input.get_value())

    # connect to the camera
    camera = _cv2.VideoCapture(channel)

    
    
    # for the frames per second calculation    
    t0 = _t.time()
    n  = 0
    
    # global variables for script execution
    g = _np.__dict__
    

    # loop until we're told not to
    while button_stream.is_checked():

        
        # get an image
        success, image = camera.read()
        if success:
            
            # process the image
            image = image_to_rgb_data(image)
            image = _cv2.flip(image,0)
            g.update(dict(r=image[:,:,0],
                          g=image[:,:,1],
                          b=image[:,:,2]))

            # the try/except thing here prevents a bad script from
            # pooping out the program. 
            try:
                # get the plot data based on the script
                data = eval(text_script.get_text(), g)
                
                data = data[::-1]
                image_raw.set_data(data)        
                #image_raw2.set_data(data)                  

            # If the script pooped. Quietly do nothing. The 
            # script box should be pink already
            except: 
                pass
                
            # update the frames per second
            n = n+1
            if n%10 == 0:
                label_fps.set_text("FPS = " + str(int(1.0*n/(_t.time()-t0))))
                n = 0
                t0 = _t.time()
        
        # let the gui update every frame. Otherwise it freezes!    
        window.process_events()

    # release the camera
    camera.release()
    

def button_stream2_pressed(*a):
    '''
    Called whenever the stream button 2 is pressed.
    '''

    #let the loop shut itself down
    #if not button_stream2.is_checked(): 
        #return
    
    channel = int(video_input.get_value())

    # connect to the camera
    camera = _cv2.VideoCapture(channel)

    
    
    # for the frames per second calculation    
    t0 = _t.time()
    n  = 0
    
    # global variables for script execution
    g = _np.__dict__
    

    # loop until we're told not to
    while button_stream2.is_checked():

        
        # get an image
        success, image = camera.read()
        if success:
            
            # process the image
            image = image_to_rgb_data(image)
            image = _cv2.flip(image,0)
            g.update(dict(r=image[:,:,0],
                          g=image[:,:,1],
                          b=image[:,:,2]))

            # the try/except thing here prevents a bad script from
            # pooping out the program. 
            try:
                # get the plot data based on the script
                data = eval(text_script.get_text(), g)
                
                data = data[::-1]
                #image_raw.set_data(data)        
                image_raw2.set_data(data)     
                

            # If the script pooped. Quietly do nothing. The 
            # script box should be pink already
            except: 
                pass
                
            # update the frames per second
            n = n+1
            if n%10 == 0:
                label_fps.set_text("FPS = " + str(int(1.0*n/(_t.time()-t0))))
                n = 0
                t0 = _t.time()
        
        # let the gui update every frame. Otherwise it freezes!    
        window.process_events()

    # release the cameram
    camera.release()


    
    
    
# connect the button to the function
window.connect(button_stream.signal_clicked, button_stream_pressed)
window.connect(button_stream2.signal_clicked, button_stream2_pressed)
window.show()

def show(self):
    window.connect(button_stream.signal_clicked, button_stream_pressed)
    window.connect(button_stream2.signal_clicked, button_stream2_pressed)
    window.show()

  
