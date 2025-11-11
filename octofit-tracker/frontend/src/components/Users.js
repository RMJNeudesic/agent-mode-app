import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const baseUrl = codespace ? `https://${codespace}-8000.app.github.dev/api/users/` : 'http://localhost:8000/api/users/';

  useEffect(() => {
    console.log('Fetching Users from:', baseUrl);
    fetch(baseUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Fetched Users:', results);
      });
  }, [baseUrl]);

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <ul className="list-group">
        {users.map((user, idx) => (
          <li key={idx} className="list-group-item">
            {user.name} ({user.email}) - Team: {user.team}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Users;
