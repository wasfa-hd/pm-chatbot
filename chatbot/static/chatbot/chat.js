let editingTurn = null;

function quickSend(text) {
    document.getElementById("user-input").value = text;
    sendMessage();
}

async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    const chatBox = document.getElementById("chat-box");

    if (!message) return;

    input.value = "";

    // If editing, update existing chat-turn
    let userMsg, botMsg;
    if (editingTurn) {
        userMsg = editingTurn.querySelector(".user-question");
        userMsg.innerHTML = `<strong>You:</strong> ${message}`;
        botMsg = editingTurn.querySelector(".bot-response");
        botMsg.innerHTML = "<em>PM is typing...</em>";
    } else {
        const turn = document.createElement("div");
        turn.className = "chat-turn";
        turn.innerHTML = `
            <div class="user-question" onclick="editMessage(this)"><strong>You:</strong> ${message}</div>
            <div class="bot-response"><em>PM is typing...</em></div>
            <button class="copy-btn" onclick="copyToClipboard(this)">📋 Copy</button>
        `;
        chatBox.appendChild(turn);
        editingTurn = turn;
    }

    chatBox.scrollTop = chatBox.scrollHeight;

    const res = await fetch("/chat/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message }),
    });

    const data = await res.json();
    const reply = data.reply || "Something went wrong.";

    const formatted = reply
        .replace(/^### (.*$)/gim, "<h3>$1</h3>")
        .replace(/^## (.*$)/gim, "<h2>$1</h2>")
        .replace(/^# (.*$)/gim, "<h1>$1</h1>")
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/\n/g, "<br>");

    editingTurn.querySelector(".bot-response").innerHTML = `<strong>PM:</strong> ${formatted}`;
    chatBox.scrollTop = chatBox.scrollHeight;
    editingTurn = null;
    

}

function editMessage(elem) {
    const oldText = elem.innerText.replace("You:", "").trim();
    const input = document.getElementById("user-input");
    input.value = oldText;
    editingTurn = elem.closest(".chat-turn");
    input.focus();
}

function copyToClipboard(copyBtn) {
    const text = copyBtn.previousElementSibling.innerText;
    navigator.clipboard.writeText(text).then(() => {
        copyBtn.innerText = "✅ Copied!";
        setTimeout(() => {
            copyBtn.innerText = "📋 Copy";
        }, 1200);
    });
}
function clearChat() {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML = "";
}
function exportChatToPDF() {
    const chatBox = document.getElementById("chat-box");
    const originalContent = document.body.innerHTML;
    const chatHTML = `
        <html>
        <head>
            <title>Chat Export - Project Manager Bot</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 20px; }
                .chat-turn { margin-bottom: 20px; }
                .user-question { font-weight: bold; color: #007bff; }
                .bot-response { margin-top: 5px; }
            </style>
        </head>
        <body>
            <h2>Chat Export - Project Manager Assistant</h2>
            ${chatBox.innerHTML}
        </body>
        </html>
    `;
    const printWindow = window.open('', '_blank');
    printWindow.document.open();
    printWindow.document.write(chatHTML);
    printWindow.document.close();
    printWindow.print();
}
