import soundfile as sf
import sounddevice as sd

# Read the audio file
def playsound():
    data, fs = sf.read("charlie\web\assests\audio\www_assets_audio_start_sound.mp3")

    # Play the audio
    sd.play(data, fs)
    sd.wait()

playsound()