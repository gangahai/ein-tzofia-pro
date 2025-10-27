"""
עין-צופיה Pro v3.0 - Main Application
Gemini 2.5 Flash + Prompt Management System
"""

import streamlit as st
import time
from pathlib import Path
import sys
from datetime import datetime

# Add to path
sys.path.insert(0, str(Path(__file__).parent))

from config import *
from styles.minimalist_css import get_minimalist_css
from utils.prompt_manager import prompt_manager

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS
st.markdown(get_minimalist_css(), unsafe_allow_html=True)

# ============================================
# SESSION STATE
# ============================================

if 'page' not in st.session_state:
    st.session_state.page = 'analyze'

if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None

if 'selected_prompt' not in st.session_state:
    prompts = prompt_manager.get_prompt_names()
    st.session_state.selected_prompt = prompts[0] if prompts else "ברירת מחדל"

# ============================================
# SIDEBAR
# ============================================

with st.sidebar:
    st.markdown(f"# {APP_ICON} {APP_TITLE}")
    st.markdown(f"<p style='color: #5f6368; font-size: 14px;'>גרסה {VERSION}</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigation
    if st.button("📹 ניתוח וידאו", use_container_width=True, key="nav_analyze"):
        st.session_state.page = 'analyze'
        st.rerun()
    
    if st.button("📝 ניהול פרומפטים", use_container_width=True, key="nav_prompts"):
        st.session_state.page = 'prompts'
        st.rerun()
    
    if st.button("📱 שליחת WhatsApp", use_container_width=True, key="nav_whatsapp"):
        st.session_state.page = 'whatsapp'
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📊 מידע מהיר")
    
    prompts_count = len(prompt_manager.get_prompt_names())
    st.metric("פרומפטים שמורים", prompts_count)

# ============================================
# PAGE: VIDEO ANALYSIS
# ============================================

if st.session_state.page == 'analyze':
    st.title("📹 ניתוח וידאו עם AI")
    
    st.markdown("""
    <div class='simple-card'>
        <p>העלה סרטון לניתוח מקצועי עם Gemini 2.5 Flash</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Prompt selection
    st.markdown("### 📝 בחר פרומפט לניתוח")
    
    prompt_names = prompt_manager.get_prompt_names()
    
    selected_prompt_name = st.selectbox(
        "פרומפט:",
        options=prompt_names,
        index=prompt_names.index(st.session_state.selected_prompt) if st.session_state.selected_prompt in prompt_names else 0,
        key="prompt_selector"
    )
    
    st.session_state.selected_prompt = selected_prompt_name
    
    # Show prompt content in expander
    with st.expander("👁️ צפה בתוכן הפרומפט"):
        current_prompt = prompt_manager.get_prompt(selected_prompt_name)
        st.code(current_prompt, language="text")
    
    st.markdown("---")
    
    # File uploader
    st.markdown("### 📤 העלאת וידאו")
    
    uploaded_file = st.file_uploader(
        "גרור קובץ או לחץ לבחירה",
        type=['mp4', 'avi', 'mov', 'mkv', 'webm'],
        help=f"גודל מקסימלי: {MAX_VIDEO_SIZE_MB}MB"
    )
    
    if uploaded_file:
        # Save file
        video_path = UPLOADS_DIR / uploaded_file.name
        with open(video_path, 'wb') as f:
            f.write(uploaded_file.read())
        
        # Display video
        st.video(str(video_path))
        
        st.markdown("---")
        
        # Analyze button
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if st.button("🤖 התחל ניתוח", type="primary", use_container_width=True, key="analyze_btn"):
                with st.spinner(""):
                    # Progress bar
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    # Simulate progress
                    for i in range(30):
                        progress_bar.progress(i + 1)
                        status_text.text(f"מעלה וידאו... {i+1}%")
                        time.sleep(0.02)
                    
                    try:
                        # Import Gemini
                        import google.generativeai as genai
                        
                        # Configure API
                        genai.configure(api_key=GEMINI_API_KEY)
                        
                        # Upload video
                        status_text.text("מעלה וידאו ל-Gemini...")
                        video_file = genai.upload_file(str(video_path))
                        
                        for i in range(30, 60):
                            progress_bar.progress(i + 1)
                            status_text.text(f"מעבד וידאו... {i+1}%")
                            time.sleep(0.02)
                        
                        # Wait for processing
                        while video_file.state.name == "PROCESSING":
                            time.sleep(1)
                            video_file = genai.get_file(video_file.name)
                        
                        # Get the selected prompt
                        analysis_prompt = prompt_manager.get_prompt(selected_prompt_name)
                        
                        # Add current time and camera source to prompt
                        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
                        camera_source = f"קובץ: {uploaded_file.name}"
                        
                        full_prompt = analysis_prompt.replace("{current_time}", current_time)
                        full_prompt = full_prompt.replace("{camera_source}", camera_source)
                        
                        # Create model
                        model = genai.GenerativeModel(GEMINI_MODEL)
                        
                        # Analyze
                        status_text.text("מנתח עם AI...")
                        for i in range(60, 95):
                            progress_bar.progress(i + 1)
                            time.sleep(0.03)
                        
                        response = model.generate_content([video_file, full_prompt])
                        
                        progress_bar.progress(100)
                        status_text.text("הושלם!")
                        
                        # Save result
                        st.session_state.analysis_result = response.text
                        
                        # Clean up
                        genai.delete_file(video_file.name)
                        
                        st.success("✅ הניתוח הושלם בהצלחה!")
                        time.sleep(1)
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f"❌ שגיאה בניתוח: {e}")
                        st.info("ודא שה-API Key תקין ושהוידאו תקין")
        
        # Display result
        if st.session_state.analysis_result:
            st.markdown("---")
            st.markdown("### 📊 תוצאות הניתוח")
            
            # Display in card
            st.markdown(f"""
            <div class='simple-card' style='max-width: 100%; text-align: right; white-space: pre-wrap;'>
{st.session_state.analysis_result}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Action buttons
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("📄 הורד טקסט", use_container_width=True):
                    st.download_button(
                        "⬇️ הורד קובץ",
                        st.session_state.analysis_result,
                        file_name=f"analysis_{int(time.time())}.txt",
                        use_container_width=True
                    )
            
            with col2:
                if st.button("📋 העתק", use_container_width=True):
                    st.code(st.session_state.analysis_result)
            
            with col3:
                if st.button("📱 שלח WhatsApp", use_container_width=True):
                    st.session_state.page = 'whatsapp'
                    st.rerun()

# ============================================
# PAGE: PROMPT MANAGEMENT
# ============================================

elif st.session_state.page == 'prompts':
    st.title("📝 ניהול פרומפטים")
    
    st.markdown("""
    <div class='simple-card'>
        <p>נהל את הפרומפטים שלך - העלה, שמור, ומחק</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for different operations
    tab1, tab2, tab3 = st.tabs(["📋 פרומפטים קיימים", "➕ הוסף חדש", "📁 ייבא מקובץ"])
    
    with tab1:
        st.markdown("### 📋 פרומפטים שמורים")
        
        prompt_names = prompt_manager.get_prompt_names()
        
        if not prompt_names:
            st.info("אין פרומפטים שמורים")
        else:
            for name in prompt_names:
                with st.expander(f"📄 {name}"):
                    content = prompt_manager.get_prompt(name)
                    
                    # Show content
                    st.text_area(
                        "תוכן:",
                        value=content,
                        height=200,
                        key=f"view_{name}",
                        disabled=True
                    )
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        if st.button("📥 ייצא", key=f"export_{name}", use_container_width=True):
                            st.download_button(
                                "⬇️ הורד קובץ",
                                content,
                                file_name=f"{name}.txt",
                                key=f"download_{name}",
                                use_container_width=True
                            )
                    
                    with col2:
                        if len(prompt_names) > 1:  # Don't allow delete if it's the last one
                            if st.button("🗑️ מחק", key=f"delete_{name}", use_container_width=True):
                                if prompt_manager.delete_prompt(name):
                                    st.success(f"הפרומפט '{name}' נמחק")
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.error("לא ניתן למחוק - חייב להישאר פרומפט אחד לפחות")
    
    with tab2:
        st.markdown("### ➕ יצירת פרומפט חדש")
        
        new_name = st.text_input(
            "שם הפרומפט:",
            placeholder="לדוגמה: ניתוח מקוצר",
            key="new_prompt_name"
        )
        
        new_content = st.text_area(
            "תוכן הפרומפט (באנגלית):",
            height=300,
            placeholder="You are an expert...",
            key="new_prompt_content"
        )
        
        if st.button("💾 שמור פרומפט", type="primary", use_container_width=True):
            if new_name and new_content:
                prompt_manager.save_prompt(new_name, new_content)
                st.success(f"✅ הפרומפט '{new_name}' נשמר!")
                time.sleep(1)
                st.rerun()
            else:
                st.warning("אנא מלא שם ותוכן")
    
    with tab3:
        st.markdown("### 📁 ייבוא פרומפט מקובץ")
        
        import_name = st.text_input(
            "שם לפרומפט המיובא:",
            placeholder="לדוגמה: פרומפט מיובא",
            key="import_name"
        )
        
        uploaded_prompt = st.file_uploader(
            "בחר קובץ TXT",
            type=['txt'],
            key="prompt_uploader"
        )
        
        if uploaded_prompt and import_name:
            if st.button("📥 ייבא ושמור", type="primary", use_container_width=True):
                content = uploaded_prompt.read()
                success, message = prompt_manager.import_from_file(content, import_name)
                
                if success:
                    st.success(f"✅ {message}")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error(message)

# ============================================
# PAGE: WHATSAPP
# ============================================

elif st.session_state.page == 'whatsapp':
    st.title("📱 שליחת WhatsApp")
    
    st.markdown("""
    <div class='simple-card'>
        <p>שלח את תוצאות הניתוח ב-WhatsApp</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Phone number
    phone = st.text_input(
        "מספר טלפון (פורמט: 972501234567)",
        value=DEFAULT_PHONE,
        help="ללא + או -"
    )
    
    # Message
    if st.session_state.analysis_result:
        message = st.text_area(
            "הודעה:",
            value=st.session_state.analysis_result,
            height=400
        )
    else:
        message = st.text_area(
            "הודעה:",
            value="שלום מעין-צופיה Pro",
            height=400
        )
    
    # Send button
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("📤 שלח הודעה", type="primary", use_container_width=True):
            try:
                import pywhatkit
                
                phone_clean = phone.replace("+", "").replace("-", "").replace(" ", "")
                
                with st.spinner("שולח..."):
                    pywhatkit.sendwhatmsg_instantly(
                        f"+{phone_clean}",
                        message,
                        wait_time=10,
                        tab_close=True
                    )
                    
                    st.success("✅ ההודעה נשלחה!")
                    
            except Exception as e:
                st.error(f"❌ שגיאה: {e}")
                st.info("ודא ש-WhatsApp Web מחובר בדפדפן")

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #5f6368; font-size: 13px; padding: 15px;'>
    <p>עין-צופיה Pro v{} • Powered by Gemini 2.5 Flash</p>
    <p style='margin-top: 5px;'>www.gan-gah.com</p>
</div>
""".format(VERSION), unsafe_allow_html=True)
