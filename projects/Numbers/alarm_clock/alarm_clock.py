import pygame as pg
import time
import datetime

'''
play MP3 music files using Python module pygame
pygame is free from: http://www.pygame.org
(does not create a GUI frame in this case)
'''
def play_ringtone(ringtone="Numbers\ringtone1.mp3", volume=0.75):
    
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''

    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(ringtone)
        #print("Music file {} loaded!".format(ringtone))
    except pg.error:
        print("File {} not found! ({})".format(ringtone, pg.get_error()))
        return

    pg.mixer.music.play()
    
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

def menu():
    while True:
        print("+-------------------------------------+\n")
        print("\t\t MENU\n")
        print("+-------------------------------------+")        
        # Choose to set alarm after a certain time interval
        # or at a specific time
        print("""\tEnter (t)imer or (a)larm
            Enter help for hints""")
        mode = input("> ")

        if mode == 't' or mode  == 'timer':
            timer()
        
        elif mode == 'a' or mode  == 'alarm':
            alarm()

        elif mode == "config":
            config()

        elif mode == "exit" or mode == "q":
            raise KeyboardInterrupt

        else:
            print("Wrong input")
            raise ValueError

def timer():
    print("Enter hours, then minutes")
    hours = int(input("Hours\n> "))
    minutes = int(input("Minutes\n> "))

    if hours == 0 and minutes != 0:
        seconds = minutes*60
    elif hours != 0 and minutes == 0:
        seconds = hours*360
    else:
        seconds = hours*360 + minutes*60

    print("timing...")
    while seconds > 0:
        time.sleep(1)
        print(".", end="")
        seconds -= 1
    
    play_ringtone()

def alarm():
    time = input("Enter time\n>")
    print("timing...")
    
    while str(f"{datetime.datetime.now():%H:%M:%S}") != time:
        print(".", end="")
    
    play_ringtone()
    
def help():
    pass

def config():
    pass

if __name__ == "__main__":
    try:
        print("+-------------------------------------+\n")
        print("\t\tALARM\n")
        print("+-------------------------------------+") 
        
        #time = f"{datetime.datetime.now():%H:%M:%S}"
        #print(time)
        
        menu()

    except KeyboardInterrupt:
        exit()