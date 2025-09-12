#!/usr/bin/env python
"""
QR Cody Server Startup Script
Simple and reliable server startup with error handling
"""
import os
import sys
import subprocess

def main():
    print("🚀 Starting QR Cody Server...")
    print("=" * 40)
    
    try:
        # Start the Django development server
        print("📡 Server starting at http://127.0.0.1:8000")
        print("🌐 Open your browser and go to: http://localhost:8000")
        print("⏹️  Press Ctrl+C to stop the server")
        print("-" * 40)
        
        # Run the server
        subprocess.run([
            sys.executable, "manage.py", "runserver", "127.0.0.1:8000"
        ])
        
    except KeyboardInterrupt:
        print("\n✅ Server stopped successfully!")
    except FileNotFoundError:
        print("❌ Error: Python or Django not found. Make sure you've installed the requirements:")
        print("   pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you're in the QR Cody directory")
        print("2. Install requirements: pip install -r requirements.txt")
        print("3. Try running: python manage.py runserver")

if __name__ == "__main__":
    main()