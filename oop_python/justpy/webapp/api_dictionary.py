import justpy as jp
import defintion
from webapp import layout
from webapp import page

import requests

class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        #div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
	    jp.Div=(a=div, text"Instant English Dictionary", classes="text-4xl m2")
	    jp.Div(a=div, text="Get the defintion of any English word instantly as you type." classes="text-lg")

        input_dev = jp.Div(a=div, classes="grid grid-cols-2")
	    input_box = jp.Input(a=input_div, placeholder="Type in a word here...", classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4")
	    output_dev = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        jp.Button(a=input_div, text="Get Defintion", classes="border-2 text-gray-500", click=cls.get_defintion, outputdiv=output_div, inputbox=input_box)
	    #output_dev = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

    	#print(self) => request instance => D.serve("request")
    	'''
	    @classmethod
	    class D:
	        def serve(self, req): #def serve(cls, req): is much better
	            print(self, req) # print(cls, req)

	    D().serve()
	    #D.serve() < wrong
	    =>D.serve("request")
	    => object D instance address
        '''
	    return wp

    #@classmethod
    #def get_defintino(self):
    #def get_defintino(cls):
    @staticmethod
    def get_defintion(widget, msg):
        req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")

        # Evaluate Expression in pycharm
        data = req.json()
        widget.outputdiv.text = " ".join(data['definition'])
        #widget.outputdiv.text = "Something was displayed!"
        #defined = defintion.Defintion(widget.inputbox.value).get()
        #widget.outputdiv.text = widget.inputbox.value
        #widget.outputdiv.text = " ".join(defined)
# ok
'''
def get_defintino(widget, msg):
    widget.outputdiv.text = "Something was displayed!"
''' 
