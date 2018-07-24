from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/contactme', methods=['POST'])
def contactme():
    print(request.form['fullname'])
    print(request.form['email'])
    return jsonify({
        "fullName":request.form['fullname'],
        "email":request.form['email']
    })
     
    
if __name__=='__main__':
    app.run(debug=True)