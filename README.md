# 🔐 Password Strength Checker (Web App)

An interactive and responsive web-based application built using **Flask (Python)** and **HTML/CSS/JS**, which evaluates password strength in real-time and suggests secure passwords.

---

## 💡 Features

- ✅ Real-time password strength analysis
- ✅ Password strength bar and tips
- ✅ Strong password suggestion generator
- ✅ Clean and responsive UI with custom styling
- ✅ Flask backend with API endpoints

---

## 🧪 Password Strength Criteria

The app checks for:
- Minimum **8 characters**
- Presence of **uppercase letters**
- Presence of **numbers**
- Presence of **special characters**

Strength is shown on a visual bar with improvement tips.

---

## 🛠️ Tech Stack

| Frontend | Backend |
|----------|---------|
| HTML5, CSS3, JavaScript | Python (Flask) |

Additional:
- FontAwesome Icons
- Google Fonts (Poppins)
- Flask `render_template`, `jsonify`, etc.

---

## 📂 Folder Structure

Password/
├── app.py # Flask backend
├── frontend.html # Main web UI
├── practice.html # Alternate design version
├── static/
│ ├── background.jpg # Background image
│ ├── logo.png # Logo for branding
│ ├── styles.css # (if separated later)
│ └── script.js # (optional JS if modularized)


---

## 🎮 How to Run Locally

1. **Install Python & Flask**
   ```bash
   pip install flask
Run the app

bash
python app.py
Open your browser

http://127.0.0.1:5000/

ScreenShot
[Home page]
![Screenshot 2025-06-30 123825](https://github.com/user-attachments/assets/1627da31-b29c-420b-a06b-462ab6e642f9)

[Home Page with the Strength Checking box]
![Screenshot 2025-06-30 123842](https://github.com/user-attachments/assets/576bfa30-187b-4a99-b5d4-d134ef29a527)

[Home Page with About Company]
![Screenshot 2025-06-30 123856](https://github.com/user-attachments/assets/15e013c9-9adc-44bf-b0cc-4ff66215e6a7)

[Strength Checking box with One Condition = true]
![Screenshot 2025-06-30 123920](https://github.com/user-attachments/assets/d40bc628-4cc4-4f3f-aa16-6618830245eb)

[Strength Container with two conditions = true]
![Screenshot 2025-06-30 124017](https://github.com/user-attachments/assets/ac9b0f75-5742-415c-ae19-ec2778bdbe81)

[Strength Box with ALL conditions =true]
![Screenshot 2025-06-30 124045](https://github.com/user-attachments/assets/69f11eee-7bf0-4f1f-84f8-25aa2e4ba335)

[Strength Box Suggesting STrong password]
![Screenshot 2025-06-30 124058](https://github.com/user-attachments/assets/625e57ba-5541-4444-a4cf-d64c0c06587c)

[Background turned to 'Dark Mode' when toggle pressed-1]
![Screenshot 2025-06-30 124123](https://github.com/user-attachments/assets/9e2cccdc-274e-4da8-b96f-bc88018d84a6)

[Background turned to 'Dark Mode' when toggle pressed-2]
![Screenshot 2025-06-30 124135](https://github.com/user-attachments/assets/7b4aa6a9-42fa-4c52-ab54-dd5ce9f4fa20)


📜 License
This project is open-source and free to use under the MIT License.

yaml
Copy
Edit

---

## ✅ What To Do Now:
1. Create a file in your folder:  
   `Password/README.md`

2. Paste the content above in it

3. Commit and push to GitHub:
```bash
git add README.md
git commit -m "Added custom README"
git push
