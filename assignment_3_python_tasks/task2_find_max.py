def find_max(*numbers):
    return max(numbers) if numbers else None

if __name__ == "__main__":
    print(find_max(3, 7, 2, 10))
