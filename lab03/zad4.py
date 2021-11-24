def reverse(txt: str) -> str:
    if len(txt) == 0:
        return ''
    return txt[len(txt) - 1] + reverse(txt[: len(txt) - 1])


print(reverse("misja"))
