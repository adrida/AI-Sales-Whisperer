import config
import openai
import os, glob
from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)
# find most recent files in a directory
recordings_dir = os.path.join('recordings', '*')

# model = whisper.load_model("base")

# list to store which wav files have been transcribed
transcribed = []

def run_transcription():
    files = sorted(glob.iglob(recordings_dir), key=os.path.getctime, reverse=False)
    if len(files) < 1:
        pass
    
    
    latest_recording = files[0]

    # if os.path.exists(latest_recording) and not latest_recording in transcribed:
    full_text = ""
    for file in files:
        if file not in ["recordings/transcribed"]:
            print("-")
            
            audio_file = open(file, "rb")
            
            result = client.audio.transcriptions.create(
                model="whisper-1",file=audio_file,prompt="Extrait dialogue entretien sales/client: ",
                response_format="text"
                )
            
            os.rename(file, file.split('/')[0]+"/transcribed/"+file.split('/')[1])
            print(result)
            full_text += result
            with open(config.TRANSCRIPT_FILE, 'a') as f:
                f.write(result)
            f.close()









