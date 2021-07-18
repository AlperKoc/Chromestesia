import random
import math
from Barney import Barney
from Time import Time

barnies = []
beats = []
time = Time(133,60)

def setup():
    size(700,700)
    background(248,250,244)
    frameRate(60)
    
    global beats
    global time
    beats = [1]
    
    
    barney_config = {"x":0,"y":0,"z":0,
                     "direction_x": True,
                     "direction_y": True,
                     "rand_x":0, "rand_y":0,
                     "fill":(128,128,128),"stroke":(128,128,128),
                     "angle":0, "size": 1, "speed":1, "fade_speed":1,
                     "local_rand": 0, "global_rand": 0,
                     "bpm":120, "beat_speed":4,"shape":"circle", 
                     "centralize":0.5,'instrument':'bassline'}
    
    barney_config2 = {"x":0,"y":0,"z":0,
                     "direction_x": True,
                     "direction_y": True,
                     "rand_x":0, "rand_y":0,
                     "fill":(22,22,22),"stroke":(222,222,222),
                     "angle":0, "size": 1, "speed":1, "fade_speed":1,
                     "local_rand": 0, "global_rand": 0,
                     "bpm":120, "beat_speed":0.5, "shape":"circle", 
                     "centralize":0.5,'instrument':'bassline'}
    
    barney  = Barney(barney_config,time)#(0,0,True,True,1,1,0,0,0.25)
    barney2 = Barney(barney_config2,time)#(0,0,True,True,1,1,0,0,0.25)

    barnies.append(barney)
    barnies.append(barney2)
    
def draw():
    global barnies
    global time
    
    time.update_time()
    time.check_beat(0.5)
    

    for barney in barnies:
        barney.update()
        barney.draw()



   
