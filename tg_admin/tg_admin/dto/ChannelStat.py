from __future__ import annotations
import typing as tp
import dto
from dataclasses import dataclass
from collections import defaultdict
import datetime


@dataclass
class AdminStat:
    name: str = ""
    total_messages: int = 0

    messages_with_views: int = 0
    total_views: int = 0

    messages_with_forwards: int = 0
    total_forwards: int = 0

    total_reactions: int = 0
    reactions: tp.Dict[str, int] = None

    top_posts: tp.List[tp.Tuple[str, int]] = None

    def __init__(self):
        self.reactions = defaultdict(int)
        self.top_posts = []

    def add(self, message):
        self.total_messages += 1

        if message.views is not None:
            self.messages_with_views += 1
            self.total_views += message.views

            self.top_posts.append((message.link, message.views))
            self.top_posts.sort(key=lambda x: -x[1])
            self.top_posts = self.top_posts[:3]

        if message.forwards is not None:
            self.messages_with_forwards += 1
            self.total_forwards += message.forwards

        if message.reactions is not None:
            for reaction in message.reactions.reactions:
                if reaction.emoji is None or reaction.count is None:
                    continue
                self.total_reactions += reaction.count
                self.reactions[reaction.emoji] += reaction.count

    def __str__(self):
        reactions_list = list(self.reactions.items())
        reactions_list.sort(key=lambda x: -x[1])
        reactions_list = reactions_list[:3]

        avg_views = round(self.total_views / self.messages_with_views, 2)
        avg_forwards = round(self.total_forwards / self.messages_with_forwards, 2)

        return (
            f"**{self.name}**\n"
            + f"Всего постов: {self.total_messages}\n"
            + f"Всего просмотров: {self.total_views}\n"
            + f"Среднее количество просмотров: {avg_views}\n"
            + f"Всего репостов: {self.total_forwards}\n"
            + f"Среднее количество репостов: {avg_forwards}\n"
            + f"Всего реакций: {self.total_reactions}\n"
            + f"Самые популярные реакции:\n\t"
            + "\n\t".join([f"{r[0]} - {r[1]}" for r in reactions_list])
            + "\n"
            + f"Самые популярные посты:\n\t"
            + "\n\t".join([f"{p[0]} - {p[1]}" for p in self.top_posts])
        )


class ChannelStat:
    def __init__(self):
        self.stat = defaultdict(AdminStat)
        self.min_date = None
        self.max_date = None

    def add(self, message):
        self.min_date = (
            min(self.min_date, message.date)
            if self.min_date is not None
            else message.date
        )
        self.max_date = (
            max(self.max_date, message.date)
            if self.max_date is not None
            else message.date
        )

        admins = ["Общая статистика"]
        if message.author_signature is not None:
            admins.append(message.author_signature)

        for admin in admins:
            self.stat[admin].name = admin
            self.stat[admin].add(message)

    def __str__(self):
        stat_list = list(self.stat.values())
        stat_list.sort(key=lambda x: -x.total_messages)
        return "\n\n".join([str(stat_piece) for stat_piece in stat_list])

    def in_chunks(self):
        max_len = 4096
        stat_list = list(self.stat.values())
        stat_list.sort(key=lambda x: -x.total_messages)

        min_date_str = self.min_date.strftime("%d.%m.%Y")
        max_date_str = self.max_date.strftime("%d.%m.%Y")

        res = [f"**Статистика канала за период {min_date_str} - {max_date_str}**\n\n"]
        for i in range(len(stat_list)):
            if i != 0:
                to_add = "\n\n"
            else:
                to_add = ""
            to_add += str(stat_list[i])

            if len(to_add) + len(res[-1]) > max_len:
                res.append(to_add)
            else:
                res[-1] += to_add

        return res
