from moviepy.editor import *
from pydub import AudioSegment
import sys,os
import wave
print("**START**")
vidofile = input("Enter Video Path:")
video = VideoFileClip(vidofile)
audio = video.audio
audio_file=  input("Enter Audio file name:")
audio.write_audiofile(audio_file)

def mp3_to_wav(audio_file_name):
    if audio_file_name.split('.')[1] == 'mp3':    
        sound = AudioSegment.from_mp3(audio_file_name)
        audio_file_name = audio_file_name.split('.')[0] + '.wav'
        sound.export(audio_file_name, format="wav")
        print("Converted into wav")
    return audio_file_name
def stero_to_mono(audio_file_name):
    sound = AudioSegment.from_wav(audio_file_name)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound.export(audio_file_name, format="wav")
    print("converting channel into mono")

def frame_rate_channel(audio_file_name):
    with wave.open(audio_file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate,channels

print("Converting Mp3 into wav")
wav_file = mp3_to_wav(audio_file)
print(wav_file)
audio_file = audio_file.split("/")[-1]
# print(audio_file)
os.remove(audio_file)
frame_rate,channels = frame_rate_channel(wav_file)
if channels>1:
    stero_to_mono(wav_file)
    frame_rate,channels = frame_rate_channel(wav_file)
print(frame_rate,channels)
print("**DONE**")







