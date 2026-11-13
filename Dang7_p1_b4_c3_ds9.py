import random
import math
from sympy import Rational, latex

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    tu = random.choice([1, 2, 3, 4, 5])
    mau = random.choice([2, 3, 4, 5, 7])
    while math.gcd(tu, mau) != 1:
        mau = random.choice([2, 3, 4, 5, 7])
        
    dau = random.choice([1, -1])
    phan_so_goc = Rational(dau * tu, mau)
    phan_so_lap_phuong = phan_so_goc**3
    
    da = f'${latex(phan_so_goc)}$'
    s = [
        f'${latex(-phan_so_goc)}$',
        f'${latex(phan_so_goc**2)}$',
        f'${latex(Rational(dau * (tu**3), mau))}$',
        f'${latex(Rational(dau * tu, mau**3))}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Kết quả của phép khai căn $\\sqrt[3]{{{latex(phan_so_lap_phuong)}}}$ là'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Vì $\\left({latex(phan_so_goc)}\\right)^3 = {latex(phan_so_lap_phuong)}$ nên $\\sqrt[3]{{{latex(phan_so_lap_phuong)}}} = {latex(phan_so_goc)}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
