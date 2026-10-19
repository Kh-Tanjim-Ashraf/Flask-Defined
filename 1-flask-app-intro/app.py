from flask import Flask

# Initialize an instance of Flask
app = Flask(__name__)

# Provide a base route of the server
@app.route('/')
def index():
    return "<h1>Hello to Flask Introductory App</h1>"

# Run the Flask server only if this file is executed directly
# It will run at localhost:5000 by default
if __name__ == "__main__":
    app.run(debug=True)