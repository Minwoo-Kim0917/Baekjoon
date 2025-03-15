

N, B = input().split()  
B = int(B) 

decimal_value = 0 


for i, digit in enumerate(reversed(N)):
    if '0' <= digit <= '9':  
        num_value = int(digit)
    else:  
        num_value = ord(digit) - ord('A') + 10 


    decimal_value += num_value * (B ** i)

print(decimal_value)  # 결과 출력
