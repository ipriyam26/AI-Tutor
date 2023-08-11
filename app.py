import random
import time
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
chain:Chains = None
loadingMessage = None
outlineDone = False  
writeEssay = False

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
    global msg_ai, more, loadingMessage,outlineDone,writeEssay
    if more and not outlineDone :
        msg_ai, more = chain.gen_info(question)
        print(f"AI Message:{msg_ai}\nMore:{more}")
        emit("response", {"ai_msg": msg_ai, "more": more}, broadcast=True)

    if not more and not outlineDone and not writeEssay:
        generate_outline()
        outlineDone = True
    elif outlineDone and not writeEssay:
        generate_review(question)
        writeEssay = True
    # elif writeEssay:
        # generate_essay()
    

def generate_outline():
    emit("done", "Here is an example of the thesis....")
    thesis = chain.gen_thesis()
    print(f"Thesis: {thesis}")
    emit("essay_part_generated", {"part": "Thesis", "content": thesis}, broadcast=True)

    emit("done", "Here is an outline that we can use to write your own essay....")
    outline = chain.gen_outline()
    print(f"Outline: {outline}")
    emit(
        "essay_part_generated",
        {"part": "Outline", "content": "\n".join(outline)},
        broadcast=True,
    )

def generate_review(question:str):
    rating = random.randint(0, 50)
    time.sleep(30)
    emit("response", {"ai_msg": f"Your Rating: {rating}/100 based on plagerism & originality", "more": False}, broadcast=True)


def generate_essay():
    emit("done", "Fixing Essay, this may take a while...")
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
