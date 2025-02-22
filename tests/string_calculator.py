#Add test for empty string and initial implementation of add function
'''def add(numbers: str) -> int:
    if numbers == "":
        return 0'''

#Add test for single number and update add function to handle it        
'''def add(numbers: str) -> int:
    if numbers == "":
        return 0
    return int(numbers) '''      

#Add test for multiple numbers and update add function to handle it
'''def add(numbers: str) -> int:
    if numbers == "":
        return 0
    number_list = numbers.split(",")
    return sum(int(num) for num in number_list)'''
 
#Add test for new lines between numbers and update add function to handle it    
'''def add(numbers: str) -> int:
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")
    return sum(int(num) for num in number_list)'''
    
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")
    return sum(int(num) for num in number_list)        