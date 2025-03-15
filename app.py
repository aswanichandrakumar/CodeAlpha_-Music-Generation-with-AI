from flask import Flask, render_template, request, send_file
import numpy as np # type: ignore
from music21 import stream, note, midi # type: ignore

app = Flask(__name__)

# Function to generate a random music sequence
def generate_music_sequence():
    possible_notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
    generated_notes = np.random.choice(possible_notes, size=8)  # Generate 8 random notes
    return generated_notes.tolist()

# Convert the generated sequence to a MIDI file
def create_midi(notes, output_file="output.mid"):
    midi_stream = stream.Stream()
    for note_name in notes:
        midi_stream.append(note.Note(note_name))
    midi_stream.write("midi", fp=output_file)
    return output_file

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    notes = generate_music_sequence()
    midi_file = cr # type: ignore
