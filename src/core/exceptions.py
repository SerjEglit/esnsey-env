# src/core/exceptions.py
class SecurityBreach(Exception):
    """Исключение для нарушений безопасности системы"""
    def __init__(self, message="Security breach detected"):
        super().__init__(message)
        self.system_alert_level = "CRITICAL"
