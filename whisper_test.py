from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np

print("Whisper load ho raha hai...")

model = WhisperModel("tiny", device="cpu", compute_type="int8")

print("🎤 5 seconds bolo...")

audio = sd.rec(
    int(5 * 16000),
    samplerate=16000,
    channels=1,
    dtype="float32"
)

sd.wait()

audio = audio.flatten()

print("Audio record ho gaya.")
print("🔄 Hindi speech ko text mein convert kar raha ho...")

segments, info = model.transcribe(
    audio,
    language="hi"
)

text = ""

for segment in segments:
    text += segment.text

print("\n📝 Tumne kaha:")
print(text)