"""
create a function that
number n
even numbers from 1 to n
return

10

1-10
2 4 6 8 10
%2 == 0

5

loop > 1 to n
if > even
function > logic

def count_even(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
            count += 1
        return count

result = count_even(10)
print(result)
"""
def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

marks = int(input("Enter your marks: "))

result = check_result(marks)
print(result)


