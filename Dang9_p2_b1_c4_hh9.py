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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_Dang9_p2_b1_c4_hh9(self):
    def round_vn(val, digits):
        fmt = '0.' + '0' * digits if digits > 0 else '0'
        d = Decimal(str(val)).quantize(Decimal(fmt), rounding=ROUND_HALF_UP)
        return str(d).replace('.', ',')

    def deg_to_dm(deg_float):
        total_minutes = int(Decimal(str(deg_float * 60)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        return total_minutes // 60, total_minutes % 60

    # Khai báo biến
    sin_val = round(random.uniform(0.3215, 0.6845), 4)
    deg_exact = math.degrees(math.asin(sin_val))
    d_goc, m_goc = deg_to_dm(deg_exact)
    rad_round = math.radians(d_goc + m_goc / 60.0)
    cos_kq = round_vn(math.cos(rad_round), 3)
    tan_kq = round_vn(math.tan(rad_round), 3)

    d_phu = 89 - d_goc if m_goc > 0 else 90 - d_goc
    m_phu = 60 - m_goc if m_goc > 0 else 0

    sin_str = str(sin_val).replace('.', ',')
    goc_str = '%d^{\\circ}%d\'' % (d_goc, m_goc)
    goc_phu_str = '%d^{\\circ}%d\'' % (d_phu, m_phu)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho góc nhọn $\\alpha$ thỏa mãn $\\sin \\alpha = %s$. Sử dụng máy tính cầm tay để tính toán và xét tính đúng sai của các khẳng định sau:''' % sin_str)

    nb_da_1_d = '\\True Số đo góc $\\alpha$ làm tròn đến phút bằng $%s$' % goc_str
    nb_da_1_s = 'Số đo góc $\\alpha$ làm tròn đến phút bằng $%d^{\\circ}%d\'$' % (d_goc + 1, m_goc)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Bấm máy tính $\\sin^{-1}(%s)$, làm tròn đến phút được $\\alpha \\approx %s$.''' % (sin_str, goc_str))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Giá trị của $\\cos \\alpha$ làm tròn đến chữ số thập phân thứ ba bằng $%s$' % cos_kq
    th_da_1_s = 'Giá trị của $\\cos \\alpha$ làm tròn đến chữ số thập phân thứ ba bằng $%s$' % round_vn(math.cos(rad_round) + 0.05, 3)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Với $\\alpha \\approx %s$, bấm $\\cos %s \\approx %s$.''' % (goc_str, goc_str, cos_kq))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Giá trị của $\\tan \\alpha$ làm tròn đến chữ số thập phân thứ ba bằng $%s$' % tan_kq
    vd_da_1_s = 'Giá trị của $\\tan \\alpha$ làm tròn đến chữ số thập phân thứ ba bằng $%s$' % round_vn(math.tan(rad_round) + 0.08, 3)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Với $\\alpha \\approx %s$, bấm $\\tan %s \\approx %s$.''' % (goc_str, goc_str, tan_kq))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Góc $\\beta$ phụ với góc $\\alpha$ có số đo làm tròn đến phút bằng $%s$' % goc_phu_str
    vdc_da_1_s = 'Góc $\\beta$ phụ với góc $\\alpha$ có số đo làm tròn đến phút bằng $%d^{\\circ}%d\'$' % (90 - d_goc, m_goc)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $\\beta = 90^{\\circ} - %s = %s$.''' % (goc_str, goc_phu_str))
    list_vdc_2 = [loigiai_vdc_1]
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

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

    content = (
        '\\begin{minipage}{\\textwidth} \n'
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
        '\\end{ex}\n \\end{minipage}\n\n'
    )
    return content
