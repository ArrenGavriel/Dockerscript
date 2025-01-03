FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src/mysite mysite

# not for publishing port, but just for human readibility between the user who build image and the user who run the image
EXPOSE 8000

# specify the default command that will be used if none is supplied when run the container
# will be executed using /bin/sh
CMD ["uvicorn", "mysite.main:app", "--host", "0.0.0.0", "--port", "8000"]