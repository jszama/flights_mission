"use server";

import { registerFormSchema } from "@/lib/types";
import { connectToDatabase } from "@/database/database";
import bcrypt from "bcryptjs";
import { User } from "@/database/models/User";
import { createSession } from "@/lib/session";
import { redirect } from "next/navigation";

export default async function handleRegister(prevState: any, formData: FormData) {
  let success = false;
  try {
    const validatedFields = registerFormSchema.safeParse({
      firstName: formData.get('firstName'),
      lastName: formData.get('lastName'),
      email: formData.get('email'),
      password: formData.get('password'),
    });

    if (!validatedFields.success) {
      return {
        errors: {
          firstName: validatedFields.error.flatten().fieldErrors?.firstName?.[0] as string,
          lastName: validatedFields.error.flatten().fieldErrors?.lastName?.[0] as string,
          email: validatedFields.error.flatten().fieldErrors?.email?.[0] as string,
          password: validatedFields.error.flatten().fieldErrors?.password?.[0] as string,
        },
      };
    }

    const { firstName, lastName, email, password } = validatedFields.data;

    const registeredUser = await registerUser( firstName, lastName, email, password);

    await createSession(registeredUser._id as string);
    console.log("User registered:", registeredUser);

    success = true;
  } catch (error) {
    console.error("Register error:", error);

    return {
      errors: {
        email: "An error occurred.",
        },
    };
  } finally {
    if (success) redirect("/dashboard");
  }
}

async function registerUser(firstName: string, lastName: string, email: string, password: string) {
  await connectToDatabase();
  const user = await User.findOne({ email });

  if (user) {
    return { errors: { email: "Email already in use."} };
  }
  
  const hashedPassword = await bcrypt.hash(password, 10);
  const newUser = new User({ firstName, lastName, email, password: hashedPassword });
  await newUser.save();

  return newUser;
}