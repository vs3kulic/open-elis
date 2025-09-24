# ELIS Frontend 🎨

A **beautiful, modern, vanilla JavaScript frontend** for the ELIS Therapist Finder API.

## ✨ Features

- **🎯 Modern Design**: Clean, professional UI with smooth animations
- **📱 Fully Responsive**: Looks gorgeous on desktop, tablet, and mobile
- **⚡ Lightning Fast**: No framework overhead, pure vanilla JavaScript
- **🔄 Real-time Search**: Auto-search as you select criteria
- **💫 Smooth Animations**: Delightful micro-interactions and loading states
- **🎨 Beautiful Gradients**: Eye-catching design with professional color palette
- **♿ Accessible**: Semantic HTML and keyboard navigation support

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

### Production
Simply upload the `frontend/` folder contents to any static hosting service:
- **Netlify**: Drag & drop deployment
- **Vercel**: Connect to GitHub repo
- **GitHub Pages**: Enable in repository settings

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

## 🎨 Design System

### Colors
- **Primary**: `#6366f1` (Indigo)
- **Secondary**: `#8b5cf6` (Purple)  
- **Accent**: `#06b6d4` (Cyan)
- **Success**: `#10b981` (Emerald)

### Typography
- **Font**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700

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

## 📱 Browser Support

- ✅ Chrome 60+
- ✅ Firefox 60+
- ✅ Safari 12+
- ✅ Edge 79+

## 🤝 Contributing

This is a student project, but feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

MIT License - feel free to use this code for your own projects!

## 🎯 What Makes This Special

**No Framework, Maximum Beauty** - This frontend proves that you don't need React, Vue, or Angular to create stunning, professional web applications. Sometimes vanilla is the best flavor! 🍦

---

*Built with ❤️ by a 2nd semester CS student*