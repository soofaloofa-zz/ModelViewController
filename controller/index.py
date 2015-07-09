import jinja2
import webapp2

from model.user import User


JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader('view'))


class HelloWorld(webapp2.RequestHandler):

    def get(self):
        name = self.request.params.get('name')
        user = User.get_or_create(name)

        name = user.name if user else 'World'

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(name=name))
