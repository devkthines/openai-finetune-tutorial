import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.File.create(
  file=open("dataset.jsonl", "rb"),
  purpose='fine-tune'
)

openai.FineTuningJob.create(training_file="file-cLQHXCqHc6KnGFKEeSp6Rq9s", model="gpt-3.5-turbo")