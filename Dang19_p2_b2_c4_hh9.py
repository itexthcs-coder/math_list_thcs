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


def bt_Dang19_p2_b2_c4_hh9(self):
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
    goc = random.choice([21, 24, 25])
    qd1 = random.choice([200, 250, 300])
    sau1_val = qd1 * math.sin(math.radians(goc))
    sau1_round = int(Decimal(str(sau1_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    sau1_sai = sau1_round + 18

    v_kmh = random.choice([9, 12, 15])
    v_mphut = (v_kmh * 1000) // 60
    v_mphut_sai = v_mphut + 50

    sau2 = random.choice([200, 250])
    qd2_val = sau2 / math.sin(math.radians(goc))
    qd2_round = int(Decimal(str(qd2_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    qd2_sai = qd2_round - 80

    t_phut_val = qd2_val / v_mphut
    t_phut_str = rnd(t_phut_val, 1)
    t_phut_sai_str = rnd(t_phut_val + 1.8, 1)

    hinh_tikz = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (H) at (4.5,0);\n'
        '\\coordinate (B) at (4.5,-2.0);\n'
        '\\draw[line width=1pt] (-0.5,0)--(5.0,0);\n'
        '\\draw[line width=1pt] (A)--(B);\n'
        '\\draw[line width=1pt, dashed] (H)--(B);\n'
        '\\draw[line width=1pt] (4.25,0)--(4.25,-0.25)--(4.5,-0.25);\n'
        '\\draw[line width=1pt] (0.85,0) arc (0:-24:0.85);\n'
        '\\node at (1.25,-0.22) {$%s^\\circ$};\n'
        '\\fill (A) circle (1pt) node[above left] {$A$};\n'
        '\\fill (H) circle (1pt) node[above right] {$H$};\n'
        '\\fill (B) circle (1pt) node[below right] {$B$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (goc)

    noidungcauhoi = (
        'Trong một buổi tập trận, một tàu ngầm đang ở trên mặt biển bắt đầu di chuyển theo đường thẳng tạo với mặt nước biển một góc $%s^\\circ$ để lặn xuống với tốc độ không đổi $%s\\text{ km/h}$.\\n%s'
        % (goc, v_kmh, hinh_tikz)
    )

    # Nhận biết
    nb_da_1_d = '\\True Tốc độ của tàu ngầm đổi ra đơn vị mét/phút là $%s\\text{ m/phút}$' % (v_mphut)
    nb_da_1_s = 'Tốc độ của tàu ngầm đổi ra đơn vị mét/phút là $%s\\text{ m/phút}$' % (v_mphut_sai)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Ta có $%s\\text{ km/h} = \\dfrac{%s \\cdot 1000\\text{ m}}{60\\text{ phút}} = %s\\text{ m/phút}$.'
        % (v_kmh, v_kmh, v_mphut)
    )

    # Thông hiểu
    th_da_1_d = '\\True Khi tàu di chuyển theo đường xiên đi được $%s\\text{ m}$, tàu ở độ sâu xấp xỉ $%s\\text{ m}$ so với mặt nước biển (làm tròn đến mét)' % (qd1, sau1_round)
    th_da_1_s = 'Khi tàu di chuyển theo đường xiên đi được $%s\\text{ m}$, tàu ở độ sâu xấp xỉ $%s\\text{ m}$ so với mặt nước biển (làm tròn đến mét)' % (qd1, sau1_sai)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Xét tam giác $ABH$ vuông tại $H$ có $AB = %s\\text{ m}$ và $\\widehat{BAH} = %s^\\circ$. '
        'Độ sâu của tàu so với mặt nước biển là: $BH = AB \\cdot \\sin %s^\\circ = %s \\cdot \\sin %s^\\circ \\approx %s\\text{ m}$.'
        % (qd1, goc, goc, qd1, goc, sau1_round)
    )

    # Vận dụng
    vd_da_1_d = '\\True Để đạt độ sâu $%s\\text{ m}$ so với mặt nước biển, quãng đường tàu phải di chuyển theo quỹ đạo xiên xấp xỉ bằng $%s\\text{ m}$' % (sau2, qd2_round)
    vd_da_1_s = 'Để đạt độ sâu $%s\\text{ m}$ so với mặt nước biển, quãng đường tàu phải di chuyển theo quỹ đạo xiên xỉ bằng $%s\\text{ m}$' % (sau2, qd2_sai)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Khi độ sâu $BH = %s\\text{ m}$, quãng đường tàu di chuyển theo phương xiên là: '
        '$AB = \\dfrac{BH}{\\sin %s^\\circ} = \\dfrac{%s}{\\sin %s^\\circ} \\approx %s\\text{ m}$.'
        % (sau2, goc, sau2, goc, qd2_round)
    )

    # Vận dụng cao
    vdc_da_1_d = '\\True Thời gian để tàu lặn từ mặt biển xuống độ sâu $%s\\text{ m}$ xấp xỉ bằng $%s$ phút' % (sau2, t_phut_str)
    vdc_da_1_s = 'Thời gian để tàu lặn từ mặt biển xuống độ sâu $%s\\text{ m}$ xấp xỉ bằng $%s$ phút' % (sau2, t_phut_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Thời gian tàu lặn xuống độ sâu $%s\\text{ m}$ là: '
        '$t = \\dfrac{AB}{v} \\approx \\dfrac{%s}{%s} \\approx %s\\text{ phút}$.'
        % (sau2, qd2_round, v_mphut, t_phut_str)
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
