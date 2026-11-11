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


def bt_dang29_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm định dạng số thập phân dùng dấu phẩy
    def format_dec(val):
        val_float = float(val)
        if val_float.is_integer():
            return str(int(val_float))
        return str(val_float).replace('.', ',')
    
    # Dạng bài: Gửi tiết kiệm tổng số tiền S (triệu đồng) vào hai ngân hàng A và B.
    # Ngân hàng A trả lãi suất r_A %/năm, ngân hàng B trả lãi suất r_B %/năm.
    # Tổng tiền lãi thu được là L (triệu đồng).
    # Mẫu gốc: S = 200, r_A = 6, r_B = 7, L = 13 triệu đồng (nghiệm: x = 100, y = 100)
    
    while True:
        r_A = random.choice([5, 6, 7, 8])
        r_B = random.choice([6, 7, 8, 9])
        if r_A != r_B:
            # Chọn số tiền gửi ở ngân hàng A (x0) và ngân hàng B (y0) tròn chục triệu đồng
            x0 = random.choice([60, 80, 100, 120, 140])
            y0 = random.choice([60, 80, 100, 120, 140])
            total_S = x0 + y0
            
            # Tiền lãi: L = (r_A * x0 + r_B * y0) / 100
            interest_sum_100 = r_A * x0 + r_B * y0
            if interest_sum_100 % 100 == 0:
                total_L = interest_sum_100 // 100
                break
    
    # Lãi suất dạng số thập phân: ví dụ 6% -> 0,06; 7% -> 0,07
    dec_rA_str = format_dec(round(r_A / 100, 2))
    dec_rB_str = format_dec(round(r_B / 100, 2))
    
    # Phương trình lãi: 0,06x + 0,07y = 13 hay 6x + 7y = 1300
    pt_lai_dec = '%sx + %sy = %s' % (dec_rA_str, dec_rB_str, total_L)
    pt_lai_simp = '%sx + %sy = %s' % (r_A, r_B, interest_sum_100)
    
    # Cặp nghiệm phân biệt khác để tạo đáp án sai/nhiễu
    if x0 == y0:
        x_fake = x0 + 20
        y_fake = y0 - 20
    else:
        x_fake = y0
        y_fake = x0
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một người gửi tiết kiệm tổng số tiền %s triệu đồng vào hai ngân hàng A và B. Ngân hàng A trả lãi suất %s\\%%/năm, ngân hàng B trả lãi suất %s\\%%/năm. Sau một năm, tổng tiền lãi thu được từ cả hai ngân hàng là %s triệu đồng. Gọi $x$ (triệu đồng) gửi ở ngân hàng A, $y$ (triệu đồng) gửi ở ngân hàng B.''' % (total_S, r_A, r_B, total_L))
    
    ############################################################################# Nhận biết #################################################
    # a) Phương trình tổng số tiền gửi là x + y = total_S
    total_S_wrong = total_S + 20
    nb_da_1_d = '\\True Phương trình tổng số tiền gửi là $x + y = %s$' % (total_S)
    nb_da_1_s = 'Phương trình tổng số tiền gửi là $x + y = %s$' % (total_S_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Tổng số tiền gửi vào hai ngân hàng A và B là %s triệu đồng nên ta có phương trình: $x + y = %s$.''' % (total_S, total_S))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Phương trình tổng số tiền lãi sau một năm là pt_lai_dec (hay pt_lai_simp)
    pt_lai_simp_wrong = '%sx + %sy = %s' % (r_B, r_A, interest_sum_100)
    th_da_1_d = '\\True Phương trình tổng số tiền lãi sau một năm là $%s$ (hay $%s$)' % (pt_lai_dec, pt_lai_simp)
    th_da_1_s = 'Phương trình tổng số tiền lãi sau một năm là $%s$ (hay $%s$)' % (pt_lai_dec, pt_lai_simp_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Tiền lãi sau một năm tại ngân hàng A là $%s\\%% x = %s x$ (triệu đồng). \\\\ Tiền lãi sau một năm tại ngân hàng B là $%s\\%% y = %s y$ (triệu đồng). \\\\ Tổng số tiền lãi thu được là %s triệu đồng nên ta có phương trình: $%s$. \\\\ Nhân cả hai vế với $100$, ta được phương trình tương đương: $%s$.''' % (r_A, dec_rA_str, r_B, dec_rB_str, total_L, pt_lai_dec, pt_lai_simp))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Số tiền gửi tại ngân hàng A là x0 triệu đồng và ngân hàng B là y0 triệu đồng
    vd_da_1_d = '\\True Số tiền gửi tại ngân hàng A là %s triệu đồng và ngân hàng B là %s triệu đồng' % (x0, y0)
    vd_da_1_s = 'Số tiền gửi tại ngân hàng A là %s triệu đồng và ngân hàng B là %s triệu đồng' % (x_fake, y_fake)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Ta có hệ phương trình: $\\begin{cases} x + y = %s \\\\ %s = %s \\end{cases}$. \\\\ Nhân hai vế của phương trình thứ nhất với $%s$, ta được: $\\begin{cases} %sx + %sy = %s \\\\ %s = %s \\end{cases}$. \\\\ Trừ từng vế hai phương trình: \\\\ $(%s - %s)y = %s - %s \\Leftrightarrow %sy = %s \\Leftrightarrow y = %s$. \\\\ Thay $y = %s$ vào phương trình $x + y = %s$, ta được: $x = %s - %s = %s$. \\\\ Vậy số tiền gửi tại ngân hàng A là %s triệu đồng và ngân hàng B là %s triệu đồng.''' % (total_S, pt_lai_simp, interest_sum_100, r_A, r_A, r_A, r_A * total_S, pt_lai_simp, interest_sum_100, r_B, r_A, interest_sum_100, r_A * total_S, r_B - r_A, interest_sum_100 - r_A * total_S, y0, y0, total_S, total_S, y0, x0, x0, y0))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Nghiệm của hệ là x = x0 triệu đồng và y = y0 triệu đồng (mẫu gốc: x = 120, y = 80 -> Sai)
    vdc_da_1_d = '\\True Nghiệm của hệ là $x = %s$ triệu đồng và $y = %s$ triệu đồng' % (x0, y0)
    vdc_da_1_s = 'Nghiệm của hệ là $x = %s$ triệu đồng và $y = %s$ triệu đồng' % (x_fake, y_fake)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Từ kết quả giải hệ phương trình ở trên, nghiệm duy nhất của hệ phương trình là $x = %s$ triệu đồng và $y = %s$ triệu đồng. \\\\ Do đó khẳng định nghiệm của hệ là $x = %s$ triệu đồng và $y = %s$ triệu đồng là %s.''' % (x0, y0, x_fake if '\\True' not in vdc_da_1 else x0, y_fake if '\\True' not in vdc_da_1 else y0, 'sai' if '\\True' not in vdc_da_1 else 'đúng'))
    
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
