
# if you add a dependency to to requirements.txt, you need these 2 lines
# before you use those dependencies, see lib/README.md
from google.appengine.ext import vendor
vendor.add('lib')

import bottle
import json
from bottle import route, post, template, error, request, response
from models import get_rick_rolls_list, RickRoll
from core import respond
from google.appengine.ext.webapp.util import run_wsgi_app


@route('/')
def index():
    rick_roll = RickRoll()
    rick_roll.ip = request.environ.get('REMOTE_ADDR')
    rick_roll.put()
    rick_rolls_list = get_rick_rolls_list()
    return respond('rick_rolls.html', params={'count': len(rick_rolls_list),'data': rick_rolls_list})


bottle.debug(True)
# session_opts = {
#     'session.type': 'ext:google'
# }
# app = beaker.middleware.SessionMiddleware(app, session_opts)
# from google.appengine.ext.appstats import recording
# app = recording.appstats_wsgi_middleware(app)
app = bottle.app()


@error(403)
def error403(code):
    return respond('403.html')

@error(404)
def error404(code):
    return respond('404.html')
