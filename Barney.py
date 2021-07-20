import random
import math

class Barney():
    def __init__(self,config,time):
        self.count       = 0                     # int - total frame count of barney
        self.step        = 0
        self.x           = config['x']           # int [0,width]
        self.y           = config['y']           # int [0,height]
        self.z           = config['z']           # for later
        self.direction_x = config['direction_x'] # bool
        self.direction_y = config['direction_y'] # bool
        self.rand_x      = config['rand_x']      # int
        self.rand_y      = config['rand_y']      # int
        self.rand_global = config['rand_global']  # int [0,10]
        self.rand_local  = config['rand_local'] # int [0,10]
        self.angle       = config['angle']       # int
        self.speed       = config['speed']       # int [0,10]
        self.step_size   = height/ config['step_size'] # int [0,10]
        self.fade_speed  = config['fade_speed']  # int [0,10]
        self.beat_speed  = config['beat_speed']  # float 0.25, 2, 8, 0.50 etc.
        self.centralize  = config['centralize']  # [0,1] 0 to edges, 1 to center, 0.5 freewalk
        self.instrument  = config['instrument']
        self.walk_style  = config['walk_style']
        self.fill        = config['fill']        # (H,S,B)
        self.stroke      = config['stroke']      # (H,S,B)
        self.size        = config['size']        # int [0,10]
        self.shape       = config['shape']       # 'point' shape of barney
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
    def get_locs(self):
        mid_x = width/2; mid_y = height/2
        return self.get_x(), self.get_y(), self.get_direction_x(), self.get_direction_y(), mid_x, mid_y
    def get_rands(self):
        return self.rand_x,self.rand_y,self.rand_local,self.rand_global
    def get_colors(self):
        fill = self.fill
        stroke = self.stroke
        return fill,stroke
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
    def step_up(self):
        self.step +=1
    
    def jail(self):
        x,y,direction_x,direction_y,mid_x,mid_y = self.get_locs()
        
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
            
    def random_walk(self):
        x,y,direction_x,direction_y,mid_x,mid_y = self.get_locs()
        
        c = 40
        r = 9
        if direction_x:
            x += c * self.rand_x + random.uniform(-r, r)
            self.set_x(x)
        else:
            x -= c * self.rand_x + random.uniform(-r, r)
            
            
            self.set_x(x)
        if direction_y:
            y += c * self.rand_y + random.uniform(-r, r)
            self.set_y(y)
        else: 
            y -= c * self.rand_y + random.uniform(-r, r)
            self.set_y(y)
            
        if self.get_count() % 200 == 0:
            self.set_direction_x(random.choice([True, False]))
            self.set_direction_y(random.choice([True, False]))
            self.set_rand_x(random.uniform(0, 1))
            self.set_rand_y(random.uniform(0, 1))
            
    def square_walk(self):
        x,y,direction_x,direction_y,mid_x,mid_y = self.get_locs()
        # direction = self.direction
        
        # if direction == 'right':
        #         direction = 'down'
        # elif direction == 'down':
        #         direction = 'left'
        # elif direction == 'left':
        #         direction = 'up'    
        # elif direction == 'up':
        #         direction = 'right'
    def check_turn(self):
        self.count_up() # count += 1
        time = self.time
        beat_speed = self.beat_speed
        return time.check_beat(beat_speed)
        
    def smooth(self):
        x,y,direction_x,direction_y,mid_x,mid_y = self.get_locs()
        c = self.count
        fill(c%120+54 + c%134+98 ,c%200+34)
        stroke(12,108,231,10)
        circle(x,y,c%56+1)
        if c % 10 == 0:
            line(mid_x, mid_y, x, y)
        stroke(c%20+100 + c%20+20 ,c%50+200)
    
    def simple(self):
        x,y,direction_x,direction_y,mid_x,mid_y = self.get_locs()
        stroke(90,60,50)
        circle(x,y,10)

    
    def render(self):
        self.step_up()
        shape = self.shape
        fill_, stroke_ = self.get_colors()
       
        colorMode(HSB, 100)
        fill  (*fill_)
        stroke(*stroke_)
        
        if self.shape == 'simple':
            self.simple()
            
        if self.shape == 'smooth':
            self.smooth()
            
    def update(self):        
        self.jail() # check edges and keep it inside
        if self.walk_style == 'random':
            self.random_walk() # add local random movements
        if self.walk_style == 'square':
            self.square_walk() # add local random movements

    def draw(self):
        if self.check_turn():
            self.render()


        
