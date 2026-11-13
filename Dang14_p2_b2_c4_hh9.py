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


def bt_Dang14_p2_b2_c4_hh9(self):
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
    ab = random.choice([1, 2])
    ec = random.choice([2, 3, 4])
    cd = ab + ec
    ad = random.choice([5, 6, 7, 8])

    g = math.gcd(ec, ad)
    tu = ec // g
    mau = ad // g

    goc_deg = math.degrees(math.atan(ec / ad))
    do_val = int(goc_deg)
    phut_val = int(Decimal(str((goc_deg - do_val) * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    if phut_val == 60:
        do_val += 1
        phut_val = 0
    phut_sai = (phut_val + 18) % 60

    bc_val = math.sqrt(ad**2 + ec**2)
    bc_str = rnd(bc_val, 1)
    bc_sai_str = rnd(bc_val + 1.5, 1)

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (I) at (0,0);\n'
        '\\coordinate (A) at (1.5,0);\n'
        '\\coordinate (D) at (5.2,0);\n'
        '\\coordinate (B) at (1.5,0.9);\n'
        '\\coordinate (E) at (5.2,0.9);\n'
        '\\coordinate (C) at (5.2,3.1);\n'
        '\\draw[line width=1pt] (A)--(D)--(C)--(B)--cycle;\n'
        '\\draw[line width=1pt, dashed] (I)--(A) (I)--(B) (B)--(E);\n'
        '\\draw[line width=1pt] (1.5,0.22)--(1.72,0.22)--(1.72,0);\n'
        '\\draw[line width=1pt] (4.98,0)--(4.98,0.22)--(5.2,0.22);\n'
        '\\draw[line width=1pt] (4.98,0.9)--(4.98,1.12)--(5.2,1.12);\n'
        '\\draw[line width=1pt] (0.65,0) arc (0:31:0.65);\n'
        '\\node at (0.95,0.22) {$\\alpha$};\n'
        '\\fill (I) circle (1pt) node[below] {$I$};\n'
        '\\fill (A) circle (1pt) node[below] {$A$};\n'
        '\\fill (D) circle (1pt) node[below] {$D$};\n'
        '\\fill (B) circle (1pt) node[above left] {$B$};\n'
        '\\fill (E) circle (1pt) node[right] {$E$};\n'
        '\\fill (C) circle (1pt) node[above right] {$C$};\n'
        '\\node[left] at (1.5,0.45) {$%s$};\n'
        '\\node[below] at (3.35,0) {$%s$};\n'
        '\\node[right] at (5.2,1.55) {$%s$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (ab, ad, cd)

    noidungcauhoi = (
        'Một bức tường đang xây dở có dạng hình thang vuông $ABCD$, vuông góc ở $A$ và $D$, với $AB = %s\\text{ m}$, $CD = %s\\text{ m}$, $AD = %s\\text{ m}$ (góc làm tròn đến phút, độ dài làm tròn đến chữ số thập phân thứ nhất).\\n%s'
        % (ab, cd, ad, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Kẻ $BE \\perp CD$ tại $E$, ta có $BE = %s\\text{ m}$ và $EC = %s\\text{ m}$' % (ad, ec)
    nb_da_1_s = 'Kẻ $BE \\perp CD$ tại $E$, ta có $BE = %s\\text{ m}$ và $EC = %s\\text{ m}$' % (ad, cd)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Tứ giác $ABED$ là hình chữ nhật (vì $\\widehat{A} = \\widehat{D} = \\widehat{BED} = 90^\\circ$) nên $BE = AD = %s\\text{ m}$ và $ED = AB = %s\\text{ m}$. '
        'Suy ra $EC = CD - ED = %s - %s = %s\\text{ m}$.'
        % (ad, ab, cd, ab, ec)
    )

    # Thông hiểu
    th_da_1_d = '\\True Góc $\\alpha$ tạo bởi đường thẳng $BC$ và mặt đất $AD$ thỏa mãn $\\tan \\alpha = \\dfrac{%s}{%s}$' % (tu, mau)
    th_da_1_s = 'Góc $\\alpha$ tạo bởi đường thẳng $BC$ và mặt đất $AD$ thỏa mãn $\\tan \\alpha = \\dfrac{%s}{%s}$' % (mau, tu)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Gọi $I$ là giao điểm của $BC$ và $AD$. Vì $BE // AD$ nên $\\widehat{EBC} = \\widehat{DIC} = \\alpha$ (hai góc đồng vị). '
        'Xét tam giác $BEC$ vuông tại $E$, ta có: $\\tan \\alpha = \\tan \\widehat{EBC} = \\dfrac{EC}{BE} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.'
        % (ec, ad, tu, mau)
    )

    # Vận dụng
    vd_da_1_d = '\\True Số đo góc $\\alpha$ xấp xỉ bằng $%s^\\circ %s\'$' % (do_val, phut_val)
    vd_da_1_s = 'Số đo góc $\\alpha$ xấp xỉ bằng $%s^\\circ %s\'$' % (do_val, phut_sai)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Từ $\\tan \\alpha = \\dfrac{%s}{%s}$, bấm máy tính ta tính được $\\alpha \\approx %s^\\circ %s\'$.'
        % (tu, mau, do_val, phut_val)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Độ dài cạnh nghiêng $BC$ của bức tường xấp xỉ bằng $%s\\text{ m}$' % (bc_str)
    vdc_da_1_s = 'Độ dài cạnh nghiêng $BC$ của bức tường xấp xỉ bằng $%s\\text{ m}$' % (bc_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Áp dụng định lí Pythagore vào tam giác $BEC$ vuông tại $E$, ta có: '
        '$BC = \\sqrt{BE^2 + EC^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} \\approx %s\\text{ m}$.'
        % (ad, ec, ad**2 + ec**2, bc_str)
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
