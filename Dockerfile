FROM python:3.10

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY app/ .

# Use ddtrace-run to enable auto-instrumentation
CMD ["ddtrace-run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
