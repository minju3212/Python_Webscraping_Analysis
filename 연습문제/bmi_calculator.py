weight = int(input("체중(kg): "))
height = int(input("키(cm): "))
m_height = height / 100
bmi = weight / (m_height**2)
print(f'BMI : {bmi:.1f}')