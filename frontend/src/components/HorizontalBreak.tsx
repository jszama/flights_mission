interface HorizontalBreakProps {
    text: string;
    width: string;
  }
  
  export default function HorizontalBreak({ text, width }: HorizontalBreakProps) {
    return (
      <div className='horizontal-break' style={{ width: width }}>
        <hr />
        <p>{text}</p>
        <hr />
      </div>
    )
  }