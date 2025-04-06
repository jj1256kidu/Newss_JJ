import React from 'react';
import { useParams } from 'react-router-dom';
import {
  Container,
  Box,
  Card,
  CaardContent,
  Typography,
  Button,
  Grid,
  Chip,
  LinearProgress,
  Divider,
} from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import BusinessIcon from '@mui/icons-material/Business';
import FormatQuoteIcon from '@mui/icons-material/FormatQuote';
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import FileDownloadIcon from '@mui/icons-material/FileDownload';
import ShareIcon from '@mui/icons-material/Share';

// Mock data for profiles
const mockProfiles = [
  {
    id: 1,
    name: 'John Smith',
    role: 'CTO',
    company: 'TechCorp',
    quote: 'We\'re investing $100M in AI research to push the boundaries of what\'s possible in enterprise technology.',
    confidence: 95,
    linkedInUrl: 'https://linkedin.com/in/johnsmith',
  },
  {
    id: 2,
    name: 'Sarah Johnson',
    role: 'Head of AI Research',
    company: 'TechCorp',
    quote: 'This investment will accelerate our development of next-generation AI solutions for businesses.',
    confidence: 88,
    linkedInUrl: 'https://linkedin.com/in/sarahjohnson',
  },
  {
    id: 3,
    name: 'Michael Chen',
    role: 'VP of Engineering',
    company: 'TechCorp',
    quote: 'Our team is excited to lead the charge in developing cutting-edge AI technologies.',
    confidence: 92,
    linkedInUrl: 'https://linkedin.com/in/michaelchen',
  },
];

function ProfileView() {
  const { articleId } = useParams();

  const handleExport = (format) => {
    console.log(`Exporting profiles in ${format} format`);
    // Implement export functionality
  };

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box sx={{ mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Extracted Profiles
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
          Found {mockProfiles.length} profiles in the article
        </Typography>

        <Box sx={{ display: 'flex', gap: 2, mb: 4 }}>
          <Button
            variant="outlined"
            startIcon={<FileDownloadIcon />}
            onClick={() => handleExport('CSV')}
          >
            Export CSV
          </Button>
          <Button
            variant="outlined"
            startIcon={<FileDownloadIcon />}
            onClick={() => handleExport('JSON')}
          >
            Export JSON
          </Button>
          <Button
            variant="outlined"
            startIcon={<ShareIcon />}
          >
            Share
          </Button>
        </Box>
      </Box>

      <Grid container spacing={3}>
        {mockProfiles.map((profile) => (
          <Grid item xs={12} key={profile.id}>
            <Card>
              <CardContent>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
                  <Box>
                    <Typography variant="h6" component="h2" gutterBottom>
                      <PersonIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                      {profile.name}
                    </Typography>
                    <Typography variant="body1" color="text.secondary" gutterBottom>
                      <BusinessIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                      {profile.role} at {profile.company}
                    </Typography>
                  </Box>
                  <Chip
                    label={`${profile.confidence}% Confidence`}
                    color={profile.confidence > 90 ? 'success' : 'warning'}
                    sx={{ height: 32 }}
                  />
                </Box>

                <Box sx={{ mb: 2 }}>
                  <Typography variant="body2" color="text.secondary" gutterBottom>
                    <FormatQuoteIcon sx={{ mr: 1, verticalAlign: 'middle' }} />
                    Quote
                  </Typography>
                  <Typography variant="body1" sx={{ pl: 2 }}>
                    "{profile.quote}"
                  </Typography>
                </Box>

                <Divider sx={{ my: 2 }} />

                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <Button
                    variant="outlined"
                    size="small"
                    startIcon={<LinkedInIcon />}
                    href={profile.linkedInUrl}
                    target="_blank"
                  >
                    View LinkedIn Profile
                  </Button>
                  <Button
                    variant="contained"
                    size="small"
                  >
                    Generate Outreach
                  </Button>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}

export default ProfileView; 
