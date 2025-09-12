#!/usr/bin/env python
import os
import sys
import subprocess
import time
import socket

def check_port(port):
    """Check if port is available"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result != 0

def test_server():
    """Test server startup"""
    print("QR Cody Server Test")
    print("=" * 30)
    
    # Check if port 8000 is available
    if check_port(8000):
        port = 8000
        print(f"✓ Port {port} is available")
    elif check_port(8001):
        port = 8001
        print(f"✓ Port {port} is available (8000 was busy)")
    else:
        print("✗ Both ports 8000 and 8001 are busy")
        return False
    
    try:
        print("Starting Django server...")
        print(f"Server will be available at: http://127.0.0.1:{port}")
        print("Press Ctrl+C to stop the server")
        print("-" * 50)
        
        subprocess.run([
            sys.executable, "manage.py", "runserver", f"127.0.0.1:{port}"
        ])
        
    except KeyboardInterrupt:
        print("\n✓ Server stopped successfully")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    test_server()