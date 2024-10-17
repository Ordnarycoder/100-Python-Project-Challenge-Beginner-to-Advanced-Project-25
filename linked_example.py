import collections

linked_example = collections.deque()

linked_example.append("John")
linked_example.append("Carl")
linked_example.append("Max")

print(linked_example)

linked_example.insert(3, "Anya")

print(linked_example)

linked_example.pop()

print(linked_example)

linked_example.remove("John")

print(linked_example)