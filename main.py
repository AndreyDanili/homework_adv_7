class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def balance(text):
    brackets = "()[]{}"
    opening, closing = brackets[::2], brackets[1::2]
    stack = Stack()
    for item in text:
        if item in opening:
            stack.push(opening.index(item))
        elif item in closing:
            if len(stack.items) != 0 and stack.items[-1] == closing.index(item):
                stack.pop()
            else:
                return print('Несбалансированно')
    if len(stack.items) == 0:
        return print('Сбалансированно')
    else:
        return print('Несбалансированно')


new_stack = Stack()
print(new_stack.isEmpty())
new_stack.push('23')
new_stack.push('-45')
new_stack.push('test')
print(new_stack.pop())
print(new_stack.peek())
print(new_stack.size())

balance('[([])((([[[]]])))]{()}')
balance('[[{())}]')
