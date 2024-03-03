import React from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

const NoteEditor = () => {
  return (
    <div>
      <ReactQuill theme="snow" />
    </div>
  );
};

export default NoteEditor;
