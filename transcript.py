import whisper
# Load the model (options: tiny, base, small, medium, large) Medium took my computer 30 minutes to transcribe a 34 minute video, so choose based on your needs and hardware capabilities. 
# The larger the model, the better the accuracy, but also the longer the processing time. The tiny model is very fast but less accurate, while the large model is the most accurate but also the slowest.
model = whisper.load_model("medium")
# Video name (Must be is the same folder as this script), Language (Optional, default is English)
result = model.transcribe("anderson part 2 new.mp4", language="English")

# Full transcript (without timestamps)

print(result["text"])

# Timestamped segments (Speaker diarization is not supported, so segments are based on pauses in speech)
for seg in result["segments"]:
    print(f"[{seg['start']:.1f}s - {seg['end']:.1f}s] {seg['text']}")

# Save to file
with open("whisper_transcript.txt", "w") as f:
    f.write(result["text"])