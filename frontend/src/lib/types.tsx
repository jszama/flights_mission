import { z } from "zod";

export const loginFormSchema = z.object({
  email: z.string(),
  password: z.string()
})

export const registerFormSchema = z.object({
  firstName: z.string()
    .regex(/^[a-zA-Z]*$/, {
    message: "First name must contain only alphabetic characters.",
  }),
  lastName: z.string()
    .regex(/^[a-zA-Z]*$/, {
    message: "Last name must contain only alphabetic characters.",
  }),
  email: z.string().email({
    message: "Invalid email address.",
  }),
  password: z.string()
    .min(8, {
      message: "Password must be at least 8 characters long."
    })
    .refine((password) => /[A-Z]/.test(password), {
      message: "Password must contain at least one uppercase letter.",
    })
    .refine((password) => /[0-9]/.test(password), {
      message: "Password must contain at least one number.",
    })
    .refine((password) => /[^a-zA-Z0-9]/.test(password), {
      message: "Password must contain at least one special character.",
    }),
})

export enum buttonType {
    signin_with = "signin_with",
    signup_with = "signup_with"
}

export enum authPageHeaderType {
    LOGIN = "LOGIN",
    REGISTER = "REGISTER"
}