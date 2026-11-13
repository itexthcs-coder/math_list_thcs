import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    k = random.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6])
    nghiem = k**3
    
    da = f'$x = {nghiem}$'
    s = [
        f'$x = {-nghiem}$',
        f'$x = {k**2}$',
        f'$x = {3*k}$',
        f'$x = {nghiem + 1}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Giá trị của $x$ thỏa mãn $\\sqrt[3]{{x}} = {k}$ là'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Theo định nghĩa căn bậc ba, $\\sqrt[3]{{x}} = {k} \\Leftrightarrow x = ({k})^3 = {nghiem}$.' if k < 0 else f'Theo định nghĩa căn bậc ba, $\\sqrt[3]{{x}} = {k} \\Leftrightarrow x = {k}^3 = {nghiem}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
