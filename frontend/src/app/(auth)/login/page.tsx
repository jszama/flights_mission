import React from 'react'

import LoginForm from './components/LoginForm';
import { CustomGoogleLogin } from '@/components/ui/googleLogin';
import { buttonType, authPageHeaderType } from '@/lib/types';
import Image from 'next/image';
import PageHeader from '@/components/Auth/PageHeader';
import HorizontalBreak from '@/components/HorizontalBreak';

export default function Login() {
  return (
      <main className='login-page'>
        <section className='login-header'>
          <PageHeader type={authPageHeaderType.LOGIN} />
        </section>
        <section className='login-content'>
          <LoginForm />
          <HorizontalBreak text='or' width='70%' />
          <CustomGoogleLogin text={buttonType.signin_with} />
          <p className='password-reset'>Forgot your password? <a>Reset Password </a></p>
        <Image src='/dotted-plane.png' alt='login-image' width={500} height={500} style={{opacity: 0.6 }} className='relative bottom-0'/>
        </section>
    </main>
  )
}