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


def bt_Dang18_p2_b2_c4_hh9(self):
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
    ab = random.choice([3, 4])
    h_dap = 3.5
    tan_d = 1.25
    tan_c = 1.5
    dh = 2.8
    ck = 7.0 / 3.0
    cd_val = dh + ab + ck
    cd_str = rnd(cd_val, 1)
    cd_sai_str = rnd(cd_val + 1.4, 1)

    ad_val = math.sqrt(h_dap**2 + dh**2)
    ad_str = rnd(ad_val, 1)
    ad_sai_str = rnd(ad_val + 1.2, 1)

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (D) at (0,0);\n'
        '\\coordinate (H) at (1.5,0);\n'
        '\\coordinate (K) at (3.2,0);\n'
        '\\coordinate (C) at (4.5,0);\n'
        '\\coordinate (A) at (1.5,2.2);\n'
        '\\coordinate (B) at (3.2,2.2);\n'
        '\\draw[line width=1pt] (D)--(C)--(B)--(A)--cycle;\n'
        '\\draw[line width=1pt, dashed] (A)--(H) (B)--(K);\n'
        '\\draw[line width=1pt] (1.5,0.22)--(1.72,0.22)--(1.72,0);\n'
        '\\draw[line width=1pt] (3.2,0.22)--(3.42,0.22)--(3.42,0);\n'
        '\\fill (D) circle (1pt) node[below left] {$D$};\n'
        '\\fill (H) circle (1pt) node[below] {$H$};\n'
        '\\fill (K) circle (1pt) node[below] {$K$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\fill (A) circle (1pt) node[above left] {$A$};\n'
        '\\fill (B) circle (1pt) node[above right] {$B$};\n'
        '\\node[above] at (2.35,2.2) {$%s\\text{ m}$};\n'
        '\\node[right] at (1.5,1.1) {$3,5\\text{ m}$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (ab)

    noidungcauhoi = (
        'Mặt cắt ngang của một đập ngăn nước có dạng hình thang $ABCD$ với chiều rộng mặt trên $AB = %s\\text{ m}$ và chiều cao đập là $3,5\\text{ m}$. Biết độ dốc sườn $AD$ là $\\tan D = 1,25$ và độ dốc sườn $BC$ là $\\tan C = 1,5$ (các kết quả làm tròn đến $\\text{dm}$).\\n%s'
        % (ab, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Hình chiếu của sườn $AD$ lên đáy lớn $CD$ có độ dài là $2,8\\text{ m}$'
    nb_da_1_s = 'Hình chiếu của sườn $AD$ lên đáy lớn $CD$ có độ dài là $4,375\\text{ m}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Kẻ đường cao $AH$ và $BK$ của hình thang ($H, K \\in CD$). '
        'Xét tam giác $ADH$ vuông tại $H$, ta có $\\tan D = \\dfrac{AH}{DH}$, suy ra $DH = \\dfrac{AH}{\\tan D} = \\dfrac{3,5}{1,25} = 2,8\\text{ m}$.'
    )

    # Thông hiểu
    th_da_1_d = '\\True Hình chiếu của sườn $BC$ lên đáy lớn $CD$ có độ dài là $\\dfrac{7}{3}\\text{ m}$ (xấp xỉ $2,3\\text{ m}$)'
    th_da_1_s = 'Hình chiếu của sườn $BC$ lên đáy lớn $CD$ có độ dài là $5,25\\text{ m}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Xét tam giác $BCK$ vuông tại $K$, ta có $\\tan C = \\dfrac{BK}{CK}$, suy ra $CK = \\dfrac{BK}{\\tan C} = \\dfrac{3,5}{1,5} = \\dfrac{7}{3} \\approx 2,3\\text{ m}$.'
    )

    # Vận dụng
    vd_da_1_d = '\\True Chiều rộng $CD$ của chân đập xấp xỉ bằng $%s\\text{ m}$' % (cd_str)
    vd_da_1_s = 'Chiều rộng $CD$ của chân đập xấp xỉ bằng $%s\\text{ m}$' % (cd_sai_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Vì $ABKH$ là hình chữ nhật nên $HK = AB = %s\\text{ m}$. '
        'Chiều rộng chân đập là: $CD = DH + HK + CK = 2,8 + %s + \\dfrac{7}{3} \\approx %s\\text{ m}$.'
        % (ab, ab, cd_str)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Chiều dài sườn $AD$ xấp xỉ bằng $%s\\text{ m}$' % (ad_str)
    vdc_da_1_s = 'Chiều dài sườn $AD$ xấp xỉ bằng $%s\\text{ m}$' % (ad_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Áp dụng định lí Pythagore vào tam giác $ADH$ vuông tại $H$, ta có: '
        '$AD = \\sqrt{AH^2 + DH^2} = \\sqrt{3,5^2 + 2,8^2} = \\sqrt{20,09} \\approx %s\\text{ m}$.'
        % (ad_str)
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
