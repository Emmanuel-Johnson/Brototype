import React, { useState } from "react";

function App() {
  const [isOn, setIsOn] = useState(false);

  function handleToggle() {
    setIsOn(!isOn);
  }

  return (
    <div>
      <button onClick={handleToggle}>
        {isOn ? "ON" : "OFF"}
      </button>
    </div>
  );
}

export default App;