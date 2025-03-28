import React, { useState } from 'react';

const SanctionsListSearch = () => {
  const [type, setType] = useState('All');
  const [name, setName] = useState('');
  const [idAddress, setIdAddress] = useState('');
  const [program, setProgram] = useState('All');
  const [address, setAddress] = useState('');
  const [city, setCity] = useState('');
  const [stateProvince, setStateProvince] = useState('');
  const [country, setCountry] = useState('All');
  const [list, setList] = useState('All');
  const [nameScore, setNameScore] = useState(85);

  const typeOptions = ['All', 'Individual', 'Entity', 'Vessel'];
  const programOptions = ['All', 'Counter Terrorism', 'Non-SDN Palestinian Legislative Council', 'Sectoral Sanctions'];
  const countryOptions = ['All', 'United States', 'Iran', 'Russia', 'China', 'North Korea'];

  const handleSearch = () => {
    // Implement search logic here
    console.log('Search parameters:', {
      type, name, idAddress, program, 
      address, city, stateProvince, 
      country, list, nameScore
    });
  };

  const handleReset = () => {
    // Reset all form fields
    setType('All');
    setName('');
    setIdAddress('');
    setProgram('All');
    setAddress('');
    setCity('');
    setStateProvince('');
    setCountry('All');
    setList('All');
    setNameScore(85);
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-4xl mx-auto bg-white shadow-lg rounded-lg p-6">
        <h1 className="text-2xl font-bold text-blue-800 mb-4">Search OFAC's Sanctions Lists</h1>
        
        <p className="text-gray-600 mb-6">
          This Sanctions List Search application ("Sanctions List Search") is designed to facilitate the use of the Specially Designated Nationals and Blocked Persons list ("SDN List") and other sanctions lists administered by OFAC. <a href="#" className="text-blue-600 hover:underline">Read More</a>
        </p>

        <div className="grid grid-cols-3 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Type:</label>
            <select 
              value={type}
              onChange={(e) => setType(e.target.value)}
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            >
              {typeOptions.map((option) => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Name:</label>
            <input 
              type="text" 
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Enter name"
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">ID #/Digital Currency Address:</label>
            <input 
              type="text" 
              value={idAddress}
              onChange={(e) => setIdAddress(e.target.value)}
              placeholder="Enter ID or address"
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            />
          </div>
        </div>

        <div className="grid grid-cols-3 gap-4 mt-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Program:</label>
            <select 
              value={program}
              onChange={(e) => setProgram(e.target.value)}
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            >
              {programOptions.map((option) => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Address:</label>
            <input 
              type="text" 
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              placeholder="Enter address"
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">City:</label>
            <input 
              type="text" 
              value={city}
              onChange={(e) => setCity(e.target.value)}
              placeholder="Enter city"
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            />
          </div>
        </div>

        <div className="grid grid-cols-3 gap-4 mt-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">State/Province:</label>
            <input 
              type="text" 
              value={stateProvince}
              onChange={(e) => setStateProvince(e.target.value)}
              placeholder="Enter state/province"
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Country:</label>
            <select 
              value={country}
              onChange={(e) => setCountry(e.target.value)}
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            >
              {countryOptions.map((option) => (
                <option key={option} value={option}>{option}</option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">List:</label>
            <select 
              value={list}
              onChange={(e) => setList(e.target.value)}
              className="w-full border border-gray-300 rounded-md shadow-sm py-2 px-3"
            >
              <option value="All">All</option>
              <option value="SDN">SDN List</option>
              <option value="Non-SDN">Non-SDN List</option>
            </select>
          </div>
        </div>

        <div className="mt-4 flex items-center space-x-4">
          <div className="flex-grow">
            <label className="block text-sm font-medium text-gray-700 mb-1">Minimum Name Score:</label>
            <div className="flex items-center space-x-4">
              <input 
                type="range" 
                min="0" 
                max="100" 
                value={nameScore}
                onChange={(e) => setNameScore(Number(e.target.value))}
                className="flex-grow"
              />
              <span className="text-sm text-gray-600">{nameScore}</span>
            </div>
          </div>
        </div>

        <div className="mt-6 flex justify-end space-x-4">
          <button 
            onClick={handleSearch}
            className="bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 flex items-center space-x-2"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <span>Search</span>
          </button>
          <button 
            onClick={handleReset}
            className="bg-gray-200 text-gray-700 py-2 px-4 rounded-md hover:bg-gray-300 flex items-center space-x-2"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M3 2v6h6"></path>
              <path d="M21 12A9 9 0 006 5.3L3 8"></path>
              <path d="M21 22v-6h-6"></path>
              <path d="M3 12a9 9 0 0015 6.7l3-2.7"></path>
            </svg>
            <span>Reset</span>
          </button>
        </div>
      </div>
    </div>
  );
};

// Render the component
function App() {
  return <SanctionsListSearch />;
}

ReactDOM.render(<App />, document.getElementById('root'));

export default SanctionsListSearch;