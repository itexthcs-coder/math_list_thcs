import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    k = random.randint(2, 12)
    a = k**3
    
    da = f'${k}$'
    s = [
        f'${k-1}$',
        f'${k+1}$',
        f'$-{k}$',
        f'${k**2}$',
        f'${3*k}$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Giá trị của $\\sqrt[3]{{{a}}}$ bằng bao nhiêu?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Vì ${k}^3 = {a}$ nên $\\sqrt[3]{{{a}}} = \\sqrt[3]{{{k}^3}} = {k}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
