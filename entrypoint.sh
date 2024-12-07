#!/bin/sh
./wait-for-it.sh db:3306 --timeout=60 --strict -- echo "MySQL is up"
# python3 manage.py makemigrations
python manage.py clear_cache  # If using Django cache system

python3 manage.py makemigrations
# Gere as migrações para o modelo de usuários
python manage.py makemigrations accounts

# python3 manage.py migrate --noinput
# python3 manage.py migrate && python manage.py createsuperuser --noinput || true
# Executar as migrações do banco de dados
echo "Executando migrações..."
python3 manage.py makemigrations
python3 manage.py migrate

# Criar o superusuário automaticamente, se não existir
echo "Criando superusuário..."
echo "Verificando se o superusuário existe..."
python manage.py shell -c "
from django.contrib.auth import get_user_model;
from django.core.exceptions import ObjectDoesNotExist;

User = get_user_model()

try:
    # Tentando buscar o superusuário pelo email
    User.objects.get(email='$DJANGO_SUPERUSER_EMAIL')
    print('Superusuário já existe.')
except ObjectDoesNotExist:
    # Se o superusuário não existir, criar um novo
    User.objects.create_superuser(
        email='$DJANGO_SUPERUSER_EMAIL',
        password='$DJANGO_SUPERUSER_PASSWORD'
    )
    print('Superusuário criado.')
"

# python3 manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL

# # Definir a senha do superusuário com a variável de ambiente
# echo "Definindo a senha do superusuário..."
# python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(email='$DJANGO_SUPERUSER_EMAIL'); user.set_password('$DJANGO_SUPERUSER_PASSWORD'); user.save()"


# python3 manage.py runserver 0.0.0.0:8000
bash -c "gunicorn backend.wsgi:application -b 0.0.0.0:8000"

# ./wait-for-it.sh -t 10 db:3306 && python manage.py runserver 0.0.0.0:8000

