from filestack import Client
class FileSharer: #open for extension and closed for modification

    def __init__(self, filepath, api_key="something"): # alt + enter
        self.api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath=self.filepath)
        #print(type(new_filelink))
        #print(new_filelink.url)
        return new_filelink.url