import os
import re
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
UPLOAD_FOLDER="./data"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def fileFrontPage():
    return render_template('index.html')

@app.route("/handleUpload", methods=['POST'])


# For Uploading File
def handleFileUpload():
    if 'Bill' in request.files:
        txt_file =request.files['Bill']
        filename = secure_filename(txt_file.filename)
        txt_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        print("*********",(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
        reed_txt = open((os.path.join(app.config['UPLOAD_FOLDER'], filename)), 'r')


# For Reading Text File and with the help of Regular Experssion we remove unwanted things
        count = []
        for line in reed_txt:
            rec = re.findall('[a-zA-Z]\S*', line)
            for rec_1 in rec:
                count.append(rec_1)
        def func(count):
            count1 = 0
            count2 = 0
            for ele in count:
                if ele != 'Amount':
                    count1 += 1
                if ele == 'Amount':
                    for ele_1 in count:
                        if ele_1 != 'Total':
                            count2 += 1
                        if ele_1 == 'Total':
                            break
                    break
            total_count = count[count1 + 1:count2]
            return total_count

        count_1 = func(count)


# For creating new Text File and it will save automatically in the project folder with Items Name
        with open('New.txt', 'w') as c7:
            for count_ele in count_1:
                c7.write(count_ele + '\n')
        print(count)

    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    app.run()     