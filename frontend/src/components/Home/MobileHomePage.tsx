import Image from 'next/image';
import { Carousel } from '../Carousel/Carousel';

export default function MobileHomePage() {
    return (
        <main className="landing-page">
            <section id='top' className='hero'>
                <h1>
                    Holiday planning made easy.
                </h1>
                <p>
                    No more stressful nights looking for the right flight, we got it all sorted!
                </p>
                <button>Start Chat</button>
            </section>

            <section className='demo'>
                <Image src="/demo.png" alt="Chat" width={196} height={300} />
                <article>
                    <h2>
                        How does it work?
                    </h2>
                    <ul>
                        <li>
                            <h3><Image src={'/one.png'} alt='One' width={18} height={18} />Start the Chat</h3>
                            <p>Begin a conversation with the AI assistant.</p>
                        </li>
                        <li>
                            <h3><Image src={'/two.png'} alt='Two' width={18} height={18} />Enter Your Needs</h3>
                            <p>Provide your travel details.</p>
                        </li>
                        <li>
                            <h3><Image src={'/three.png'} alt='Three' width={18} height={18} />Get Your Options</h3>
                            <p>Receive flight options tailored to your needs.</p>
                        </li>
                        <li>
                            <h3><Image src={'/four.png'} alt='Four' width={18} height={18} />You&apos;re All Set!</h3>
                            <p>Choose your flight, and you&apos;re all set to book your next adventure!</p>
                        </li>
                    </ul>
                </article>
            </section>

            <section className='features'>
                <h2>Why Plane Jane?</h2>
                <ul>
                    <li>
                        <h3><Image src={'/chat.png'} alt='One' width={24} height={24} />Ease of Use</h3>
                        <p>Booking your next flight has never been easier. Just tell our AI what you are looking for, and it does the rest!</p>
                    </li>
                    <hr />
                    <li>
                        <h3><Image src={'/time.png'} alt='Two' width={24} height={24} />Time-Saving</h3>
                        <p>Stop wasting time on endless flight searches. Let our chatbot find the best options in a fraction of the time.</p>
                    </li>
                    <hr />
                    <li>
                        <h3><Image src={'/filter.png'} alt='Three' width={24} height={24} />Tailored Recommendations</h3>
                        <p>Forget generic flight lists — our chatbot customises results ensuring you find the perfect flight every time.</p>
                    </li>
                </ul>
            </section>

            <section className='reviews'>
                <h2>What people are saying</h2>
                <Carousel />
                <Image src={'/trustpilot.png'} alt='Trustpilot' width={128} height={42} />
            </section>

            <section className='footer'>
                <section className='about'>
                    <h2>
                        About Plane Jane
                    </h2>
                    <p>
                        Lorem ipsum odor amet, consectetuer adipiscing elit. Semper magnis interdum mollis sagittis vulputate pellentesque; facilisis tristique. Turpis eleifend metus bibendum;
                    </p>
                </section>

                <section className='contact'>
                    <h2>
                        Get In Touch
                    </h2>
                    <p>
                        Have feedback or a question? We&apos;d love to hear from you.
                    </p>
                    <button>CONTACT US<Image src="/contact-arrow.png" alt="Contact Icon" width={24} height={24} /></button>
                </section>
                <a className='back-to-top' href="#top">
                    <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M32 24L24 16M24 16L16 24M24 16V32M44 24C44 35.0457 35.0457 44 24 44C12.9543 44 4 35.0457 4 24C4 12.9543 12.9543 4 24 4C35.0457 4 44 12.9543 44 24Z" stroke="#E0E0E0" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                    </svg>
                </a>
            </section>
        </main>)
}