#pip install justpy
import justpy as jp

@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hello World!",
            claaes="text-green-900 bg-yellow-500 font-serif text-lg") # tailwindcss.com/docs
    jp.Div(a=wp, text="Hello again!") # wp = webpage
    return wp

@jp.SetRoute("/about")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hi World!")
    jp.Div(a=wp, text="Hi again!") # wp = webpage
    return wp


#jp.Route("/", home) # port = 8000
jp.justpy()
