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


def bt_dang10_p2_b2_c1_ds9(self):
    # Khai báo biến
    m1 = random.choice([3, 5, 7, 9])
    m2 = random.choice([2, 4, 5, 7])
    while m1 == m2:
        m2 = random.choice([2, 4, 5, 7])
    
    u0 = random.choice([1, 2, 3])
    v0 = random.choice([-3, -2, -1])
    x0 = m1 * u0
    y0 = m2 * v0
    
    a1 = random.choice([2, 3, 4])
    b1 = random.choice([-3, -2])
    a2 = random.choice([1, 2, 3])
    b2 = random.choice([2, 3, 4])
    while a1 * b2 - a2 * b1 == 0:
        b2 = random.choice([2, 3, 4])
    
    c1 = a1 * u0 + b1 * v0
    c2 = a2 * u0 + b2 * v0
    
    pt1_str = latex(Rational(a1, m1) * x + Rational(b1, m2) * y) + '=' + latex(c1)
    pt2_str = latex(Rational(a2, m1) * x + Rational(b2, m2) * y) + '=' + latex(c2)
    
    u_sym, v_sym = symbols('u v')
    pt1_uv = latex(a1 * u_sym + b1 * v_sym) + '=' + latex(c1)
    pt2_uv = latex(a2 * u_sym + b2 * v_sym) + '=' + latex(c2)
    tich_xy = x0 * y0
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$. Xét tính đúng sai của các khẳng định sau:'''
                     % (pt1_str, pt2_str))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Nếu đặt $u = \\frac{x}{%s}$ và $v = \\frac{y}{%s}$ thì hệ phương trình đã cho trở thành $\\begin{cases} %s \\\\ %s \\end{cases}$' % (latex(m1), latex(m2), pt1_uv, pt2_uv)
    nb_da_1_s = 'Nếu đặt $u = \\frac{x}{%s}$ và $v = \\frac{y}{%s}$ thì hệ phương trình đã cho trở thành $\\begin{cases} %s \\\\ %s \\end{cases}$' % (latex(m1), latex(m2), latex(a1 * u_sym - b1 * v_sym) + '=' + latex(c1), pt2_uv)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Đặt $u = \\frac{x}{%s}$ và $v = \\frac{y}{%s}$, hệ phương trình đã cho trở thành $\\begin{cases} %s \\\\ %s \\end{cases}$.'''
                    % (latex(m1), latex(m2), pt1_uv, pt2_uv))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Giải hệ phương trình theo hai ẩn $u, v$, ta tìm được $u = %s$ và $v = %s$' % (latex(u0), latex(v0))
    th_da_1_s = 'Giải hệ phương trình theo hai ẩn $u, v$, ta tìm được $u = %s$ và $v = %s$' % (latex(u0), latex(-v0))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Giải hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$ bằng phương pháp cộng đại số, ta tìm được $u = %s$ và $v = %s$.'''
                    % (pt1_uv, pt2_uv, latex(u0), latex(v0)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Hệ phương trình ban đầu có nghiệm duy nhất là $(%s; %s)$' % (latex(x0), latex(y0))
    vd_da_1_s = 'Hệ phương trình ban đầu có nghiệm duy nhất là $(%s; %s)$' % (latex(u0), latex(v0))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Từ $u = %s$ và $v = %s$, suy ra $x = %s \\cdot %s = %s$ và $y = %s \\cdot (%s) = %s$. Vậy hệ phương trình ban đầu có nghiệm duy nhất là $(%s; %s)$.'''
                    % (latex(u0), latex(v0), latex(m1), latex(u0), latex(x0), latex(m2), latex(v0), latex(y0), latex(x0), latex(y0)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Tích hai thành phần nghiệm $x_0 \\cdot y_0$ của hệ phương trình ban đầu bằng $%s$' % (latex(tich_xy))
    vdc_da_1_s = 'Tích hai thành phần nghiệm $x_0 \\cdot y_0$ của hệ phương trình ban đầu bằng $%s$' % (latex(-tich_xy))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $x_0 \\cdot y_0 = %s \\cdot (%s) = %s$.'''
                     % (latex(x0), latex(y0), latex(tich_xy)))
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
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\n' '\\choiceTFn \n' '{' + str(shuffled_answers_nb[0]) + '}\n' '{' + str(shuffled_answers_th[0]) + '}\n' '{' + str(shuffled_answers_vd[0]) + '}\n' '{' + str(shuffled_answers_vdc[0]) + '}\n' '\\loigiai{ \n' '\\begin{enumEX}[a)]{1} \n' '\\item ' + str(shuffled_solutions_nb[0]) + '\n' '\\item ' + str(shuffled_solutions_th[0]) + '\n' '\\item ' + str(shuffled_solutions_vd[0]) + '\n' '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' '\\end{enumEX}} \n' '\\end{ex}\n \\end{minipage}\n\n')

    return content
