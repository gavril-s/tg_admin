from __future__ import annotations
import typing as tp
from dataclasses import dataclass


@dataclass
class Message:
    id: str
    user_id: int
    from_chat_id: int
    to_chat_id: int