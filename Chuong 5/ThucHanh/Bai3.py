with open('demo_file1.txt', 'w') as f:
    f.write('Thuc \n hanh \n voi \n file \n IO \n')
with open('demo_file1.txt', 'r') as f:
    chu = f.read()
    print("Câu a:", chu.replace('\n', ' '))
with open('demo_file1.txt', 'r') as f:
    print("Câu b:")
    print(f.read())