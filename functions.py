def filter_query(param: str, data):
    return filter(lambda x: param in x, data)


def map_query(param: str, data):
    col_number = int(param)
    return map(lambda x: x.split(' ')[col_number], data)


def unique_query(data, *args, **kwargs):
    return set(data)


def sort_query(param: str, data):
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data):
    limit = int(param)
    return list(data)[:limit]
