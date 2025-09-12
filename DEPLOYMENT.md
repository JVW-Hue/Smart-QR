# Deployment Guide

## Quick Deploy to Render

1. **Push to GitHub**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Connect to Render**
- Go to [render.com](https://render.com)
- Connect your GitHub repository
- Choose "Web Service"

3. **Configure Render**
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn qr_app.wsgi:application`
- **Environment**: `python3`

4. **Set Environment Variables**
```
SECRET_KEY=your-secret-key-here
DEBUG=False
STRIPE_PUBLISHABLE_KEY=AbmBtIQOsBT6AGDU74TWQTq1laS2MaNt3P8HGPo26p3xD8m6dBjkNTu4fmpVmZzc9ky2O2N1_NpU6zCX
STRIPE_SECRET_KEY=your-paypal-secret-key
```

5. **Deploy**
- Click "Create Web Service"
- Wait for deployment to complete
- Your app will be live!

## Alternative: Heroku

```bash
heroku create smart-qr-generator
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
heroku config:set STRIPE_PUBLISHABLE_KEY=AbmBtIQOsBT6AGDU74TWQTq1laS2MaNt3P8HGPo26p3xD8m6dBjkNTu4fmpVmZzc9ky2O2N1_NpU6zCX
git push heroku main
```

## Files Required for Deployment

✅ All files are ready:
- `Procfile` - Web server config
- `build.sh` - Build script  
- `runtime.txt` - Python version
- `requirements.txt` - Dependencies
- `.gitignore` - Git ignore rules
- `.env.example` - Environment template