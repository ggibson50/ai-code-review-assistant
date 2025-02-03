# 🚀 AI Code Review Assistant

---

## **🛠 Setup Instructions**

### **1️⃣ Install Dependencies**
Ensure you have **Python 3.8+** and **PostgreSQL** installed.

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/ai-code-review.git
   cd ai-code-review
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

---

### **2️⃣ Configure Environment Variables**
Create a `.env` file in the project root and add the following:

```ini
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=postgres://your_user:your_password@localhost:5432/your_database
OPENAI_API_KEY=your-openai-api-key
GITHUB_ACCESS_TOKEN=your-github-token
```
- Replace **`your-django-secret-key`** OR **`secret`**, **`your-database`**, and **API keys** with real values.

---

### **3️⃣ Set Up the Database**
1. **Apply Migrations**  
   ```sh
   python manage.py migrate
   ```

2. **Create a Superuser (Admin Login)**  
   ```sh
   python manage.py createsuperuser
   ```

---

### **4️⃣ Run the Servers**
#### **📌 Start Django Backend**
```sh
python manage.py runserver
```
The backend API will be available at:  
📍 `http://127.0.0.1:8000/`

#### **📌 Start WebSocket Server for Real-time Collaboration**
```sh
python backend/collaboration.py
```
This runs a WebSocket server on:  
📍 `ws://localhost:6789/`

---

### **5️⃣ Running the Frontend**
Simply open the `frontend/index.html` file in a browser.

OR use a simple HTTP server:
```sh
python -m http.server 8080
```
Then, visit:  
📍 `http://localhost:8080/frontend/index.html`

---

## **🔧 Usage**
1. **Login with GitHub** – Authenticated via OAuth  
2. **Paste Code** – Upload code for AI review  
3. **AI Analysis** – AI detects best practices, security, and performance issues  
4. **Live Collaboration** – Multiple users edit code in real time  
5. **GitHub PR Integration** – AI comments on pull requests  


### **🐳 Docker (Optional)**
For easy deployment, use Docker:

```sh
docker-compose up --build
```
This will spin up:
- PostgreSQL Database  
- Django Backend  
- WebSocket Server  

---

## **💡 Contributing**
Want to improve this project? **Pull requests are welcome!**

---

## **🛠 Tech Stack**
- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Frontend:** HTML, Tailwind CSS, JavaScript  
- **AI Integration:** OpenAI API (GPT-4)  
- **Collaboration:** WebSockets  
- **CI/CD:** GitHub API  

---

## **📜 License**
MIT License © Geoff Gibson
