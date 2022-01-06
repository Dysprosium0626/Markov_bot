from flask import Flask, url_for, request, render_template, redirect
from service.article_service import ArticleService
from service.text_serivce import TextService

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html', image="../logo/markov_grey.png")
    else:
        theme = request.form.get('theme')
        number = int(request.form.get('number'))
        if request.files["myfile"].filename == '':
            article_service = ArticleService(theme, number)
            result = article_service.generate_text()
        else:
            try:
                file = request.files["myfile"]
                str = bytes.decode(file.read(), encoding="utf-8")
                text_service = TextService(number)
                result = text_service.generate_text(str)
            except Exception:
                return render_template('login.html', str="请上传.txt文件")

        return render_template('login.html', str=result)


@app.route('/loginen', methods=['POST', 'GET'])
def loginen():
    if request.method == 'GET':
        return render_template('loginen.html')
    elif request.method == 'POST':
        print(request.form.get('theme'))
        theme = request.form.get('theme')
        number = int(request.form.get('number'))
        if request.files["myfile"].filename == '':
            article_service = ArticleService(theme, number)
            result = article_service.generate_text()
        else:
            try:
                file = request.files["myfile"]
                str = bytes.decode(file.read(), encoding="utf-8")
            except UnicodeDecodeError:
                return render_template('loginen.html', str="请上传.txt文件")
            text_service = TextService(number)
            result = text_service.generate_text(str)
        return render_template('loginen.html', str=result)


@app.route('/github', methods=['POST', 'GET'])
def github():
    if request.method == 'GET':
        return redirect("https://github.com/Dysprosium0626/Markov_bot")



if __name__ == "__main__":
    app.run(debug=True)
