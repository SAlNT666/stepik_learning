def remove_marks(text, marks):
    remove_marks.count += 1
    return ''.join(i for i in text if i not in marks)


remove_marks.count = 0

text = 'Hi! Will we go together?'
marks = '!?'

print(remove_marks(text, '!?'))
print(remove_marks.count)
