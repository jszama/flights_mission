frontend/
├── .next/                  # Next.js build output (automatically generated)
├── node_modules/           # Node.js dependencies (automatically generated)
├── public/                 # Static assets
│   ├── images/             # Images used across the app
│   ├── fonts/              # Custom fonts
│   └── favicon.ico         # Favicon ( website icon )
├── src/
│   ├── middleware.ts       # Very useful way to check if user is authorised for certain pages ( not registered can not access dashboard or profile yk)
│   ├── app/                # App Router (Next.js feature so we don't need to define a Router, makes life a lot easier)
│   │   ├── (auth)/         # Grouped route for authentication-related pages ( just for readability, parentheses ignore it from the url)
│   │   │   └── login/      # Login page (www.website.com/login, (auth) is ignored)
│   │   │       ├── components/  # Subcomponents for the login page ( like the actual form )
│   │   │       │   └── LoginForm.tsx  # LoginForm component ( having this here makes the page code look nicer )
│   │   │       ├── actions/     # Server actions for login ( nextjs allows us to make a backend for each page so it looks nicer )
│   │   │       │   └── login.ts # login form handling
│   │   │       └── page.tsx     # Actual login page code
│   │   ├── (main)/         # Grouped route for main app pages
│   │   │   └── dashboard/  # Example of a protected page
│   │   │       └── page.tsx
│   │   ├── api/            # API routes (backend) but I dont't think we will need it
│   │   │   ├── auth/       
│   │   │   │   └── route.ts 
│   │   │   └── ...         
│   │   ├── layout.tsx      # Root layout for the app ( layout applied to every page )
│   │   └── page.tsx        # Home page (www.website.com)
│   ├── components/         # Shared components (for example a header)
│   ├── styles/             # Global and modular styles ( styling stuffs )
│   │   ├── globals.css     # Global CSS
│   │   ├── theme.css       # Theming styles
│   │   └── ...             
│   ├── types/              # TypeScript types/interfaces ( think of it as schemas pretty much )
│   └── utils/              # Utility functions and libraries (if we have functions that are used in more than one page put them here)
├── .env.local              # Environment variables (local)
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
### Don't have to touch the rest unless making console scripts
├── .eslintrc.js            # ESLint configuration ( code analysis )
├── next.config.js          # Next.js configuration 
├── package.json            # Project dependencies and scripts
└── tsconfig.json           # TypeScript configuration
