def foo(zdanie):
    zdanie = zdanie.replace(" ", "").lower()
    if zdanie == zdanie[::-1]:
        print("Jest to palindrom")
    else:
        print("Nie jest to palindrom")


zdanie = "Kamil ślimak"
foo(zdanie)
