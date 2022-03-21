def replace_first(items: list) -> Iterable:
        # your code here
    # create a new list with last item as first
    if len(items) <=1:
        return items
    first = items[0]
    new_list = items[1:]
    # add rest of original list apart from last item to the new list
    new_list.append(first)
    return new_list