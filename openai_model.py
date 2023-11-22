import openai;
from pathlib import Path;

file_path = Path(__file__).parent / "output.mp3";

response = openai.Completion.create(
  model="tts-1",
  voice="alloy",
  input="The quick brown fox jumped over the lazy dog.",
  max_tokens=50
)

response.stream_to_file(file_path);