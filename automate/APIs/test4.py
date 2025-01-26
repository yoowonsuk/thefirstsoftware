import requests

#url = curl -i -X GET \
url = "https://graph.facebook.com/v13.0/me?fields=id%2Cname&access_token=EAAJIitQMcZBABAEZBMY7shwy9brRQzgC3WmRdST9b4oXy0t24LSZC0KEaVCvVQ4PmQwtrx0tUsv64dg5gT4FEN5UCfZAaJwSDLrqdXAjyZAJKCNHsomPBBKgtVQDdWnr301GumkMi266I3xIzPKJTcbr2ybMiwGVE9pMyZAWVyuYaKgKFegmwKtvd0geqijSCYlfgSZCrP17BnHUek8BslsJqqQ5ygMQLHLMK4HDScV1dn1jdCUBxq2ZBmkfLZB8u6HsZD"

#url = "https://graph.facebook.com/v13.0/105360698771730?fields=link%2Cimages&access_token=EAAJIitQMcZBABAEZBMY7shwy9brRQzgC3WmRdST9b4oXy0t24LSZC0KEaVCvVQ4PmQwtrx0tUsv64dg5gT4FEN5UCfZAaJwSDLrqdXAjyZAJKCNHsomPBBKgtVQDdWnr301GumkMi266I3xIzPKJTcbr2ybMiwGVE9pMyZAWVyuYaKgKFegmwKtvd0geqijSCYlfgSZCrP17BnHUek8BslsJqqQ5ygMQLHLMK4HDScV1dn1jdCUBxq2ZBmkfLZB8u6HsZD"

#me?fields=id,name,posts then fields=id%2Cname%2Cpost&access_token=
# Wanting only posts then me -> id of posts  & replace posts with comments
#only “me” “me/posts” “me/photos/uploaded” “{specific_photo_id}?fields=link,images”

response = requests.get(url)
#print(response.content)
print(response.text)

# “{specific_photo_id}?fields=link,images” => str (string)
# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests
import json

url = "https://graph.facebook.com/v13.0/105360698771730?fields=link%2Cimages&access_token=EAAJIitQMcZBABAEZBMY7shwy9brRQzgC3WmRdST9b4oXy0t24LSZC0KEaVCvVQ4PmQwtrx0tUsv64dg5gT4FEN5UCfZAaJwSDLrqdXAjyZAJKCNHsomPBBKgtVQDdWnr301GumkMi266I3xIzPKJTcbr2ybMiwGVE9pMyZAWVyuYaKgKFegmwKtvd0geqijSCYlfgSZCrP17BnHUek8BslsJqqQ5ygMQLHLMK4HDScV1dn1jdCUBxq2ZBmkfLZB8u6HsZD"

response = requests.get(url)
data = response.text

data = json.loads(data)
image_url = data['images'][0]['source']

image_bytes = requests.get(image_url).content

with open('image.jpg', 'wb') as file:
    file.write(image_bytes)

Docs -> Graph API reference

Import requests
#languagetool.org/http-api/#/default
url = ‘http://api.languagetool.org/v2/check’
Data = {
    ‘text’: ‘Tis is a nixe day!’,
    ‘language’: ‘auto’
}
response = requests.post(url, data=data)

#print(type(response.text)) str
result = json.loads(response.text)

