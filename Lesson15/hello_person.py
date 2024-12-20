def hello(name, lang="English"):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo"
    }
    message = f"{greetings[lang]}, {name}!"
    print(message)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument("-n", "--name", metavar="name", required=True, help="Name of the person to greet.")
    parser.add_argument("-l", "--lang", metavar="language", required=True, choices=["English", "Spanish", "German"], help="Language of the person to greet.")

    args = parser.parse_args()
    hello(args.name, args.lang)

    # message = f"Hello, {args.name}"
    # print(message)