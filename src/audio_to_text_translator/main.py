#!/usr/bin/env python
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from openai import AzureOpenAI
from pydub import AudioSegment
from pydub.utils import make_chunks
from pathlib import Path
import os
from dotenv import load_dotenv

from crews.audio_to_text_translator_crew.audio_to_text_translator_crew import AudioTextTranslatorCrew
# Load environment variables
load_dotenv(override=True)

# Initialize OpenAI client
client = AzureOpenAI(
            api_key=os.getenv("WHISPER_API_KEY"), 
            base_url=os.getenv("WHISPER_API_BASE"),
            api_version=os.getenv("WHISPER_API_VERSION")
        )

class AudioTextTranslatorState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""

class AudioTextTranslatorFlow(Flow[AudioTextTranslatorState]):

    @start()
    def transcribe_audio(self):
        print("Generating Transcription")

        SCRIPT_DIR = Path(__file__).parent
        audio_path = str(SCRIPT_DIR / "audio" / "audio.mp4")
        deployment_name = "whisper-gs"
        # if not os.path.exists(audio_path):
        #     print(f"File not found: {audio_path}")
        #     return

        # Load and split the audio into 1-minute chunks
        audio = AudioSegment.from_file(audio_path, format="mp4")
        chunk_length_ms = 60000
        chunks = make_chunks(audio, chunk_length_ms)

        full_transcription = ""
        chunk_dir = Path("audio_chunks")
        chunk_dir.mkdir(parents=True, exist_ok=True)

        for i, chunk in enumerate(chunks):
            print(f"Transcribing chunk {i+1}/{len(chunks)}")
            chunk_path = chunk_dir / f"chunk_{i}.mp4"
            chunk.export(chunk_path, format="mp4")

            with open(chunk_path, "rb") as audio_file:
                response = client.audio.transcriptions.create(
                    model=deployment_name, 
                    file=audio_file
                )
                full_transcription += response.text + " "

        print("Transcription:", response.text)
        self.state.transcript = full_transcription
        print(f"Transcription: {self.state.transcript}")

    @listen(transcribe_audio)
    def generate_audio_text_translator(self):
        print("Generating Meeting Minutes")
        crew = AudioTextTranslatorCrew()
        inputs = {"transcript": self.state.transcript}
        meeting_minutes = crew.crew().kickoff(inputs)
        self.state.meeting_minutes = meeting_minutes

def kickoff():
    audio_to_text_translator_flow = AudioTextTranslatorFlow()
    audio_to_text_translator_flow.plot()
    audio_to_text_translator_flow.kickoff()

if __name__ == "__main__":
    kickoff()


# import os
# from pathlib import Path
# import openai
# from openai import OpenAI
# from dotenv import load_dotenv

# # Load API key from .env file
# load_dotenv()
# client = OpenAI(api_key=os.getenv("AZURE_API_KEY"), base_url=os.getenv("AZURE_API_BASE"))

# # Path to your test audio file (MP3, MP4, WAV, M4A supported)
# SCRIPT_DIR = Path(__file__).parent
# audio_path = str(SCRIPT_DIR / "audio" / "audio.mp4")

# with open(audio_path, "rb") as audio_file:
#     response = client.audio.transcriptions.create(
#         model=deployment_name,  # Ensure you have access to this model
#         file=audio_file
#     )

# # Print the transcribed text
# print("Transcription:", response.text)
