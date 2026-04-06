n = int(input("Nhap so dong n"))
with open ('text.txt', 'r') as f:
    tat_ca_cac_dong = f.readline()
    for i in range(n):
        print(tat_ca_cac_dong[i])
