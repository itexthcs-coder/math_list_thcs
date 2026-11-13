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


def bt_Dang16_p2_b2_c4_hh9(self):
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
    ab = random.choice([40, 50, 60])
    goc = random.choice([35, 40, 42])
    d_val = ab * math.tan(math.radians(goc))
    d_round = int(Decimal(str(d_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    d_sai = d_round + 9

    ac_val = ab / math.cos(math.radians(goc))
    ac_round = int(Decimal(str(ac_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    ac_sai = ac_round - 10

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (B) at (3.8,0);\n'
        '\\coordinate (C) at (3.8,3.1);\n'
        '\\draw[line width=1pt] (-0.6,0)--(4.6,0) (-0.6,3.1)--(4.6,3.1);\n'
        '\\draw[line width=1pt] (A)--(C);\n'
        '\\draw[line width=1pt, dashed] (B)--(C);\n'
        '\\draw[line width=1pt] (3.55,0)--(3.55,0.25)--(3.8,0.25);\n'
        '\\draw[line width=1pt] (0.7,0) arc (0:39:0.7);\n'
        '\\node at (1.05,0.25) {$%s^\\circ$};\n'
        '\\fill (A) circle (1pt) node[below] {$A$};\n'
        '\\fill (B) circle (1pt) node[below] {$B$};\n'
        '\\fill (C) circle (1pt) node[above] {$C$};\n'
        '\\node[below] at (1.9,0) {$%s\\text{ m}$};\n'
        '\\node[right] at (3.8,1.55) {$d$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (goc, ab)

    noidungcauhoi = (
        'Để đo chiều rộng $d$ của một dòng sông, người ta chọn hai điểm $A, B$ trên một bờ sông cách nhau $%s\\text{ m}$ sao cho điểm $B$ đối diện vuông góc với một gốc cây $C$ bên kia bờ, còn điểm $A$ nhìn gốc cây $C$ dưới một góc $%s^\\circ$ so với bờ sông (làm tròn đến mét).\\n%s'
        % (ab, goc, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Chiều rộng $d$ của dòng sông được tính bởi công thức $d = %s \\cdot \\tan %s^\\circ$' % (ab, goc)
    nb_da_1_s = 'Chiều rộng $d$ của dòng sông được tính bởi công thức $d = %s \\cdot \\cot %s^\\circ$' % (ab, goc)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Xét tam giác $ABC$ vuông tại $B$, theo Định lí 2 ta có: $d = BC = AB \\cdot \\tan A = %s \\cdot \\tan %s^\\circ$.'
        % (ab, goc)
    )

    # Thông hiểu
    th_da_1_d = '\\True Chiều rộng $d$ của dòng sông xấp xỉ bằng $%s\\text{ m}$' % (d_round)
    th_da_1_s = 'Chiều rộng $d$ của dòng sông xấp xỉ bằng $%s\\text{ m}$' % (d_sai)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Ta có $d = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ m}$.'
        % (ab, goc, d_round)
    )

    # Vận dụng
    vd_da_1_d = '\\True Khoảng cách đường nhìn xiên từ điểm quan sát $A$ đến gốc cây $C$ xấp xỉ bằng $%s\\text{ m}$' % (ac_round)
    vd_da_1_s = 'Khoảng cách đường nhìn xiên từ điểm quan sát $A$ đến gốc cây $C$ xấp xỉ bằng $%s\\text{ m}$' % (ac_sai)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Trong tam giác $ABC$ vuông tại $B$, ta có $\\cos A = \\dfrac{AB}{AC}$, suy ra '
        '$AC = \\dfrac{AB}{\\cos %s^\\circ} = \\dfrac{%s}{\\cos %s^\\circ} \\approx %s\\text{ m}$.'
        % (goc, ab, goc, ac_round)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu góc nhìn đo được là $45^\\circ$ thì chiều rộng dòng sông bằng $%s\\text{ m}$' % (ab)
    vdc_da_1_s = 'Nếu góc nhìn đo được là $45^\\circ$ thì chiều rộng dòng sông bằng $%s\\sqrt{2}\\text{ m}$' % (ab // 2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Khi góc nhìn bằng $45^\\circ$, tam giác $ABC$ vuông cân tại $B$ nên $d = %s \\cdot \\tan 45^\\circ = %s\\text{ m}$.'
        % (ab, ab)
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
