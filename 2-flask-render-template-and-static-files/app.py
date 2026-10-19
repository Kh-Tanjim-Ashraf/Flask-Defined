from flask import Flask, render_template

app = Flask(__name__)

# Render an HTML file with CSS through the Home route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)