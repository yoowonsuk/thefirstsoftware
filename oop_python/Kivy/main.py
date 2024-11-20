# App, ScreenManager, Screen, Widget object
# Widget is composed of Button, TextInput, Image, etc

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
#    def search_image(self): # split
    def get_image_link(self):
        #print("Working...")

        # Get User query from Text Input
        query = self.manager.current_screen.ids.user_query.text
        #print(query)
        # Get wikipedia page and list of image urls or the first image link
        page = wikipedia.page("Key(" + query + ")") #https://stackabuse.com/getting-started-with-pythons-wikipedia-api/
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # Download the image
        ''' non-browser request blocked'''
        # Download the image
        # Add fake header to appear as though we are a browser.  Apparently the site blocks non-browser requests
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}  # This is chrome, you can set whatever browser you like
        req = requests.get(image_link, headers=headers) # self.get_image_link()
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        return imagepath

    def set_image(self):
        # Set the image in the Image widget
        # ids is list
        self.manager.current_screen.ids.xyz.source = imagepath # self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
