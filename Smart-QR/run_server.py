#!/usr/bin/env python
import os
import sys
import subprocess

def run_server():
    """Run Django development server with proper error handling"""
    try:
        # Try port 8000 first
        port = 8000
        print(f"Starting QR Cody server on port {port}...")
        
        # Run migrations first
        print("Running database migrations...")
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
        
        # Start server
        subprocess.run([
            sys.executable, "manage.py", "runserver", f"127.0.0.1:{port}"
        ], check=True)
        
    except subprocess.CalledProcessError as e:
        if "Address already in use" in str(e) or e.returncode == 1:
            # Try port 8001
            port = 8001
            print(f"Port 8000 busy, trying port {port}...")
            try:
                subprocess.run([
                    sys.executable, "manage.py", "runserver", f"127.0.0.1:{port}"
                ], check=True)
            except subprocess.CalledProcessError:
                print("Both ports 8000 and 8001 are busy. Please free up a port and try again.")
                sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_server()