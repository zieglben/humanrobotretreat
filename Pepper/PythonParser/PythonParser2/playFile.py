def play(filename, asynch=False): #asynch false means wait until finished
    from playsound import playsound
    playsound(filename, asynch)