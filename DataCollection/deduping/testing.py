import importlib
from deduping import string_edit_check, unshorten_url


def testing():
    print("#1:", string_edit_check("abcfeg", "xabcdeg") == 2)
    print("#2:", string_edit_check("", "xcdeg") == 5)
    print("#3:", string_edit_check("123123456", "123456") == 3)

    print("4:", unshorten_url("http://www.youtube.com"))
    # print('w')
    print("5:", unshorten_url("http://y2u.be/j4dMnAPZu70") == "https://www.youtube.com/watch?v=j4dMnAPZu70")
    print("6:", unshorten_url("https://bit.ly/2NhJtop"))
    print("7:", unshorten_url("https://www.youtube.com/watch?v=j4dMnAPZu70"))


testing()
