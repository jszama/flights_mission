'use client';
import React from 'react'
import Image from 'next/image'

export default function Chatbot() {
  return (
    <main className='chatbot'>
      <section className='chatbot-body'>
        <section className='chatbot-header'>
          <button>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M7.825 13L13.425 18.6L12 20L4 12L12 4L13.425 5.4L7.825 11H20V13H7.825Z" fill="#1D1B20" /></svg>
          </button>
            <div className='chatbot-title'>
                <Image src='/chatbot.png' alt='chatbot' height={48} width={48} /> 
            <h1>Plane Jane</h1>
          </div>
          <button>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <g clipPath="url(#clip0_60_191)">
                <path d="M23 4.00001V10M23 10H17M23 10L18.36 5.64001C17.2853 4.56473 15.9556 3.77922 14.4952 3.35679C13.0348 2.93436 11.4911 2.88877 10.0083 3.22427C8.52547 3.55978 7.1518 4.26545 6.01547 5.27543C4.87913 6.28542 4.01717 7.5668 3.51 9.00001M1 20V14M1 14H7M1 14L5.64 18.36C6.71475 19.4353 8.04437 20.2208 9.50481 20.6432C10.9652 21.0657 12.5089 21.1113 13.9917 20.7758C15.4745 20.4402 16.8482 19.7346 17.9845 18.7246C19.1209 17.7146 19.9828 16.4332 20.49 15" stroke="#444444" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"/>
              </g>
              <defs>
                <clipPath id="clip0_60_191">
                <rect width="24" height="24" fill="white"/>
                </clipPath>
              </defs>
            </svg>
          </button>
        </section>
        <section className='chatbot-messages'>
          <div className='chatbot-sequence'>
            <Image src='/chatbot.png' alt='chatbot' height={24} width={24} />
            <div className='chatbot-message-container'>
              <div className='chatbot-waiting'>
                <span></span>
              </div>
              <div className='chatbot-message'>
                <p>Hello there! 👋 It&apos;s nice to meet you, I am <span>Plane Jane</span> and I will be assisting you!</p>
              </div>
              <div className='chatbot-message'>
                <p>Tell me about your holiday plans! Please use the navigation below for any assistance or ask me anything about this system.</p>
              </div>
            </div>
          </div>
        </section>
        <section className='chatbot-input-container'>
          <textarea placeholder='Write a message...'/>
          <div className='chatbot-buttons'>
            <button>
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clipPath="url(#clip0_140_122)">
                  <path d="M15.8333 8.33333V9.99999C15.8333 11.5471 15.2188 13.0308 14.1248 14.1248C13.0308 15.2187 11.5471 15.8333 10 15.8333M10 15.8333C8.45291 15.8333 6.96918 15.2187 5.87522 14.1248C4.78125 13.0308 4.16667 11.5471 4.16667 9.99999V8.33333M10 15.8333V19.1667M6.66667 19.1667H13.3333M10 0.833328C9.33696 0.833328 8.70108 1.09672 8.23224 1.56556C7.7634 2.0344 7.5 2.67029 7.5 3.33333V9.99999C7.5 10.663 7.7634 11.2989 8.23224 11.7678C8.70108 12.2366 9.33696 12.5 10 12.5C10.663 12.5 11.2989 12.2366 11.7678 11.7678C12.2366 11.2989 12.5 10.663 12.5 9.99999V3.33333C12.5 2.67029 12.2366 2.0344 11.7678 1.56556C11.2989 1.09672 10.663 0.833328 10 0.833328Z" stroke="#333333" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </g>
                <defs>
                  <clipPath id="clip0_140_122">
                  <rect width="20" height="20" fill="white"/>
                  </clipPath>
                </defs>
              </svg>
            </button>
            <button>
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 20V4L22 12L3 20ZM5 17L16.85 12L5 7V10.5L11 12L5 13.5V17ZM5 17V12V7V10.5V13.5V17Z" fill="#007BFF"/>
              </svg>
            </button>
          </div>
        </section>
      </section>
    </main>
  )
}
