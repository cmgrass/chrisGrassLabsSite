import web

urls = (
    '/', 'index',
    '/main.css', 'mainCss'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
    def GET(self):
        greeting = "Bacon Dinner"
        return render.index(message = greeting) # Render `index.html`

class mainCss(object):
    def GET(self):
        return render.main()    # Render `main.css`

if __name__ == "__main__":
    app.run()
