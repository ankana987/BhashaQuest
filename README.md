# BhashaQuest

A React + Vite + FastAPI gamified language-learning MVP. It includes Hindi, English and Bengali, learning worlds, missions, an AI Mentor panel, speech recognition, tolerant evaluation, XP/badges/progress, and light/dark theme support.

## Windows quick start

### 1. Backend
Open PowerShell in the project folder:

```powershell
.\start-backend.bat
```

Keep this terminal open. The API runs at `http://127.0.0.1:8000`.

### 2. Frontend
Open a **second** PowerShell terminal in the project folder:

```powershell
.\start-frontend.bat
```

Open the URL Vite prints, normally `http://localhost:5173`.

> In PowerShell, use `.[31mstart-backend.bat[0m` / `.[31mstart-frontend.bat[0m`, not just the filename.

## Manual setup

### Frontend
```powershell
cd frontend
npm install
npm run dev
```

### Backend
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/d786eb4b-5454-4365-a1a9-bb11f5402fa5" />


## AI Mentor
Copy `backend/.env.example` to `backend/.env` and add your LLM endpoint/key if you want a real AI provider. The app has local fallback behavior when no provider is configured.

Never put an API secret in the React frontend.
