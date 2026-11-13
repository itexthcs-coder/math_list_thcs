import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    bien_x = random.choice(['x', 'y', 'm', 't'])
    bien_a = random.choice(['a', 'b', 'c', 'n'])
    
    da = f'${bien_x}^3 = {bien_a}$'
    s = [
        f'${bien_x}^2 = {bien_a}$',
        f'${bien_a}^3 = {bien_x}$',
        f'${bien_x} = 3{bien_a}$',
        f'${bien_x}^3 = -{bien_a}$',
        f'${bien_x} = {bien_a}^2$'
    ]
    
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Căn bậc ba của một số thực ${bien_a}$ là số thực ${bien_x}$ thỏa mãn điều kiện nào sau đây?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = f'Theo định nghĩa, căn bậc ba của số thực ${bien_a}$ là số thực ${bien_x}$ thỏa mãn ${bien_x}^3 = {bien_a}$.'

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
