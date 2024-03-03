import React from 'react';
import ReactDOM from 'react-dom';
import FileTree from './components/FileTree';
import NoteEditor from './components/NoteEditor';

const App = () => {
  return (
    <div>
      <FileTree />
      <NoteEditor />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
