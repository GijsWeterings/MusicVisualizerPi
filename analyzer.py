from midiutil.MidiFile import MIDIFile
import sys

if len(sys.argv) != 3:
    print("Error in reading input.\n\nUsage: python %s filename.wav 128" % sys.argv[0])
    sys.exit(-1)

filename = sys.argv[1]
bpm = int(sys.argv[2])

# create MIDI object with one track
mf = MIDIFile(1)
track = 0

time = 0    # start at the beginning
mf.addTrackName(track, time, filename.split(".")[0])
mf.addTempo(track, time, bpm)

# add some notes
channel = 0
volume = 100

pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 2             # start on beat 2
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 4             # start on beat 4
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

mf.close()
# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
    
