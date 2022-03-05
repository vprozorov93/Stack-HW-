from Stack import Stack


def balance(string_):
    b_dict = {')': '(', '}': '{', ']': '['}
    if len(string_) % 2 != 0:
        return False

    stack = Stack()
    stack.push(string_[0])
    for letter in string_[1:]:
        if stack.peek() is not None and stack.peek() == b_dict.get(letter):
            stack.pop()
        else:
            stack.push(letter)

    if stack.is_empty():
        return True

    return False




