FROM python:3.12.7-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_ENV=production \
    FLASK_APP=wsgi.py

# Create non-root user
RUN useradd --create-home appuser

WORKDIR /home/appuser/app

# Copy only requirements first (leveraging layer cache)
COPY requirements.txt .

# Install into the system Python
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Now copy your app code
COPY . .

USER appuser

EXPOSE 8000

# Call gunicorn via the global install
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app", "--workers", "4", "--worker-class", "sync"]