from playsound import playsound
import eel


@eel.expose
def playassistantsound():
    music_dir = r"charlie\web\assests\audio\www_assets_audio_start_sound.mp3"
    playsound(music_dir)
