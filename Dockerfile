# Latin Analyzer Dockerfile
# Uses Python 3.13 for CLTK 2.x compatibility

FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY latin_analyzer.py .
COPY latin_analyzer_cli.py .
COPY setup_models.py .

# Create directory for CLTK data (will be mounted as volume)
RUN mkdir -p /root/cltk_data

# Set environment variable for CLTK data directory
ENV CLTK_DATA_DIR=/root/cltk_data

# Default command: interactive CLI
CMD ["python", "latin_analyzer_cli.py"]
