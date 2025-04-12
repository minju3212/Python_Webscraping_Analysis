id_number = "901212-1234567"
if id_number[7] == '1' or id_number[7] == '2':
    print(f'19{id_number[:2]}년 {id_number[2:4]}월 {id_number[4:6]}일')
elif id_number[7] == '3' or id_number[7] == '4':
    print(f'20{id_number[:2]}년 {id_number[2:4]}월 {id_number[4:6]}일')
else:
    print("잘못된 주민등록번호 형식입니다.")