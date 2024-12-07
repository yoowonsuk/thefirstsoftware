#pip install justpy
import justpy as jp

@jp.SetRoute("/home")
def home():
    wp = jp.QuasarPage() # ignore tailwind
    #wp = jp.QuasarPage(tailwind=True) 

    wp = jp.WebPage() # if nothing inside, 500 error
    # wp = jp.WebPage(classes="bg-gray-200") # not working
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4 p-4 border border-black")

    in_1 = jp.Input(a=div1, placeholder="Enter first value", classes="form-input") # command + D or ctrl D for copy the line
    in_2 = jp.Input(a=div1, placeholder="Enter second value", classes="form-input") 
    d_output = jp.Div(a=div1, text="Result goes here...", class="text-gray-600")
    jp.Div(a=div1, text="Just another div...", class="text-gray-600")
    jp.Div(a=div1, text="Yet another div", class="text-gray-600")

    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")

    '''
    jp.Button(a=div2, text="Calculate", click=sum_up, in1=in_1, in2=in_2, d = d_output, mouseenter=mouse_enter, mouseleave=mouse_leave, classes="border border-blue=500 m-2 p-2 rounded "
    "text-blue-600 hover:bg-red-500 hover:text-white") # margin padding py-2 means padding vertical
    '''

# quasar.dev page
# Vue(.js) Components # javascript framework
    jp.QBtn(a=div2, color="primary", label="primary", icon="map", text="Calculate", click=sum_up, in1=in_1, in2=in_2, d = d_output, mouseenter=mouse_enter, mouseleave=mouse_leave)
    jp.Div(a=div2, text="I am a cool interactive div!")
    #jp.Div(a=div2, text="I am a cool interactive div!", classes="hover:bg-red-500") # but classes' usually concerned about styling


'''
    jp.Input(a=wp, placeholder="Enter first value", classes="form-input") # command + D or ctrl D for copy the line
    jp.Input(a=wp, placeholder="Enter second value", classes="form-input") 
    jp.Div(a=wp, text="Result goes here...", class="text-gray-600")
    jp.Button(a=wp, text="Calculate", classes="border border-blue=500 m-2 p-2 rounded "
    "text-blue-600 hover:bg-red-500 hover:text-white") # margin padding py-2 means padding vertical
'''


    #jp.Div(a=wp, text="Hello World!",
            claaes="text-green-900 bg-yellow-500 font-serif text-lg") # tailwindcss.com/docs
    #jp.Div(a=wp, text="Hello again!") # wp = webpage
    return wp

@jp.SetRoute("/about")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hi World!")
    jp.Div(a=wp, text="Hi again!") # wp = webpage
    return wp

def sum_up(widget, msg): # widget => button instance, msg => event (msg.page)
    print("Clicked!")
    # print(widget.in1, widget.in2)
    # print(widget.in1.value, widget.in2.value)
    sum = float(widget.in1.value) + float(widget.in2.value)
    widget.d.text = sum

def mouse_etner(widget, msg):
    widget.text = "A mouse entered the house!"

def mouse_leave(widget, msg):
    widget.text = "The mouse left!"

#jp.Route("/", home) # port = 8000
jp.justpy()
