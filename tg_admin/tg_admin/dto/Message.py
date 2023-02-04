from __future__ import annotations
import dto
import typing as tp
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    id: str
    local_id: int
    user_id: int
    from_chat_id: int
    to_chat_id: int
    sending_time: tp.Optional[datetime]

    def to_db(self) -> tp.Optional[tp.Tuple]:
        try:
            return (
                self.id,
                self.local_id,
                self.user_id,
                self.from_chat_id,
                self.to_chat_id,
                self.sending_time,
            )
        except:
            return None

    @staticmethod
    def from_db(res: tp.Tuple):
        try:
            return Message(res[0], res[1], res[2], res[3], res[4], res[5])
        except:
            return None
