def num_to_words(n):
    if n == 0:
        return "Zero"
    elif abs(n) > 999999999999999:
        return "Number out of range"
    elif n < 0:
        return "Negative " + num_to_words(-n)
     
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion","Trillion", "Quadrillion"]
    def chunk_to_words(n):
        word = ""
        if n > 99:
            word += ones[n // 100] + " Hundred "
            n %= 100
        if n > 19:
            word += tens[n // 10] + " "
            n %= 10
        elif n > 9:
            word += teens[n - 10] + " "
        else:
            if n > 0:
                word += ones[n] + " "
        return word.strip()
    word = ""
    i = 0
    while n>0:
        if n % 1000 != 0:
            word = chunk_to_words(n % 1000) + " " + thousands[i] + " " + word
        n //= 1000
        i += 1
    return word.strip()
n = int(input("Enter a number: "))
print(num_to_words(n))
