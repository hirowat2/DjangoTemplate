from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from .forms import ContactForm


@require_http_methods(['POST'])
def send_contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        subject = form.cleaned_data.get('title')
        message = form.cleaned_data.get('body')
        sender = form.cleaned_data.get('email')
        send_mail(
            subject,
            message,
            sender,
            ['localhost'],
            fail_silently=False,
        )
        return redirect('core:index')
 Traceback (most recent call last):
django_app          |   File "/app/manage.py", line 22, in <module>
django_app          |     main()
django_app          |   File "/app/manage.py", line 18, in main
django_app          |     execute_from_command_line(sys.argv)
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
django_app          |     utility.execute()
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/core/management/__init__.py", line 382, in execute
django_app          |     settings.INSTALLED_APPS
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/conf/__init__.py", line 81, in __getattr__
django_app          |     self._setup(name)
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/conf/__init__.py", line 68, in _setup
django_app          |     self._wrapped = Settings(settings_module)
django_app          |                     ^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/conf/__init__.py", line 166, in __init__
django_app          |     mod = importlib.import_module(self.SETTINGS_MODULE)
django_app          |           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
django_app          |     return _bootstrap._gcd_import(name[level:], package, level)
django_app          |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
django_app          |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
django_app          |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
django_app          |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
django_app          |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
django_app          |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
django_app          |   File "/app/backend/settings.py", line 125, in <module>
django_app          |     EMAIL_PORT = config('EMAIL_PORT', 1025, cast=int)
django_app          |                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/decouple.py", line 243, in __call__
django_app          |     return self.config(*args, **kwargs)
django_app          |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/decouple.py", line 105, in __call__
django_app          |     return self.get(*args, **kwargs)
django_app          |            ^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/decouple.py", line 99, in get
django_app          |     return cast(value)
django_app          |            ^^^^^^^^^^^
django_app          | ValueError: invalid literal for int() with base 10: '1025  # Porta padrão do MailHog'
django_app          | [2024-12-09 11:50:58 +0000] [144] [INFO] Starting gunicorn 20.1.0
django_app          | [2024-12-09 11:50:58 +0000] [144] [INFO] Listening at: http://0.0.0.0:8000 (144)
django_app          | [2024-12-09 11:50:58 +0000] [144] [INFO] Using worker: sync
django_app          | [2024-12-09 11:50:58 +0000] [145] [INFO] Booting worker with pid: 145
django_app          | [2024-12-09 11:50:58 +0000] [145] [ERROR] Exception in worker process
django_app          | Traceback (most recent call last):
django_app          |   File "/usr/local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 589, in spawn_worker
django_app          |     worker.init_process()
django_app          |   File "/usr/local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 134, in init_process
django_app          |     self.load_wsgi()
django_app          |   File "/usr/local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
django_app          |     self.wsgi = self.app.wsgi()
django_app          |                 ^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/gunicorn/app/base.py", line 67, in wsgi
django_app          |     self.callable = self.load()
django_app          |                     ^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
django_app          |     return self.load_wsgiapp()
django_app          |            ^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
django_app          |     return util.import_app(self.app_uri)
django_app          |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/gunicorn/util.py", line 359, in import_app
django_app          |     mod = importlib.import_module(module)
django_app          |           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
django_app          |     return _bootstrap._gcd_import(name[level:], package, level)
django_app          |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
django_app          |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
django_app          |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
django_app          |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
django_app          |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
django_app          |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
django_app          |   File "/app/backend/wsgi.py", line 16, in <module>
django_app          |     application = get_wsgi_application()
django_app          |                   ^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/core/wsgi.py", line 12, in get_wsgi_application
django_app          |     django.setup(set_prefix=False)
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/__init__.py", line 19, in setup
django_app          |     configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
django_app          |                       ^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/conf/__init__.py", line 81, in __getattr__
django_app          |     self._setup(name)
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/conf/__init__.py", line 68, in _setup
django_app          |     self._wrapped = Settings(settings_module)
django_app          |                     ^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/django/conf/__init__.py", line 166, in __init__
django_app          |     mod = importlib.import_module(self.SETTINGS_MODULE)
django_app          |           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
django_app          |     return _bootstrap._gcd_import(name[level:], package, level)
django_app          |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
django_app          |   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
django_app          |   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
django_app          |   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
django_app          |   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
django_app          |   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
django_app          |   File "/app/backend/settings.py", line 125, in <module>
django_app          |     EMAIL_PORT = config('EMAIL_PORT', 1025, cast=int)
django_app          |                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/decouple.py", line 243, in __call__
django_app          |     return self.config(*args, **kwargs)
django_app          |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/decouple.py", line 105, in __call__
django_app          |     return self.get(*args, **kwargs)
django_app          |            ^^^^^^^^^^^^^^^^^^^^^^^^^
django_app          |   File "/usr/local/lib/python3.12/site-packages/decouple.py", line 99, in get
django_app          |     return cast(value)
django_app          |            ^^^^^^^^^^^
django_app          | ValueError: invalid literal for int() with base 10: '1025  # Porta padrão do MailHog'