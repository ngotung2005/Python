_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

n = int(input("Nhập n: "))

count = 0

for word in _list:
    if len(word) >= n: 
        if word[0] == word[-1]: 
            count += 1

print("Số chuỗi thỏa mãn là:", count)