from messages_functions import send_messages as sm

messages = ["1st message", "2nd message", "3rd message"]
# show_messages(messages)

print(f"\n*** sending messages ***")
sent_messages = []

sm(messages[:], sent_messages)

print(f"\n*** print messages ***")
for message in messages:
    print(message)

print(f"\n*** print sent messages ***")
for sent_message in sent_messages:
    print(sent_message)
