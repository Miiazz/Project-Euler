#Loops through numbers (3,5) within the limit

def SumMultiples(numbers, limit):
    # Create a set to hold unique multiples
    multiples = set()
    for n in numbers:
        # Add multiples of each number to the set
        multiples.update(range(n, limit, n))
    return sum(multiples)

# Example usage
limit = 100
numbers = [3, 5]
print(SumMultiples(numbers, limit))
