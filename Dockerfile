# NOTE: Because of the change in the directory structure, and inserting all codebase to "app" directory,
# make sure to change all the import from inside the project to fit to the new path.
# for example: instead of "from core import Database" use "from app.core import Database", etc.

FROM python:3.12-slim
LABEL authors="pplevins & berale"
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY app ./app
COPY data ./data
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]