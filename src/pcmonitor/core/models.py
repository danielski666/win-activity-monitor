from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ProcessEvent:
    timestamp: datetime
    event_id: int
    process_id: int
    process_guid: str | None
    executable_path: str
    command_line: str | None
    parent_process_id: int | None
    parent_image: str | None
    user: str | None
