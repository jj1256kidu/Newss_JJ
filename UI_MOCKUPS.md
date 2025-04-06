# NewsNex UI Mockups

## 🎨 Design Philosophy

NewsNex follows a clean, professional design language that emphasizes:
- **Clarity**: Clear information hierarchy and readability
- **Efficiency**: Quick access to key features and actions
- **Professionalism**: Enterprise-grade interface suitable for business users
- **Consistency**: Unified design language across all components

## 🖥️ Main Interface

### 1. Dashboard View
```
+------------------------------------------------------------------+
|  NewsNex - Turning Headlines into Human Intelligence              |
+------------------------------------------------------------------+
|  🔍 Search Bar                                                    |
|  +----------------------------------------------------------+    |
|  | Paste URL or article content...                          |    |
|  +----------------------------------------------------------+    |
|                                                                   |
|  📊 Recent Extractions                                            |
|  +------------------+  +------------------+  +------------------+ |
|  | Article Title    |  | Article Title    |  | Article Title    | |
|  | 3 profiles found |  | 5 profiles found |  | 2 profiles found | |
|  | 2h ago          |  | 4h ago          |  | 1d ago          | |
|  +------------------+  +------------------+  +------------------+ |
|                                                                   |
|  ⚡ Quick Actions                                                  |
|  +------------------+  +------------------+  +------------------+ |
|  | New Extraction   |  | Export All      |  | Settings        | |
|  +------------------+  +------------------+  +------------------+ |
+------------------------------------------------------------------+
```

### 2. Profile Extraction View
```
+------------------------------------------------------------------+
|  Article: "Tech Giant Announces Major AI Investment"             |
+------------------------------------------------------------------+
|  📋 Extracted Profiles (3)                                       |
|  +----------------------------------------------------------------+
|  | 👤 John Smith                                                  |
|  | 🏢 CTO, TechCorp                                              |
|  | 💬 "We're investing $100M in AI research..."                  |
|  | 🔗 [LinkedIn Profile]                                         |
|  | 📊 Confidence: 95%                                            |
|  +----------------------------------------------------------------+
|  | 👤 Sarah Johnson                                              |
|  | 🏢 Head of AI Research                                        |
|  | 💬 "This investment will accelerate..."                       |
|  | 🔗 [LinkedIn Profile]                                         |
|  | 📊 Confidence: 88%                                            |
|  +----------------------------------------------------------------+
|                                                                   |
|  📥 Export Options                                                |
|  [ ] CSV  [ ] JSON  [ ] LinkedIn List                            |
|                                                                   |
|  ⚡ Actions                                                       |
|  [Generate Outreach] [Save to CRM] [Share]                       |
+------------------------------------------------------------------+
```

### 3. Chrome Extension Popup
```
+------------------------+
| NewsNex Extension      |
+------------------------+
| 🔍 Analyzing Article   |
|                        |
| 📊 3 Profiles Found    |
|                        |
| ⚡ Quick Actions       |
| [View Profiles]        |
| [Export]              |
| [Settings]            |
+------------------------+
```

## 🎯 Key UI Components

### 1. Search/Input Area
- Large, prominent search bar
- Support for both URL and text input
- Clear visual feedback during processing
- Recent searches history

### 2. Profile Cards
- Clean, card-based layout
- Visual hierarchy for key information
- Confidence score indicator
- Quick action buttons
- LinkedIn integration

### 3. Export Panel
- Multiple format options
- Custom field selection
- Batch export capabilities
- Integration options

## 📱 Responsive Design

### Desktop View
- Full-width layout
- Sidebar navigation
- Multi-column profile display
- Advanced filtering options

### Tablet View
- Single-column layout
- Collapsible sidebar
- Optimized card sizes
- Touch-friendly controls

### Mobile View
- Stacked layout
- Bottom navigation
- Simplified actions
- Focused content view

## 🎨 Color Scheme

### Primary Colors
- Primary: #2563EB (Blue)
- Secondary: #4F46E5 (Indigo)
- Accent: #10B981 (Green)

### Neutral Colors
- Background: #F9FAFB
- Text: #1F2937
- Borders: #E5E7EB

## 🖼️ Iconography

### System Icons
- 🔍 Search
- 📊 Analytics
- ⚡ Actions
- 📥 Export
- 🔗 Links

### Profile Icons
- 👤 Person
- 🏢 Company
- 💬 Quote
- 📊 Confidence

## 🎮 Interactive Elements

### Buttons
- Primary: Solid, prominent
- Secondary: Outlined
- Tertiary: Text-only

### Input Fields
- Clear validation states
- Autocomplete suggestions
- Error messaging

### Dropdowns
- Clear hierarchy
- Searchable options
- Multi-select support

## 📊 Data Visualization

### Confidence Score
```
[██████████░░] 80%
```
- Color-coded based on score
- Visual progress bar
- Numerical percentage

### Profile Distribution
```
Company A: ██████████ (50%)
Company B: ████ (20%)
Company C: ██████ (30%)
```
- Horizontal bar chart
- Percentage labels
- Color differentiation

## 🔄 Loading States

### Initial Load
```
+------------------------+
| Loading Article...     |
| [████████░░░░░░░░] 60% |
+------------------------+
```

### Profile Extraction
```
+------------------------+
| Extracting Profiles    |
| Found: 3              |
| Processing...         |
+------------------------+
```

## 🎯 Error States

### Invalid URL
```
+------------------------+
| ❌ Invalid URL         |
| Please check the URL  |
| and try again.        |
+------------------------+
```

### No Profiles Found
```
+------------------------+
| No profiles found     |
| Try another article   |
| or check the content. |
+------------------------+
```

## 📱 Mobile-Specific Features

### Bottom Navigation
```
+------------------------+
| Home | Search | Export |
+------------------------+
```

### Quick Actions
```
+------------------------+
| [Share] [Save] [More] |
+------------------------+
```

## 🎨 Accessibility Features

### High Contrast Mode
- Increased contrast ratios
- Larger text options
- Clear focus indicators

### Screen Reader Support
- ARIA labels
- Semantic HTML
- Keyboard navigation

## 🔄 Animation Guidelines

### Micro-interactions
- Subtle hover effects
- Smooth transitions
- Loading animations

### State Changes
- Fade transitions
- Slide animations
- Progress indicators 