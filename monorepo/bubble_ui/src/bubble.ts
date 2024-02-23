interface Message {
    text: string;
    sender: string;
    formatting?: {
      bold: boolean;
      italic: boolean;
      underline: boolean;
    };
  }
  
  const messageContainer = document.getElementById('message-container');
  const messageInput = document.getElementById('message-input') as HTMLTextAreaElement;
  const sendButton = document.getElementById('send-button');
  const boldButton = document.getElementById('bold-button');
  const italicButton = document.getElementById('italic-button');
  const underlineButton = document.getElementById('underline-button');
  
  const messages: Message[] = [];
  
  // function addMessage(text: string, sender: string = 'user'): void {
  //   const message = { text, sender, formatting: {} }; // Initialize formatting object
  //   messages.push(message);
  
  //   const messageElement = document.createElement('div');
  //   messageElement.classList.add('message-bubble');
  //   messageElement.classList.add(sender === 'user' ? 'user-message' : 'system-message');
  
  //   const authorElement = document.createElement('p');
  //   authorElement.classList.add('message-author');
  //   authorElement.textContent = sender;
  //   messageElement.appendChild(authorElement);
  
  //   const textElement = document.createElement('p');
  //   textElement.classList.add('formatted-text'); // Apply formatting styles here
  //   textElement.textContent = text;
  //   messageElement.appendChild(textElement);
  
  //   messageContainer.appendChild(messageElement);
  //   messageContainer.scrollTop = messageContainer.scrollHeight;
  // }
  
  // function sendMessage(): void {
  //   const text = messageInput.value.trim();
  //   if (!text) {
  //     return;
  //   }
  
  //   const formatting = {
  //     bold: boldButton.classList.contains('active'),
  //     italic: italicButton.classList.contains('active'),
  //     underline: underlineButton.classList
  //   }
  // }
  