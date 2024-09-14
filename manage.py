#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv

dotenv_path = 'll_env/.env'
dotenv_dotdev_path = 'll_env/.env.dev'

env_file = load_dotenv(dotenv_path)
if not env_file and os.path.exists(dotenv_path):
    raise ValueError(
        '.env file contains no environmental variables '
        '(e.g. SECRET_KEY for settings.py)'
    )
elif not os.path.exists(dotenv_path):
    raise FileNotFoundError(f'.env file not found at {dotenv_path}')

if os.path.exists(dotenv_dotdev_path):
    load_dotenv(dotenv_dotdev_path)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
