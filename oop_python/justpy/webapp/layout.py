import justpy as jp

class DefaultLayout(jp.QLayout):

    def __init__(self, view="hHh lpR fFf", **kwargs)):
        super().__init__(view=view, **kwargs)
        #super().__init__(**kwargs)
        #jp.QLayout.__init__(**kwargs)
        # kwargs = {"a":wp, "view":"hh.."}
        #layout = jp.QLayout(a=wp, view="hHh LpR fFf")

        # do with examples/file.html
        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)
        #jp.QBtn(dense=True, flat=True, round=True, icon="menu",
        #        click=cls.move_drawer, drawer=drawer)
        #jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        drawer = jp.QDrawer(a=self, how_if_above=True, v_mode="left", bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes = "p-2, m-2, text-lg text-blue-400 hover:text-blue-700"
        #jp.A(a=qlist, text="Home", href="/home", classes=a_classes)
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)


        jp.QBtn(dense=True, flat=True, round=True, icon="menu",
                click=self.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        #container = jp.QPageContainer(a=layout)
        #container = jp.QPageContainer(a=self)

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value = True:
            widget.drawer.value = False
        else:
            widget.drawer.value = True

