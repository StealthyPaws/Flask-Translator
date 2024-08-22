from flask import Flask, request, render_template
from datetime import date
from googletrans import Translator

app = Flask(__name__)

translator = Translator()

def translatetext(text, target_lang):
    translation = translator.translate(text, dest=target_lang)
    return translation.text

@app.route('/')
def home():
    return render_template('main.html', datetoday2=date.today().strftime("%d-%B-%Y"), res='')

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['sourcetext']
    target_lang = request.form['languages']


    # Translate to the target language
    res = translatetext(input_text, target_lang)

    return render_template('main.html', datetoday2=date.today().strftime("%d-%B-%Y"), res=res)

if __name__ == '__main__':
    app.run(debug=True)









# app.route connects URLs to functions in your code.
# render_template helps you create web pages by mixing HTML templates with your data.


