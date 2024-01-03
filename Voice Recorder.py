import sounddevice
from scipy.io.wavfile import write

time = int(input("Enter time limit for recording in seconds : "))
name = input("Enter the name that you want the file to be saved with the extension .wav")

def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")

voice_recorder(time,name)