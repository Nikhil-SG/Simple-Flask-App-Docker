# from python:3.10-slim 
# workdir /app
# copy requirements.txt ./
# run pip install -r requirements.txt 
# copy app.py ./
# expose 5070
# cmd ["python3","app.py"]
# # Use official Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file first (for better caching)
COPY requirements.txt ./

# Install Python dependencies
RUN pip3.10 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py ./

# Expose the port your Flask app listens on
EXPOSE 5070

# Run the app
CMD ["python3", "app.py"]
