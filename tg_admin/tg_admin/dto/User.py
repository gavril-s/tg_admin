from __future__ import annotations
import typing as tp
import dto
from dataclasses import dataclass
from db import add_user, delete_user


@dataclass
class User:
    id: int
    is_bot: bool
    first_name: str
    last_name: tp.Optional[str]
    username: tp.Optional[str]
    is_premium: tp.Optional[bool]
    chat_id: tp.Optional[int]
    state: UserState

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
                dic["chat_id"],
                UserState.DEFAULT,
            )
        except:
            return None

    @staticmethod
    def from_db(res: tp.Tuple) -> tp.Optional[User]:
        try:
            return User(
                res[0],
                res[1],
                res[2],
                res[3],
                res[4],
                res[5],
                res[6],
                dto.UserState(res[7]),
            )
        except:
            return None

    def to_db(self) -> tp.Optional[tp.Tuple]:
        try:
            return (
                self.id,
                self.is_bot,
                self.first_name,
                self.last_name,
                self.username,
                self.is_premium,
                self.chat_id,
                self.state.value,
            )
        except:
            return None

    async def commit(self):
        await delete_user(self)
        await add_user(self)
