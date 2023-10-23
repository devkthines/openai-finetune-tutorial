import openai

# List 10 fine-tuning jobs
openai.FineTuningJob.list(limit=10)

# Retrieve the state of a fine-tune
openai.FineTuningJob.retrieve("ftjob-DqYmBepc1mivDgy3opQVMQuH")

# Cancel a job
# openai.FineTuningJob.cancel("ftjob-DqYmBepc1mivDgy3opQVMQuH")

# List up to 10 events from a fine-tuning job
# openai.FineTuningJob.list_events(id="ftjob-DqYmBepc1mivDgy3opQVMQuH", limit=10)

# Delete a fine-tuned model (must be an owner of the org the model was created in)
# openai.Model.delete("ft:gpt-3.5-turbo:acemeco:suffix:ftjob-DqYmBepc1mivDgy3opQVMQuH")

completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo-0613:personal::8CLO75St",
  messages=[
    {"role": "system", "content": "Given a sports headline, provide the following fields in a JSON dict, where applicable: player (full name), team, sport, and gender"},
    {"role": "user", "content": "Richardson wins 100m at worlds to cap comeback"}
  ]
)

print(completion.choices[0].message)