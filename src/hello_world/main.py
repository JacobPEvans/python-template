"""Main module for Hello World application."""


def greet(name: str = "World") -> str:
    """
    Generate a greeting message.

    Args:
        name: Name to greet (default: "World")

    Returns:
        Greeting message
    """
    return f"Hello, {name}!"


def main() -> None:
    """Main entry point."""
    print(greet())


if __name__ == "__main__":
    main()
