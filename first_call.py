from dotenv import load_dotenv
import anthropic


load_dotenv()
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    messages=[
        {"role": "user", "content": "Explain in 3 sentences what a key account manager does."}
    ],
)


print(message.content[0].text)