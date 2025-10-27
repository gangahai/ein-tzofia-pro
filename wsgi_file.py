"""
WSGI config for עין-צופיה Pro on PythonAnywhere
=================================================

Replace 'YOUR_USERNAME' with your actual PythonAnywhere username!

Example: If your username is 'aharonnais', replace:
    '/home/YOUR_USERNAME/ein_tzofia_v3'
with:
    '/home/aharonnais/ein_tzofia_v3'
"""

import sys
import os

# ============================================
# IMPORTANT: Replace YOUR_USERNAME with your actual username!
# ============================================
USERNAME = 'YOUR_USERNAME'  # <-- CHANGE THIS!

# Add project directory to Python path
project_folder = f'/home/{USERNAME}/ein_tzofia_v3'
if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

# Import and run Streamlit
os.chdir(project_folder)

# Set environment variables for Streamlit
os.environ['STREAMLIT_SERVER_PORT'] = '8000'
os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'

def application(environ, start_response):
    """
    WSGI application entry point
    """
    # Import streamlit
    try:
        from streamlit.web import cli as stcli
        import threading
        
        # Run streamlit in a thread
        if not hasattr(application, 'streamlit_started'):
            def run_streamlit():
                sys.argv = ["streamlit", "run", "app.py", "--server.port=8000"]
                stcli.main()
            
            thread = threading.Thread(target=run_streamlit, daemon=True)
            thread.start()
            application.streamlit_started = True
        
        # Return response
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        
        return [b'''
        <html>
        <head>
            <meta http-equiv="refresh" content="0; url=http://''' + environ['HTTP_HOST'].encode() + b''':8000" />
        </head>
        <body>
            <p>Redirecting to Streamlit app...</p>
        </body>
        </html>
        ''']
        
    except Exception as e:
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [f'Error: {str(e)}'.encode()]
