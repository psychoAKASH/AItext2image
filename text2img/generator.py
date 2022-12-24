import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def gene(word):
    response = openai.Image.create(
        prompt=word,
        n=3,
        size="512x512"
    )
    image_url1 = response['data'][0]['url']
    image_url2 = response['data'][1]['url']
    image_url3 = response['data'][2]['url']
    # url= (image_url1,image_url2,image_url3)
    return [image_url1, image_url2, image_url3]
