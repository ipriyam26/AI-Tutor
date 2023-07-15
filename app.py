from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from hero.chains import Chains
from colorama import Fore, Style
from flask_cors import CORS


app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app)

socketio = SocketIO(app)
msg_ai = None
more = None
chain = None
loadingMessage = None


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("start")
def handle_start(question):
    global msg_ai, more, loadingMessage, chain
    chain = Chains()
    msg_ai, more = chain.gen_info(question)
    emit("response", {"ai_msg": msg_ai, "more": more}, broadcast=True)


@socketio.on("continue")
def handle_continue(question: str):
    global msg_ai, more, loadingMessage
    if more:
        msg_ai, more = chain.gen_info(question)
        # print(f"{Fore.GREEN} AI: {msg_ai} {Style.RESET_ALL}")
        # print(f"{Fore.GREEN} More: {str(more)} {Style.RESET_ALL}")
        emit("response", {"ai_msg": msg_ai, "more": more}, broadcast=True)
    if not more:
        generate_essay()


def generate_essay():
    emit("done", "Generating Thesis")
    thesis = chain.gen_thesis()
    emit("essay_part_generated", {"part": "Thesis", "content": thesis}, broadcast=True)

    emit("done", "Generating Outline")
    outline = chain.gen_outline()
    emit(
        "essay_part_generated",
        {"part": "Outline", "content": "\n".join(outline)},
        broadcast=True,
    )

    emit("done", "Generating Essay, this may take a while...")
    chain.gen_essay()
    emit(
        "essay_part_generated",
        {"part": "Essay", "content": chain.essay},
        broadcast=True,
    )
    emit("done", "Fixing AI detection")
    ai_fix = chain.prevent_ai_detection()
    emit("essay_part_generated", {"part": "AI Fix", "content": ai_fix}, broadcast=True)
    # emit("done", "Final Essay Length: " + str(len(ai_fix.split(" "))))
    emit("finished", "Finished")


if __name__ == "__main__":
    socketio.run(app, debug=True, port=9090)
