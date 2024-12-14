import justpy as jp
from webapp import layout
from webapp import page

class Home(page.Page):
#    path = "/home"
    path = "/"

    @classmethod
    #def serve(self):
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        #lay = layout.DefaultLayout(a=wp, view="hHh LpR fFf")
        lay = layout.DefaultLayout(a=wp)
'''
        # do with examples/file.html
        layout = jp.QLayout(a=wp, view="hHh LpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)
        #jp.QBtn(dense=True, flat=True, round=True, icon="menu",
        #        click=cls.move_drawer, drawer=drawer)
        #jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        drawer = jp.QDrawer(a=layout, how_if_above=True, v_mode="left", bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes = "p-2, m-2, text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/home", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)


        jp.QBtn(dense=True, flat=True, round=True, icon="menu",
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        container = jp.QPageContainer(a=layout)
        '''
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")

        #div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    	jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
    	jp.Div(a=div, text="""
        Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur
	""", classes="text-lg")
	    return wp
'''
go to layout.py
    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value = True:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
            '''


jp.Route(Home.path, Home.serve)
jp.justpy(port=8001)
