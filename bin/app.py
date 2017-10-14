import web

urls = (
    '/', 'index',
    '/main.css', 'mainCss',
    '/blog', 'blog',
    '/techResource', 'techResource',
    '/randomness', 'randomness',
    '/register', 'register',
    '/blog20171009A', 'blog20171009A',
    '/blog20171010A', 'blog20171010A'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")
render_plain = web.template.render('templates/')

class index(object):
    def GET(self):
        greeting = "I passed this string from Python... SWEET!!!"
        return render.index(message = greeting) # Render `index.html`

class mainCss(object):
    def GET(self):
        return render_plain.main()    # Render `main.css`

class blog(object):
    def GET(self):
        return render.blog()    # Render `blog.html`

class techResource(object):
    def GET(self):
        return render.techResource()    # Register `techResource.html`

class randomness(object):
    def GET(self):
        return render.randomness()  # Render `randomness.html`

class register(object):
    def GET(self):
        return render.registerForm()    # Render `register.html`

    def POST(self):
        form = web.input(name="Nobody", email="you@domain", message="..")
        userFeedback = '''Hi %s, thanks for registering! Your email is: `%s`,
                          and you wanted to say: "%s". I won't be getting back
                          to you because I'm not storing this information yet.
                          Soon I would like to create a nice set of CSS classes
                          for this registration page, create user state, and
                          eventually log to a database!''' % (form.name,
                                                             form.email,
                                                             form.message)

        return render.register(userFeedback = userFeedback)

class blog20171009A(object):
    def GET(self):
        return render.blog20171009A()    # Render `blog20171009A.html`

class blog20171010A(object):
    def GET(self):
        return render.blog20171010A()    # Render `blog20171010A.html`

if __name__ == "__main__":
    app.run()
