from time import time, strftime, localtime

class StopWatch:

    def __init__(self):
        self.start_time = 0
        self.pause_time = 0 # time spent on pause
        self.on_pause = False

    def start(self):
        if self.on_pause:
            self.start_time += time() - self.pause_time
            self.on_pause = False
            self.pause_time = 0
        else:
            self.start_time = time()

    def pause(self):
        self.on_pause = True
        self.pause_time = time()
    
    def stop(self):
        self.pause()
    
    def reset(self):
        self.on_pause=False
        self.start()
        self.on_pause=True

    def change_time(self, hours=0, minutes=0, seconds=0):
        self.start_time = min(
                            time(), 
                            (self.start_time 
                                + (hours * 3600) 
                                + (minutes * 60) 
                                + seconds
                                )
                            )

    def add_second(self):       self.change_time(seconds=-1)
    def remove_second(self):    self.change_time(seconds=1)
    def add_minute(self):       self.change_time(minutes=-1)
    def remove_minute(self):    self.change_time(minutes=1)
    def add_hour(self):         self.change_time(hours=-1)
    def remove_hour(self):      self.change_time(hours=1)

    def get_time(self) -> tuple:
        "Returns time as tuple (hour, minute, second) since start"
        t = time()
        if self.on_pause:
            t -= t - self.pause_time
        return localtime(t-self.start_time)[3:6]


