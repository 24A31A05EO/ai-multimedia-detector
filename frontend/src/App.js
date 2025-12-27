import React from "react";
import UploadForm from "./components/UploadForm";
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>AI Multimedia Detector</h1>
        <UploadForm />
      </header>
    </div>
  );
}

export default App;
