# 👁️ עין-צופיה Pro v3.0

## מערכת ניתוח וידאו מבוססת Gemini 2.5 Flash

---

## ✨ מה חדש בגרסה 3.0

### 🚀 Gemini 2.5 Flash Integration
- ניתוח וידאו **ישיר** (לא צריך frames)
- **מהיר פי-10** מהגרסה הקודמת
- **מדויק יותר** - רואה את כל הוידאו

### 📝 מערכת פרומפטים מלאה
- העלאת פרומפטים מקובץ TXT
- שמירה עם שם מותאם אישית
- רשימה נפתחת לבחירה מהירה
- עריכה ומחיקה של פרומפטים
- פרומפטים **באנגלית**, תוצאות **בעברית**

### 🎨 עיצוב מינימליסטי
- קופסאות **50% רוחב**
- ממוקם **במרכז המסך**
- נקי ופשוט

---

## 🚀 התקנה מקומית (בדיקה)

### שלב 1: הורד והתקן
```bash
# הורד את התיקייה
# חלץ אותה

# הרץ
RUN.bat
```

### שלב 2: בדוק שהכל עובד
1. עלה וידאו
2. בחר פרומפט
3. נתח
4. בדוק תוצאות

---

## 🌐 פרסום לאינטרנט (Streamlit Cloud)

### שלב 1: הכנה
1. צור חשבון ב-GitHub (אם אין לך)
2. צור repository חדש בשם `ein-tzofia-pro`
3. העלה את כל הקבצים לrepository

### שלב 2: פרסום
1. היכנס ל-**Streamlit Cloud**: https://share.streamlit.io
2. התחבר עם GitHub
3. לחץ "New app"
4. בחר את הrepository שלך
5. בחר `app.py` כקובץ ראשי
6. לחץ "Deploy"

### שלב 3: קבל כתובת
אחרי 2-3 דקות תקבל כתובת:
```
https://ein-tzofia-pro.streamlit.app
```

---

## 📱 הטמעה באתר Wix

### שיטה 1: iframe (מומלץ)

#### שלב 1: בעורך Wix
1. פתח את עורך ה-Wix
2. לחץ **"+ הוסף"** בצד שמאל
3. בחר **"Embed" → "Custom Element"** (או "HTML iframe")

#### שלב 2: הדבק קוד
```html
<iframe 
  src="https://ein-tzofia-pro.streamlit.app" 
  width="100%" 
  height="900" 
  style="border: none; border-radius: 8px;">
</iframe>
```

#### שלב 3: התאם גודל
- רוחב: 100%
- גובה: 900px (או כמה שאתה רוצה)

#### שלב 4: פרסם
לחץ **"פרסם"** והמערכת תופיע באתר!

---

### שיטה 2: Custom Code (מתקדם)

אם אתה רוצה שליטה מלאה:

1. **Wix Editor** → **Settings** → **Custom Code**
2. **Add Custom Code** → **Body - End**
3. הדבק:

```html
<script>
window.addEventListener('load', function() {
  const iframe = document.createElement('iframe');
  iframe.src = 'https://ein-tzofia-pro.streamlit.app';
  iframe.style.width = '100%';
  iframe.style.height = '900px';
  iframe.style.border = 'none';
  iframe.style.borderRadius = '8px';
  
  // Find where to put it
  const container = document.getElementById('your-container-id');
  container.appendChild(iframe);
});
</script>
```

---

## 🎯 איך זה נראה למשתמש

```
┌─────────────────────────────────────┐
│  🌐 www.gan-gah.com                 │
├─────────────────────────────────────┤
│                                     │
│  [תוכן האתר שלך]                    │
│                                     │
│  ┌───────────────────────────────┐  │
│  │ 👁️ עין-צופיה Pro              │  │
│  │                               │  │
│  │ 📹 ניתוח וידאו                │  │
│  │                               │  │
│  │ [העלה וידאו]                  │  │
│  │ [בחר פרומפט]                  │  │
│  │ [התחל ניתוח]                  │  │
│  │                               │  │
│  └───────────────────────────────┘  │
│                                     │
│  [המשך תוכן]                        │
│                                     │
└─────────────────────────────────────┘
```

---

## 📝 שימוש במערכת

### 1. ניתוח וידאו
```
1. בחר פרומפט מהרשימה
2. העלה וידאו (עד 500MB)
3. לחץ "התחל ניתוח"
4. המתן 30-60 שניות
5. קבל תוצאות בעברית
```

### 2. ניהול פרומפטים
```
📋 פרומפטים קיימים:
- צפה בפרומפטים
- ייצא לקובץ
- מחק (אם יש יותר מאחד)

➕ הוסף חדש:
- כתוב שם
- כתוב תוכן (באנגלית)
- שמור

📁 ייבא מקובץ:
- בחר קובץ TXT
- תן שם
- ייבא
```

### 3. שליחת WhatsApp
```
1. הזן מספר (972501234567)
2. ערוך הודעה (אוטומטי מהניתוח)
3. שלח
```

---

## 🔧 הגדרות מתקדמות

### שינוי API Key
ערוך את `config.py`:
```python
GEMINI_API_KEY = "YOUR_NEW_KEY_HERE"
```

### שינוי גודל קופסאות
ערוך את `styles/minimalist_css.py`:
```python
.main .block-container {
    max-width: 800px !important;  # שנה ל-600px או 1000px
}
```

### שינוי מודל Gemini
ערוך את `config.py`:
```python
GEMINI_MODEL = "gemini-2.0-flash-exp"  # או gemini-pro
```

---

## 📊 מפרט טכני

### טכנולוגיות
- **Frontend**: Streamlit 1.40+
- **AI**: Google Gemini 2.5 Flash
- **WhatsApp**: PyWhatKit
- **Storage**: JSON Files

### קבצים
```
ein_tzofia_v3/
├── app.py                 # אפליקציה ראשית
├── config.py              # הגדרות
├── requirements.txt       # תלויות
├── RUN.bat               # הרצה מקומית
├── README.md             # מדריך זה
├── styles/
│   └── minimalist_css.py # עיצוב
├── utils/
│   └── prompt_manager.py # ניהול פרומפטים
└── data/
    ├── uploads/          # וידאו מועלים
    └── prompts/          # פרומפטים שמורים
```

---

## ❓ שאלות ותשובות

### ש: המערכת איטית?
**ת:** לא! Gemini 2.5 Flash מהיר מאוד (20-40 שניות לוידאו).

### ש: כמה זה עולה?
**ת:** 
- Streamlit Cloud: **חינמי**
- Gemini API: **חינמי** עד 1,500 בקשות ליום

### ש: אפשר לשנות עיצוב?
**ת:** כן! ערוך `styles/minimalist_css.py`

### ש: איך מוסיפים פרומפט?
**ת:** לך ל"ניהול פרומפטים" → "הוסף חדש"

### ש: WhatsApp לא עובד?
**ת:** ודא ש-WhatsApp Web מחובר בדפדפן

---

## 🆘 תמיכה

### בעיות נפוצות

#### שגיאת API Key
```
ודא שה-API Key תקין:
https://makersuite.google.com/app/apikey
```

#### וידאו לא נטען
```
פורמטים נתמכים: MP4, AVI, MOV, MKV, WEBM
גודל מקסימלי: 500MB
```

#### פרומפט לא עובד
```
ודא שהפרומפט באנגלית
בדוק שאין תווים מיוחדים
```

---

## 🎉 מוכן!

המערכת שלך מוכנה:
1. ✅ Gemini 2.5 Flash
2. ✅ מערכת פרומפטים
3. ✅ עיצוב 50% רוחב
4. ✅ מוכן להטמעה ב-Wix

**תהנה! 🚀**

---

**גרסה:** 3.0  
**תאריך:** 2025-01-01  
**אתר:** www.gan-gah.com

Made with ❤️ by Ein Tzofia Team
