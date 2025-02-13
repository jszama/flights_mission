import React from 'react'
import Image from 'next/image'

export default function Review() {
  return (
    <article className='review'>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud  
          </p>
        <section>
              <Image src={'/profile.png'} alt="User profile picture" width={40} height={40} />
              <span>
                <h3>
                    First Last Name
                </h3>
                <h4>
                    Date
                </h4>
                </span>
          </section>
    </article>
  )
}
