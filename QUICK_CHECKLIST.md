# ✅ רשימת בדיקה מהירה - PythonAnywhere

## 📋 לפני שמתחילים

- [ ] יש לך חשבון PythonAnywhere (free account)
- [ ] המייל אומת
- [ ] הורדת את ein_tzofia_v3_final.zip

---

## 🚀 תהליך ההעלאה (20 דקות)

### שלב 1: העלאת קבצים (5 דקות)
- [ ] פתחת את לשונית **Files**
- [ ] העלאת את `ein_tzofia_v3_final.zip`
- [ ] פתחת **Bash console**
- [ ] הרצת: `cd ~ && unzip ein_tzofia_v3_final.zip`
- [ ] בדקת שהקבצים קיימים: `ls -la ein_tzofia_v3`

### שלב 2: התקנת תלויות (3 דקות)
- [ ] הרצת: `cd ~/ein_tzofia_v3`
- [ ] הרצת: `pip3.10 install --user streamlit google-generativeai pywhatkit pillow`
- [ ] ראית "Successfully installed..."

### שלב 3: יצירת Web App (5 דקות)
- [ ] פתחת את לשונית **Web**
- [ ] לחצת **"Add a new web app"**
- [ ] בחרת **"Manual configuration"**
- [ ] בחרת **"Python 3.10"**
- [ ] סיימת את האשף

### שלב 4: הגדרת WSGI (7 דקות)
- [ ] פתחת את קובץ ה-WSGI (קישור כחול)
- [ ] מחקת את כל התוכן הישן
- [ ] הדבקת את הקוד מ-`wsgi_file.py`
- [ ] **החלפת `YOUR_USERNAME` בשם המשתמש האמיתי שלך!**
- [ ] שמרת (Save)
- [ ] חזרת ללשונית Web
- [ ] עדכנת **Source code:** `/home/YOUR_USERNAME/ein_tzofia_v3`
- [ ] עדכנת **Working directory:** `/home/YOUR_USERNAME/ein_tzofia_v3`

### שלב 5: Reload והפעלה (2 דקות)
- [ ] לחצת על הכפתור הירוק **"Reload"**
- [ ] המתנת 15 שניות
- [ ] פתחת את `http://YOUR_USERNAME.pythonanywhere.com`
- [ ] **רואה את עין-צופיה Pro!** 🎉

---

## 🧪 בדיקות

### בדיקה 1: האתר טוען
- [ ] `http://YOUR_USERNAME.pythonanywhere.com` פותח
- [ ] רואה "עין-צופיה Pro"
- [ ] רואה "📹 ניתוח וידאו"

### בדיקה 2: העלאת וידאו
- [ ] אפשר להעלות וידאו
- [ ] רואה את הוידאו
- [ ] הפרומפטים מופיעים ברשימה

### בדיקה 3: ניתוח עובד
- [ ] הניתוח מתחיל
- [ ] רואה progress bar
- [ ] מקבל תוצאות בעברית

---

## 🔧 פתרון בעיות

### אם לא עובד:
- [ ] בדקת Error log (Web → Log files → Error log)
- [ ] בדקת Console output
- [ ] ודאת ש-USERNAME הוחלף בקובץ WSGI
- [ ] נסית Reload שוב
- [ ] רעננת דפדפן (Ctrl+F5)

### אם עדיין לא עובד:
- [ ] נסה את הפתרון החלופי ב-`PYTHONANYWHERE_GUIDE.md`
- [ ] פתח Bash console והרץ: `cd ~/ein_tzofia_v3 && streamlit run app.py --server.port=8000`

---

## 📱 הטמעה ב-Wix

### לאחר שהמערכת עובדת:
- [ ] פתחת עורך Wix
- [ ] הוספת HTML iframe
- [ ] הדבקת:
```html
<iframe 
  src="http://YOUR_USERNAME.pythonanywhere.com" 
  width="100%" 
  height="900px" 
  frameborder="0">
</iframe>
```
- [ ] פרסמת את האתר
- [ ] בדקת שהמערכת עובדת בתוך Wix

---

## ✅ סיום

- [ ] המערכת עובדת ב-PythonAnywhere
- [ ] המערכת מוטמעת ב-Wix
- [ ] בדקת על מובייל
- [ ] בדקת על דסקטופ
- [ ] **הכל עובד!** 🎉

---

## 💡 זכור:

**חשבון Free של PythonAnywhere:**
- ✅ חינמי לתמיד
- ⚠️ 100 שניות CPU ליום
- ⚠️ המערכת "נרדמת" אחרי 3 חודשים ללא כניסה
- ⚠️ לא custom domain (רק ב-$5/חודש)

**אבל זה מספיק כדי להתחיל!** 🚀

---

📧 **צריך עזרה?** תשלח screenshot של השגיאה!
