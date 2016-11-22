#!/usr/bin/env python

import os

import jinja2
import webapp2
import urllib2
import json
import urllib, json
from operator import itemgetter


import scipy
# import numpy

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)




class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        #self.response.write(*a,**kw)
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n',0)

        n = n and int(n)
        self.render('fizzbuzz.html', n=n)

class MainHandler(Handler):
    def get(self):
        url = "https://www.reddit.com/r/news.json?"
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        items = []
        x=1
        for point in data['data']['children']:
            items.append({'number':x, 'title':point['data']['title'], 'classified':'Voilent' , 'url':point['data']['url']})
            x+=1
            if x==11:
                break
            # print point['data']['title']
            # print point['data']['url']


        # items= []
        # items.append({'number':1, 'content':'Blah......... Blah fghdsfl  fks', 'classified':'Voilent' , 'url':'http://stackoverflow.com/'})
        # items.append({'number':2, 'content':'FAST......... FAST YAhasd asdk gss', 'classified':'Non Voilent' , 'url':'http://yahoo.com/'})
        # items = self.request.get_all("food")
        self.render("classified.html", items=items)



'''
class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        #self.response.write(*a,**kw)
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n',0)

        n = n and int(n)
        self.render('fizzbuzz.html', n=n)

class MainHandler(Handler):
    def get(self):
        self.render("classified.html")

'''

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/fizzbuzz', FizzBuzzHandler),
], debug=True)
