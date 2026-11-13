import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    bien = random.choice(['a', 'x', 'm', 'A'])
    
    da = 'Chỉ số của căn.'
    s = [
        'Số mũ của biểu thức lấy căn.',
        'Hệ số của căn thức.',
        'Bậc của đa thức.',
        'Cơ số của lũy thừa.'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Trong kí hiệu $\\sqrt[3]{{{bien}}}$, số $3$ được gọi là gì?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Trong kí hiệu $\\sqrt[3]{{{bien}}}$, số $3$ được gọi là chỉ số của căn.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
