def add(numbers):
    if numbers == "":
        return 0
    delimiter = ","
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    parts = numbers.replace("\n", delimiter).split(delimiter)
    result = 0
    for part in parts:
        if part:
            result += int(part)
    return result
