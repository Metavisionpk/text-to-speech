#*****************Section2*******************#
#speech to text using Amazon polly 
import boto3
import os
from dotenv import load_dotenv


load_dotenv()


aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")


polly_client = boto3.client(
    "polly",
    region_name=aws_region,
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key
)

# Convert text to speech
response = polly_client.synthesize_speech(
    Text="Hello faisal,  this is a test using Amazon Polly!",
    OutputFormat="mp3",
    VoiceId="Joanna"  
)


with open("output.mp3", "wb") as f:
    f.write(response["AudioStream"].read())

print("Speech synthesized and saved as output.mp3")
#*****************Section2*******************#
# speech to text you some pretrained model

from TTS.api import TTS

# Load a model
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to("cpu")


tts.tts_to_file(text="Hello faisal, this is a test of Coqui TTS.", file_path="output.wav")


