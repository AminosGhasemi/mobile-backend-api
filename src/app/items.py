items = []

def add_item(item: dict) -> None:
    items.append(item)

def find_item_by_id(item_id):

    for item in items:
        if item["id"] == item_id:
            return item
    return None