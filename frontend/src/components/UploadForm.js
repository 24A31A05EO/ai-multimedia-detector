import React, { useState } from "react";
import client from "../api/client";

function UploadForm() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await client.post("/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResponse(res.data.message);
    } catch (error) {
      setResponse("Upload failed: " + error.message);
    }
  };

  return (
    <div>
      <h2>Upload Your File</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      <p>{response}</p>
    </div>
  );
}

export default UploadForm;
