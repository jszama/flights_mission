"use server";

import { loginFormSchema } from "@/lib/types";
import { connectToDatabase } from "@/database/database";
import bcrypt from "bcryptjs";
import { User } from "@/database/models/User";
import { redirect } from "next/navigation";
import { createSession } from "@/lib/session";

export default async function handleLogin(prevState: any, formData: FormData) {
  let success = false;
  try {
    const validatedFields = loginFormSchema.safeParse({
      email: formData.get("email"),
      password: formData.get("password"),
    });

    if (!validatedFields.success) {
      return {
        errors: {
          email: validatedFields.error.flatten().fieldErrors?.email?.[0] as string,
          password: validatedFields.error.flatten().fieldErrors?.password?.[0] as string,
        },
      };
    }

    const { email, password } = validatedFields.data;

    const authenticatedUser = await authenticateUser(email, password);

    await createSession(authenticatedUser._id as string);
    console.log("User logged in:", authenticatedUser);

    success = true;
  } catch (error) {
    console.error("Login error:", error);

    return {
      errors: {
        email: "An error occurred.",
      },
    };
  } finally {
    if (success) redirect("/dashboard");
  }
}

async function authenticateUser(email: string, password: string) {
  await connectToDatabase();
  const user = await User.findOne({ email });

  if (user && (await bcrypt.compare(password, user.password as string))) {
    return user;
  }

  return {
    errors: {
      email: "Invalid email or password.",
    },
  };;
}