import React from 'react'
import Image from 'next/image'

export default function HamburgerContent() {
  const isLogged = true;

  const ProfileBanner = () => {
    return (
      <section className='profile-banner'>
        <span className='flex flex-row'>
        <Image src='/profile.png' height={40} width={40} alt="Profile Icon" />
        <h2>John <a className='text-[18px]'>Doe</a></h2>
        </span>
        <button>Log Out</button>
      </section>
    )
  }

  const LoginBanner = () => {
    return (
      <section className='login-banner'>
        <button className='sign-in'>Sign In</button>
        <button className='sign-up'>Sign Up</button>
      </section>
    )
  }
  const UserMenu = () => {
    return (
      <section className='visible-menu'>
        <ul>
          <li><Image src='/chatbot.png' height={32} width={32} alt="Chatbot Icon"/><span>Start Chatting</span></li>
          <li><Image src='/bookings.png' height={32} width={32} alt="Bookings Icon"/><span>Your Bookings</span></li>
          <li><Image src='/settings.png' height={32} width={32} alt="Settings Icon"/><span>Settings</span></li>
        </ul>
      </section>
    )
  }

  const HiddenMenu = () => {
    return (
      <section className='hidden-menu' >
        <ul>
          <li><Image src='/chatbot.png' height={32} width={32} alt="Chatbot Icon"/><span>Start Chatting</span></li>
          <li><Image src='/bookings.png' height={32} width={32} alt="Bookings Icon"/><span>Your Bookings</span></li>
          <li><Image src='/settings.png' height={32} width={32} alt="Settings Icon"/><span>Settings</span></li>
        </ul>
        <p>
          Sign in or create an account in order to access our full range of services!
        </p>
      </section>
    )
  }

  const UserView = () => {
    return (
      <>
        <ProfileBanner />
        <hr />
        <UserMenu />
      </>
    )
  }

  const GuestView = () => {
    return (
      <>
        <LoginBanner />
        <hr />
        <HiddenMenu />
      </>
    )
  }

  const HamburgerContent = () => {
    return (
      <div className='hamburger-content'>
          <div className='triangle'/>
          {isLogged ? <UserView /> : <GuestView />}
      </div>
    )
  }

  return (
    <HamburgerContent />
  )
}
