import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    k = random.randint(2, 6)
    chenh = random.choice([-3, -2, -1, 1, 2, 3])
    so_trong_can = k**3 + chenh
    
    if k**3 > so_trong_can:
        da = '$a > b$'
        dau_ss = '>'
    else:
        da = '$a < b$'
        dau_ss = '<'
        
    s = [
        '$a > b$',
        '$a < b$',
        '$a = b$',
        'Không so sánh được'
    ]
    s.remove(da)
    
    das1 = s[0]
    das2 = s[1]
    das3 = s[2]
    
    noidungcauhoi = f'So sánh hai số $a = {k}$ và $b = \\sqrt[3]{{{so_trong_can}}}$, khẳng định nào sau đây đúng?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Ta có $a = {k} = \\sqrt[3]{{{k}^3}} = \\sqrt[3]{{{k**3}}}$. Vì ${k**3} {dau_ss} {so_trong_can}$ nên $\\sqrt[3]{{{k**3}}} {dau_ss} \\sqrt[3]{{{so_trong_can}}}$, hay $a {dau_ss} b$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
