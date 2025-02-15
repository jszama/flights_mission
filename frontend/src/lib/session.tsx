import "server-only";
import { SignJWT, jwtVerify } from 'jose';
import { cookies } from 'next/headers';
import { redirect } from "next/navigation";

const key = new TextEncoder().encode(process.env.SECRET);

const cookie = {
  name: 'session',
  options: { httpOnly: true, secure: process.env.NODE_ENV === 'production', sameSite: 'lax', path: '/' },
  duration: 60 * 60 * 24 * 7, // 1 week
};

export async function encrypt(payload: any) {
  return await new SignJWT(payload)
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('1h')
    .sign(key);
}

export async function decrypt(token: string) {
  try {
    const { payload } = await jwtVerify(token, key, { algorithms: ['HS256'] });
    return payload;
  } catch (error) {
    console.error('Error decrypting token:', error);
    throw new Error('Invalid token');
  }
}

export async function createSession(userId: string) {
    const expires = new Date(Date.now() + cookie.duration * 1000);
    const session = await encrypt({ userId, expires });

    (await cookies()).set(cookie.name, session, { ...cookie.options, expires, sameSite: cookie.options.sameSite as "lax" });
}

export async function verifySession() {
  const userCookie = (await cookies()).get(cookie.name)?.value;
  const session = await decrypt(userCookie || '');

    if (!session) {
        redirect("/login");
    }

  return { userId: session.userId };
}

export async function deleteSession() {
    (await cookies()).delete(cookie.name);
    redirect("/login");
}