FROM python:3.12
# FROM python:3.13.0-alpine3.20
LABEL author="hirowat2"
LABEL project="djangotemplate"

ARG GITHUB_PAT=${GITHUB_PAT}

# Configure as variáveis de ambiente para o R
ENV GITHUB_PAT=${GITHUB_PAT}
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1
ENV RPY2_CFFI_MODE=ABI
ENV PYTHONPATH="/app:${PYTHONPATH}"

RUN mkdir /app
WORKDIR /app
EXPOSE 8000

RUN pip install --upgrade pip
RUN [ "pip", "install", "--no-cache-dir", "poetry==1.8.4" ]

COPY poetry.lock .
COPY pyproject.toml .

RUN [ "poetry", "config", "virtualenvs.create", "false"]
RUN [ "poetry", "install", "--no-root", "--no-interaction", "--no-ansi"]

COPY manage.py .
COPY backend backend

COPY . .

COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

EXPOSE 80

CMD python manage.py collectstatic --no-input
ENTRYPOINT [ "./entrypoint.sh" ]
