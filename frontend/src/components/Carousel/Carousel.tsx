'use client';

import React from 'react'
import useEmblaCarousel from 'embla-carousel-react'
import Autoplay from 'embla-carousel-autoplay'

import Review from './Review';

export function Carousel() {
  const [emblaRef] = useEmblaCarousel({ loop: true }, [Autoplay()])

  return (
    <div className="embla" ref={emblaRef}>
      <div className="embla__container">
        <div className="embla__slide"><Review/></div>
        <div className="embla__slide"><Review/></div>
        <div className="embla__slide"><Review/></div>
      </div>
    </div>
  )
}
