#!/bin/bash
# עין-צופיה Pro - PythonAnywhere Installation Script
# Run this in a Bash console on PythonAnywhere

echo "=========================================="
echo "  עין-צופיה Pro v3.0"
echo "  PythonAnywhere Installation"
echo "=========================================="
echo ""

# Get username
USERNAME=$(whoami)
echo "Username: $USERNAME"
echo ""

# Create project directory
echo "📁 Creating project directory..."
mkdir -p ~/ein_tzofia_v3
cd ~/ein_tzofia_v3

echo "✅ Directory created: ~/ein_tzofia_v3"
echo ""

# Install dependencies
echo "📦 Installing Python packages..."
pip3.10 install --user streamlit google-generativeai pywhatkit pillow

echo ""
echo "✅ Packages installed!"
echo ""

echo "=========================================="
echo "  ✅ Installation Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Upload your project files to ~/ein_tzofia_v3"
echo "2. Go to Web tab"
echo "3. Create a new web app"
echo "4. Follow the WSGI configuration"
echo ""
echo "Good luck! 🚀"
