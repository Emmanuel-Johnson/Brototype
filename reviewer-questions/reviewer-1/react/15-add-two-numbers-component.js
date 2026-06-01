import React, { useState } from 'react'

function App() {
  const [num1, setNum1] = useState("")
  const [num2, setNum2] = useState("")
  const [result, setResult] = useState("")

  function handleAdd() {
    setResult(Number(num1) + Number(num2))
  }

  return (
    <>
      <div>
        <label>Enter Number 1</label>
        <input
          type="number"
          value={num1}
          onChange={(e) => setNum1(e.target.value)}
        />
      </div>

      <div>
        <label>Enter Number 2</label>
        <input
          type="number"
          value={num2}
          onChange={(e) => setNum2(e.target.value)}
        />
      </div>

      <button onClick={handleAdd}>Add</button>

      <h1>Result: {result}</h1>
    </>
  )
}

export default App