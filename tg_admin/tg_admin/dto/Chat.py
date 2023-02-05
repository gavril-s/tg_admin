from dataclasses import dataclass
import typing as tp

@dataclass
class Chat:
    id: int
    chat_type: str
    title: tp.Optional[str]
    username: tp.Optional[str]
