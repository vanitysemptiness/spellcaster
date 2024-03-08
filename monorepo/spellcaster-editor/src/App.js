import React, { useState } from 'react';

function App() {
  const [text, setText] = useState('');

  const handleChange = (event) => {
    setText(event.target.value);
  };

  return (
    <div>
      <h1>Text Editor</h1>
      <textarea
        value={text}
        onChange={handleChange}
        rows={10}
        cols={50}
      />
    </div>
  );
}

export default App;
