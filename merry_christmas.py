from microbit import *
import music
while True:
    display.scroll("Merry Christmas", delay=75, wait=False, loop=True)
    tune = ["C4:4", "F4", "F4:2", "G4", "F4", "E4", "D4:4", "D4:4", "D4:4",
            "G4", "G4:2", "A4", "G4", "F4", "E4:4", "E4", "E4", "A4",
            "A4:2", "A#4:2", "A4:2", "G4:2", "F4:4", "D4", "C4:2", "C4:2",
            "D4:4", "G4:4", "E4:4", "F4:8"]
    music.play(tune)