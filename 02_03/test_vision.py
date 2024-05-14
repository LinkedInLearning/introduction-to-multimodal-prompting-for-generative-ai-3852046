import base64
import click
from openai import OpenAI

client = OpenAI()

IMAGE_URL = "https://binaryville.com/images/products/rex-microcontrollers-mug-black.jpg"

with open("rex-microcontrollers-mug-black.jpg", "rb") as f:
    file_content = f.read()
    base64_image = base64.b64encode(file_content).decode("utf-8")

response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": 'As an interior designer you are capable of describing very specific colors. What colors are used in this mug? \
                        Avoid generic color names. Output should be a JSON list: ["color1", "color2",...]',
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)
try:
    click.secho(response.choices[0].message.content, fg="cyan")
except:
    print(response.choices[0].message.content)
