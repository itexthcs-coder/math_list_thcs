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


def bt_Dang9_p2_b2_c4_hh9(self):
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
    goc1 = random.choice([32, 34, 36, 38])
    bong1 = random.choice([8.6, 9.2, 10.5, 11.4])
    bong1_str = fmt_num(bong1)

    h1_val = bong1 * math.tan(math.radians(goc1))
    h1_round = int(Decimal(str(h1_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    h1_sai = h1_round + 3

    bong_cay1 = random.choice([20, 25, 30])
    h_cay1_str = rnd(bong_cay1 * math.tan(math.radians(goc1)), 1)
    h_cay1_sai_str = rnd(bong_cay1 / math.tan(math.radians(goc1)), 1)

    goc2 = random.choice([40, 42, 44])
    h_cay2_str = rnd(bong_cay1 * math.tan(math.radians(goc2)), 1)
    h_cay2_sai_str = rnd(bong_cay1 * math.sin(math.radians(goc2)), 1)

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (B) at (4.2,0);\n'
        '\\coordinate (C) at (4.2,2.8);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
        '\\draw[line width=1pt] (3.95,0)--(3.95,0.25)--(4.2,0.25);\n'
        '\\draw[line width=1pt] (0.75,0) arc (0:34:0.75);\n'
        '\\node at (1.15,0.25) {$%s^\\circ$};\n'
        '\\fill (A) circle (1pt) node[below left] {$A$};\n'
        '\\fill (B) circle (1pt) node[below right] {$B$};\n'
        '\\fill (C) circle (1pt) node[above right] {$C$};\n'
        '\\node[below] at (2.1,0) {$%s\\text{ m}$};\n'
        '\\node[right] at (4.2,1.4) {$h$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (goc1, bong1_str)

    noidungcauhoi = (
        'Vào một thời điểm trong ngày, các tia nắng mặt trời tạo với mặt đất một góc $%s^\\circ$ và bóng của một tòa tháp trên mặt đất dài $%s\\text{ m}$.\\n%s'
        % (goc1, bong1_str, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Chiều cao $h$ của tòa tháp được tính theo công thức $h = %s \\cdot \\tan %s^\\circ$' % (bong1_str, goc1)
    nb_da_1_s = 'Chiều cao $h$ của tòa tháp được tính theo công thức $h = %s \\cdot \\cot %s^\\circ$' % (bong1_str, goc1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Vì đường cao $h$ của tháp đối diện với góc $%s^\\circ$ (góc tạo bởi tia nắng mặt trời và bóng tháp trên mặt đất) nên theo Định lí 2 ta có: $h = %s \\cdot \\tan %s^\\circ$.'
        % (goc1, bong1_str, goc1)
    )

    # Thông hiểu
    th_da_1_d = '\\True Chiều cao của tòa tháp (làm tròn đến mét) xấp xỉ bằng $%s\\text{ m}$' % (h1_round)
    th_da_1_s = 'Chiều cao của tòa tháp (làm tròn đến mét) xấp xỉ bằng $%s\\text{ m}$' % (h1_sai)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Ta có $h = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ m}$.'
        % (bong1_str, goc1, h1_round)
    )

    # Vận dụng
    vd_da_1_d = '\\True Nếu cũng tại thời điểm đó, bóng của một cái cây dài $%s\\text{ m}$ thì chiều cao của cây xấp xỉ bằng $%s\\text{ m}$' % (bong_cay1, h_cay1_str)
    vd_da_1_s = 'Nếu cũng tại thời điểm đó, bóng của một cái cây dài $%s\\text{ m}$ thì chiều cao của cây xấp xỉ bằng $%s\\text{ m}$' % (bong_cay1, h_cay1_sai_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Cùng một thời điểm, góc tạo bởi tia nắng mặt trời và mặt đất vẫn là $%s^\\circ$ nên chiều cao của cây là: '
        '$h_{\\text{cây}} = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ m}$.'
        % (goc1, bong_cay1, goc1, h_cay1_str)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Khi tia nắng mặt trời tạo với mặt đất một góc $%s^\\circ$, một cái cây có bóng dài $%s\\text{ m}$ sẽ cao khoảng $%s\\text{ m}$ (làm tròn đến $\\text{dm}$)' % (goc2, bong_cay1, h_cay2_str)
    vdc_da_1_s = 'Khi tia nắng mặt trời tạo với mặt đất một góc $%s^\\circ$, một cái cây có bóng dài $%s\\text{ m}$ sẽ cao khoảng $%s\\text{ m}$ (làm tròn đến $\\text{dm}$)' % (goc2, bong_cay1, h_cay2_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Chiều cao của cây khi tia nắng tạo với mặt đất góc $%s^\\circ$ là: '
        '$h = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ m}$.'
        % (goc2, bong_cay1, goc2, h_cay2_str)
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
