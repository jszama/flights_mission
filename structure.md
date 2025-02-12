my-nextjs-app/
├── .next/                  # Next.js build output (automatically generated)
├── node_modules/           # Node.js dependencies (automatically generated)
├── public/                 # Static assets (e.g., images, fonts, favicon)
│   ├── images/             # Images used across the app
│   ├── fonts/              # Custom fonts
│   └── favicon.ico         # Favicon ( website icon )
├── src/
│   ├── app/                # App Router (Next.js 13+)
│   │   ├── (auth)/         # Grouped route for authentication-related pages
│   │   │   └── login/      # Login page
│   │   │       ├── components/  # Subcomponents for the login page ( components within the login page like the form )
│   │   │       │   └── LoginForm.tsx  # LoginForm component (colocated)
│   │   │       ├── actions/     # Server actions for login
│   │   │       │   └── login.ts # Server action for login logic
│   │   │       └── page.tsx     # Login page
│   │   ├── (main)/         # Grouped route for main app pages
│   │   │   └── dashboard/  # Example of a protected page
│   │   │       └── page.tsx
│   │   ├── api/            # API routes (backend) but I dont't think we will need
│   │   │   ├── auth/       
│   │   │   │   └── route.ts 
│   │   │   └── ...         
│   │   ├── layout.tsx      # Root layout for the app
│   │   └── page.tsx        # Home page
│   ├── components/         # Shared components (if any)
│   ├── lib/                # Utility functions and libraries
│   ├── styles/             # Global and modular styles
│   │   ├── globals.css     # Global CSS
│   │   ├── theme.css       # Theming styles
│   │   └── ...             # Other styles
│   ├── types/              # TypeScript types/interfaces
│   └── utils/              # Utility functions
├── .env.local              # Environment variables (local)
├── .eslintrc.js            # ESLint configuration
├── .gitignore              # Git ignore file
├── next.config.js          # Next.js configuration
├── package.json            # Project dependencies and scripts
├── tsconfig.json           # TypeScript configuration
└── README.md               # Project documentation