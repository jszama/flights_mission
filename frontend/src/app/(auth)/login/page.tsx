import React from 'react'

import LoginForm from './components/LoginForm';
import { CustomGoogleLogin } from '@/components/ui/googleLogin';
import { buttonType } from '@/types/buttonType';
import Link from 'next/link';
import Image from 'next/image';

export default function Login() {
  return (
      <main className='login-page'>
        <section className='login-header'>
          <h1>Plane Jane</h1>
          <h2>Welcome Back!</h2>
          <h3>Don&apos;t have an account? <Link href={'/register'}>Sign up</Link></h3>
        </section>
        <section className='login-content'>
          <LoginForm />
          <div className='horizontal-break'>
            <hr />
            <p>Or</p>
            <hr />
          </div>
          <CustomGoogleLogin text={buttonType.signin_with} />
          <p className='password-reset'>Forgot your password? <a>Reset Password </a></p>
        <Image src='/dotted-plane.png' alt='login-image' width={500} height={500} style={{opacity: 0.6 }} className='relative bottom-0'/>
        </section>
    </main>
  )
}