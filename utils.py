def get_memo_lists(client, board_name, list_completed_name, list_review_name, list_memory_name):
    boards = client.list_boards()
    target_board = [_ for _ in boards if _.name == board_name]
    if len(target_board) == 0:
        raise ValueError("Wrong board_name: " + board_name + '. no board name is ' + board_name)
    elif len(target_board) > 1:
        raise ValueError("Wrong board_name: " + board_name + '. Too many board names are ' + board_name)
    else:
        target_board = target_board[0]
    lists = target_board.list_lists()

    target_lists = []
    for target_names in (list_completed_name, list_review_name, list_memory_name):
        _list = [_ for _ in lists if _.name == target_names]
        if len(_list) == 0:
            raise ValueError("Wrong list_name: " + target_names + '. no list name is ' + target_names)
        elif len(_list) > 1:
            raise ValueError("Wrong list_name: " + target_names + '. Too many list names are ' + target_names)
        else:
            target_lists += _list
    list_complete, list_review, list_memory = target_lists
    return list_complete, list_review, list_memory


def get_memo_cards(trello_list):
    cards = trello_list.list_cards()
    return cards
