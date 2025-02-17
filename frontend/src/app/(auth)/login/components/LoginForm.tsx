"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { useActionState } from "react";

import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { loginFormSchema } from "@/lib/types";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import handleLogin from "@/app/(auth)/login/actions/handleLogin";

export default function LoginForm() {
  const [state, action, pending] = useActionState(handleLogin, null);

  const form = useForm<z.infer<typeof loginFormSchema>>({
    resolver: zodResolver(loginFormSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  return (
    <Form {...form}>
      <form action={action} className="space-y-4">
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel className="login-form-label">Email</FormLabel>
              <FormControl>
                <Input
                  className="login-form-input"
                  placeholder="johndoe@email.com"
                  {...field}
                  required
                  autoFocus
                  autoComplete="email"
                />
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
                  required
                  autoComplete="current-password"
                />
              </FormControl>
            </FormItem>
          )}
        />
        {state?.errors?.email && (  
          <FormMessage className="text-red-500">{state.errors.email}</FormMessage>
        )}
        <Button
        className="bg-[var(--cta-colour)] text-white font-thin text-[16px]"
        type="submit"
        disabled={pending}
      >
        {pending ? "Signing in..." : "Sign in"}
      </Button>
      </form>
    </Form>
  );
}