"""Flickr Photo Search"""

import re
import urllib.request
import xml.etree.ElementTree as etree
SEARCH_URL = 'https://api.flickr.com/services/feeds/photos_public.gne?tags='
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def ex49():
    """Search Flickr for Photots"""
    q = request.args.get('q')
    links = []
    if q is not None:
        with urllib.request.urlopen(SEARCH_URL + 'nature') as response:
            body = response.read()
        doc = etree.fromstring(body)
        entries = doc.findall('{http://www.w3.org/2005/Atom}entry')
        contents = [x.find('{http://www.w3.org/2005/Atom}content') for x in entries]
        links = [re.findall(r'<img src="([^"]+)"', c.text)[0] for c in contents]
    return render_template("module49.html", q=q, links=links)
