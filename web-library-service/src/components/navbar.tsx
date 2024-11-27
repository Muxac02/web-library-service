import * as React from 'react';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';
import HomeIcon from '@mui/icons-material/Home';
import BookIcon from '@mui/icons-material/Book';
import AccountBoxIcon from '@mui/icons-material/AccountBox';
import LoginIcon from '@mui/icons-material/Login';

export default function Navbar() {
  return (
    <div role="navigation">
      <Breadcrumbs aria-label="breadcrumb" separator=" | ">
        <Link
          underline="hover"
          sx={{ display: 'flex', alignItems: 'center' }}
          color="inherit"
          href="/"
        >
          <HomeIcon sx={{ mr: 0.5 }} fontSize="inherit" />
          Home
        </Link>
        <Link
          underline="hover"
          sx={{ display: 'flex', alignItems: 'center' }}
          color="inherit"
          href="/books"
        >
          <BookIcon sx={{ mr: 0.5 }} fontSize="inherit" />
          Books
        </Link>
        <Link
          underline="hover"
          sx={{ display: 'flex', alignItems: 'center' }}
          color="inherit"
          href="/profile"
        >
          <AccountBoxIcon sx={{ mr: 0.5 }} fontSize="inherit" />
          Profile
        </Link>
        <Link
          underline="hover"
          sx={{ display: 'flex', alignItems: 'center' }}
          color="inherit"
          href="/login"
        >
          <LoginIcon sx={{ mr: 0.5 }} fontSize="inherit" />
          Login
        </Link>
      </Breadcrumbs>
    </div>
  );
}
