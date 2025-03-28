import React from 'react';
import ReactDOM from 'react-dom';
import SanctionsListSearch from './SanctionsListSearch';

function App() {
  return (
    <div className="App">
      <SanctionsListSearch />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));