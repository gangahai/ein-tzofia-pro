"""
עין-צופיה Pro - Prompt Manager
ניהול פרומפטים: שמירה, טעינה, מחיקה
"""

import json
from pathlib import Path
from config import PROMPTS_DIR, DEFAULT_PROMPT

class PromptManager:
    """מנהל פרומפטים"""
    
    def __init__(self):
        self.prompts_file = PROMPTS_DIR / "prompts.json"
        self._ensure_prompts_file()
    
    def _ensure_prompts_file(self):
        """וודא שקובץ הפרומפטים קיים"""
        if not self.prompts_file.exists():
            # Create with default prompt
            default_prompts = {
                "ברירת מחדל - ניתוח מקצועי": DEFAULT_PROMPT
            }
            self.save_all_prompts(default_prompts)
    
    def get_all_prompts(self):
        """קבל את כל הפרומפטים"""
        try:
            with open(self.prompts_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {"ברירת מחדל - ניתוח מקצועי": DEFAULT_PROMPT}
    
    def save_all_prompts(self, prompts_dict):
        """שמור את כל הפרומפטים"""
        with open(self.prompts_file, 'w', encoding='utf-8') as f:
            json.dump(prompts_dict, f, ensure_ascii=False, indent=2)
    
    def save_prompt(self, name, content):
        """שמור פרומפט חדש"""
        prompts = self.get_all_prompts()
        prompts[name] = content
        self.save_all_prompts(prompts)
        return True
    
    def delete_prompt(self, name):
        """מחק פרומפט"""
        prompts = self.get_all_prompts()
        if name in prompts and len(prompts) > 1:  # Don't delete if it's the last one
            del prompts[name]
            self.save_all_prompts(prompts)
            return True
        return False
    
    def get_prompt(self, name):
        """קבל פרומפט לפי שם"""
        prompts = self.get_all_prompts()
        return prompts.get(name, DEFAULT_PROMPT)
    
    def get_prompt_names(self):
        """קבל רשימת שמות פרומפטים"""
        prompts = self.get_all_prompts()
        return list(prompts.keys())
    
    def import_from_file(self, file_content, name):
        """ייבא פרומפט מקובץ"""
        try:
            # Decode if bytes
            if isinstance(file_content, bytes):
                content = file_content.decode('utf-8')
            else:
                content = file_content
            
            # Save with given name
            self.save_prompt(name, content)
            return True, "הפרומפט נשמר בהצלחה"
        except Exception as e:
            return False, f"שגיאה: {e}"
    
    def export_to_file(self, name):
        """ייצא פרומפט לקובץ"""
        content = self.get_prompt(name)
        return content

# Global instance
prompt_manager = PromptManager()
