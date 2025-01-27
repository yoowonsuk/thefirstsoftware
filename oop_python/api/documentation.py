#newsapi.org

import justpy as jp

class Doc():

    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    	jp.Div(a=div, text="Instant Dictionary API", clases="text-4xl m-2")
	    jp.Div(a=div, text="Get defintions of words", classes="text-lg")
        jp.Hr(a=div) # horizontal line
        jp.Div(a=div, text="www.example.com/api?=w=moon")
        jp.Hr(a=div) # horizontal line
        jp.Div(a=div, text="""
        {"word": "moon", "definition":
        ["A natural satelite of a planet.", "A month, particularly a lunar month (approximately 28 days).",
        "To fuss over adoringly or with great affection.",
        "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).",
        "To be lost in phantaise or be carried away by some internal vision, having temporaily lost (part of) contant to reality."]}
        """)
    	return wp

