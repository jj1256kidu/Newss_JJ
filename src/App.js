import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Dashboard from './components/Dashboard';
import ProfileView from './components/ProfileView';
import Navbar from './components/Navbar';

const theme = createTheme({
  palette: {
    primary: {
      main: '#2563EB',
    },
    secondary: {
      main: '#4F46E5',
    },
    success: {
      main: '#10B981',
    },
    background: {
      default: '#F9FAFB',
    },
    text: {
      primary: '#1F2937',
    },
  },
  typography: {
    fontFamily: '"Inter", "Helvetica", "Arial", sans-serif',
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
          borderRadius: 8,
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
        },
      },
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <div className="App">
          <Navbar />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/profiles/:articleId" element={<ProfileView />} />
          </Routes>
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App; 
