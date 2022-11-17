from collections import defaultdict


def best_sender(messages, senders):
    result = defaultdict(int)
    for s, m in zip(senders, messages):
        result[s] += len(m.split())
    return max(result, key=lambda x: (result[x], x))


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))