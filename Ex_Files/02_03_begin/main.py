NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2] # prints John, Paul
GEORGE_RINGO = NAMES[2:] # prints George Ringo
REVERSE = NAMES[::-1] #from Ringo to John
EVERY_OTHER = NAMES[::2] # John, George

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
print(EVERY_OTHER)
