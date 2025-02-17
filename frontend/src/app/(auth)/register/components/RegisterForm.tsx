"use client"
import { useActionState, useState } from "react";
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { registerFormSchema } from "@/lib/types"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
} from "@/components/ui/form"
import { Progress } from "@/components/ui/progress"

import handleRegister from "@/app/(auth)/register/actions/handleRegister";
import { getStrengthColor } from "@/lib/utils";

const getPasswordStrength = (password: string) => {
  let strength = 0;

  if (password.length >= 8) {
    strength += 1;
  }

  if (password.match(/[a-z]+/)) {
    strength += 1;
  }

  const hasUppercase = password.match(/[A-Z]+/);
  if (hasUppercase) {
    strength += 1;
  }

  const hasNumber = password.match(/[0-9]+/);
  if (hasNumber) {
    strength += 1;
  }

  const hasSpecialChar = password.match(/[^a-zA-Z0-9]+/);
  if (hasSpecialChar) {
    strength += 1;
  }

  if (strength > 3 && (!hasUppercase || !hasNumber || !hasSpecialChar)) {
    strength = 3;
  }

  return strength;
};

export default function RegisterForm() {
  const [passwordStrength, setPasswordStrength] = useState(0);

  const form = useForm<z.infer<typeof registerFormSchema>>({
    resolver: zodResolver(registerFormSchema),
    defaultValues: {
      firstName: "",
      lastName: "",
      email: "",
      password: ""
    },
  })


  const [state, action, pending] = useActionState(handleRegister, null)

  return (
    <Form {...form}>
      <form action={action} className="space-y-4">
        <FormField
          control={form.control}
          name="firstName"
          render={({ field }) => (
            <FormItem>
              <FormLabel className="login-form-label">First Name</FormLabel>
              <FormControl>
                <Input className="login-form-input" placeholder="John" {...field} required autoFocus autoComplete="given-name" />
              </FormControl>
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="lastName"
          render={({ field }) => (
            <FormItem>
              <FormLabel className="login-form-label">Last Name</FormLabel>
              <FormControl>
                <Input className="login-form-input" placeholder="Doe" {...field} required autoComplete="family-name"/>
              </FormControl>
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel className="login-form-label">Email</FormLabel>
              <FormControl>
                <Input className="login-form-input" placeholder="johndoe@email.com" {...field} autoComplete="email" />
              </FormControl>
              </FormItem>
            )}
        />
        <FormField
            control={form.control}
            name="password"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="login-form-label">Password</FormLabel>
                <FormControl>
                  <Input
                  className="login-form-input"
                  placeholder="••••••••"
                  type="password"
                  {...field}
                  onChange={(e) => {
                    field.onChange(e.target.value.replace(/\s/g, ''));
                    setPasswordStrength(getPasswordStrength(e.target.value.replace(/\s/g, '')));
                  }}
                  />
                </FormControl>
                <Progress
                  value={passwordStrength}
                />
                <h3 className={`font-bold text-${getStrengthColor(passwordStrength)}-500`}>{passwordStrength === 0 ? '' : passwordStrength === 1 ? 'Weak' : passwordStrength === 2 ? 'Fair' : passwordStrength === 3 ? 'Good' : passwordStrength === 4 ? 'Strong' : 'Very Strong'}</h3>
              </FormItem>
          )}
        />
        { state?.errors && (
          <>
          <details className="error-box" open>
          <summary>Errors</summary>
            <ul>
              {state?.errors?.firstName && (
              <>
                <li>{state.errors.firstName}</li>
                <hr className="border-black/50 my-2" />
              </>
              )}
              {state.errors.lastName && (
              <>
                <li>{state.errors.lastName}</li>
                <hr className="border-black/50 my-2" />
              </>
              )}
              {state.errors.email && (
              <>
                <li>{state.errors.email}</li>
                <hr className="border-black/50 my-2" />
              </>
              )}
              {state.errors.password && (
              <>
                <li>{state.errors.password}</li>
              </>
              )}
            </ul>    
            </details>
          </>
        )}
        <Button
        className="bg-[var(--cta-colour)] text-white font-thin text-[16px]"
        type="submit"
        disabled={pending}
      >
        {pending ? "Signing up..." : "Sign up"}
      </Button>
      </form>
    </Form>
  )
}
