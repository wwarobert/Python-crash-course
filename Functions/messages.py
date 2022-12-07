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


messages = ["1st message", "2nd message", "3rd message"]
# show_messages(messages)

print(f"\n*** sending messages ***")
sent_messages = []

send_messages(messages[:], sent_messages)

print(f"\n*** print messages ***")
for message in messages:
    print(message)

print(f"\n*** print sent messages ***")
for sent_message in sent_messages:
    print(sent_message)
