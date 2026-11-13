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


def bt_Dang20_p2_b2_c4_hh9(self):
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
    cao_leu = random.choice([1.8, 2.0])
    day_leu = random.choice([4.4, 4.8])
    nua_day = round(day_leu / 2.0, 2)

    cao_leu_str = fmt_num(cao_leu)
    day_leu_str = fmt_num(day_leu)
    nua_day_str = fmt_num(nua_day)

    goc_leu_deg = math.degrees(math.atan(cao_leu / nua_day))
    do_leu = int(goc_leu_deg)
    phut_leu = int(Decimal(str((goc_leu_deg - do_leu) * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    if phut_leu == 60:
        do_leu += 1
        phut_leu = 0
    phut_leu_sai = (phut_leu + 20) % 60

    chan_cay = random.choice([5, 6])
    goc_cay = random.choice([20, 25])
    phan_dung_val = chan_cay * math.tan(math.radians(goc_cay))
    phan_dung_str = rnd(phan_dung_val, 1)
    phan_dung_sai_str = rnd(phan_dung_val + 1.1, 1)

    phan_gay_val = chan_cay / math.cos(math.radians(goc_cay))
    tong_cay_val = phan_dung_val + phan_gay_val
    tong_cay_str = rnd(tong_cay_val, 1)
    tong_cay_sai_str = rnd(phan_gay_val, 1)

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (H) at (1.8,0);\n'
        '\\coordinate (C) at (3.6,0);\n'
        '\\coordinate (A) at (1.8,1.8);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
        '\\draw[line width=1pt, dashed] (A)--(H);\n'
        '\\draw[line width=1pt] (1.8,0.22)--(2.02,0.22)--(2.02,0);\n'
        '\\draw[line width=1pt] (3.05,0) arc (180:135:0.55);\n'
        '\\node at (2.8,0.22) {$\\alpha$};\n'
        '\\fill (A) circle (1pt) node[above] {$A$};\n'
        '\\fill (B) circle (1pt) node[below left] {$B$};\n'
        '\\fill (H) circle (1pt) node[below] {$H$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\node[left] at (1.8,0.9) {$%s\\text{ m}$};\n'
        '\\node[below] at (1.8,-0.35) {$%s\\text{ m}$};\n'
        '\\coordinate (M) at (5.0,0);\n'
        '\\coordinate (N) at (8.5,0);\n'
        '\\coordinate (P) at (8.5,1.5);\n'
        '\\draw[line width=1pt] (M)--(N)--(P)--cycle;\n'
        '\\draw[line width=1pt] (8.28,0)--(8.28,0.22)--(8.5,0.22);\n'
        '\\draw[line width=1pt] (5.75,0) arc (0:23:0.75);\n'
        '\\node at (6.15,0.22) {$%s^\\circ$};\n'
        '\\fill (M) circle (1pt) node[below left] {$M$};\n'
        '\\fill (N) circle (1pt) node[below right] {$N$};\n'
        '\\fill (P) circle (1pt) node[above right] {$P$};\n'
        '\\node[below] at (6.75,0) {$%s\\text{ m}$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (cao_leu_str, day_leu_str, goc_cay, chan_cay)

    noidungcauhoi = (
        'Xét hai tình huống đo đạc thực tế sau:\\n'
        '\\textbullet\\ \\textit{Tình huống 1:} Một túp lều có mặt cắt là tam giác cân $ABC$, chiều cao đỉnh lều $AH = %s\\text{ m}$ và bề rộng đáy lều $BC = %s\\text{ m}$.\\n'
        '\\textbullet\\ \\textit{Tình huống 2:} Một cây cao bị gãy ngang tại $P$, ngọn cây đổ xuống mặt đất tại $M$ tạo với mặt đất góc $%s^\\circ$ và chắn ngang lối đi $MN = %s\\text{ m}$ ($N$ là gốc cây).\\n%s'
        % (cao_leu_str, day_leu_str, goc_cay, chan_cay, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Ở tình huống 1, góc nghiêng $\\alpha$ giữa cạnh mái lều và mặt đất thỏa mãn $\\tan \\alpha = \\dfrac{%s}{%s}$' % (cao_leu_str, nua_day_str)
    nb_da_1_s = 'Ở tình huống 1, góc nghiêng $\\alpha$ giữa cạnh mái lều và mặt đất thỏa mãn $\\tan \\alpha = \\dfrac{%s}{%s}$' % (cao_leu_str, day_leu_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Vì tam giác $ABC$ cân tại $A$ nên đường cao $AH$ đồng thời là đường trung tuyến, suy ra $HC = \\dfrac{BC}{2} = %s\\text{ m}$. '
        'Xét tam giác $AHC$ vuông tại $H$, ta có $\\tan \\alpha = \\dfrac{AH}{HC} = \\dfrac{%s}{%s}$.'
        % (nua_day_str, cao_leu_str, nua_day_str)
    )

    # Thông hiểu
    th_da_1_d = '\\True Ở tình huống 1, góc $\\alpha$ giữa cạnh mái lều và mặt đất (làm tròn đến phút) bằng $%s^\\circ %s\'$' % (do_leu, phut_leu)
    th_da_1_s = 'Ở tình huống 1, góc $\\alpha$ giữa cạnh mái lều và mặt đất (làm tròn đến phút) bằng $%s^\\circ %s\'$' % (do_leu, phut_leu_sai)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Từ $\\tan \\alpha = \\dfrac{%s}{%s}$, bấm máy tính đổi sang độ và phút ta được $\\alpha \\approx %s^\\circ %s\'$.'
        % (cao_leu_str, nua_day_str, do_leu, phut_leu)
    )

    # Vận dụng
    vd_da_1_d = '\\True Ở tình huống 2, phần thân cây còn đứng thẳng đứng cao xấp xỉ $%s\\text{ m}$ (làm tròn đến hàng phần mười)' % (phan_dung_str)
    vd_da_1_s = 'Ở tình huống 2, phần thân cây còn đứng thẳng đứng cao xấp xỉ $%s\\text{ m}$ (làm tròn đến hàng phần mười)' % (phan_dung_sai_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Xét tam giác $MNP$ vuông tại $N$, phần thân cây còn đứng thẳng đứng là: '
        '$NP = MN \\cdot \\tan %s^\\circ = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ m}$.'
        % (goc_cay, chan_cay, goc_cay, phan_dung_str)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Ở tình huống 2, chiều cao ban đầu của cây trước khi bị gãy (làm tròn đến hàng phần mười) xấp xỉ bằng $%s\\text{ m}$' % (tong_cay_str)
    vdc_da_1_s = 'Ở tình huống 2, chiều cao ban đầu của cây trước khi bị gãy (làm tròn đến hàng phần mười) xấp xỉ bằng $%s\\text{ m}$' % (tong_cay_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Độ dài phần ngọn cây bị gãy đổ là: $MP = \\dfrac{MN}{\\cos %s^\\circ} = \\dfrac{%s}{\\cos %s^\\circ}$. '
        'Chiều cao ban đầu của cây trước khi bị gãy là: '
        '$NP + MP = %s \\cdot \\tan %s^\\circ + \\dfrac{%s}{\\cos %s^\\circ} \\approx %s\\text{ m}$.'
        % (goc_cay, chan_cay, goc_cay, chan_cay, goc_cay, chan_cay, goc_cay, tong_cay_str)
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
