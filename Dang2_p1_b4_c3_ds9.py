import random

lisdang = ['1']
dang = random.choice(lisdang)

if dang == '1':
    loai_so = random.choice(['số thực bất kì', 'số thực âm', 'số thực dương'])
    
    if loai_so == 'số thực bất kì':
        da = 'Mọi số thực đều có duy nhất một căn bậc ba.'
        s = [
            'Chỉ có số thực không âm mới có căn bậc ba.',
            'Mọi số thực dương đều có hai căn bậc ba đối nhau.',
            'Số thực âm không có căn bậc ba.',
            'Mọi số thực đều có hai căn bậc ba.'
        ]
        giai_thich = 'Mỗi số thực $a$ đều có duy nhất một căn bậc ba.'
    elif loai_so == 'số thực âm':
        da = 'Mỗi số thực âm đều có duy nhất một căn bậc ba và đó là số âm.'
        s = [
            'Số thực âm không có căn bậc ba.',
            'Mỗi số thực âm có hai căn bậc ba đối nhau.',
            'Căn bậc ba của một số thực âm là một số dương.',
            'Số thực âm có vô số căn bậc ba.'
        ]
        giai_thich = 'Mỗi số thực $a$ đều có duy nhất một căn bậc ba. Nếu $a < 0$ thì $\\sqrt[3]{a} < 0$.'
    else:
        da = 'Mỗi số thực dương đều có duy nhất một căn bậc ba và đó là số dương.'
        s = [
            'Mỗi số thực dương có hai căn bậc ba đối nhau.',
            'Căn bậc ba của một số thực dương có thể là số âm.',
            'Số thực dương không có căn bậc ba.',
            'Căn bậc ba của số thực dương $a$ là $\\pm\\sqrt[3]{a}$.'
        ]
        giai_thich = 'Mỗi số thực $a$ đều có duy nhất một căn bậc ba. Nếu $a > 0$ thì $\\sqrt[3]{a} > 0$.'

    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    
    noidungcauhoi = f'Khẳng định nào sau đây đúng khi nói về căn bậc ba của một {loai_so}?'
    
    da_d = '\\True ' + str(da)
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)
    
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    
    loigiai = giai_thich

content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\choice \n' '{' + str(list_1[1]) + '}\n' '{' + str(list_1[2]) + '}\n' '{' + str(list_1[3]) + '}\n' '{' + str(list_1[0]) + '}\n' '\\loigiai{' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')
print(content)
