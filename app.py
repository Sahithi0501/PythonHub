from flask import Flask, render_template

app = Flask(__name__)

#This is the Homepage route:
@app.route('/')
def home():
    return render_template('index.html')

#This is the Google Photos display route:
@app.route('/photos')
def photos():
    return render_template('photos.html')

if __name__ == '__main__':
    app.run(debug=True)