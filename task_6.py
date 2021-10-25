subjects = {}

with open('task06.txt') as f:
    for row in f:
        subject_info = row.split()
        name = subject_info[0].rstrip(':')

        subjects[name] = subject_info[1:]

result = {}

for key, value in subjects.items():
    result[key] = sum(
        [
            int(hours[:hours.index('(')])
            for hours in value
            if hours != '-'
        ]
    )

print(result)