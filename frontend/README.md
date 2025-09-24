# ELIS Frontend 🎨

A vanilla JavaScript frontend for the ELIS Therapist Finder API.

## 🚀 Quick Start

### Development
1. **Start the ELIS API backend:**
   ```bash
   cd /path/to/elis-backend
   uvicorn app.main:app --reload
   ```

2. **Serve the frontend:**
   ```bash
   cd frontend
   python3 -m http.server 8001
   ```

3. **Open in browser:**
   ```
   http://127.0.0.1:8001/index.html
   ```

## 🛠️ Configuration

Update the API configuration in `script.js`:

```javascript
this.config = {
    apiBaseUrl: 'https://your-api-domain.com', // Your deployed API
    apiKey: 'your-actual-api-key-here',        // Your API key
    endpoints: {
        therapists: '/therapists'
    }
};
```

### Components
- **Hero Section**: Gradient background with floating elements
- **Search Card**: Elevated card with blur backdrop
- **Therapist Cards**: Hover animations and micro-interactions
- **Loading States**: Smooth spinner animations

## 🔧 Advanced Features

### Keyboard Shortcuts
- **Ctrl/Cmd + Enter**: Submit search
- **Escape**: Clear search and results

### Auto-Search
The app automatically searches when you change any dropdown selection, providing instant feedback.

### Error Handling
Graceful error handling with user-friendly messages for:
- Network errors
- API errors  
- Empty results

### Performance
- **Optimized animations**: 60fps smooth transitions
- **Lazy loading**: Staggered card animations
- **Minimal footprint**: ~15KB total (gzipped)
