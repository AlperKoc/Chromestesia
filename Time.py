class Time():
    def __init__(self,bpm,fps):
        self.frame_count = 0
        self.total_time = 0
        self.seconds = 0
        self.minutes = 0
        self.bpm = bpm
        self.beat_count = 0
        self.fps = fps
        self.fpb = self.get_fpb()
    
    # every frame
    def update_time(self):
        self.frame_count += 1
        if self.frame_count % 3600 == 0:
            self.minutes +=1
            self.seconds = 0
        elif self.frame_count % 60 == 0:
            self.seconds += 1
            self.total_time += 1
        time = ":".join([str(self.minutes).zfill(2),
                         str(self.seconds).zfill(2),
                         "00"])
        if self.frame_count % 60 == 0:
            print(time)
        return time
    
    def get_fpb(self): # frames per beat
        bpm = self.bpm
        fps = self.fps
        fpb = 60 * fps / bpm
        return int(fpb)
            
    def check_beat(self, bar = 1): # 0.25, 0.5, 1,2,4,8,16 etc
        fpb = self.fpb * bar
        if fpb == 0:
            return False
        if self.frame_count % fpb == 0:
            self.beat_count +=1
            return True
        return False
    

        
        
