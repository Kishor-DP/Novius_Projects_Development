import React, { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { Table, Input, Button, Form } from 'reactstrap';
import io from 'socket.io-client';

const socket = io('http://127.0.0.1:5000');

function App() {
  const [logs, setLogs] = useState([]);
  const [mvisEvents, setMvisEvents] = useState([]);
  const [filteredLogs, setFilteredLogs] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [sortConfig, setSortConfig] = useState({ key: 'Time_Stamp_Gridviewtbl', direction: 'ascending' });

  useEffect(() => {
    // Fetch initial data
    axios.get('http://127.0.0.1:5000/api/logs')
      .then(response => {
        setLogs(response.data);
        setFilteredLogs(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the logs!', error);
      });

    axios.get('http://127.0.0.1:5000/api/mvis-events')
      .then(response => {
        setMvisEvents(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching Mvis Events!', error);
      });

    // Set up WebSocket listener
    socket.on('update_logs', (data) => {
      setLogs(data);
      setFilteredLogs(data);
    });

    return () => {
      socket.off('update_logs');
    };
  }, []);

  useEffect(() => {
    const filtered = logs.filter(log =>
      log.Time_Stamp_Gridviewtbl.toLowerCase().includes(searchTerm.toLowerCase()) ||
      log.Code.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredLogs(filtered);
  }, [searchTerm, logs]);

  const handleSort = (key) => {
    let direction = 'ascending';
    if (sortConfig.key === key && sortConfig.direction === 'ascending') {
      direction = 'descending';
    }
    const sorted = [...filteredLogs].sort((a, b) => {
      if (a[key] < b[key]) {
        return direction === 'ascending' ? -1 : 1;
      }
      if (a[key] > b[key]) {
        return direction === 'ascending' ? 1 : -1;
      }
      return 0;
    });
    setSortConfig({ key, direction });
    setFilteredLogs(sorted);
  };

  return (
    <div className="container">
      <h1 className="mt-5">Mvis_Logs_Viewer</h1>
      <Form inline className="mt-3 mb-3">
        <Input
          type="text"
          placeholder="Search logs..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <Button color="primary" onClick={() => setSearchTerm('')}>Clear</Button>
      </Form>
      <h2>Train_Events</h2>
      <Table striped>
        <thead>
          <tr>
            <th onClick={() => handleSort('Time_Stamp_Gridviewtbl')}>
              Time_Stamp_Gridviewtbl {sortConfig.key === 'Time_Stamp_Gridviewtbl' ? (sortConfig.direction === 'ascending' ? '🔼' : '🔽') : ''}
            </th>
            <th onClick={() => handleSort('Code')}>
              Code {sortConfig.key === 'Code' ? (sortConfig.direction === 'ascending' ? '🔼' : '🔽') : ''}
            </th>
          </tr>
        </thead>
        <tbody>
          {filteredLogs.map((log, index) => (
            <tr key={index}>
              <td>{log.Time_Stamp_Gridviewtbl}</td>
              <td>{log.Code}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      <h2>Bogie_Events</h2>
      <Table striped>
        <thead>
          <tr>
            <th>Time_stamp</th>
            <th>Code</th>
            <th>Component</th>
            <th>Parameter</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {mvisEvents.map((event, index) => (
            <tr key={index}>
              <td>{event.Time_stamp}</td>
              <td>{event.Code}</td>
              <td>{event.Component}</td>
              <td>{event.Parameter}</td>
              <td>{event.Status}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default App;
