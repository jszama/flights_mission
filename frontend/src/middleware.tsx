import { cookies } from "next/headers";
import { type NextRequest, NextResponse } from "next/server";
import { decrypt } from "@/lib/session";

export default async function middleware(req: NextRequest) {
    const protectedRoutes = ["/dashboard", "/settings"];
    const authRoutes = ["/login", "/register"];
    const currentPath = req.nextUrl.pathname;
    const isProtected = protectedRoutes.includes(currentPath);
    const isAuthRoute = authRoutes.includes(currentPath);

    const cookie = (await cookies()).get("session")?.value;
    let session = null;
    if (cookie) {
        session = await decrypt(cookie);
    }

    if (isAuthRoute) {
        if (session) {
            return NextResponse.redirect(new URL("/dashboard", req.nextUrl));
        }
        return NextResponse.next();
    }

    if (isProtected) {
        if (!session) {
            return NextResponse.redirect(new URL("/login", req.nextUrl));
        }
    }

    return NextResponse.next();
}
