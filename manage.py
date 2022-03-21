#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# import dotenv
# import pathlib


def main():
    """Run administrative tasks."""

    # dotenv.read_dotenv()
    # dot_env_path = pathlib.Path() / '.env'
    # if dot_env_path.exists():
    #     dotenv.read_dotenv(str(dot_env_path))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
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
