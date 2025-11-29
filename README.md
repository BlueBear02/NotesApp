# NotesApp

Simple backend for a small notes app (fastapi + sqlite)

## Setup

1. Set your API key in `.env`:
```
API_KEY=your_secret_key_here
```

2. Install and run:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

All requests require `X-API-Key` header with your secret key.
