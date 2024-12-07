import justpy as jp

class About(jp.QuasarPage):
    path = "/about"

    def serve(self):
        #wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=self, classes="bg-gray-200 h-screen")

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
	jp.Div(a=div, text="This is the About page!", classes="text-4xl m-2")
	jp.Div(a=div, text="""
        Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur
	""", classes="text-lg")
	return wp

#about = About()
jp.Route(About.path, About.serve) #About().path is instance , About.serve <- just method name
jp.justpy(port=8001)
