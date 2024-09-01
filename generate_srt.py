import whisper  
import torch  
import os  
from tqdm import tqdm  
  
# Check if GPU is available  
device = "cuda" if torch.cuda.is_available() else "cpu"  
  
# Load the Whisper model  
model = whisper.load_model("medium").to(device)  
  
# Path to the directory containing your audio files  
audio_files_directory = r"E:\iCloudDrive\English\Hackers_IELTS_Speaking_MP3_8\1_learning_copy"  
  
# Get a list of all audio files in the directory  
audio_files = [f for f in os.listdir(audio_files_directory) if f.endswith(('.mp3', '.wav', '.m4a', '.ogg'))]  
  
# Process each audio file  
for audio_file in tqdm(audio_files):  
    # Full path to the audio file  
    audio_path = os.path.join(audio_files_directory, audio_file)  
  
    # Transcribe the audio file using Whisper  
    result = model.transcribe(audio_path, fp16=True)  
  
    # Prepare the output SRT file  
    srt_filename = os.path.splitext(audio_file)[0] + ".srt"  
    srt_path = os.path.join(audio_files_directory, srt_filename)  
  
    with open(srt_path, "w") as srt_file:  
        for i, segment in enumerate(result['segments']):  
            # Write the SRT format content  
            start_time = segment['start']  
            end_time = segment['end']  
            text = segment['text']  
  
            srt_file.write(f"{i + 1}\n")  
            srt_file.write(  
                f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02},{int((start_time - int(start_time)) * 1000):03} --> ")  
            srt_file.write(  
                f"{int(end_time // 3600):02}:{int((end_time % 3600) // 60):02}:{int(end_time % 60):02},{int((end_time - int(end_time)) * 1000):03}\n")  
            srt_file.write(f"{text.strip()}\n\n")  
  
print("SRT files generated successfully.")
