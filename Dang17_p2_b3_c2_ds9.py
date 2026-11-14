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


def bt_Dang17_p2_b3_c2_ds9(self):
    while True:
        d1, d2, d3, d4 = random.choice([(7, 8, 8, 9), (7, 7, 8, 9), (6, 8, 8, 9), (7, 8, 7, 9)])
        gk_str, gk_val = random.choice([("7,5", 7.5), ("7,0", 7.0), ("8,0", 8.0)])
        tong_diem_co_dinh = int(d1 + d2 + d3 + d4 + 2 * gk_val)
        x_min_thuc = (72 - tong_diem_co_dinh) / 3
        if 8.0 < x_min_thuc <= 9.5:
            break

    noidungcauhoi = ('''Để đạt danh hiệu Học sinh Giỏi môn Toán học kì I, điểm trung bình môn Toán phải đạt từ $8,0$ trở lên (trong đó điểm đánh giá thường xuyên tính hệ số $1$, điểm giữa kì tính hệ số $2$, điểm cuối kì tính hệ số $3$). Bạn Nam đã có $4$ điểm đánh giá thường xuyên là $%s; %s; %s; %s$ và điểm giữa kì là $%s$. Gọi $x$ là điểm bài kiểm tra cuối kì của bạn Nam ($0 \\le x \\le 10$). Xét tính đúng sai của các khẳng định sau:''' % (d1, d2, d3, d4, gk_str))

    nb_da_1_d = '\\True Tổng hệ số của tất cả các bài kiểm tra môn Toán của Nam là $9$'
    nb_da_1_s = 'Tổng hệ số của tất cả các bài kiểm tra môn Toán của Nam là $6$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tổng hệ số gồm $4$ điểm hệ số $1$, $1$ điểm hệ số $2$ và $1$ điểm hệ số $3$ bằng $4 \\cdot 1 + 2 + 3 = 9$.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tổng điểm đã nhân hệ số của Nam (tính cả bài cuối kì) là $%s + 3x$' % (tong_diem_co_dinh)
    th_da_1_s = 'Tổng điểm đã nhân hệ số của Nam (tính cả bài cuối kì) là $%s + x$' % (tong_diem_co_dinh)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tổng điểm hệ số là $(%s + %s + %s + %s) + %s \\cdot 2 + 3x = %s + 3x$.''' % (d1, d2, d3, d4, gk_str, tong_diem_co_dinh))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Bất phương trình biểu thị điều kiện Nam đạt điểm trung bình từ $8,0$ trở lên là $\\frac{%s + 3x}{9} \\ge 8$' % (tong_diem_co_dinh)
    vd_da_1_s = 'Bất phương trình biểu thị điều kiện Nam đạt điểm trung bình từ $8,0$ trở lên là $\\frac{%s + 3x}{6} \\ge 8$' % (tong_diem_co_dinh)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Điểm trung bình môn là $\\frac{%s + 3x}{9}$, điều kiện đạt từ $8,0$ trở lên cho bất phương trình $\\frac{%s + 3x}{9} \\ge 8$.''' % (tong_diem_co_dinh, tong_diem_co_dinh))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu đạt $8,0$ điểm ở bài kiểm tra cuối kì thì bạn Nam vẫn chưa đủ điều kiện đạt danh hiệu Học sinh Giỏi môn Toán'
    vdc_da_1_s = 'Bạn Nam chỉ cần đạt $8,0$ điểm ở bài kiểm tra cuối kì là đủ điều kiện đạt danh hiệu Học sinh Giỏi môn Toán'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Giải bất phương trình: $\\frac{%s + 3x}{9} \\ge 8 \\Leftrightarrow %s + 3x \\ge 72 \\Leftrightarrow x \\ge %.2f$. Do đó đạt $8,0$ điểm cuối kì vẫn chưa đủ $8,0$ điểm trung bình môn.''' % (tong_diem_co_dinh, tong_diem_co_dinh, x_min_thuc))
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

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
