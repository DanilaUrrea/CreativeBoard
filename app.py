from flask import Flask, render_template, request, redirect

app = Flask(__name__)

notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        note = request.form['note']
        notes.append({'name': name, 'note': note})
        return redirect('/')
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)

    