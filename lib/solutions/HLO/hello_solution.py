class EmptyStringError(Exception):
    pass


# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:

    if not isinstance(friend_name, str):
        raise TypeError("Please enter a string")

    if len(friend_name) <= 0:
        raise EmptyStringError("String must not be an empty")

    return "Hello, {friend_name}".format(friend_name=friend_name.capitalize())


