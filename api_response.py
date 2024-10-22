import json

class APIResponse:
    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data
        }

    def to_json(self):
        return json.dumps(self.to_dict()) + "\n\n"
