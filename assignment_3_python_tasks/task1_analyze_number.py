def analyze_number(n):
    even_odd = "Even" if n % 2 == 0 else "Odd"
    pos_neg = "Positive" if n > 0 else ("Negative" if n < 0 else "Zero")
    return (even_odd, pos_neg, n ** 2)

if __name__ == "__main__":
    print(analyze_number(4))
