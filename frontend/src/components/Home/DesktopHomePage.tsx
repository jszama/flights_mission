import Image from 'next/image';
import { Carousel } from '../Carousel/Carousel';

export default function DesktopHomePage() {    
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

            <section id='demo' className='demo'>
                <section className='demo-header'>
                    <h2>
                        How does it work?
                    </h2>
                    <h3>Demo</h3>
                </section>
                <section className='demo-content'>
                    <Image className='demo-image' src="/desktop-demo.png" alt="Chat" width={196} height={300} />
                    <article>
                        <ul>
                            <li>
                                <h3><Image src={'/one.png'} alt='One' width={28} height={28} />Start the Chat</h3>
                                <p>Begin a conversation with <span>Plane Jane</span>, the AI assistant.</p>
                                <Image className='background-img' src={'/step-1.png'} alt='Chatbot image' width={128} height={128} />
                            </li>
                            <li>
                                <h3><Image src={'/two.png'} alt='Two' width={28} height={28} />Enter Your Needs</h3>
                                <p>Provide <span>Plane Jane</span> with the details of your holiday.</p>
                                <Image className='background-img' src={'/step-2.png'} alt='Form image' width={128} height={128} />
                            </li>
                            <li>
                                <h3><Image src={'/three.png'} alt='Three' width={28} height={28} />Get Your Options</h3>
                                <p><span>Plane Jane</span> will show you all of the best flight options tailored to your needs.</p>
                                <Image className='background-img'src={'/step-3.png'} alt='Star image' width={128} height={128} />
                            </li>
                            <li>
                                <h3><Image src={'/four.png'} alt='Four' width={28} height={28} />You&apos;re All Set!</h3>
                                <p>Choose the flight that suits you and you&lsquo;re all set to book your next adventure!</p>
                                <Image className='background-img' src={'/step-4.png'} alt='Thumbs up image' width={128} height={128} />
                            </li>
                        </ul>
                        
                        <Image className='dotted-plane' src="/dotted-plane.png" alt="Plane image" width={790} height={442} />
                    </article>
                </section>
            </section>
            <section id='features' className='features'>
                <section className='features-header'>
                    <h2>Why Plane Jane?</h2>
                    <h3>Features</h3>
                </section>
                <ul>
                    <li>
                        <h3><Image src={'/chat.png'} alt='One' width={24} height={24} />Ease of Use</h3>
                        <p>Booking your next flight has never been easier. Just tell our AI what you are looking for, and it does the rest!</p>
                        <Image className='background-img' src={'/ease-of-use.png'} alt='Filter Icon' width={128} height={128} />
                    </li>
                    <li>
                        <h3><Image src={'/time.png'} alt='Two' width={24} height={24} />Time-Saving</h3>
                        <p>Stop wasting time on endless flight searches. Let our chatbot find the best options in a fraction of the time.</p>
                        <Image className='background-img' src={'/time-saving.png'} alt='Filter Icon' width={128} height={128} />
                    </li>
                    <li>
                        <h3><Image src={'/filter.png'} alt='Three' width={24} height={24} />Tailored Recommendations</h3>
                        <p>Forget generic flight lists — our chatbot customises results ensuring you find the perfect flight every time.</p>
                        <Image className='background-img' src={'/tailor.png'} alt='Filter Icon' width={128} height={128} />
                    </li>
                </ul>
                <p className='create-account-text'><a>Create an account now</a> and book the holiday you have been dreaming of!</p>
            </section>

            <section id='testimonials' className='reviews'>
                <section className='reviews-header'>
                    <h2>What people are saying</h2>
                    <h3>Testimonials</h3>
                </section>
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
        </main>
    )
}