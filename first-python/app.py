from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aplicación Python</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
            }
            h1 {
                color: #4CAF50;
            }
            p {
                font-size: 1.2em;
            }
        </style>
    </head>
    <body>
        <h1>¡Hola, Coders!</h1>
        <p>Esta es una aplicación Python ejecutándose en un contenedor Docker.</p>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)