from flask import Flask
from flask import render_template
from flask import request
import os
import time

work_dir = "/home/test_system"

app = Flask(__name__)
from importlib.machinery import SourceFileLoader
tester = SourceFileLoader("tester", work_dir + "/tester.py").load_module()

@app.route('/', methods=['POST', 'GET'])
def index():
    data = 0
    if request.method == 'POST':
        task = int(request.form['task'])
        if request.files['file'] and (task > 0 and task <= 5):
            file = request.files['file']
            ts = int(time.time())

            data = f"Solution number {ts}\n"

            file_save = work_dir + f"/solutions/{ts}.py"
            file.save(file_save)
            file.close()

            data += tester.run_test(task, file_save)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.debug = True
    #app.run(host='0.0.0.0', port=80)
    app.run()