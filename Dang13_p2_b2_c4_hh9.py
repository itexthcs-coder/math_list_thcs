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


def bt_Dang13_p2_b2_c4_hh9(self):
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
    ab = random.choice([1.2, 1.5, 1.6])
    he_so = random.choice([4, 5])
    bc = round(ab * he_so, 2)
    mat = random.choice([1.6, 1.65, 1.7])

    ab_str = fmt_num(ab)
    bc_str = fmt_num(bc)
    mat_str = fmt_num(mat)

    tan_val = mat / ab
    tan_str = fmt_num(tan_val) if round(tan_val, 4) == tan_val else rnd(tan_val, 3)

    cay_val = mat * he_so
    cay_str = fmt_num(cay_val)
    cay_sai_str = fmt_num(mat * (he_so - 1))

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (B) at (1.5,0);\n'
        '\\coordinate (C) at (5.2,0);\n'
        '\\coordinate (M) at (0,1.2);\n'
        '\\coordinate (N) at (5.2,3.4);\n'
        '\\draw[line width=1pt] (-0.3,0)--(5.6,0);\n'
        '\\draw[line width=1pt] (A)--(M) (C)--(N) (M)--(B)--(N);\n'
        '\\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);\n'
        '\\draw[line width=1pt] (4.98,0)--(4.98,0.22)--(5.2,0.22);\n'
        '\\draw[line width=1pt] (1.05,0) arc (180:141:0.45);\n'
        '\\draw[line width=1pt] (1.95,0) arc (0:43:0.45);\n'
        '\\fill (A) circle (1pt) node[below] {$A$};\n'
        '\\fill (B) circle (1pt) node[below] {$B$};\n'
        '\\fill (C) circle (1pt) node[below] {$C$};\n'
        '\\fill (M) circle (1pt) node[left] {$M$};\n'
        '\\fill (N) circle (1pt) node[right] {$N$};\n'
        '\\node[left] at (0,0.6) {$%s$};\n'
        '\\node[below] at (0.75,0) {$%s$};\n'
        '\\node[below] at (3.35,0) {$%s$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (mat_str, ab_str, bc_str)

    noidungcauhoi = (
        'Một người đứng tại điểm $A$, cách gương phẳng đặt nằm ngang trên mặt đất tại điểm $B$ là $%s\\text{ m}$, nhìn thấy hình phản chiếu qua gương của ngọn cây mọc thẳng đứng tại gốc $C$ cách $B$ là $%s\\text{ m}$ ($B$ nằm giữa $A$ và $C$). Biết khoảng cách từ mặt đất đến mắt người đó là $%s\\text{ m}$.\\n%s'
        % (ab_str, bc_str, mat_str, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Theo định luật phản xạ ánh sáng, góc tạo bởi tia tới và mặt đất bằng góc tạo bởi tia phản xạ và mặt đất'
    nb_da_1_s = 'Theo định luật phản xạ ánh sáng, góc tạo bởi tia tới và mặt đất gấp đôi góc tạo bởi tia phản xạ và mặt đất'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Gọi $M$ là vị trí mắt người và $N$ là ngọn cây. Theo định luật phản xạ ánh sáng, tia tới $NB$ và tia phản xạ $BM$ tạo với pháp tuyến tại $B$ hai góc bằng nhau, nên hai góc phụ với chúng là $\\widehat{ABM}$ và $\\widehat{CBN}$ bằng nhau.'
    )

    # Thông hiểu
    th_da_1_d = '\\True Giá trị tang của góc tạo bởi tia nhìn từ mắt người đến gương và mặt đất bằng $%s$' % (tan_str)
    th_da_1_s = 'Giá trị tang của góc tạo bởi tia nhìn từ mắt người đến gương và mặt đất bằng $\\dfrac{%s}{%s}$' % (ab_str, mat_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Xét tam giác $ABM$ vuông tại $A$, ta có: $\\tan \\widehat{ABM} = \\dfrac{AM}{AB} = \\dfrac{%s}{%s} = %s$.'
        % (mat_str, ab_str, tan_str)
    )

    # Vận dụng
    vd_da_1_d = '\\True Chiều cao của cây gấp $%s$ lần chiều cao từ mặt đất đến mắt người quan sát' % (he_so)
    vd_da_1_s = 'Chiều cao của cây gấp $%s$ lần chiều cao từ mặt đất đến mắt người quan sát' % (he_so - 1)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Vì $\\widehat{CBN} = \\widehat{ABM}$ nên $\\tan \\widehat{CBN} = \\tan \\widehat{ABM} \\Rightarrow \\dfrac{CN}{BC} = \\dfrac{AM}{AB} \\Rightarrow \\dfrac{CN}{AM} = \\dfrac{BC}{AB} = \\dfrac{%s}{%s} = %s$.'
        % (bc_str, ab_str, he_so)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Chiều cao của cây là $%s\\text{ m}$' % (cay_str)
    vdc_da_1_s = 'Chiều cao của cây là $%s\\text{ m}$' % (cay_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Chiều cao của cây là: $CN = %s \\cdot AM = %s \\cdot %s = %s\\text{ m}$.'
        % (he_so, he_so, mat_str, cay_str)
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
