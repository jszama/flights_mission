'use client';
import { GoogleLogin } from '@react-oauth/google';
import { buttonType } from '@/types/buttonType';

export const CustomGoogleLogin = (props: { text: buttonType; }) => {
    const { text } = props;

    return (
        <GoogleLogin
            onSuccess={
                text === buttonType.signin_with ?
                    (credentialResponse) => console.log(credentialResponse)
                    :
                    (credentialResponse) => console.log(credentialResponse)
            }
            onError={() => console.log("Google auth failed")}
            text={text}
        />
    )
};