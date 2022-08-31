from flask import Flask,request, url_for, redirect, render_template
from flask import request
# request.data
import pickle
import numpy as np
import joblib

app = Flask(__name__)

model=joblib.load(open('model_joblib_heart','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == "POST":

        int_features=[]

        for qry in range(1 , 14):
            curr_data_name = "data" + str(qry) 
            int_features.append( request.form.get(curr_data_name) )
            # print(curr_data_name , request.form.get(curr_data_name) )
            # print(request.form.get(curr_data_name) , end=" , " )

        final=[np.array(int_features)]
        print(int_features)
        print(final)
        prediction=model.predict(final)
        print(prediction)
        # output='{0:.{1}f}'.format(prediction[0][1], 0)

        if prediction==1:
            return render_template('predict.html',pred='Heart disease')
        elif prediction==0:
            return render_template('predict.html',pred=' No heart disease')

@app.route('/predict.html',methods=['POST','GET'])
def hello_world1():
    return render_template("predict.html")

@app.route('/index.html',methods=['POST','GET'])
def hello_world2():
    return render_template("index.html")

@app.route('/predict.html',methods=['POST','GET'])
def hello_world3():
    return render_template("predict.html")

@app.route('/index.html',methods=['POST','GET'])
def hello_world4():
    return render_template("index.html")

# @app.route('/analysis.html',methods=['POST','GET'])
# def hello_world5():
#     return render_template("analysis.html")

# @app.route('/aboutus.html',methods=['POST','GET'])
# def hello_world6():
#     return render_template("aboutus.html")

@app.route('/blog.html',methods=['POST','GET'])
def hello_world7():
    return render_template("blog.html")




if __name__ == '__main__':
    app.run(host="localhost",port=8000,debug=False)