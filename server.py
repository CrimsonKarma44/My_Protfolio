from flask import Flask, render_template, url_for, redirect, request, jsonify, flash
from werkzeug.utils import secure_filename
import hashlib
from storage import *

app = Flask(__name__)
app.secret_key = hashlib.sha1('password'.encode('utf-8')).hexdigest().upper()



@app.route('/')
def Home():
    return render_template('index.html')



@app.route('/<string:page>',  methods=['POST', 'GET'])
def root(page):
    if request.method == 'POST':
        # try:
        # save_to_json(request.form.to_dict())
        save_to_csv(request.form.to_dict())
        flash('Thank You, I will get back to you shortly')
        return redirect(url_for('Home'))
        # except:
        #     flash('There was a problem Try agein later')
        #     return redirect(url_for('Home'))
    return render_template(page+'.html', _page=page.title())


@app.route('/CV')
def cv():
    return redirect(url_for('static', filename='CV.pdf'))


if __name__ == '__main__':
    app.run(debug=True)
