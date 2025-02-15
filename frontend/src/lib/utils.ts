import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function getStrengthColor(strength: number) {
  switch (strength) {
    case 0:
      return "gray"
    case 1:
      return "red"
    case 2:
      return "orange"
    case 3:
      return "yellow"
    case 4:
      return "green"
    case 5:
      return "blue"
    default:
      return "gray"
  }
}

