# DjangoTemplate

## Dica de python

https://www.dicas-de-django.com.br/

## Este projeto foi feito com:

* [Python 3.12](https://www.python.org/)
* [Django 4.1.6](https://www.djangoproject.com/)
* [TailwindCSS](https://tailwindcss.com/)
* [htmx](https://htmx.org)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um arquivo .env conforme infos abaixo


```
DEBUG=True
SECRET_KEY=<gerar um token>
ALLOWED_HOSTS=127.0.0.1,.localhost,0.0.0.0, app.docker.localhost

#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#POSTGRES_DB=
POSTGRES_USER=postgres
# POSTGRES_PASSWORD=E_%ZKM1BkzCxt$DdePv?
POSTGRES_PASSWORD=postgres
#DB_HOST=localhost

DJANGO_SUPERUSER_PASSWORD=estatcamp123
DEFAULT_FROM_EMAIL='from@example.com'
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST = 'mailhog'  # Nome do serviço MailHog no seu Docker Compose
EMAIL_PORT = 1025  # Porta padrão do MailHog
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
```

* Este projeto já cria um superuser automático

### Makefile

Para verifcar os comando disponiveis no Makefile no terminal, basta informar `make help`



