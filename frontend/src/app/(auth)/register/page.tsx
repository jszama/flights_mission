import React from 'react'

import RegisterForm from './components/RegisterForm';
import { authPageHeaderType, buttonType } from '@/lib/types';
import { CustomGoogleLogin } from '@/components/ui/googleLogin';
import HorizontalBreak from '@/components/HorizontalBreak';
import PageHeader from '@/components/Auth/PageHeader';

export default function Login() {
  return (
      <main className='login-page'>
        <section className='login-header'>
          <PageHeader type={authPageHeaderType.REGISTER} />
        </section>
        <section className='login-content'>
          <RegisterForm />
          <HorizontalBreak text='or' width='70%' />
          <CustomGoogleLogin text={buttonType.signup_with}/>
        </section>
    </main>
  )
}