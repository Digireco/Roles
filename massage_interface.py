#!/usr/bin/env python3

"""Simple command-line massage interface."""

from typing import Any


def session() -> None:
    print("Massage session started. Relax...")
    duration = input("Enter duration in minutes: ")
    try:
        minutes = int(duration)
    except ValueError:
        print("Invalid duration. Please enter a number.")
        return
    print(f"Massaging for {minutes} minutes. Enjoy!")


def menu() -> None:
    while True:
        print("\nMassage Interface")
        print("1. Start massage session")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            session()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
