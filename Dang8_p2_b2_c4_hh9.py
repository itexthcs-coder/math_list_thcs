import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_Dang8_p2_b2_c4_hh9(self):
    def rnd(val, n):
        q = '1' if n == 0 else '0.' + '0' * (n - 1) + '1'
        d = Decimal(str(val)).quantize(Decimal(q), rounding=ROUND_HALF_UP)
        s = str(d)
        if '.' in s:
            s = s.replace('.', ',')
        return s

    def fmt_num(val):
        if isinstance(val, int):
            return str(val)
        if isinstance(val, float) and val.is_integer():
            return str(int(val))
        s = str(round(val, 4))
        if '.' in s:
            s = s.rstrip('0').rstrip(',')
            s = s.replace('.', ',')
        return s

    # Khai báo biến
    rong = random.choice([200, 250, 300])
    cheo = rong + random.choice([60, 70, 80, 100])
    g = math.gcd(rong, cheo)
    tu = rong // g
    mau = cheo // g

    goc_deg = math.degrees(math.acos(rong / cheo))
    do_val = int(goc_deg)
    phut_val = int(Decimal(str((goc_deg - do_val) * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    if phut_val == 60:
        do_val += 1
        phut_val = 0
    phut_sai = (phut_val + 15) % 60

    troi_val = math.sqrt(cheo**2 - rong**2)
    troi_str = rnd(troi_val, 1)
    troi_sai_str = rnd(troi_val + 25.3, 1)

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (B) at (0,3.2);\n'
        '\\coordinate (C) at (2.8,3.2);\n'
        '\\draw[line width=1pt] (-0.8,0)--(3.8,0) (-0.8,3.2)--(3.8,3.2);\n'
        '\\draw[line width=1pt, dashed] (A)--(B) (B)--(C);\n'
        '\\draw[line width=1pt] (A)--(C);\n'
        '\\draw[line width=1pt] (0,2.95)--(0.25,2.95)--(0.25,3.2);\n'
        '\\draw[line width=1pt] (0,0.65) arc (90:49:0.65);\n'
        '\\node at (0.28,0.85) {$\\alpha$};\n'
        '\\fill (A) circle (1pt) node[below] {$A$};\n'
        '\\fill (B) circle (1pt) node[above] {$B$};\n'
        '\\fill (C) circle (1pt) node[above] {$C$};\n'
        '\\node[left] at (0,1.6) {$%s\\text{ m}$};\n'
        '\\node[below right] at (1.4,1.6) {$%s\\text{ m}$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (rong, cheo)

    noidungcauhoi = (
        'Một khúc sông rộng $%s\\text{ m}$. Một con đò chèo qua sông bị dòng nước đẩy xiên nên phải chèo một quãng đường dài $%s\\text{ m}$ mới sang được bờ bên kia (góc làm tròn đến phút).\\n%s'
        % (rong, cheo, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Trong mô hình tam giác vuông, quãng đường con đò chèo $%s\\text{ m}$ đóng vai trò là cạnh huyền' % (cheo)
    nb_da_1_s = 'Trong mô hình tam giác vuông, chiều rộng khúc sông $%s\\text{ m}$ đóng vai trò là cạnh huyền' % (rong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Gọi $A$ là điểm xuất phát, $B$ là điểm đối diện $A$ qua bờ bên kia ($AB \\perp BC$) và $C$ là điểm con đò cập bến. '
        'Tam giác $ABC$ vuông tại $B$ có cạnh huyền là quãng đường chèo $AC = %s\\text{ m}$, cạnh góc vuông $AB = %s\\text{ m}$.'
        % (cheo, rong)
    )

    # Thông hiểu
    th_da_1_d = '\\True Gọi $\\alpha$ là góc lệch của hướng con đò đi so với phương vuông góc với bờ sông thì $\\cos \\alpha = \\dfrac{%s}{%s}$' % (tu, mau)
    th_da_1_s = 'Gọi $\\alpha$ là góc lệch của hướng con đò đi so với phương vuông góc với bờ sông thì $\\sin \\alpha = \\dfrac{%s}{%s}$' % (tu, mau)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Trong tam giác $ABC$ vuông tại $B$, cạnh $AB$ kề với góc $\\alpha = \\widehat{BAC}$ nên '
        '$\\cos \\alpha = \\dfrac{AB}{AC} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.'
        % (rong, cheo, tu, mau)
    )

    # Vận dụng
    vd_da_1_d = '\\True Dòng nước đã đẩy con đò đi lệch một góc $\\alpha$ xấp xỉ bằng $%s^\\circ %s\'$' % (do_val, phut_val)
    vd_da_1_s = 'Dòng nước đã đẩy con đò đi lệch một góc $\\alpha$ xấp xỉ bằng $%s^\\circ %s\'$' % (do_val, phut_sai)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Từ $\\cos \\alpha = \\dfrac{%s}{%s}$, bấm máy tính chuyển sang độ và phút ta được $\\alpha \\approx %s^\\circ %s\'$.'
        % (tu, mau, do_val, phut_val)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Con đò đã bị dòng nước đẩy trôi xuôi theo bờ sông một đoạn xấp xỉ $%s\\text{ m}$' % (troi_str)
    vdc_da_1_s = 'Con đò đã bị dòng nước đẩy trôi xuôi theo bờ sông một đoạn xấp xỉ $%s\\text{ m}$' % (troi_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Đoạn đường con đò bị đẩy trôi xuôi theo bờ sông là cạnh $BC$: '
        '$BC = \\sqrt{AC^2 - AB^2} = \\sqrt{%s^2 - %s^2} \\approx %s\\text{ m}$.'
        % (cheo, rong, troi_str)
    )

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
