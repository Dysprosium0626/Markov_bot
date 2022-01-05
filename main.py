from flask import Flask, url_for, request, render_template
from analysis import Analysis
import generator

app = Flask(__name__)


@app.route('/')
def index():
    return 'Please go to \'/login\' for more information'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        theme = request.form.get('theme')
        number = request.form.get('number')
        print('username: {}, password: {}'.format(theme, number))
        return render_template('login.html')
    elif request.method == 'POST':
        try:
            theme = request.form.get('theme')
            number = int(request.form.get('number'))
            analysis = Analysis(theme)
            sentences = analysis.split_text_into_sentences()
            dataset = analysis.prepare_dataset(sentences)
            # create a generator
            g = generator.Generator(dataset)
            result = ""
            for i in range(0, number):
                result += g.generate(' ') + '\n'
            return render_template('login.html', str=result)
        except ValueError:
            return render_template('login.html', str="Please enter a valid number!")
    #     else:
    #         return 'No such user!'
    # title = request.args.get('title', 'Default')
    # return render_template('login.html', title=title)


if __name__ == "__main__":
    app.run(debug=True)
