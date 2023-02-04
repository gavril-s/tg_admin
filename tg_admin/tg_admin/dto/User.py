from __future__ import annotations
import typing as tp
from dataclasses import dataclass


@dataclass
class User:
    id: int
    is_bot: bool
    first_name: str
    last_name: tp.Optional[str]
    username: tp.Optional[str]
    is_premium: tp.Optional[bool]
    chat_id: tp.Optional[int]

    @staticmethod
    def from_dict(dic: tp.Dict) -> tp.Optional[User]:
        try:
            return User(
                dic["id"],
                dic["is_bot"],
                dic["first_name"],
                dic["last_name"],
                dic["username"],
                dic["is_premium"],
                dic["chat_id"]
            )
        except:
            return None

    @staticmethod
    def from_db(res: tp.Dict) -> tp.Optional[User]:
        try:
            return User(res[0], res[1], res[2], res[3], res[4], res[5], res[6])
        except:
            return None
            
    def to_db(self) -> tp.Optional[tp.Tuple]:
        try:
            return (id, is_bot, first_name, last_name, username, is_premium, chat_id)
        except:
            return None