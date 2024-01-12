import os
import subprocess


def run_command(command, working_directory=None):
    subprocess.run(command, shell=True, cwd=working_directory)


def create_django_project():
    project_name = input("Enter the name of your Django project: ")

    run_command(f"python.exe -m pip install --upgrade pip")
    run_command("pip install django pillow isort black flake8")
    run_command(f"django-admin startproject {project_name}")
    print(f"{project_name} was created")

    os.chdir(project_name)
    print(os.getcwd())

    app_name = input("Enter the app name: ")
    run_command(f"python manage.py startapp {app_name}")

    os.makedirs(os.path.join("templates", app_name))
    os.makedirs("static")

    with open(os.path.join(project_name, "settings.py"), "w") as settings_file:
        settings_file.write(
            "from pathlib import Path\n\n"
            "BASE_DIR = Path(__file__).resolve().parent.parent\n\n"
            "SECRET_KEY = 'django-insecure-kdc2c_kf$f2b1b3_g_u&qaj8gpt(5g4(-gfq+!accq+q)%4m!k'\n\n"
            "DEBUG = True\n\n"
            "ALLOWED_HOSTS = []\n\n"
            "INSTALLED_APPS = [\n"
            '    "django.contrib.admin",\n'
            '    "django.contrib.auth",\n'
            '    "django.contrib.contenttypes",\n'
            '    "django.contrib.sessions",\n'
            '    "django.contrib.messages",\n'
            '    "django.contrib.staticfiles",\n'
            '    #own\n'
            f'    "{app_name}.apps.{app_name.replace("_", " ").title().replace(" ", "")}Config"\n'
            "]\n\n"
            "MIDDLEWARE = [\n"
            '    "django.middleware.security.SecurityMiddleware",\n'
            '    "django.contrib.sessions.middleware.SessionMiddleware",\n'
            '    "django.middleware.common.CommonMiddleware",\n'
            '    "django.middleware.csrf.CsrfViewMiddleware",\n'
            '    "django.contrib.auth.middleware.AuthenticationMiddleware",\n'
            '    "django.contrib.messages.middleware.MessageMiddleware",\n'
            '    "django.middleware.clickjacking.XFrameOptionsMiddleware",\n'
            "]\n\n"
            "ROOT_URLCONF = 'my_project.urls'\n\n"
            "TEMPLATES = [\n"
            '    {\n'
            '        "BACKEND": "django.template.backends.django.DjangoTemplates",\n'
            '        "DIRS": [BASE_DIR / "templates"],\n'
            '        "APP_DIRS": True,\n'
            '        "OPTIONS": {\n'
            '            "context_processors": [\n'
            '                "django.template.context_processors.debug",\n'
            '                "django.template.context_processors.request",\n'
            '                "django.contrib.auth.context_processors.auth",\n'
            '                "django.contrib.messages.context_processors.messages",\n'
            '            ],\n'
            '        },\n'
            '    },\n'
            "]\n\n"
            "WSGI_APPLICATION = 'my_project.wsgi.application'\n\n"
            "DATABASES = {\n"
            '    "default": {\n'
            '        "ENGINE": "django.db.backends.sqlite3",\n'
            '        "NAME": BASE_DIR / "db.sqlite3",\n'
            '    }\n'
            "}\n\n"
            "AUTH_PASSWORD_VALIDATORS = [\n"
            '    {\n'
            '        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",\n'
            '    },\n'
            '    {\n'
            '        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",\n'
            '    },\n'
            '    {\n'
            '        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",\n'
            '    },\n'
            '    {\n'
            '        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",\n'
            '    },\n'
            "]\n\n"
            "LANGUAGE_CODE = 'en-us'\n\n"
            "TIME_ZONE = 'UTC'\n\n"
            "USE_I18N = True\n\n"
            "USE_TZ = True\n\n"
            "STATIC_URL = 'static/'\n"
            "STATIC_ROOT = BASE_DIR / 'staticfiles'\n"
            "STATICFILES_DIRS = [(BASE_DIR / 'static'), ]\n\n"
            "MEDIA_URL = 'media/'\n"
            "MEDIA_ROOT = BASE_DIR / 'media'\n\n"
            "DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'\n")

    with open(os.path.join(project_name, "urls.py"), "w") as urls_file:
        urls_file.write(
            'from django.conf import settings\n'
            'from django.conf.urls.static import static\n'
            'from django.contrib import admin\n'
            'from django.urls import include, path\n\n'
            'urlpatterns = [\n'
            '    path("admin/", admin.site.urls),\n'
            f'    path("", include("{app_name}.urls")),\n'
            ']\n\n'
            'if settings.DEBUG:\n'
            '    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)'
        )

    os.chdir(app_name)

    with open("urls.py", "w") as app_urls_file:
        app_urls_file.write(
            'from django.urls import path\n'
            'from .views import index\n\n'
            'urlpatterns = [\n'
            '    path("", index, name="index"),\n]'
        )

    with open("views.py", "w") as views_file:
        views_file.write(
            'from django.http import HttpResponse\n\n'
            'def index(request):\n'
            '    return HttpResponse("<h1>Hello world !!!</h1>")'
        )

    os.chdir("..")
    run_command("python manage.py runserver")


if __name__ == "__main__":
    create_django_project()
