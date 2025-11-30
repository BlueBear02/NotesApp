# NotesApp

Simple backend for a notes app (fastapi + sqlite)

**Frontend:** https://github.com/BlueBear02/NotepadApp

## Setup

### 1. Create `.env` file with your API key

**Windows:**
```cmd
echo API_KEY=your_secret_key_here > .env
```

**Linux/Mac:**
```bash
echo "API_KEY=your_secret_key_here" > .env
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### API Documentation

- Swagger UI: `http://127.0.0.1:8000/docs`

All requests require `X-API-Key` header with your secret key.
