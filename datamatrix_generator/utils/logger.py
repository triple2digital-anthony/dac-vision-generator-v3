"""
Logging module for tracking application access.
"""

import os
import json
import datetime
from typing import Dict, Any

class AccessLogger:
    def __init__(self):
        """Initialize the access logger."""
        # Get the absolute path to the project root directory
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.log_dir = os.path.join(current_dir, 'logs')
        self.log_file = os.path.join(self.log_dir, 'access_log.json')
        self._ensure_log_directory()

    def _ensure_log_directory(self):
        """Ensure the log directory exists."""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                json.dump([], f)

    def log_access(self, ip_address: str, user_agent: str):
        """Log an access attempt."""
        timestamp = datetime.datetime.now().isoformat()
        
        log_entry = {
            'timestamp': timestamp,
            'ip_address': ip_address,
            'user_agent': user_agent,
            'location': {
                'type': 'Local Development',
                'environment': 'Development Instance'
            }
        }

        try:
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
            
            logs.append(log_entry)
            
            with open(self.log_file, 'w') as f:
                json.dump(logs, f, indent=2)
        except Exception as e:
            print(f"Error logging access: {e}")

    def get_logs(self, admin_password: str) -> list:
        """Get all access logs if admin password is correct."""
        if admin_password != "FG3bI<r3,3D7.~}y=g<0V":
            return []
        
        try:
            with open(self.log_file, 'r') as f:
                return json.load(f)
        except Exception:
            return [] 