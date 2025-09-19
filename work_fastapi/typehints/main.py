def add(num1: int, num2: int) -> str:
  result: str = "sum result is: "
  return result + str(num1 + num2)

def greet(name: str) -> str:
  return f"Hello, {name}!"

def divide(dividend: float, divisor: float) -> float:
  return dividend / divisor

from typing import List
def get_first_three_elements(elements: List[int]) -> List[int]:
  return elements[:3]

from typing import Dict
def get_value(dictionary: Dict[str, int], key: str) -> int:
  return dictionary[key]

def process_items(items: List[str]) -> None:
  for item in items:
    print(item)

def count_characters(word_list: list[str]) -> dict[str, int]:
  count_map: dict[str, int] = {}
  for word in word_list:
    count_map[word] = len(word)
  return count_map



# call
result_add = add(5, 10)
print(result_add)  # Output: sum result is: 15

greeting = greet("Alice")
print(greeting)  # Output: Hello, Alice!

result_divide = divide(10.0, 2.0)
print(result_divide)  # Output: 5.0

elements = get_first_three_elements([1, 2, 3, 4, 5])
print(elements)  # Output: [1, 2, 3]

value = get_value({"a": 1, "b": 2}, "a")
print(value)  # Output: 1

process_items(["apple", "banana", "cherry"])
  # Output: apple
  #         banana
  #         cherry

character_count = count_characters(["apple", "banana", "cherry"])
print(character_count)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}
