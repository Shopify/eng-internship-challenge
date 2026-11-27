import "./App.css";
import { useState } from "react";
import { generateKeyMatrix, decrypt } from "../../javascript/solution";

function App() {
  const [keyValue, setKeyValue] = useState("SUPERSPY");
  const [encryptedValue, setEncryptedValue] = useState(
    "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
  );
  const [decryptedMessage, setDecryptedMessage] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    try {
      const keyMatrix = generateKeyMatrix(keyValue);
      const decryptedText = decrypt(keyMatrix, encryptedValue);
      setDecryptedMessage(decryptedText);
    } catch (error) {
      console.error(error);
      alert("Failed to decrypt: " + error.message);
    }
  };

  const handleKeyChange = (event) => {
    setKeyValue(event.target.value);
  };

  const handleEncryptedChange = (event) => {
    setEncryptedValue(event.target.value);
  };

  return (
    <div className="app">
      <div className="top">
        <div className="header-container">
          <h1>Welcome to Spy City!</h1>
          <h2>Solve the cipher to enter.</h2>
        </div>
      </div>
      <main className="app-main">
        <form onSubmit={handleSubmit}>
          <div className="form-label-container">
            <label>Enter your key:</label>
            <input type="text" value={keyValue} onChange={handleKeyChange} />
          </div>
          <div className="form-label-container">
            <label>Enter your encrypted message:</label>
            <input
              type="text"
              value={encryptedValue}
              onChange={handleEncryptedChange}
            />
          </div>
          <button type="submit">Crack the Code</button>
        </form>
        {decryptedMessage && (
          <div className="form-response">
            <h3>Decrypted message:</h3>
            <p>{decryptedMessage}</p>
            <p>
              Give this password to the door-person and they will give you
              access to their illustrious spy club!
            </p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
