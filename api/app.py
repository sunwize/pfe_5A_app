#!/usr/bin/env python
# coding: utf-8

# imports globaux
from __future__ import unicode_literals, print_function

# import declared routes
#from routes import *

from routes import app

if __name__ == '__main__':
    app.run(debug=True)
