import random
import math

class Barney():
    def __init__(self,config,time):
        self.x           = config['x']           # int [0,width]
        self.y           = config['y']           # int [0,height]
        self.z           = config['z']           # for later
        self.direction_x = config['direction_x'] # bool
        self.direction_y = config['direction_y'] # bool
        self.rand_x      = config['rand_x']      # int
        self.rand_y      = config['rand_y']      # int
        self.fill        = config['fill']        # (H,S,B)
        self.stroke      = config['stroke']      # (H,S,B)
        self.count       = 0                     # int - total frame count of barney
        self.angle       = config['angle']       # int
        self.size        = config['size']        # int [0,10]
        self.speed       = config['speed']       # int [0,10]
        self.fade_speed  = config['fade_speed']  # int [0,10]
        self.local_rand  = config['local_rand']  # int [0,10]
        self.global_rand = config['global_rand'] # int [0,10]
        self.bpm         = config['bpm']         # bpm of track
        self.beat_speed  = config['beat_speed']  # float 0.25, 2, 8, 0.50 etc.
        self.shape       = config['shape']       # 'point' shape of barney
        self.centralize  = config['centralize']  # [0,1] 0 to edges, 1 to center, 0.5 freewalk
        self.instrument  = config['instrument']
        self.time        = time
        
     
        
        
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_direction_x(self):
        return self.direction_x
    def get_direction_y(self):
        return self.direction_y
    def get_count(self):
        return self.count
    def get_loc(self):
        mid_x = width/2
        mid_y = height/2
        return self.get_x(), self.get_y(), mid_x, mid_y
    
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_direction_x(self,direction_x):
        self.direction_x = direction_x
    def set_direction_y(self,direction_y):
        self.direction_y = direction_y
    def set_rand_x(self,rand_x):
        self.rand_x = rand_x
    def set_rand_y(self,rand_y):
        self.rand_y = rand_y
    def count_up(self):
        self.count +=1
    
    def jail(self):
        x = self.get_x()
        y = self.get_y()
        
        if x <= 0:
            self.set_direction_x(True)
            self.set_rand_x(random.uniform(0, 1))
            self.set_rand_y(random.uniform(0, 1))
        elif x >= width:
            self.set_direction_x(False)
            self.set_rand_x(random.uniform(0, 1))
            self.set_rand_y(random.uniform(0, 1))
        if y <= 0:
            self.set_direction_y(True)
            self.set_rand_x(random.uniform(0, 1))
            self.set_rand_y(random.uniform(0, 1))
        elif y >= height:
            self.set_direction_y(False)
            self.set_rand_x(random.uniform(0, 1))
            self.set_rand_y(random.uniform(0, 1))
            
    def random_machine(self):
        direction_x = self.get_direction_x()
        direction_y = self.get_direction_y()
        x = self.get_x()
        y = self.get_y()
        
        if direction_x:
            x += 1 * self.rand_x + random.uniform(-3, 3)
            self.set_x(x)
        else:
            x -= 1 * self.rand_x + random.uniform(-3, 3)
            self.set_x(x)
        if direction_y:
            y += 1 * self.rand_y + random.uniform(-3, 3)
            self.set_y(y)
        else: 
            y -= 1 * self.rand_y + random.uniform(-3, 3)
            self.set_y(y)
            
        if self.get_count() % 40 == 0:
            self.set_direction_x(random.choice([True, False]))
            self.set_direction_y(random.choice([True, False]))
            self.set_rand_x(random.uniform(0, 1))
            self.set_rand_y(random.uniform(0, 1))

    def update(self):        
        self.count_up() # count += 1
        self.jail() # check edges and keep it inside
        self.random_machine() # add local random movements
        
    def walk(self, _fill, _stroke, speed, evolve_speed, beat_speed, angle):
        x,y,mid_x,mid_y = self.get_loc()

        colorMode(HSB, 100)
        fill  (*self.fill)
        stroke(*self.stroke)
        
        if beat_speed:
            circle(x,y,30)
        else:
            stroke(90,60,50)
            circle(x,y,10)
        
    def splash(self, fill, stroke, speed, evolve_speed, beat_speed):
        pass
        # fill(count%120+54 + count%134+98 ,count%200+34)
        # stroke(12,108,231,10)
        # circle(x,y,count%56+1)
        # if barnies[0].count % 10 == 0:
        #     line(mid_x, mid_y, x, y)
        # stroke(count%20+100 + count%20+20 ,count%50+200)
        
        # if count == 100: 
        #   start_x = random.randint(0,width)
        #   start_y = random.randint(0,height)

        #   barney2 = Barney(start_x,start_y,True,True,1,1,0,0)
        #   barnies.append(barney2)
        
    def is_it_my_turn(self):
        time = self.time
        beat_speed = self.beat_speed
        return time.check_beat(beat_speed)
    
    def draw(self):
        if self.is_it_my_turn():
            print(self.beat_speed)
            self.walk(self.fill,
                self.stroke,
                self.speed,
                self.fade_speed ,
                self.beat_speed,
                self.angle)


        
