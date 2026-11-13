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


def bt_Dang12_p2_b2_c4_hh9(self):
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
    gk = random.choice([1.5, 1.6, 1.7])
    gk_str = fmt_num(gk)
    nm = random.choice([20, 25, 30])
    alpha = random.choice([27, 30, 32])
    beta = random.choice([18, 19, 21])

    cot_a = 1.0 / math.tan(math.radians(alpha))
    cot_b = 1.0 / math.tan(math.radians(beta))
    ph_val = nm / (cot_b - cot_a)
    ph_str = rnd(ph_val, 2)
    ph_sai_str = rnd(ph_val + 4.5, 2)

    h_lau_dai = float(Decimal(str(ph_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)) + gk
    h_ld_str = rnd(h_lau_dai, 2)
    h_ld_sai_str = rnd(h_lau_dai - gk, 2)

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (N) at (0,0);\n'
        '\\coordinate (M) at (1.8,0);\n'
        '\\coordinate (P) at (5.4,0);\n'
        '\\coordinate (N1) at (0,0.5);\n'
        '\\coordinate (M1) at (1.8,0.5);\n'
        '\\coordinate (H) at (5.4,0.5);\n'
        '\\coordinate (P1) at (5.4,2.8);\n'
        '\\draw[line width=1pt] (-0.3,0)--(5.8,0);\n'
        '\\draw[line width=1pt] (N)--(N1) (M)--(M1) (P)--(P1);\n'
        '\\draw[line width=1pt] (N1)--(H) (N1)--(P1) (M1)--(P1);\n'
        '\\draw[line width=1pt] (5.18,0.5)--(5.18,0.72)--(5.4,0.72);\n'
        '\\draw[line width=1pt] (0.75,0.5) arc (0:23:0.75);\n'
        '\\node at (1.05,0.68) {$%s^\\circ$};\n'
        '\\draw[line width=1pt] (2.45,0.5) arc (0:33:0.65);\n'
        '\\node at (2.75,0.72) {$%s^\\circ$};\n'
        '\\fill (N) circle (1pt) node[below] {$N$};\n'
        '\\fill (M) circle (1pt) node[below] {$M$};\n'
        '\\fill (P) circle (1pt) node[below] {$P$};\n'
        '\\fill (N1) circle (1pt) node[above left] {$N\'$};\n'
        '\\fill (M1) circle (1pt) node[above left] {$M\'$};\n'
        '\\fill (H) circle (1pt) node[right] {$H$};\n'
        '\\fill (P1) circle (1pt) node[above right] {$P\'$};\n'
        '\\node[below] at (0.9,0) {$%s\\text{ m}$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (beta, alpha, nm)

    noidungcauhoi = (
        'Để đo chiều cao của một tòa lâu đài, người ta đặt giác kế thẳng đứng cao $%s\\text{ m}$ tại điểm $M$ thì nhìn thấy đỉnh $P\'$ dưới góc nâng $\\alpha = %s^\\circ$. Lùi ra xa thêm $%s\\text{ m}$ đến điểm $N$ ($NM = %s\\text{ m}$), đặt giác kế thẳng đứng thì nhìn thấy đỉnh $P\'$ dưới góc nâng $\\beta = %s^\\circ$ (kết quả làm tròn đến chữ số thập phân thứ hai).\\n%s'
        % (gk_str, alpha, nm, nm, beta, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Gọi $H$ là hình chiếu của $P\'$ trên đường thẳng nằm ngang qua ống ngắm, ta có $M\'H = P\'H \\cdot \\cot %s^\\circ$' % (alpha)
    nb_da_1_s = 'Gọi $H$ là hình chiếu của $P\'$ trên đường thẳng nằm ngang qua ống ngắm, ta có $M\'H = P\'H \\cdot \\sin %s^\\circ$' % (alpha)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Xét tam giác $P\'M\'H$ vuông tại $H$ có $\\widehat{P\'M\'H} = %s^\\circ$. Theo Định lí 2, ta có: $M\'H = P\'H \\cdot \\cot %s^\\circ$.'
        % (alpha, alpha)
    )

    # Thông hiểu
    th_da_1_d = '\\True Khoảng cách $N\'H$ thỏa mãn hệ thức $N\'H = P\'H \\cdot \\cot %s^\\circ$' % (beta)
    th_da_1_s = 'Khoảng cách $N\'H$ thỏa mãn hệ thức $N\'H = P\'H \\cdot \\tan %s^\\circ$' % (beta)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Tương tự, xét tam giác $P\'N\'H$ vuông tại $H$ có $\\widehat{P\'N\'H} = %s^\\circ$, ta có: $N\'H = P\'H \\cdot \\cot %s^\\circ$.'
        % (beta, beta)
    )

    # Vận dụng
    vd_da_1_d = '\\True Độ cao $P\'H$ tính từ tầm ngắm giác kế đến đỉnh lâu đài xấp xỉ bằng $%s\\text{ m}$' % (ph_str)
    vd_da_1_s = 'Độ cao $P\'H$ tính từ tầm ngắm giác kế đến đỉnh lâu đài xấp xỉ bằng $%s\\text{ m}$' % (ph_sai_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Ta có $N\'M\' = NM = %s\\text{ m}$ và $N\'H - M\'H = N\'M\'$, suy ra '
        '$P\'H(\\cot %s^\\circ - \\cot %s^\\circ) = %s \\Rightarrow P\'H = \\dfrac{%s}{\\cot %s^\\circ - \\cot %s^\\circ} \\approx %s\\text{ m}$.'
        % (nm, beta, alpha, nm, nm, beta, alpha, ph_str)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Chiều cao thực tế của tòa lâu đài tính từ mặt đất xấp xỉ bằng $%s\\text{ m}$' % (h_ld_str)
    vdc_da_1_s = 'Chiều cao thực tế của tòa lâu đài tính từ mặt đất xấp xỉ bằng $%s\\text{ m}$' % (h_ld_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Chiều cao của tòa lâu đài là: $P\'P = P\'H + HP = %s + %s = %s\\text{ m}$.'
        % (ph_str, gk_str, h_ld_str)
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
