from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, world'

# if __name__ == '__main':
app.run(port = 8080)