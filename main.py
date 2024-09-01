import speech_recognition as sr
from os import path
from pydub import AudioSegment


def transcribe_audio():
        # convert mp3 file to wav
        sound = AudioSegment.from_mp3('transcript.mp3')
        sound.export("transcript.wav", format="wav")


        # transcribe audio file
        wav_file= "transcript.wav"

        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(wav_file) as source:
                audio = r.record(source)  # read the entire audio file
                print("Transcription: " + r.recognize_google(audio))
                
transcribe_audio()