import inspect
import justpy as jp

from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
from webapp import page


imports = list(globals().values())
for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)


'''
imports = list(globals().values())
for obj in imports:
    if hasattr(obj, 'path'):
        jp.Route(obj.path, obj.serve)
'''
'''
imports = globals()
for key, value in imports.items():
    if hasattr(key, 'path'):
        jp.Route(key.path, key.serve)
'''

'''
jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)
'''

jp.justpy(port=8001) # remove exact same code in the files in webapp dierctory
