import type { Metadata } from "next";
import { Roboto, Lora, Inter } from "next/font/google";
import "../styles/globals.css";

import { GoogleOAuthProvider } from '@react-oauth/google';
import Header from "../components/Header/Header";

const roboto = Roboto({
  subsets: ["latin"],
  weight: ['400', '700'],
  variable: '--font-roboto',
});

const lora = Lora({
  subsets: ["latin"],
  weight: ['400', '700'],
  variable: '--font-lora',
});

const inter = Inter({
  subsets: ["latin"],
  weight: ['400', '700'],
  variable: '--font-inter',
});

export const metadata: Metadata = {
  title: "Plane Jane",
  description: "Your favourite holiday chat bot!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <GoogleOAuthProvider clientId="YOUR_CLIENT_ID">
      <html lang="en">
        <body
          className={`${roboto.variable} ${lora.variable} ${inter.variable} antialiased`}
        >
          <Header />
          {children}
        </body>
      </html>
    </GoogleOAuthProvider>
  );
}
