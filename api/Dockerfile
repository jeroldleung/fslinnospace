FROM python:3.12-slim

WORKDIR /app

COPY ./app ./app

COPY pyproject.toml .

# using uv temporarily
RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    uv pip install --system --no-cache -r pyproject.toml

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
