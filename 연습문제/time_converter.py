a_second = 12345
hour = a_second // 3600
r_second = a_second % 3600
minute = r_second // 60
second = r_second % 60
print(f'{a_second}초는 {hour}시간 {minute}분 {second}초입니다.')