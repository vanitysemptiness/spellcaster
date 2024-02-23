// TextBox.tsx
import React from 'react';
import './TextBox.css';

interface TextBoxProps {
  text: string;
}

const TextBox: React.FC<TextBoxProps> = ({ text }) => {
  return (
    <div className="text-box">
      <div className="outline">
        <div className="content">{text}</div>
      </div>
    </div>
  );
};

export default TextBox;
