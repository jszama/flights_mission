'use client';

import React, { useState, useEffect } from 'react';
import DesktopHomePage from '../components/Home/DesktopHomePage';
import MobileHomePage from '../components/Home/MobileHomePage';

export default function Home() {
  const [isMobile, setIsMobile] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const handleResize = () => {
        setIsMobile(window.innerWidth <= 768);
    };

    handleResize();
    setIsLoading(false);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);
  
  return !isLoading && ( isMobile ? <MobileHomePage/> : <DesktopHomePage/>)
}
