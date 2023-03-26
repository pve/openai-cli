import openai
import argparse
import csv
import os
from dotenv import load_dotenv
#chatgpt, obsolete

load_dotenv() 

openai.api_key = os.getenv("OPENAI_API_KEY")

parser = argparse.ArgumentParser(description="OpenAI chatbot command line interface")
parser.add_argument("--model", default="gpt-3.5-turbo", help="Name of the GPT-3 model to use")
parser.add_argument("--prompt", default="", help="Initial prompt to start the conversation")
parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature for the model")
parser.add_argument("--max_tokens", type=int, default=50, help="Maximum number of tokens to generate for each response")
parser.add_argument("--stop_sequence", default="", help="Sequence to stop generation at")
parser.add_argument("--csv_file", default="conversation.csv", help="Name of the CSV file to store the conversation in")
args = parser.parse_args()

with open(args.csv_file, "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    if csvfile.tell() == 0:
        writer.writerow(["Speaker 1", "Message 1", "Speaker 2", "Message 2"])

    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        response = openai.Completion.create(
            engine=args.model,
            prompt=args.prompt + message,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            stop=args.stop_sequence,
        )
        text = response.choices[0].text.strip()
        print("AI: " + text)
        writer.writerow(["You", message, "AI", text])
