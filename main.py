# User management system with in-memory storage

# Global state: module-level list to store user names
users = []


def add_user(name):
    """
    Add a new user to the system.

    Args:
        name: The user's name (string)

    Returns:
        True on success

    Raises:
        ValueError: If name is empty or only whitespace
        TypeError: If name is not a string
    """
    # Validate that name is a string
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    # Validate that name is not empty or only whitespace
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    # Strip whitespace and add to users list
    cleaned_name = name.strip()
    users.append(cleaned_name)
    return True


def get_user_count():
    """
    Return the current number of users.

    Returns:
        Integer count of users in the list
    """
    return len(users)


def get_all_users():
    """
    Retrieve all users.

    Returns:
        Copy of the users list (prevents external modification)
    """
    return users.copy()


def clear_users():
    """
    Remove all users from the system.
    """
    users.clear()


def remove_user(name):
    """
    Remove first occurrence of a user by name.

    Args:
        name: The user's name to remove (string)

    Returns:
        True on success

    Raises:
        ValueError: If user not found in the list
    """
    if name not in users:
        raise ValueError("User not found")

    users.remove(name)
    return True
