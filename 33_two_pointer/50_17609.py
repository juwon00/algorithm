def is_pseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def is_palindrome(word, left, right):
    if word == word[::-1]:
        return 0
    else:
        while left < right:
            if word[left] != word[right]:
                check_left = is_pseudo(word, left + 1, right)
                check_right = is_pseudo(word, left, right - 1)

                if check_left or check_right:
                    return 1

                else:
                    return 2
            else:
                left += 1
                right -= 1


n = int(input())

for _ in range(n):
    word = input()
    left, right = 0, len(word) - 1
    print(word)
    print(is_palindrome(word, left, right))


# 처음엔 아래와 같이 코드를 작성했다가 오류를 발견
# ex) 1 xyyyyxy
# -> 항상 left+1 부터 확인하기에 생긴 오류
# -> left+1과 right-1을 동시에 확인해야함

# n = int(input())
#
# for _ in range(n):
#     str = input()
#     left, right = 0, len(str) - 1
#     palindrome = True
#     pseudo = True
#     print(str)
#
#     while True:
#         print(left, right)
#
#         if left > right:
#             print("break")
#             break
#         elif str[left] == str[right]:
#             print("same")
#             left += 1
#             right -= 1
#         elif str[left + 1] == str[right] and pseudo::
#             print("start += 2")
#             pseudo = False
#             left += 2
#             right -= 1
#         elif str[left] == str[right - 1] and pseudo:
#             print("end -= 2")
#             pseudo = False
#             left += 1
#             right -= 2
#         else:
#             print("no")
#             palindrome = False
#             break
#
#     if palindrome and pseudo:
#         print(0)
#     elif palindrome:
#         print(1)
#     else:
#         print(2)
