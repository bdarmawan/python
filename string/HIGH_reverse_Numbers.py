def reverse(number: int) -> int:
    result = 0
    while number > 0:
        remain = number % 10
        number = number // 10
        result = result * 10 + remain
    print(result)

number = 135
reverse(number)   # RESULT: 531

number = 123456789
reverse(number)   # RESULT: 987654321

number = 0
reverse(number)   # RESULT: 0


