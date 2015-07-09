import webapp2


ROUTES = [
    webapp2.Route('/', handler='controller.index.HelloWorld')
]

APPLICATION = webapp2.WSGIApplication(ROUTES)
