import os
from flask import Flask, jsonify, render_template
from sqlalchemy import text
from src.db.database import init_db
from src.db.database import db
from src.routes.student_routes import student_bp
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno

def create_app():
    app = Flask(__name__, 
                static_folder=os.path.abspath('src/static'),
                template_folder=os.path.abspath('src/templates'))
    
     # Deshabilitar caché durante el desarrollo
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    
    @app.after_request
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    # Configurar la clave secreta
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    init_db(app)

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/test-db')
    def test_db():
        try:
            db.session.execute(text('SELECT 1'))
            return jsonify({"message": "Database connection successful!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    app.register_blueprint(student_bp)
    # Registra otros blueprints aquí
    
    # @app.route('/')
    # def home():
    #     return jsonify({"message": "Welcome to the Music Academy API!"})
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run( port=5000, debug=os.getenv('DEBUG', 'False').lower() == 'true')















""" from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos= ['TODO 1', 'TODO 2', 'TODO 3']

@app.route('/')

def index():


    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response 

@app.route('/hello')
def hello():

    user_ip = request.cookies.get('user_ip')

    context = {
        'user_ip': user_ip,
        'todos': todos
    }

    return render_template('hello.html', **context)

    if __name__ == "__main__":
     app.run(port=5000, debug=True)   """