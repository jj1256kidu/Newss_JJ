import React, { useState } from 'react';
import {
  Container,
  Box,
  TextField,
  Button,
  Card,
  CardContent,
  Typography,
  Grid,
  CircularProgress,
  Alert,
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import SearchIcon from '@mui/icons-material/Search';
import FileUploadIcon from '@mui/icons-material/FileUpload';
import HistoryIcon from '@mui/icons-material/History';

// Mock data for recent extractions
const recentExtractions = [
  {
    id: 1,
    title: 'Tech Giant Announces Major AI Investment',
    profiles: 3,
    timeAgo: '2h ago',
  },
  {
    id: 2,
    title: 'Startup Raises $50M in Series B Funding',
    profiles: 5,
    timeAgo: '4h ago',
  },
  {
    id: 3,
    title: 'Industry Leader Appoints New CTO',
    profiles: 2,
    timeAgo: '1d ago',
  },
];

function Dashboard() {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleExtract = async () => {
    if (!url) {
      setError('Please enter a URL');
      return;
    }

    setLoading(true);
    setError('');

    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 2000));
      navigate('/profiles/1'); // Navigate to profile view
    } catch (err) {
      setError('Failed to extract profiles. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box sx={{ mb: 6 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Extract Profiles from News Articles
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
          Paste a news article URL or upload content to extract key decision-makers and experts.
        </Typography>

        <Box sx={{ display: 'flex', gap: 2, mb: 4 }}>
          <TextField
            fullWidth
            variant="outlined"
            placeholder="Paste article URL here..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            error={!!error}
            helperText={error}
          />
          <Button
            variant="contained"
            size="large"
            onClick={handleExtract}
            disabled={loading}
            startIcon={loading ? <CircularProgress size={20} /> : <SearchIcon />}
          >
            Extract
          </Button>
          <Button
            variant="outlined"
            size="large"
            startIcon={<FileUploadIcon />}
          >
            Upload
          </Button>
        </Box>

        {error && (
          <Alert severity="error" sx={{ mb: 4 }}>
            {error}
          </Alert>
        )}
      </Box>

      <Typography variant="h5" component="h2" gutterBottom sx={{ mb: 3 }}>
        Recent Extractions
      </Typography>

      <Grid container spacing={3}>
        {recentExtractions.map((extraction) => (
          <Grid item xs={12} sm={6} md={4} key={extraction.id}>
            <Card
              sx={{
                height: '100%',
                cursor: 'pointer',
                '&:hover': {
                  boxShadow: 6,
                },
              }}
              onClick={() => navigate(`/profiles/${extraction.id}`)}
            >
              <CardContent>
                <Typography variant="h6" component="h3" gutterBottom>
                  {extraction.title}
                </Typography>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Typography variant="body2" color="text.secondary">
                    {extraction.profiles} profiles found
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    •
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    {extraction.timeAgo}
                  </Typography>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}

export default Dashboard; 
