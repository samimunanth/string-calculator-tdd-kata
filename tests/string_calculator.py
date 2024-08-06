#Add test for empty string and initial implementation of add function
'''def add(numbers: str) -> int:
    if numbers == "":
        return 0'''

#Add test for single number and update add function to handle it        
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    return int(numbers)   

