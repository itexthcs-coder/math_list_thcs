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


def bt_dang7_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm phụ trợ tạo biểu thức vế trái dạng ax + by
    def make_expr_str(a, b):
        if a == 1:
            res = 'x'
        elif a == -1:
            res = '-x'
        else:
            res = '%sx' % (a)
        
        if b == 1:
            res += ' + y'
        elif b == -1:
            res += ' - y'
        elif b > 0:
            res += ' + %sy' % (b)
        else:
            res += ' - %sy' % (abs(b))
        return res
    
    # Dạng bài: Hệ hai phương trình vô số nghiệm (hai phương trình tỉ lệ với nhau)
    # Phương trình 1: a1*x + b1*y = c1
    # Phương trình 2: a2*x + b2*y = c2 với a2 = k*a1, b2 = k*b1, c2 = k*c1
    while True:
        a1 = random.choice([2, 3, 4, -2, -3])
        b1 = random.choice([1, -1, 2, -2])
        c1 = random.choice([3, 4, 5, 6, 7])
        k_val = random.choice([2, 3])
        
        a2 = k_val * a1
        b2 = k_val * b1
        c2 = k_val * c1
        
        # Tìm 2 cặp nghiệm nguyên thoả mãn: (x1_sol, y1_sol) và (x2_sol, y2_sol)
        # Lấy x2_sol = 0 nếu c1 chia hết cho b1, hoặc tìm 2 nghiệm nguyên đơn giản
        solutions = []
        for x_cand in range(-5, 6):
            rem = c1 - a1 * x_cand
            if rem % b1 == 0:
                solutions.append((x_cand, rem // b1))
                if len(solutions) == 2:
                    break
        if len(solutions) >= 2:
            break
    
    (x1_sol, y1_sol) = solutions[0]
    (x2_sol, y2_sol) = solutions[1]
    
    lhs1_str = make_expr_str(a1, b1)
    lhs2_str = make_expr_str(a2, b2)
    
    # Nội dung câu hỏi (hệ phương trình viết dạng ngoặc nhọn \begin{cases} ... \end{cases})
    noidungcauhoi = ('''Cho hệ phương trình: $\\begin{cases} %s = %s \\\\ %s = %s \\end{cases}$.''' % (lhs1_str, c1, lhs2_str, c2))
    
    ############################################################################# Nhận biết #################################################
    # a) Phương trình thứ hai gấp k_val lần phương trình thứ nhất
    k_wrong = k_val + 1
    nb_da_1_d = '\\True Phương trình thứ hai gấp %s lần phương trình thứ nhất' % (k_val)
    nb_da_1_s = 'Phương trình thứ hai gấp %s lần phương trình thứ nhất' % (k_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Nhân cả hai vế của phương trình thứ nhất với $%s$, ta được: \\\\ $%s \\cdot (%s) = %s \\cdot %s \\Leftrightarrow %s = %s$. \\\\ Đây chính là phương trình thứ hai của hệ. Do đó, phương trình thứ hai gấp $%s$ lần phương trình thứ nhất.''' % (k_val, k_val, lhs1_str, k_val, c1, lhs2_str, c2, k_val))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Hai đường thẳng biểu diễn tập nghiệm của hai phương trình trên mặt phẳng Oxy trùng nhau (mẫu đề bài ghi song song với nhau là sai)
    th_da_1_d = '\\True Hai đường thẳng biểu diễn tập nghiệm của hai phương trình trên mặt phẳng $Oxy$ trùng nhau'
    th_da_1_s = 'Hai đường thẳng biểu diễn tập nghiệm của hai phương trình trên mặt phẳng $Oxy$ song song với nhau'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Vì phương trình thứ hai tương đương với phương trình thứ nhất nên hai phương trình có cùng tập nghiệm. \\\\ Do đó, trên mặt phẳng toạ độ $Oxy$, hai đường thẳng biểu diễn tập nghiệm của hai phương trình trùng nhau (không phải song song với nhau).''' )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Hệ phương trình đã cho có vô số nghiệm
    vd_da_1_d = '\\True Hệ phương trình đã cho có vô số nghiệm'
    vd_da_1_s = 'Hệ phương trình đã cho vô nghiệm'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Vì hai phương trình tương đương nhau nên mọi cặp số $(x; y)$ thoả mãn phương trình thứ nhất đều thoả mãn phương trình thứ hai. \\\\ Một phương trình bậc nhất hai ẩn có vô số nghiệm nên hệ phương trình đã cho có vô số nghiệm.''' )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Cặp số (x1_sol; y1_sol) và (x2_sol; y2_sol) đều là nghiệm của hệ phương trình
    y2_wrong = y2_sol + 1
    vdc_da_1_d = '\\True Cặp số $(%s; %s)$ và $(%s; %s)$ đều là nghiệm của hệ phương trình' % (x1_sol, y1_sol, x2_sol, y2_sol)
    vdc_da_1_s = 'Cặp số $(%s; %s)$ và $(%s; %s)$ đều là nghiệm của hệ phương trình' % (x1_sol, y1_sol, x2_sol, y2_wrong)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Thay lần lượt các cặp số vào phương trình $%s = %s$: \\\\ + Với $(%s; %s)$: $(%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$ (thoả mãn). \\\\ + Với $(%s; %s)$: $(%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$ (thoả mãn). \\\\ Do hai phương trình trong hệ tương đương nhau, nên cả hai cặp số $(%s; %s)$ và $(%s; %s)$ đều là nghiệm của hệ phương trình.''' % (lhs1_str, c1, x1_sol, y1_sol, a1, x1_sol, b1, y1_sol, c1, x2_sol, y2_sol, a1, x2_sol, b1, y2_sol, c1, x1_sol, y1_sol, x2_sol, y2_sol))
    
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
