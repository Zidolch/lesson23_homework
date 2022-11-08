import re
from typing import Iterable, List, Set


def filter_query(param: str, data: Iterable[str]) -> Iterable[str]:
    return filter(lambda x: param in x, data)


def map_query(param: str, data: Iterable[str]) -> Iterable[str]:
    col_number = int(param)
    return map(lambda x: x.split(' ')[col_number], data)


def unique_query(data: Iterable[str], *args, **kwargs) -> Set[str]:
    return set(data)


def sort_query(param: str, data: Iterable[str]) -> Iterable[str]:
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data: Iterable[str]) -> List[str]:
    limit = int(param)
    return list(data)[:limit]


def regex_query(param: str, data: Iterable[str]) -> List[str]:
    return [item for item in data if re.search(pattern=param, string=item)]
