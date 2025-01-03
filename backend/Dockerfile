# the following is for demonstrating multistage builds
# stage 1
FROM python:3.12-slim As builder
WORKDIR /app

# ???
COPY pyproject.toml requirements.txt ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels -r requirements.txt

COPY src src
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels .

# stage 2
FROM python:3.12-slim AS runner

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/* && rm -rf /wheels

EXPOSE 8000

CMD [ "uvicorn", "mysite.main:app", "--host", "0.0.0.0", "--port", "8000" ]





### the following is for building single stage only upon the frontend/ host workdir
# FROM python:3.12-slim

# WORKDIR /app

# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r /app/requirements.txt

# COPY src/mysite mysite

# # not for publishing port, but just for human readibility between the user who build image and the user who run the image
# EXPOSE 8000

# # specify the default command that will be used if none is supplied when run the container
# # will be executed using /bin/sh
# CMD ["uvicorn", "mysite.main:app", "--host", "0.0.0.0", "--port", "8000"]