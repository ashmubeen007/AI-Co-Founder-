# Use a lightweight Python version
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy your requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your frontend and backend files into the container
COPY . .

# Expose the port Hugging Face needs
EXPOSE 7860

# Run FastAPI in the background and Streamlit in the foreground
CMD ["bash", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/app.py --server.port 7860 --server.address 0.0.0.0"]