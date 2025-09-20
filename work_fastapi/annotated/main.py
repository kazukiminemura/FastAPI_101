from typing import Annotated

def process_value(
    value: Annotated[int, "range(0, 100)"]
  ):
    if 0 <= value < 100:
        print(f"Value is within the valid range: {value}")
    else:
        print(f"Value is out of the valid range: {value}")

# call 

process_value(50)

try:
    process_value(150)
except ValueError as e:
    print(e)