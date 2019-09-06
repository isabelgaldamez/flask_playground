from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('play')
@app.route('/play')
def render_three():
    return render_template('index.html')
# @app.route('/play/')
# def render_three_x():
#     return render_template('index.html')
@app.route('/play/<int:times>')
def render_x(times):
    return render_template('index.html', display_times = times)
@app.route('/play/<int:times>/<sq_color>')
def change_color(times, sq_color):
        print('*' * 10)
        return render_template('index.html', display_times = times, square_color = sq_color)

if __name__ == '__main__':
    app.run(debug = True)