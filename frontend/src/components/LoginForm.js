import React, { useState } from 'react';
import '../LoginForm.css';

function LoginForm() {
  const [LID, setLID] = useState('');
  const [YER, setYER] = useState('');
  const [SWD, setSWD] = useState('');
  const [ES2, setES2] = useState('');
  const [responseData, setResponseData] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      fetch('https://our.com Endpoint', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          LID: `${LID}`,
          YER: `${YER}`,
          SWD: `${SWD}`,
          ES2: `${ES2}`,
        }),
      })
        .then((response) => response.json())
        .then();
    } catch (error) {
      console.log(error);
    }

    alert(`Stats entered:\nLID: ${LID}\nYER: ${YER}\nSWD: ${SWD}\nES2: ${ES2}`);
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      {/* LeagueID */}
      <label>
        LeagueID (LID):
        <input
          type="number"
          value={LID}
          onChange={(e) => setLID(e.target.value)}
        />
      </label>

      {/* Year */}
      <label>
        Year (YER):
        <input
          type="number"
          value={YER}
          onChange={(e) => setYER(e.target.value)}
        />
      </label>

      {/* SWID */}
      <label>
        Points (SWD):
        <input
          type="text"
          value={SWD}
          onChange={(e) => setSWD(e.target.value)}
        />
      </label>

      {/* ESPNS2 */}
      <label>
        ESPNS2 (ES2):
        <input
          maxLength={500}
          type="text"
          value={ES2}
          onChange={(e) => setES2(e.target.value)}
        />
      </label>
      <input className="btn" type="submit" value="Submit info" />
    </form>
  );
}

export default LoginForm;
