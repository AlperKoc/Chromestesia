import random
import math
from Barney import Barney
from Time import Time
 
barnies = []
beats = []
time = Time(112,60)

def setup():
    size(700,700)
    background(248,250,244)
    frameRate(60)
    
    global beats
    global time
    beats = [1]
    
    
    barney_config = {"x":0,"y":10,"z":0,
                     "direction_x": True,
                     "direction_y": False,
                     "rand_x":0, "rand_y":0,
                     "rand_local": 0, "rand_global": 0,
                     "angle":0, "speed":1, "step_size":16,
                     "fade_speed":1,"beat_speed":1,
                     "centralize":0.5,'instrument':'bassline',
                     "walk_style": "random",
                     "fill":(128,128,128),"stroke":(255,255,255),
                     "size": 1, "shape":"simple"}
    
    barney_config2 = {"x":0,"y":0,"z":0,'direction':'right',
                     "direction_x": True,
                     "direction_y": True,
                     "rand_x":0, "rand_y":0,
                     "rand_local": 0, "rand_global": 0,
                     "angle":0, "speed":1,"step_size":10,
                     "fade_speed":1,"beat_speed":0.5,
                     "centralize":0.5,'instrument':'bassline',
                     "walk_style": "random",
                     "fill":(22,22,22),"stroke":(222,222,222),
                     "size": 1, "shape":"smooth"}

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
        if barney.check_turn():
            print(barney.walk_style)
            barney.update()
            barney.draw()



   
