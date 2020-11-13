from flask import Flask, url_for, render_template

app = Flask(__name__, static_folder = 'static')

@app.route('/')
def main_chat_window():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)