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


def bt_dang6_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm phụ trợ tạo biểu thức vế trái dạng ax + by
    def make_expr_str(a, b):
        # Biểu diễn ax
        if a == 1:
            res = 'x'
        elif a == -1:
            res = '-x'
        else:
            res = '%sx' % (a)
        
        # Biểu diễn by
        if b == 1:
            res += ' + y'
        elif b == -1:
            res += ' - y'
        elif b > 0:
            res += ' + %sy' % (b)
        else:
            res += ' - %sy' % (abs(b))
        return res
    
    # Random nghiệm nguyên (x0, y0) và hệ số hai phương trình
    while True:
        x0 = random.choice([1, 2, 3, 4, -1, -2, -3])
        y0 = random.choice([1, 2, 3, 4, -1, -2, -3])
        a1 = random.choice([1, 2, 3, -1, -2])
        b1 = random.choice([1, 2, -1, -2, -3])
        a2 = random.choice([1, 2, 3, -1, -2])
        b2 = random.choice([1, 2, 3, -1, -2])
        
        # Định thức D khác 0 để hệ có nghiệm duy nhất
        det = a1 * b2 - a2 * b1
        if det != 0:
            c1 = a1 * x0 + b1 * y0
            c2 = a2 * x0 + b2 * y0
            break
    
    lhs1_str = make_expr_str(a1, b1)
    lhs2_str = make_expr_str(a2, b2)
    
    # Nội dung câu hỏi (hệ phương trình viết dạng ngoặc nhọn \begin{cases} ... \end{cases})
    noidungcauhoi = ('''Cho hệ hai phương trình bậc nhất hai ẩn: $\\begin{cases} %s = %s \\\\ %s = %s \\end{cases}$.''' % (lhs1_str, c1, lhs2_str, c2))
    
    ############################################################################# Nhận biết #################################################
    # a) Cặp số (x0; y0) là nghiệm của phương trình thứ nhất a1*x + b1*y = c1
    x_wrong = x0 + random.choice([1, -1])
    nb_da_1_d = '\\True Cặp số $(%s; %s)$ là nghiệm của phương trình thứ nhất $%s = %s$' % (x0, y0, lhs1_str, c1)
    nb_da_1_s = 'Cặp số $(%s; %s)$ là nghiệm của phương trình thứ nhất $%s = %s$' % (x_wrong, y0, lhs1_str, c1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của phương trình thứ nhất, ta được: \\\\ $(%s) \\cdot (%s) + (%s) \\cdot (%s) = %s = VP$. \\\\ Do đó, cặp số $(%s; %s)$ là nghiệm của phương trình thứ nhất $%s = %s$.''' % (x0, y0, a1, x0, b1, y0, c1, x0, y0, lhs1_str, c1))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Cặp số (x0; y0) là nghiệm của hệ hai phương trình đã cho
    th_da_1_d = '\\True Cặp số $(%s; %s)$ là nghiệm của hệ hai phương trình đã cho' % (x0, y0)
    th_da_1_s = 'Cặp số $(%s; %s)$ không phải là nghiệm của hệ hai phương trình đã cho' % (x0, y0)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Thay $x = %s$ và $y = %s$ vào phương trình thứ hai: \\\\ $(%s) \\cdot (%s) + (%s) \\cdot (%s) = %s = VP$. \\\\ Vì cặp số $(%s; %s)$ thoả mãn cả hai phương trình của hệ nên nó là nghiệm của hệ hai phương trình đã cho.''' % (x0, y0, a2, x0, b2, y0, c2, x0, y0))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Hai đường thẳng biểu diễn hai phương trình của hệ cắt nhau tại điểm I(x0; y0)
    vd_da_1_d = '\\True Hai đường thẳng biểu diễn hai phương trình của hệ cắt nhau tại điểm $I(%s; %s)$' % (x0, y0)
    vd_da_1_s = 'Hai đường thẳng biểu diễn hai phương trình của hệ song song với nhau'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Nghiệm của hệ phương trình chính là toạ độ giao điểm của hai đường thẳng biểu diễn tập nghiệm của mỗi phương trình trong hệ. \\\\ Vì hệ có nghiệm duy nhất là $(%s; %s)$ nên hai đường thẳng cắt nhau tại điểm $I(%s; %s)$.''' % (x0, y0, x0, y0))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Hệ phương trình có nghiệm duy nhất / vô số nghiệm
    vdc_da_1_d = '\\True Hệ phương trình đã cho có nghiệm duy nhất là $(%s; %s)$' % (x0, y0)
    vdc_da_1_s = 'Hệ phương trình có vô số nghiệm vì mỗi phương trình thành phần đều có vô số nghiệm'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Mặc dù mỗi phương trình bậc nhất hai ẩn có vô số nghiệm, nhưng nghiệm của hệ là tập các cặp số đồng thời thoả mãn cả hai phương trình. \\\\ Ở đây hai đường thẳng cắt nhau tại đúng một điểm, nên hệ chỉ có nghiệm duy nhất $(%s; %s)$, không phải có vô số nghiệm.''' % (x0, y0))
    
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
