
from typing import Optional, Iterable, List, Callable, TypeGuard, Dict
from functions import filter_query, map_query, unique_query, sort_query, limit_query, regex_query

FILE_NAME = 'data/apache_logs.txt'

CMD_TO_FUNCTION: Dict[str, Callable] = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex_query
}


def iter_file(file_name: str) -> Iterable[str]:
    with open(file_name)as file:
        for row in file:
            yield row


def query_builder(cmd: str, value: Callable[[str], TypeGuard[str]], data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepared_data: Iterable[str] = iter_file(FILE_NAME)
    else:
        prepared_data = data
    result: Iterable[str] = CMD_TO_FUNCTION[cmd](param=value, data=prepared_data)
    return list(result)


