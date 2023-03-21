import openai

openai.api_key = "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"
openai.organization = "org-bEMWLibPaMNoZX9kxwESHX8f"
response = openai.Image.create(
        prompt="among us",
        n=1,
        size="256x256"
)
image_url = response['data'][0]['url']
