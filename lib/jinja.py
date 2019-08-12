import jinja2
import os 
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '..')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)