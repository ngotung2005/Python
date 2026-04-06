nhap_chu = input("Nhập chữ bạn muốn ghi: ")
with open('output.txt', 'w') as f:
    f.write(nhap_chu)
with open('output.txt', 'r') as f:
    print(f.read()) 