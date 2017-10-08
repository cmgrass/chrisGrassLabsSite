import web

urls = (
    '/', 'index',
    '/main.css', 'mainCss',
    '/blog.html', 'blog',
    '/techResource.html', 'techResource',
    '/randomness.html', 'randomness',
    '/register.html', 'register'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
    def GET(self):
        greeting = "I passed this string from Python... SWEET!!!"
        return render.index(message = greeting) # Render `index.html`

class mainCss(object):
    def GET(self):
        return render.main()    # Render `main.css`

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
        return render.register()    # Render `register.html`

if __name__ == "__main__":
    app.run()
