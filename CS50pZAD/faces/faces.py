def convert(text):
    text = text.replace(":)", "🙂")

    text = text.replace(":(", "🙁")

    return text

def main():

    word = input()

    result = convert(word)

    print(result)

main()
