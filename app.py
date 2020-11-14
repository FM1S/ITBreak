from flask import Flask, url_for, render_template

app = Flask(__name__, static_folder = 'static')

chat_started = 0


class MessagePair(object):
    def __init__(self, quest, resp):
        self.quest = quest
        self.resp = resp


pairs = []


@app.route('/')
def main_chat_window():
    if chat_started == 0:
        return render_template('index.html', chat_visibility="none", btn_visibility="block")
    elif chat_started == 1:
        return render_template('index.html', chat_visibility="block", btn_visibility="none")


@app.route('/new_quest/<quest_text>')
def render_msgs(quest_text):
    chat_started = 1
    rsp = "Я тебя услышал :)"
    pairs.append(MessagePair(quest_text, rsp))
    return render_template('message_pair.html', pairs=pairs)


if __name__ == "__main__":
    app.run(debug=True)