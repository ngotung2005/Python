_list = ['abc', 'hello', 'hi', 'python', 'code']

n = int(input("Nhập n: "))

_new = []

for word in _list:
    if len(word) > n:   
        _new.append(word)

print("Các từ có độ dài > n là:")
print(_new)