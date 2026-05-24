# oneCompare Backend Deployment Guide

Use Python 3.12 for deployment. The included `runtime.txt` pins Render-compatible Python to `python-3.12.8`.

## MongoDB Atlas

1. Create a MongoDB Atlas project and cluster.
2. Create a database user with read/write access.
3. Add your Render or Railway outbound IPs to Network Access. For student demos, `0.0.0.0/0` works, but avoid it for production.
4. Copy the connection string and set `MONGODB_URI`.

## Render

1. Create a new Web Service.
2. Connect this repository.
3. Set the root directory to `backend`.
4. Build command:

```bash
pip install -r requirements.txt
```

5. Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

6. Add environment variables:

```env
MONGODB_URI=your-atlas-uri
MONGODB_DB_NAME=onecompare
GEMINI_API_KEY=your-gemini-key
BACKEND_CORS_ORIGINS=https://your-nextjs-app.vercel.app
```

## Railway

1. Create a Railway project.
2. Add a service from GitHub.
3. Set the service directory to `backend`.
4. Add the same environment variables.
5. Railway usually detects Python automatically. If needed, set the start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## Maintenance Checklist

- Rotate database passwords every semester or release cycle.
- Keep `MONGODB_URI`, `GEMINI_API_KEY`, and Firebase keys out of Git.
- Check API logs weekly for repeated 4xx or 5xx errors.
- Run tests before deployment:

```bash
pytest
```
