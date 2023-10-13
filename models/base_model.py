#!/usr/bin/python3
"""
The BaseModel class defines all common attributes/methods for other classes
"""

import uuid
from datetime import datetime
import models

class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

