from app.items import items, add_item, find_item_by_id


def test_find_item_by_id_returns_matching_item():
    items.clear()

    item = {
        "id": 1,
        "title": "Learn Python loops",
        "description": "Practice searching through a list.",
        "priority": 2,
        "estimated_hours": 1.5,
        "category": "Learning",
        "is_done": False,
    }

    add_item(item)

    result = find_item_by_id(1)

    assert result == item


def test_find_item_by_id_finds_item_later_in_list():
    items.clear()

    first_item = {
        "id": 1,
        "title": "First task",
        "description": "This item should not match the search.",
        "priority": 1,
        "estimated_hours": 1.0,
        "category": "Study",
        "is_done": False,
    }

    second_item = {
        "id": 2,
        "title": "Second task",
        "description": "This item should be found after the loop continues.",
        "priority": 3,
        "estimated_hours": 2.5,
        "category": "Project",
        "is_done": False,
    }

    add_item(first_item)
    add_item(second_item)

    result = find_item_by_id(2)

    assert result == second_item


def test_find_item_by_id_finds_second_item():
    items.clear()

    first_item = {
        "id": 1,
        "title": "First task",
        "description": "This should not match the search.",
        "priority": 1,
        "estimated_hours": 1.0,
        "category": "Study",
        "is_done": False,
    }

    second_item = {
        "id": 2,
        "title": "Second task",
        "description": "This item should be found.",
        "priority": 2,
        "estimated_hours": 2.5,
        "category": "Project",
        "is_done": False,
    }

    add_item(first_item)
    add_item(second_item)

    result = find_item_by_id(2)

    assert result == second_item