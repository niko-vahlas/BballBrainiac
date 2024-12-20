import React, { useState } from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';
import '../LoginForm.css';

function LoginForm() {
  const [LID, setLID] = useState('');
  const [YER, setYER] = useState('');
  const [SWD, setSWD] = useState('');
  const [ES2, setES2] = useState('');
  const [teamName, setTeamName] = useState('');
  const [days, setDays] = useState('');
  const [responseData, setResponseData] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:5000/process_data', {
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
          teamName: `${teamName}`,
          days: `${days}`,
        }),
      });

      const data = await response.json();
      setResponseData(data); // Set response data to state
    } catch (error) {
      console.log(error);
    }

    alert(
      `Stats entered:\nLID: ${LID}\nYER: ${YER}\nSWD: ${SWD}\nES2: ${ES2}\nTeam Name: ${teamName}\nDays: ${days}`
    );
  };

  return (
    <div>
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

        {/* Team Name */}
        <label>
          Team Name:
          <input
            type="text"
            value={teamName}
            onChange={(e) => setTeamName(e.target.value)}
          />
        </label>

        {/* Days */}
        <label>
          Days to Optimize:
          <input
            type="number"
            value={days}
            onChange={(e) => setDays(e.target.value)}
          />
        </label>

        <input className="btn" type="submit" value="Submit info" />
      </form>

      {responseData && (
        <div className="response-data">
          <TableContainer component={Paper}>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>New Team Points</TableCell>
                  <TableCell>Swapped In</TableCell>
                  <TableCell>Player's Avg Points (Swapped In)</TableCell>
                  <TableCell>Swapped Out</TableCell>
                  <TableCell>Player's Avg Points (Swapped Out)</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {responseData.data.map((item, index) => (
                  <TableRow key={index}>
                    <TableCell>{item.new_team_points}</TableCell>
                    <TableCell>
                      {item.swapped_in.name} ({item.swapped_in.team})
                    </TableCell>
                    <TableCell>{item.swapped_in.avg_points}</TableCell>
                    <TableCell>
                      {item.swapped_out.name} ({item.swapped_out.team})
                    </TableCell>
                    <TableCell>{item.swapped_out.avg_points}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </div>
      )}
    </div>
  );
}

export default LoginForm;
