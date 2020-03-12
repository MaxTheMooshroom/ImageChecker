from flask import Flask, render_template, request
import predictor as model

APP = Flask(__name__)

@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/receiver', methods=['GET', 'POST'])
def receiver():
    if request.method == 'POST':
        if 'imagefile' in request.files:
            img = request.files.get('imagefile', '')
            response = model.predict(img)
            return { 'response':response }

    elif request.method == 'GET':
        return redirect('/')


if __name__ == '__main__':
    APP.run(debug=True)
