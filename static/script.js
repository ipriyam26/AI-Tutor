// Create a custom renderer for marked
const renderer = new marked.Renderer();
renderer.code = function (code, language) {
    const validLang = language && hljs.getLanguage(language) ? language : 'python';
    const highlightedCode = hljs.highlight(validLang, code).value;
    return `<pre><code class="hljs ${language}">${highlightedCode}</code></pre>`;
};
let isFirstMessage = true;

document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const chatContent = document.getElementById("chat-content");
    const input = document.getElementById("input");
    let loadingMessage;
    const socket = io.connect('http://localhost:9099');

    // Event listeners
    socket.on('response', function (data) {
        updateMessage(loadingMessage, data.ai_msg, false);
        if (data.more) {
            input.removeAttribute('disabled');
        }
    });

    socket.on('done', function (message) {
        // updateMessage(loadingMessage, message, false);
        appendMessage("bot", message, false);
        setTimeout(() => {
            loadingMessage = appendMessage("bot", createLoadingDots(), true);
        }, 1000);
    });

    socket.on('essay_part_generated', function (data) {
        const message = data.content;
        updateMessage(loadingMessage, message, false);
    });
    // socket.on('finised', function (data) {});
    //when finised event is received, disable the input field, and show the reload button

    socket.on('finished', function () {
        input.setAttribute('disabled', true);
        const sendButton = document.querySelector('.chat-submit');
        sendButton.textContent = 'Reload';
        sendButton.addEventListener('click', function (e) {
            e.preventDefault();
            location.reload();
        });
    })

    chatForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const question = input.value;
        if (!question) {
            return;
        }

        appendMessage("user", question, false);
        input.value = "";
        input.setAttribute('disabled', true);

        if (isFirstMessage) {
            appendMessage("bot", "The First Message takes a while to load as the server is sleeping....", false);
            socket.emit('start', question);
            isFirstMessage = false;
        } else {
            socket.emit('continue', question);
        }

        // wait for a second before showing the loading dots
        setTimeout(() => {
            loadingMessage = appendMessage("bot", createLoadingDots(), true);
        }, 1000);
    });

    // sourcery skip: avoid-function-declarations-in-blocks
    function createLoadingDots() {
        return `<div class="loading-dots">
                  <div></div>
                  <div></div>
                  <div></div>
                  <div></div>
                  <div></div>
                </div>`;
    }

    function appendMessage(cssClass, text, loading) {
        const messageWrapper = document.createElement("div");
        messageWrapper.classList.add("message-wrapper", cssClass);

        const message = document.createElement("div");
        message.classList.add("message");
        if (loading) {
            message.innerHTML = text;
        } else {
            message.innerHTML = marked.parse(text);
        }

        messageWrapper.appendChild(message);
        chatContent.appendChild(messageWrapper);
        chatContent.scrollTop = chatContent.scrollHeight;
        return message;
    }

    function updateMessage(message, text, loading) {
        message.innerHTML = marked.parse(text);
        chatContent.scrollTop = chatContent.scrollHeight;
    }
});
