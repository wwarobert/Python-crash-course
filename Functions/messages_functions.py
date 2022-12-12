def show_messages(messages):
    """ Print messages """
    while messages:
        current_message = messages.pop()
        print(current_message)


def send_messages(messages, sent_messages):
    while messages:
        curent_message = messages.pop()
        print(curent_message)
        sent_messages.append(curent_message)
