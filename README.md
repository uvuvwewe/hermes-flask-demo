# hermes-flask-demo

A minimal Flask application with two routes.

## Routes

| Route  | Response                          |
|--------|-----------------------------------|
| `/`    | `Hello, World!` (plain text)      |
| `/news`| JSON greeting `{"message": ..., "status": "ok"}` |

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

The app starts on `http://localhost:5000` by default.

## Run with Docker

```bash
docker build -t hermes-flask-demo .
docker run -p 5000:5000 hermes-flask-demo
```
