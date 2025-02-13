'use client';

import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
import HamburgerContent from './HamburgerContent';

export default function Header() {
    const [menuOpen, setMenuOpen] = React.useState(false);

    const expandMenu = () => {
        setMenuOpen(!menuOpen);
    };

  return (
    <div className="header">
      <h1 className='header-title'><Link href={'/'}>Plane Jane</Link></h1>
      <nav className='header-nav'>
        <a href='#demo'>Demo</a>
        <a href='#features'>Features</a>
        <a href='#testimonials'>Testimonials</a>
        <div className='vertical-divider'/>
        <div className='login-banner'>
          <button className='sign-in'>Sign In</button>
          <button className='sign-up'>Sign Up</button>
        </div>
      </nav>

      <section className='hamburger-menu' >
        <button className='hamburger-button' onClick={expandMenu}>
            <Image src="/hamburger.png" alt="Hamburger Menu" width={40} height={40} />
        </button>
        {menuOpen && <HamburgerContent />}
      </section>    
    </div>
  )
}
