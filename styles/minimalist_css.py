"""
עין-צופיה Pro - Minimalist CSS with 50% width containers
"""

def get_minimalist_css():
    """החזר CSS מינימליסטי עם קופסאות 50%"""
    
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [class*="css"] {
        font-family: 'Roboto', 'Segoe UI', sans-serif;
        direction: rtl;
        text-align: right;
        background: #ffffff;
        color: #202124;
    }
    
    /* ============================================
       MAIN CONTAINER - 50% WIDTH & CENTERED
    ============================================ */
    .main .block-container {
        max-width: 800px !important;
        margin: 0 auto;
        padding: 2rem 1rem;
    }
    
    .stApp {
        background: #ffffff;
    }
    
    /* ============================================
       CLEAN CARDS - 50% WIDTH
    ============================================ */
    .simple-card {
        background: #ffffff;
        border: 1px solid #dadce0;
        border-radius: 8px;
        padding: 20px;
        margin: 10px auto;
        max-width: 600px;
        box-shadow: 0 1px 2px 0 rgba(60,64,67,.3);
    }
    
    /* ============================================
       BUTTONS
    ============================================ */
    .stButton > button {
        background: #1a73e8;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        font-size: 14px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.2s;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: #1765cc;
        box-shadow: 0 1px 3px rgba(60,64,67,.3);
    }
    
    /* ============================================
       INPUTS
    ============================================ */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border: 1px solid #dadce0;
        border-radius: 4px;
        padding: 10px;
        background: #ffffff;
        width: 100%;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #1a73e8;
        outline: none;
    }
    
    /* ============================================
       HEADERS
    ============================================ */
    h1 {
        font-size: 28px;
        font-weight: 400;
        color: #202124;
        margin-bottom: 8px;
        text-align: center;
    }
    
    h2 {
        font-size: 22px;
        font-weight: 400;
        color: #202124;
        margin: 20px 0 10px 0;
    }
    
    h3 {
        font-size: 18px;
        font-weight: 500;
        color: #202124;
        margin: 15px 0 8px 0;
    }
    
    /* ============================================
       SIDEBAR
    ============================================ */
    section[data-testid="stSidebar"] {
        background: #f8f9fa;
        border-left: 1px solid #dadce0;
        width: 220px !important;
    }
    
    section[data-testid="stSidebar"] .stButton > button {
        text-align: right;
        justify-content: flex-start;
        padding: 12px 16px;
        margin-bottom: 8px;
    }
    
    /* ============================================
       FILE UPLOADER - CENTERED
    ============================================ */
    [data-testid="stFileUploader"] {
        border: 2px dashed #dadce0;
        border-radius: 8px;
        padding: 30px;
        background: #f8f9fa;
        text-align: center;
        max-width: 600px;
        margin: 20px auto;
    }
    
    /* ============================================
       VIDEO PLAYER - CENTERED
    ============================================ */
    video {
        max-width: 600px;
        width: 100%;
        height: auto;
        display: block;
        margin: 20px auto;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* ============================================
       PROGRESS BAR
    ============================================ */
    .stProgress > div > div > div {
        background: #1a73e8;
    }
    
    /* ============================================
       ALERTS
    ============================================ */
    .stAlert {
        border-radius: 4px;
        border: 1px solid #dadce0;
        max-width: 600px;
        margin: 10px auto;
    }
    
    /* ============================================
       EXPANDER
    ============================================ */
    .streamlit-expanderHeader {
        background: #f8f9fa;
        border: 1px solid #dadce0;
        border-radius: 4px;
        font-weight: 500;
    }
    
    /* ============================================
       SELECTBOX
    ============================================ */
    .stSelectbox {
        max-width: 600px;
        margin: 10px auto;
    }
    
    /* ============================================
       TEXT AREA
    ============================================ */
    .stTextArea {
        max-width: 600px;
        margin: 10px auto;
    }
    
    /* ============================================
       COLUMNS - CENTERED
    ============================================ */
    [data-testid="column"] {
        padding: 0 8px;
    }
    
    /* ============================================
       HIDE STREAMLIT BRANDING
    ============================================ */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* ============================================
       SCROLLBAR
    ============================================ */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f3f4;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #dadce0;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #bdc1c6;
    }
    
    /* ============================================
       RESPONSIVE
    ============================================ */
    @media (max-width: 768px) {
        .main .block-container {
            max-width: 100% !important;
            padding: 1rem 0.5rem;
        }
        
        .simple-card,
        [data-testid="stFileUploader"],
        video,
        .stAlert,
        .stSelectbox,
        .stTextArea {
            max-width: 100%;
        }
    }
    
    /* ============================================
       FOCUS STATES
    ============================================ */
    *:focus {
        outline: 2px solid #1a73e8;
        outline-offset: 2px;
    }
    </style>
    """
