from flask import Flask, url_for, request, render_template, redirect
from service.article_service import ArticleService
from service.text_serivce import TextService


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        theme = request.form.get('theme')
        number = int(request.form.get('number'))
        if request.files["myfile"].filename == '':
            article_service = ArticleService(theme, number)
            result = article_service.generate_text()
        else:
            file = request.files["myfile"]
            str = bytes.decode(file.read(), encoding="utf-8")
            text_service = TextService(number)
            result = text_service.generate_text(str)
        return render_template('login.html', str=result)

    #     else:
    #         return 'No such user!'
    # title = request.args.get('title', 'Default')
    # return render_template('login.html', title=title)


if __name__ == "__main__":
    app.run(debug=True)
