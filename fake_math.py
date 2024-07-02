def divide(first: int, second: int):
    div = 0
    if second == 0:
        div = 'Ошибка'
        return div
    elif second > 0:
        div = first / second
        return div
