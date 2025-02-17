import Link from "next/link";
import { authPageHeaderType } from "@/lib/types";

interface PageHeaderProps {
    type: authPageHeaderType;
}

export default function PageHeader({ type }: PageHeaderProps) {
    return (
        <section className='login-header'>
          <h1>Plane Jane</h1>
            { 
                type === authPageHeaderType.REGISTER ? (<>
                    <h2>Get Started!</h2>
                    <h3>Already have an account? <Link href={'/login'}>Sign in</Link></h3>
                </>)
                    :
                (<>
                    <h2>Welcome Back!</h2>
                    <h3>Don&apos;t have an account? <Link href={'/register'}>Sign up</Link></h3>
                </>)                      
            }
        </section>
    )
}