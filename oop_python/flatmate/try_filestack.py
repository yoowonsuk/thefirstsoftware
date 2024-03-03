#get api key for filestack

from filestack import Client
client = Client('<YOUR_API_KEY>')

new_filelink = client.upload(filepath='path/to/file')
#print(type(new_filelink))
print(new_filelink.url)
