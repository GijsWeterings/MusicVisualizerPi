# play an embedded midi music file on your computer's sound card
# experiments with module pygame from: http://www.pygame.org/
# tested with Python25 and PyGame171      vegaseat      04sep2007
"""
# use this short program to create the base64 encoded midi music string
# (base64 encoding simply produces a readable string from binary data)
# then copy and paste the result into your pygame program ...
import base64
mid_file = "FishPolka.mid"
print "mid64='''\\\n" + base64.encodestring(open(mid_file, 'rb').read()) + "'''"
"""
import pygame
import base64
import io

# print "If this crashes, the wav file might be unsigned. Load it in audacity and export it as a .wav file (signed 16 bit)"

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    # pygame.mixer.music.load(music_file)
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file %s loaded!" % music_file)
    except pygame.error:
        print("File %s not found! (%s)" % (music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    # check if playback has finished
    while pygame.mixer.music.get_busy():
        
        clock.tick(30)
mid64='''\
TVRoZAAAAAYAAQACA8BNVHJrAAAACwD/UQMFuNgA/y8ATVRyawAAAC4A/wMJZmVlc3R0ZW50AJA8
ZIdAgDxkh0CQQGSHQIBAZIdAkENkh0CAQ2QA/y8A
'''

# create a memory file object

midi_str = base64.b64decode(mid64)
music_file = io.BytesIO(midi_str)
freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)
try:
    # use the midi file object from memory
    play_music("feesttent.wav")
    # print music_file.next()
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit
