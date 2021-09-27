# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# For more information, please refer to https://aka.ms/vscode-docker-python-user-rights`
EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Sets a default directory where the application is going to be installed (root/app)
WORKDIR /app

# Copy all files from my computer folder to the workdir
COPY . /app

# Install pip requirements
RUN python -m pip install -r requirements.txt 

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "users.app:app"]
# 0.0.0.0 is for all interfaces
