# 🚀 AI Code Review Assistant (Phase 2: Security & Performance Analysis)

This phase introduces **security vulnerability detection and performance optimization analysis**.

## **🎯 Features**
✔ **All Phase 1 Features** (AI Code Review, GitHub OAuth, PostgreSQL, Django REST API)  
✔ **NEW: AI-Powered Security Analysis** – Detects potential security flaws in the code  
✔ **NEW: Performance Optimization Suggestions** – AI-based performance insights  
✔ **Refactored API** – Handles security & performance reviews  

---

## **🛠 Setup Instructions**
_(Same as Phase 1, with additional security & performance endpoints)_

### **1️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **2️⃣ Configure `.env` File**
Add:
```ini
OPENAI_API_KEY=your-openai-api-key
```

### **3️⃣ Run the Backend & Frontend**
```sh
python manage.py migrate
python manage.py runserver
```

---

## **💡 Tech Stack**
- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Frontend:** HTML, Tailwind CSS, JavaScript  
- **AI Integration:** OpenAI API (GPT-4)  
- **Security Analysis:** AI-powered security scanning  

---

## **📜 License**
MIT License © 2024 Geoff Gibson
