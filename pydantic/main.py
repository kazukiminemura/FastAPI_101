from datetime import datetime
from pydantic import BaseModel, ValidationError

class Event(BaseModel):
    name: str
    start_datetime: datetime
    participants: list[str] = []
    
external_data = {
  "name": "FastAPI Workshop",
  # "start_datetime": "2024-07-01T10:00:00",
  "start_datetime": "abc",
  "participants": ["Alice", "Bob", "Charlie"]
}

try:
    event = Event(**external_data)
    print("Event Name:", event.name, type(event.name))
    print("Event Start Date:", event.start_datetime, type(event.start_datetime))
    print("Event Participants:", event.participants, type(event.participants))
except ValidationError as e:
    print("Validation Error:", e.errors())