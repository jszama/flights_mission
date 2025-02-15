import React from 'react'

import RegisterForm from './components/RegisterForm';
import { buttonType } from '@/types/buttonType';
import { CustomGoogleLogin } from '@/components/ui/googleLogin';
import Link from 'next/link';

export default function Login() {
  return (
      <main className='login-page'>
        <section className='login-header'>
          <h1>Plane Jane</h1>
          <h2>Get Started!</h2>
          <h3>Already have an account? <Link href={'/login'}>Sign in</Link></h3>
        </section>
        <section className='login-content'>
          <RegisterForm />
          <div className='horizontal-break'>
            <hr />
            <p>Or</p>
            <hr />
          </div>
          <CustomGoogleLogin text={buttonType.signup_with}/>
        </section>
    </main>
  )
}