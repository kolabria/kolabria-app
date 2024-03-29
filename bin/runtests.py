#!/usr/bin/env python
import os, sys

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kolabria.settings.testing")

    from django.core.management import call_command
    from django.conf import settings

    apps_for_testing = [app[16:] for app in settings.INSTALLED_APPS
            if app.startswith("kolabria.apps")]

    call_command("test", *apps_for_testing)
