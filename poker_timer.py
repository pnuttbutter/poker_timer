from Tkinter import *
import json
import time

config_file = 'D:\\poker_timer\\pk_config.json'

FONT = 'arial'
BACKGROUND = 'green'


class Stopwatch(Frame):
   
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        root.geometry("1800x900")
        root.configure(background=BACKGROUND)
        self.create_widgets()
        
        self.reset()

    def create_widgets(self):
        self.lbl_players = Label(root,font=(FONT,40), fg='white', bg=BACKGROUND)
        self.lbl_players.place(x = 100, y = 100, width=1600, height=100)

        self.btn_player_inc = Button(root,text='+',command=self.btn_player_inc_handler, font=(FONT,20), fg='white', bg=BACKGROUND)
        self.btn_player_inc.place(x=1600,y=100,width=100,height=50)

        self.btn_player_dec = Button(root,text='-', command=self.btn_player_dec_handler, font=(FONT,20), fg='white', bg=BACKGROUND)
        self.btn_player_dec.place(x=1600,y=150,width=100,height=50)
        
        self.lbl_clock = Label(root, font=(FONT,200), fg='white', bg=BACKGROUND )
        self.lbl_clock.place(x = 100, y = 200, width=1600, height=300)

        self.lbl_small=Label(root, font=(FONT,75), fg='white', bg=BACKGROUND  )
        self.lbl_small.place(x=100,y=500,width=800,height=200)

        self.lbl_big=Label(root, font=(FONT,75), fg='white', bg=BACKGROUND)
        self.lbl_big.place(x=900,y=500,width=800,height=200)

        self.btn_main=Button(root, command=self.btn_main_handler,font=(FONT,40), fg='white', bg=BACKGROUND)
        self.btn_main.place(x = 100, y = 700, width=1600, height=100)

    ### main button handler, updates dependent on status
    def btn_main_handler(self):
        if self.status == 'STOPPED':
            self.remaining_time = self.duration
            self.elapsed_time = 0.0
            self.timer_start()            
        elif self.status == 'PAUSED':            
            self.timer_start()
        elif self.status == 'RUNNING':
            self.timer_stop()

        self.update_widgets()

    def update_widgets(self):
        self.lbl_players['text'] = str(self.players) + " players - " +  self.get_time(self.duration) + " per level"
        self.lbl_small['text']=str(self.levels[self.current_level]['small_blind']) + ' small'
        self.lbl_big['text']=str(self.levels[self.current_level]['big_blind']) + ' big'

        if self.status == 'STOPPED':
            self.btn_main['text'] = 'START'            
        elif self.status == 'PAUSED':
            self.btn_main['text'] = 'CONTINUE'
        elif self.status == 'RUNNING':
            self.btn_main['text'] = 'PAUSE'

        if self.status == 'PAUSED':
            self.lbl_clock['fg'] = 'grey'    
        elif self.time <= 10 and self.time > 0:
            self.lbl_clock['fg'] = 'red'
        else:
            self.lbl_clock['fg'] = 'white'    

    ## needs TLC
    def beep(self):
        pass        
            
    def btn_player_inc_handler(self):
        self.players +=1
        self.duration = ((self.players * self.player_seconds) + self.base_seconds)
        self.update_widgets()

    def btn_player_dec_handler(self):
        self.players +=-1 if self.players > 2 else 0
        self.duration = ((self.players * self.player_seconds) + self.base_seconds)
        self.update_widgets()

    def reset(self):
        self.status = 'STOPPED'
        self.config = json.load(open(config_file, 'r'))
        self.load_config()
        self.duration = self.base_seconds + (self.players * self.player_seconds)
        self.current_level = 0
        self.time = 0
        self.lbl_clock['text'] = self.get_time(self.time)
        self.update_widgets()

    def load_config(self):
        self.players = self.config['players']
        self.player_seconds = self.config['player_seconds']
        self.base_seconds = self.config['base_seconds']
        self.levels = self.config['levels']
        self.tables = self.config['tables']
    
    def timer_start(self):
        self.status = 'RUNNING'
        self.start = (time.time() - self.elapsed_time)
        self.timer_update()

    def timer_stop(self):
        self.after_cancel(self.timer)
        
        if self.time <= 0:            
            self.status = 'STOPPED'
            self.current_level += 1
        else:
            self.status = 'PAUSED'
        self.update_widgets()       

    def get_time(self, time):
        #self.time = self.remaining_time - round(self.elapsed_time,0)
        minutes = str(int(time) / 60)
        seconds = str(int(time) % 60)
        return minutes.zfill(2) + ':' + seconds.zfill(2)
        #self.lbl_clock['text'] = minutes.zfill(2) + ':' + seconds.zfill(2)
        
    def timer_update(self):
        self.elapsed_time = time.time() - self.start
        self.time = self.remaining_time - round(self.elapsed_time,0)
        self.lbl_clock['text'] = self.get_time(self.time)        
        self.timer = self.after(500,self.timer_update)
        self.update_widgets()            
        if self.time <= 0:      ## when timer hits zero, stop timer          
            self.timer_stop()    
        
        

if __name__ == '__main__':
   root = Tk()
   sw = Stopwatch(root)

   root.mainloop()
