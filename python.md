#+STARTUP: showall
#+TITLE: Python
#+AUTHOR: http://h4labs.com
#+HTML_HEAD: <link rel="stylesheet" type="text/css" href="/resources/css/myorg.css" />

#+INCLUDE: "dev_menu.org"
Menu: [[file:bash.org][bash]] | [[file:compilers.org][Compilers]] | [[file:go.org][Go]] | [[file:haskell.org][Haskell]] | [[file:ocaml.org][OCaml]] | [[file:perl.org][Perl]] | [[file:python.org][Python]] | [[file:r.org][R]] | [[file:scala.org][Scala]] | [[file:sql.org][SQL]] 

* Inbox

+ [[https://pypi.python.org/pypi][PyPI]] - The Python Package Index
+ http://lucumr.pocoo.org/2015/11/18/pythons-hidden-re-gems
+ http://www.dataquest.io/blog/python-vs-r
+ http://news.ycombinator.com/item?id=7727369 - Write to a Google Spreadsheet from a Python script (2009) (mattcutts.com)
+ http://www.nltk.org
+ http://madlag.github.io/jarvis/
+ http://news.ycombinator.com/item?id=7715349 - Common Python Mistakes 
+ http://pypi.python.org/pypi/goslate
+ http://www.blog.pythonlibrary.org/2014/02/26/python-101-reading-and-writing-csv-files/
+ http://github.com/binux/pyspider
+ http://news.ycombinator.com/item?id=8665820

* Django
+ http://www.marinamele.com/taskbuster-django-tutorial


#+BEGIN_Example

python3 -m http.server --cgi 8000

#+END_EXAMPLE

#+BEGIN_Example
$ cd /home/somedir
$ python -m SimpleHTTPServer

That's it! Now your http server will start in port 8000. You will get the message:

Serving HTTP on 0.0.0.0 port 8000 ...

Now open a browser and type the following address:

http://192.168.1.2:8000

You can also access it via:

http://127.0.0.1:8000

If the directory has a file named index.html, that file will be served as the initial file. If there is no index.html, then the files in the directory will be listed.

If you wish to change the port that's used start the program via:

$ python -m SimpleHTTPServer 8080

If you want to only serve on localhost you'll need to write a custom Python program such as:

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol    = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:

    port = 8000
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()

#+END_EXAMPLE

#+BEGIN_Example

http://stackoverflow.com/questions/101268/hidden-features-of-python

Games in Python: http://inventwithpython.com/chapters/

http://anandology.com/python-practice-book/index.html

Pyflakes

http://stackoverflow.com/questions/35470/are-there-any-static-analysis-tools-for-python

http://stackoverflow.com/questions/115977/using-pylint-with-django

http://articles.sitepoint.com/article/django-crash-course

http://www.sqlalchemy.org/

http://www.jonobacon.org/2010/01/08/acire-delivering-a-world-of-python-snippets/

http://dis.4chan.org/read/prog/1180084983/
300 Tutorials

ElementTree
http://effbot.org/zone/element.htm

Django
http://uswaretech.com/blog/2010/01/doing-things-with-django-forms/

#+END_EXAMPLE
