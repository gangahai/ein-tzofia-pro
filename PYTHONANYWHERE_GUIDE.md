# 🚀 מדריך העלאה ל-PythonAnywhere - צעד אחר צעד

## ✅ אתה כבר כאן! עכשיו בואו נתחיל

---

## 📋 **שלב 1: העלאת הקבצים (5 דקות)**

### 1.1 פתח את לשונית Files
1. בתפריט העליון, לחץ על **"Files"**
2. אתה אמור לראות: `/home/YOUR_USERNAME/`

### 1.2 העלה את ה-ZIP
1. גלול למטה עד **"Upload a file"**
2. לחץ **"Choose File"**
3. בחר את `ein_tzofia_v3_final.zip`
4. לחץ **"Upload"**
5. המתן עד שהעלאה תסתיים (יופיע בסטטוס)

### 1.3 חלץ את הקבצים
1. בתפריט העליון, לחץ על **"Consoles"**
2. תחת **"Start a new console"**, לחץ **"$ Bash"**
3. בconsole, הקלד:

```bash
cd ~
unzip ein_tzofia_v3_final.zip
ls -la ein_tzofia_v3
```

4. אתה אמור לראות את כל הקבצים!

---

## 🐍 **שלב 2: התקנת תלויות (3 דקות)**

### באותו Bash console, הרץ:

```bash
cd ~/ein_tzofia_v3
pip3.10 install --user streamlit google-generativeai pywhatkit pillow
```

### המתן עד שההתקנה תסתיים (1-2 דקות)

אתה אמור לראות:
```
Successfully installed streamlit-1.40.0
Successfully installed google-generativeai-0.8.3
...
```

---

## 🌐 **שלב 3: יצירת Web App (5 דקות)**

### 3.1 פתח את לשונית Web
1. בתפריט העליון, לחץ **"Web"**
2. לחץ **"Add a new web app"**

### 3.2 הגדרות ראשוניות
1. **Your web app's domain:** תראה משהו כמו `YOUR_USERNAME.pythonanywhere.com`
2. לחץ **"Next"**

### 3.3 בחר Framework
1. בחר **"Manual configuration"** (לא Flask, לא Django!)
2. לחץ **"Next"**

### 3.4 בחר Python Version
1. בחר **"Python 3.10"**
2. לחץ **"Next"**

### 3.5 סיים
לחץ **"Done"** או **"Finish"**

---

## ⚙️ **שלב 4: הגדרת WSGI (הכי חשוב! 7 דקות)**

### 4.1 מצא את קובץ WSGI
בעמוד Web, גלול למטה עד שתמצא:
```
Code:
    Source code: /home/YOUR_USERNAME
    Working directory: /home/YOUR_USERNAME
    WSGI configuration file: /var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py
```

### 4.2 ערוך את קובץ WSGI
1. לחץ על הקישור **WSGI configuration file** (הכחול)
2. זה יפתח עורך טקסט

### 4.3 מחק הכל והדבק את זה:

```python
import sys
import os

# ============================================
# IMPORTANT: Replace YOUR_USERNAME with your actual username!
# ============================================
USERNAME = 'YOUR_USERNAME'  # <-- CHANGE THIS TO YOUR ACTUAL USERNAME!

# Add project directory to Python path
project_folder = f'/home/{USERNAME}/ein_tzofia_v3'
if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

os.chdir(project_folder)

# Streamlit environment variables
os.environ['STREAMLIT_SERVER_PORT'] = '8000'
os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'

# Import app
def application(environ, start_response):
    """WSGI application"""
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/html'),
        ('X-Frame-Options', 'ALLOWALL'),  # Allow embedding in Wix
    ]
    start_response(status, response_headers)
    
    # Redirect to Streamlit port
    html = f'''
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url=http://{environ['HTTP_HOST'].replace(':80', ':8000')}" />
        <title>עין-צופיה Pro</title>
    </head>
    <body>
        <h2>מפנה לעין-צופיה Pro...</h2>
        <p>אם אתה לא מועבר אוטומטית, <a href="http://{environ['HTTP_HOST'].replace(':80', ':8000')}">לחץ כאן</a></p>
    </body>
    </html>
    '''
    return [html.encode('utf-8')]
```

### 4.4 **חשוב מאוד!**
החלף `YOUR_USERNAME` בשם המשתמש שלך!

למשל, אם המשתמש שלך הוא `aharonnais`, שנה ל:
```python
USERNAME = 'aharonnais'
```

### 4.5 שמור
לחץ **"Save"** למעלה מימין

---

## 🔧 **שלב 5: הגדרות נוספות**

### 5.1 חזור ללשונית Web

### 5.2 עדכן Directories
גלול ל-**"Code"** ומלא:

**Source code:**
```
/home/YOUR_USERNAME/ein_tzofia_v3
```

**Working directory:**
```
/home/YOUR_USERNAME/ein_tzofia_v3
```

(החלף YOUR_USERNAME בשם שלך!)

### 5.3 הוסף Static Files (אופציונלי)
תחת **"Static files"**, לחץ **"Enter path"**:

**URL:** `/static`
**Directory:** `/home/YOUR_USERNAME/ein_tzofia_v3/data`

---

## 🚀 **שלב 6: Reload והפעלה!**

### 6.1 גלול למעלה
בחלק העליון של עמוד Web, תראה כפתור ירוק גדול:

### 6.2 לחץ:
```
🔄 Reload YOUR_USERNAME.pythonanywhere.com
```

### 6.3 המתן 10-15 שניות

### 6.4 בדוק!
לחץ על הקישור:
```
http://YOUR_USERNAME.pythonanywhere.com
```

---

## ⚠️ **אם זה לא עובד...**

### בעיה 1: שגיאת 500
**פתרון:**
1. לך ל-**Web** → **Log files**
2. לחץ **"Error log"**
3. תראה את השגיאה
4. ככל הנראה שכחת להחליף `YOUR_USERNAME`

### בעיה 2: "Site not found"
**פתרון:**
1. ודא שלחצת **Reload**
2. נסה לרענן (Ctrl+F5)
3. נסה דפדפן אחר

### בעיה 3: Streamlit לא טוען
**פתרון:**
נסה את הפתרון החלופי:

---

## 🔄 **פתרון חלופי: הרצת Streamlit ישירות**

אם ה-WSGI לא עובד, נשתמש בשיטה אחרת:

### שלב 1: צור קובץ start.sh
1. **Files** → `/home/YOUR_USERNAME/ein_tzofia_v3`
2. צור קובץ חדש: `start.sh`
3. הדבק:

```bash
#!/bin/bash
cd ~/ein_tzofia_v3
streamlit run app.py --server.port=8000 --server.address=0.0.0.0
```

4. שמור

### שלב 2: הרץ ב-Console
1. פתח **Bash console**
2. הרץ:

```bash
cd ~/ein_tzofia_v3
chmod +x start.sh
./start.sh
```

### שלב 3: השאר את הConsole פתוח
**חשוב:** אל תסגור את הconsole! השאר אותו רץ.

עכשיו גש ל:
```
http://YOUR_USERNAME.pythonanywhere.com:8000
```

---

## 🎯 **הטמעה ב-Wix**

ברגע שהמערכת עובדת, חזור ל-Wix והדבק:

```html
<iframe 
  src="http://YOUR_USERNAME.pythonanywhere.com" 
  width="100%" 
  height="900px" 
  frameborder="0"
  style="border: none; border-radius: 8px;">
</iframe>
```

---

## 💡 **טיפים חשובים:**

1. **PythonAnywhere Free הגבלות:**
   - CPU: 100 שניות ליום
   - אם עובר, תקבל הודעה
   - פתרון: Upgrade ל-$5/חודש

2. **המערכת "נרדמת":**
   - אחרי 3 חודשים ללא כניסה
   - פתרון: היכנס פעם בחודש

3. **Custom Domain:**
   - דורש Upgrade ($5/חודש)
   - אבל שווה אם רוצה `ein-tzofia.gan-gah.com`

---

## ✅ **סיימת!**

אם הכל עבד, אתה אמור לראות:

```
👁️ עין-צופיה Pro
📹 ניתוח וידאו
[העלה וידאו]
```

**מזל טוב! המערכת חיה! 🎉**

---

## 🆘 **צריך עזרה?**

אם משהו לא עובד, תשלח לי screenshot של:
1. Error log מה-Web tab
2. Console output
3. מה שאתה רואה בדפדפן

ואני אעזור לתקן! 😊
