import tkinter as tk
from tkinter import BitmapImage
from tkinter.filedialog import *
import os
import pygame
from mutagen.easyid3 import EasyID3
import pyowm
from pyowm.caches.lrucache import LRUCache
from weather import user_value
from PIL import ImageTk,Image
from pygame import image

owm = pyowm.OWM("087d6d20af763d169b1d4be61e22776b")


class MusicPlayer():
    def __init__(self,root):
        super().__init__()
        self.root = root
        self.root.title("Zing MP3")
        self.root.geometry("1150x400")
        self.root.iconbitmap(r"favicon.ico")
        self.paused = False
        self.actual_song = 0
        self.song = list()
        self.current_track = StringVar()
        self.status = StringVar()
        self.input = StringVar()
        pygame.init()
        pygame.mixer.init()

        
        #Music Box
        track_name = LabelFrame(self.root,text="Song Track",font=("times new roman",15, "bold"),bg = "black", fg="white",bd= 5, relief= GROOVE)
        track_name.place(x=0,y=0,width=800,height=300)

        song = Label(track_name,textvariable=self.current_track,width=30, font=("times new roman",24, "bold"), bg = "blue", fg="white").grid(row=0,column=0,padx=10,pady =5)
        status = Label(track_name,textvariable=self.status,font=("times new roman",24,"bold"), bg ="yellow", fg="black").grid(row=0, column= 1, padx = 0, pady = 0)

        buttonFrame = LabelFrame(self.root, text="Control Area", font=("times new roman", 15, "bold"), bg="black", fg="white", bd = 5 , relief = GROOVE)
        buttonFrame.place(x=0,y=100,width=800,height=300)

        playButton = Button(buttonFrame, text = "Play", command=self.play_music, font=("times new roman",15,"bold"), bg = "black",fg="white",width=8,height=1).grid(row=0,column=0,padx=10,pady=5)
        #Pause Button
        pauseButton = Button(buttonFrame, text ="Pause", command=self.pause_music, font=("times new roman",15,"bold"), bg = "black",fg = "white", width=8,height=1).grid(row=0,column=1,padx=10,pady=5)
        #Unpause Button
        nextButton = Button(buttonFrame, text="Next", command=self.next_song, font=("times new roman",15,"bold"), bg = "black", fg = "white",width=8,height=1).grid(row=0,column=2,padx=10,pady=5)
        repeatButton = Button(buttonFrame, text="Repeat", command=self.repeat, font=("times new roman",15,"bold"), bg = "black", fg = "white",width=8,height=1).grid(row=0,column=3,padx=10,pady=5)
        #Stop Button
        stopButton = Button(buttonFrame, text="Stop", command=self.stop_music, font=("times new roman",15,"bold"), bg = "black", fg="white", width=8,height=1).grid(row=0, column=4,padx=10,pady=5)
        #Next Button
        addButton = Button(buttonFrame, text="Add",command=self.add_music, font=("times new roman",15,"bold"),bg = "black", fg="white", width=7,height=1).grid(row=0, column=5,padx=10,pady=5)

        playlistFrame = LabelFrame(self.root, text="Playlist", font=("times new roman",15,"bold"), bg="grey",fg="white",bd=5,relief=GROOVE)
        playlistFrame.place(x=750,y=0,width=400, height = 400)
        scrol_y = Scrollbar(playlistFrame,orient=VERTICAL)

        self.playlist = Listbox(playlistFrame,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE,height=200)

        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)

        self.SONG_END = pygame.USEREVENT + 1



        #Weather Box
        weatherFrame = LabelFrame(self.root, text="Weather", font=("times new roman",15,"bold"), bg="grey",fg="black",bd=5,relief=GROOVE)
        weatherFrame.place(x=0,y=200,width=375,height=200)
        name = Label(weatherFrame,text="Location: ",font=("times new roman",15,"bold"), bg="grey",fg="black").grid(row=0,column=0)
        place = Entry(weatherFrame,font=("times new roman",15,"bold"),width=20).grid(row=0,column=1)
        searchButton = Button(weatherFrame, text="Search", command=user_value, font=("times new roman",10,"bold"),bg = "black", fg="white", width=6,height=1).grid(row=0, column=2,padx=10,pady=5)
        
        
        output_weather = Label(root,font=("times new roman",15,"bold"),text="Please put in location ...",bg="grey",fg="black",bd=5,relief=GROOVE)
        output_weather.place(x=0,y=300,width=375,height=100)


        



        #Icon Box
        iconFrame = LabelFrame(self.root, text="Social Media", font=("times new roman",15,"bold"), bg="grey",fg="black",bd=5,relief=GROOVE)
        iconFrame.place(x=375,y=200,width=375,height=200)
        google_icon = Image.open("google-icon.png")
        #google_icon = google_icon.resize((50,50),Image.ANTIALIAS)
        #google_icon = ImageTk.PhotoImage(google_icon)
        #google = Label(iconFrame, image=google_icon).grid(row=0,column=0,padx=93,pady=25)
        scale = Scale(iconFrame,from_=1,to=5,resolution=1,orient=HORIZONTAL,bg="grey",relief=GROOVE,highlightbackground="grey")
        scale.pack(fill=X,side=BOTTOM)






    #Music Function Button
    def add_music(self):
        os.chdir("Music")
        songtracks = os.listdir()
        for song in songtracks:
            print(song)
            self.song.append(song)

        for key,track in enumerate(self.song):
            try:
                song = EasyID3(track)
                song_key = key
                song_data = (song['title'][0] + ' - '
                         + song['artist'][0])
                self.playlist.insert(END,song_data + "\n")
            except: 
                pass

        
    def play_music(self):
        self.current_track.set(self.song[self.actual_song])
        self.status.set("Playing")
        pygame.mixer.music.load(self.song[self.actual_song])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(self.SONG_END)
        self.paused = False
    
    def pause_music(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.status.set("Playing")
        elif not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            self.status.set("Paused")
    
    def check_music(self):
        for event in pygame.event.get():
            if event.type == self.SONG_END:
                self.next_song()

    def next_song(self):
        self.actual_song = self.get_next_song()
        self.play_music()

    def get_next_song(self):
        if self.actual_song + 2 <= len(self.song):
            return self.actual_song + 1
        else:
            return 0
    
    def repeat(self):
        self.status.set("Repeated")
        pygame.mixer.music.load(self.song[self.actual_song])
        pygame.mixer.music.play(-1)
    
    def stop_music(self):
        self.status.set("Stopped")
        pygame.mixer.music.stop()






    






            




gui = tk.Tk()
gui.title("wm min/max")
#lock the maximize screen   
gui.resizable(0,0)
MusicPlayer(gui)
gui.mainloop()

        
