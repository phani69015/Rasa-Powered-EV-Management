const inputField = document.getElementById('user-input'); 
const outputField = document.getElementById('output');
const chatContainer = document.getElementById('chat-container');

let inputText = "";
let isListening = false;
const maxOutputLength = 1000000;  
 
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        if (inputText.trim() !== "") {
            sendMessageToRasa(inputText);
            inputText = "";
            inputField.innerText = "";
        }
    } else if (event.key === 'Backspace') {
        inputText = inputText.slice(0, -1);
        inputField.innerText = inputText;
    } else if (event.key.length === 1) {
        inputText += event.key;
        inputField.innerText = inputText;
    } else if (event.key === 'Escape') {  // Change 'Escape' to any key you want to use
        window.speechSynthesis.cancel(); // Stop the voice output
    }
});

function appendMessage(message, sender) { 
    outputField.innerHTML = "";

    if (message.length > maxOutputLength) {
        message = "Here is the required output. The complete message is too long to display.";
    }

    const messageElement = document.createElement('div');
    messageElement.className = sender;
    messageElement.innerText = message;
    outputField.appendChild(messageElement);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}
 
function sendMessageToRasa(message) {
    fetch('http://localhost:5005/webhooks/rest/webhook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                sender: "user",
                message: message
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data && data.length > 0) {
                data.forEach(botMessage => {
                    appendMessage(botMessage.text, 'bot');
                    speakMessage(botMessage.text);  
                });
            }
        })
        .catch(error => {
            appendMessage("Error connecting to Rasa server", 'bot');
        });
}

function speakMessage(message) {
    const utterance = new SpeechSynthesisUtterance(message);
    window.speechSynthesis.speak(utterance);
}
 
function focusInput() {
    document.activeElement.blur();
}
 
function startVoiceInput() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = function() {
        isListening = true;
        appendMessage("Listening for voice input...", 'bot');
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        appendMessage(`You said: ${transcript}`, 'user');
        sendMessageToRasa(transcript);
    };

    recognition.onerror = function(event) {
        appendMessage('Error occurred in recognition: ' + event.error, 'bot');
    };

    recognition.onend = function() {
        isListening = false;
    };

    recognition.start();
}

document.addEventListener('keydown', function(event) {
    if ((event.key === '0' && !isListening)) { 
        startVoiceInput();
    }
});
