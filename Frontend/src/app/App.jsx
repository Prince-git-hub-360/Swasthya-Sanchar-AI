import React, { useState } from 'react';
import { AppRoutes } from './routes';
import { CinematicIntroSplash } from '../components/branding/CinematicIntroSplash';

export function App() {
  const [showSplash, setShowSplash] = useState(true);

  return (
    <>
      {showSplash && <CinematicIntroSplash onFinish={() => setShowSplash(false)} />}
      <AppRoutes />
    </>
  );
}

export default App;
