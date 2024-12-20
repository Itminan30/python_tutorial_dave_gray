counter = 1

def update_counter():
    global counter
    counter += 1

    inside_counter = 10
    def inner_updater():
        nonlocal inside_counter
        inside_counter += inside_counter

    print(inside_counter)
    inner_updater()
    print(inside_counter)

print(counter)
update_counter()
print(counter)