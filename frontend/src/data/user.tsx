import { verifySession } from "@/lib/session";
import { connectToDatabase } from "@/database/database";
import { User } from "@/database/models/User";
import { cache } from 'react'

export const getUser = cache(async () => {
    const session = await verifySession();

    await connectToDatabase();
    const user = await User.findById(session.userId).select('-password');

    return user;
})