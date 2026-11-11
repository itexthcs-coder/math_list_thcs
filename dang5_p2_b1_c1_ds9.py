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


def bt_dang5_p2_b1_c1_ds9(self):
    # Khai báo biến
    m, x, y = symbols('m x y')
    
    # Dạng bài: Xét phương trình (m - m1)x + (m - m2)y = c với m là tham số
    # Mẫu gốc: (m - 2)x + (m + 1)y = 5 (tức m1 = 2, m2 = -1, c = 5)
    while True:
        m1 = random.choice([1, 2, 3, 4])
        m2 = random.choice([-4, -3, -2, -1])
        c_val = random.choice([2, 3, 4, 5, 6, 7])
        if m1 != m2:
            break
    
    # Hệ số của x là (m - m1), hệ số của y là (m - m2)
    # Biểu thức dạng đại số: (m - m1)x + (m - m2)y
    str_a = 'm - %s' % (m1) if m1 > 0 else 'm + %s' % (abs(m1))
    str_b = 'm - %s' % (m2) if m2 > 0 else 'm + %s' % (abs(m2))
    
    noidungcauhoi = ('''Xét phương trình bậc nhất hai ẩn $(%s)x + (%s)y = %s$ với $m$ là tham số.''' % (str_a, str_b, c_val))
    
    ############################################################################# Nhận biết #################################################
    # a) Khi m = m1, phương trình trở thành b_val*y = c_val và vẫn là phương trình bậc nhất hai ẩn
    # Tại m = m1: a = 0, b = m1 - m2 != 0
    b_at_m1 = m1 - m2
    pt_m1 = '%sy = %s' % (b_at_m1, c_val)
    
    nb_da_1_d = '\\True Khi $m = %s$, phương trình trở thành $%s$ và vẫn là phương trình bậc nhất hai ẩn' % (m1, pt_m1)
    nb_da_1_s = 'Khi $m = %s$, phương trình trở thành $%s$ và không phải là phương trình bậc nhất hai ẩn' % (m1, pt_m1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Thay $m = %s$ vào phương trình, ta được: \\\\ $(%s - %s)x + (%s - (%s))y = %s \\Leftrightarrow 0x + %sy = %s \\Leftrightarrow %s$. \\\\ Vì hệ số của $y$ là $%s \\ne 0$ nên đây vẫn là phương trình bậc nhất hai ẩn.''' % (m1, m1, m1, m1, m2, c_val, b_at_m1, c_val, pt_m1, b_at_m1))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Khi m = m2, phương trình trở thành a_val*x = c_val và không còn là phương trình bậc nhất hai ẩn (Mệnh đề sai vì vẫn là pt bậc nhất hai ẩn)
    a_at_m2 = m2 - m1
    pt_m2 = '%sx = %s' % (a_at_m2, c_val)
    
    th_da_1_d = '\\True Khi $m = %s$, phương trình trở thành $%s$ và vẫn là phương trình bậc nhất hai ẩn' % (m2, pt_m2)
    th_da_1_s = 'Khi $m = %s$, phương trình trở thành $%s$ và không còn là phương trình bậc nhất hai ẩn' % (m2, pt_m2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Thay $m = %s$ vào phương trình, ta được: \\\\ $(%s - %s)x + (%s - (%s))y = %s \\Leftrightarrow %sx + 0y = %s \\Leftrightarrow %s$. \\\\ Vì hệ số của $x$ là $%s \\ne 0$ nên phương trình nhận được vẫn là phương trình bậc nhất hai ẩn.''' % (m2, m2, m1, m2, m2, c_val, a_at_m2, c_val, pt_m2, a_at_m2))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Không tồn tại giá trị nào của m để phương trình đã cho không phải là phương trình bậc nhất hai ẩn
    # Đúng vì a = 0 <=> m = m1, b = 0 <=> m = m2 mà m1 != m2 nên a và b không đồng thời bằng 0
    vd_da_1_d = '\\True Không tồn tại giá trị nào của $m$ để phương trình đã cho không phải là phương trình bậc nhất hai ẩn'
    vd_da_1_s = 'Tồn tại giá trị của $m$ để phương trình đã cho không phải là phương trình bậc nhất hai ẩn'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Phương trình đã cho không phải là phương trình bậc nhất hai ẩn khi và chỉ khi hệ số của $x$ và $y$ đồng thời bằng $0$: \\\\ $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} m = %s \\\\ m = %s \\end{cases}$ (vô nghiệm vì $%s \\ne %s$). \\\\ Do đó, không tồn tại giá trị nào của $m$ để hai hệ số đồng thời bằng $0$, tức là phương trình luôn là phương trình bậc nhất hai ẩn với mọi $m$.''' % (str_a, str_b, m1, m2, m1, m2))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Khi m = 0, cặp số (x0; y0) là một nghiệm của phương trình
    # Thay m = 0 vào pt: (-m1)x + (-m2)y = c_val
    # Chọn x0, tính y0 đúng: y0 = (c_val + m1*x0) / (-m2)
    x0 = random.choice([1, 2, 3])
    # Chọn y0 sao cho (-m1)*x0 + (-m2)*y0 = c_val
    # Tức là -m2 * y0 = c_val + m1 * x0
    # Để y0 nguyên:
    while (c_val + m1 * x0) % (-m2) != 0:
        c_val += 1
    
    y0_true = (c_val + m1 * x0) // (-m2)
    y0_wrong = y0_true + random.choice([1, 2, -1, -2])
    
    vdc_da_1_d = '\\True Khi $m = 0$, cặp số $(%s; %s)$ là một nghiệm của phương trình' % (x0, y0_true)
    vdc_da_1_s = 'Khi $m = 0$, cặp số $(%s; %s)$ là một nghiệm của phương trình' % (x0, y0_wrong)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Khi $m = 0$, phương trình trở thành: $(0 - %s)x + (0 - (%s))y = %s \\Leftrightarrow %sx + %sy = %s$. \\\\ Thay $x = %s$ và $y = %s$ vào vế trái của phương trình, ta được: \\\\ $(%s) \\cdot %s + (%s) \\cdot (%s) = %s + %s = %s = VP$. \\\\ Do đó, cặp số $(%s; %s)$ là một nghiệm của phương trình khi $m = 0$.''' % (m1, m2, c_val, -m1, -m2, c_val, x0, y0_true, -m1, x0, -m2, y0_true, -m1 * x0, -m2 * y0_true, c_val, x0, y0_true))
    
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
