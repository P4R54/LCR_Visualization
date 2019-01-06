import json
from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
import pdb
from lcr import run_lcr


@app.route('/')
def upload_file_view():
   return render_template('index.html')

@app.route('/api')
def uw():
   return json.dumps(run_lcr()) , 200

if __name__ == '__main__':
   app.run(debug = True)

