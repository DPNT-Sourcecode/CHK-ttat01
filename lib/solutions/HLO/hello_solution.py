# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:

    if not isinstance(friend_name, str):
        raise TypeError

    return "Hello, {friend_name}".format(friend_name=friend_name)

