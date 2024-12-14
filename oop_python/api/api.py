import justpy as jp
import defintion
import json

class Api:
    """Handles requests at /api?w=word
    """
    @classmethod
    def serve(cls, self):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        #jp.Div(a=wp, text=word.title())

        defined = defintion.Defintion(word).get()
        response = {
            "word":word,
            "defintion":defined
        }

        #wp.html = word.title()
        #wp.html = defined
        wp.html = json.dumps(response)

        return wp

'''
jp.Route("/", API.serve)
#webpage = 127.0.0.1:8000/?w=moon
#jp.Route("/api", API.serve)
#webpage = 127.0.0.1:8000/api?w=moon
jp.justpy()
'''

'''
import json
json.dumps({'a':1})
'''
