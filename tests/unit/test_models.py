from dataclasses import FrozenInstanceError
from datetime import datetime

from pytest import raises

from pcmonitor.core.models import ProcessEvent

timestamp = datetime(2026, 10, 25, 17, 30)
event_id = 1
process_id = 1234
process_guid = "group"
executable_path = r"C:\Windows\System32\notepad.exe"
command_line = "app --user"
parent_process_id = 123
parent_image = "parent_image"
user = "this_user"


def test_process_event_creation() -> None:
    event = ProcessEvent(
        timestamp=timestamp,
        event_id=event_id,
        process_id=process_id,
        process_guid=process_guid,
        executable_path=executable_path,
        command_line=command_line,
        parent_process_id=parent_process_id,
        parent_image=parent_image,
        user=user,
    )

    assert event.timestamp == timestamp
    assert event.event_id == event_id
    assert event.process_id == process_id
    assert event.process_guid == process_guid
    assert event.executable_path == executable_path
    assert event.command_line == command_line
    assert event.parent_process_id == parent_process_id
    assert event.parent_image == parent_image
    assert event.user == user


def test_process_event_is_immutable() -> None:
    event = ProcessEvent(
        timestamp=timestamp,
        event_id=event_id,
        process_id=process_id,
        process_guid=process_guid,
        executable_path=executable_path,
        command_line=command_line,
        parent_process_id=parent_process_id,
        parent_image=parent_image,
        user=user,
    )

    with raises(FrozenInstanceError):
        event.process_id = 1235  # type: ignore[misc]
