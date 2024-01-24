import os

from flask import *
from werkzeug.utils import secure_filename

from src.newcnn import predict

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predictt')
def predictt():
    return render_template('predict.html')

@app.route('/predict_post', methods=['POST'])
def predict_post():
    image = request.files['file']
    image.save(r"E:\lungs_cancer\lungs_cancer\src\static\image\1.jpg")
    result=predict('static/image/1.jpg')

    return render_template('result.html',res=result)


# @app.route('/result')
# def result():
#     return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
