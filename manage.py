#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the default Django settings module environment variable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')
    try:
        # Import Django's command-line execution function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an error if Django isn't installed or can't be imported
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute the command-line utility with the provided arguments
    execute_from_command_line(sys.argv)


# Run the main function if this script is executed directly
if __name__ == '__main__':
    main()
