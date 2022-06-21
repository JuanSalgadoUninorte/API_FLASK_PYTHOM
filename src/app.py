from Flask import Flask

from config import config

from routes import Movie

def page_not_found(e):
    return '<h1>Página no encontrada.</h1>',404

app.Flask(__name__)
if __name__ == '__main__':
    app.config.from_object(config['development'])
    #Planos o rutas
    app.register_blueprint(Movie.main, url_prefix='/api/movies')
    app.register_error_handler(404, page_not_found)
    app.run()