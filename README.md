# Smart QR - Professional QR Code Generator

🚀 A modern, clean web app for creating HD QR codes in 5 seconds with PayPal payment integration.

## ✨ Features

- 🎨 **Modern UI** - Clean design with Inter font and glassmorphism
- 🎯 **Instant Generation** - Create QR codes in 5 seconds
- 💧 **Free Version** - Download with JVW watermark
- 💎 **HD Premium** - $1 PayPal payment for watermark-free HD version
- 📱 **Mobile Friendly** - Fully responsive design
- ⚡ **Fast & Clean** - No ads, no clutter, no signup required
- 🎨 **Customizable** - Choose QR code and background colors

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd QR-Cody
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run migrations**
```bash
python manage.py migrate
```

4. **Start the server**
```bash
python manage.py runserver 12345
```

5. **Open your browser**
```
http://localhost:12345
```

### Environment Setup

1. **Copy environment file**
```bash
cp .env.example .env
```

2. **Edit `.env` with your settings**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
STRIPE_PUBLISHABLE_KEY=your-paypal-client-id
STRIPE_SECRET_KEY=your-paypal-secret
```

## 🌐 Deployment

### Deploy to Render

1. **Connect your GitHub repo to Render**
2. **Set environment variables in Render dashboard**
3. **Deploy automatically with these files:**
   - `Procfile` - Web server configuration
   - `build.sh` - Build script
   - `runtime.txt` - Python version
   - `requirements.txt` - Dependencies

### Deploy to Heroku

```bash
heroku create your-app-name
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
heroku config:set STRIPE_PUBLISHABLE_KEY=your-paypal-key
git push heroku main
```

## 🛠️ Tech Stack

- **Backend**: Django 4.2 + Gunicorn
- **QR Generation**: qrcode library with Pillow
- **Payments**: PayPal JavaScript SDK
- **Frontend**: Vanilla JavaScript + Inter font
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Deployment**: Render/Heroku ready

## 📁 Project Structure

```
QR-Cody/
├── qr_app/
│   ├── generator/          # Main app
│   ├── templates/          # HTML templates
│   ├── static/            # Static files
│   └── settings.py        # Django settings
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment config
├── build.sh              # Build script
├── runtime.txt           # Python version
└── README.md             # This file
```

## 💰 Business Model

- **Free**: QR codes with JVW watermark
- **Premium**: $1 PayPal payment for HD, watermark-free QR codes
- **Target**: Small businesses, cafés, events, restaurants

## 🚀 Features Roadmap

- [ ] Bulk QR generation
- [ ] Custom logos in QR codes
- [ ] Analytics dashboard
- [ ] API endpoints
- [ ] Multiple export formats (SVG, PDF)

## 📄 License

MIT License - Feel free to use for personal and commercial projects.

---

**Made with ❤️ for small businesses who need clean, professional QR codes fast.**