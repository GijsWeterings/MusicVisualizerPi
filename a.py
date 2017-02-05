import mido
# pattern = midi.read_midifile("output.mid")

with mido.open_input(14) as inport:
    for message in inport:
        print(message)