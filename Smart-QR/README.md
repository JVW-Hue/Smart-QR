# QR Cody - Professional QR Code Generator

A modern, futuristic web app for creating professional QR codes with payment integration.

## Features

- ✨ Modern, futuristic UI with glassmorphism design
- 🎨 Customizable QR code colors
- 💧 Free version with watermark
- 💎 HD version without watermark ($1)
- 📱 Fully responsive design
- ⚡ Fast QR code generation
- 💳 Stripe payment integration ready

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python run_server.py
```

The app will start on port 8000, or 8001 if 8000 is busy.

## Manual Setup

1. Run migrations:
```bash
python manage.py migrate
```

2. Create superuser (optional):
```bash
python manage.py createsuperuser
```

3. Start development server:
```bash
python manage.py runserver 8000
```

## Configuration

Edit `.env` file to configure:
- SECRET_KEY: Django secret key
- DEBUG: Debug mode (True/False)
- STRIPE_PUBLISHABLE_KEY: Your Stripe publishable key
- STRIPE_SECRET_KEY: Your Stripe secret key

## Tech Stack

- **Backend**: Django 4.2
- **QR Generation**: qrcode library with PIL
- **Payments**: Stripe
- **Frontend**: Vanilla JavaScript with modern CSS
- **Database**: SQLite (default)

## Deployment

For production deployment:
1. Set DEBUG=False in .env
2. Configure proper SECRET_KEY
3. Set up Stripe keys
4. Use a production database
5. Configure static files serving

## License

MIT License