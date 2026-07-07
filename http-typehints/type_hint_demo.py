# Type hinting examples
def greet(name: str) -> str:
    return f"Hello, {name}"

def add_numbers(a: int, b: int) -> int:
    return a + b

# Example usage
if __name__ == "__main__":
    print(greet("Alice"))
    print(add_numbers(3, 5))
    # Uncomment to see type error (runtime won't catch, but static checker would)
    # print(add_numbers(3, "5"))