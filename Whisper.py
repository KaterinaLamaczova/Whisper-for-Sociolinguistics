import whisper
import os

#Load model that will be used for transcription
model = whisper.load_model("large")

#Establish the directory with audios
directory = "C:/User/Documents/Python/whisper"

#Create a list to store audio files
files = []

#Add audio files in .WAV format found in the directory to the list
for filename in os.scandir(directory):    
    if filename.path[-3:] == "WAV":
        file_name = str(os.path.basename(filename).split('/')[-1])
        files = files + [file_name]

#Transcribe each audio file in the list and store the transcription in .txt format
#The .txt files are named according to the corresponding audio file
for file in files:
    result = model.transcribe(file)
    result = result["text"]
    with open (file + ".txt", "w", encoding="utf-8") as f:
        f.write(result)