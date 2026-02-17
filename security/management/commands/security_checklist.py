from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = "Print a simple security baseline checklist."

    def handle(self, *args, **options):
        # Use getattr to safely check settings without crashing if missing
        checks = {
            "DEBUG is False": settings.DEBUG is False,
            "SECRET_KEY set": settings.SECRET_KEY != "unsafe-secret-key-change-in-production-!@#$",
            "X_FRAME_OPTIONS is DENY": getattr(settings, "X_FRAME_OPTIONS", "") == "DENY",
            "SESSION_COOKIE_HTTPONLY": getattr(settings, "SESSION_COOKIE_HTTPONLY", False) is True,
            "CSRF_COOKIE_HTTPONLY": getattr(settings, "CSRF_COOKIE_HTTPONLY", False) is True,
        }
        self.stdout.write("--- Security Baseline Check ---")
        for check, passed in checks.items():
            status = "OK" if passed else "WARNING"
            color = self.style.SUCCESS if passed else self.style.WARNING
            self.stdout.write(color(f"[{status}] {check}"))