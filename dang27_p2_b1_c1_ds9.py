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


def bt_dang27_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm định dạng tiền tệ có khoảng trắng cách hàng nghìn
    def format_money(val):
        return '{:,}'.format(val).replace(',', ' ')
    
    # Dạng bài: Giá vé người lớn price_a (nghìn đồng), vé trẻ em price_c (nghìn đồng)
    # Mẫu gốc: giá vé người lớn 80 000 đ, vé trẻ em 50 000 đ, mua 5 vé hết 310 000 đ (2 người lớn, 3 trẻ em)
    while True:
        price_a_k = random.choice([70, 80, 90, 100])
        price_c_k = random.choice([40, 50, 60])
        if price_a_k > price_c_k:
            # Chọn số vé người lớn x0 và số vé trẻ em y0
            x0 = random.choice([2, 3])
            y0 = random.choice([2, 3, 4])
            if x0 != y0:
                total_tickets = x0 + y0
                total_k = price_a_k * x0 + price_c_k * y0
                total_money = total_k * 1000
                price_a = price_a_k * 1000
                price_c = price_c_k * 1000
                
                # Rút gọn phương trình tiền: chia cho 10
                gcd_k = math.gcd(price_a_k, price_c_k)
                gcd_k = math.gcd(gcd_k, total_k)
                u_a = price_a_k // gcd_k
                v_c = price_c_k // gcd_k
                w_total = total_k // gcd_k
                break
    
    price_a_str = format_money(price_a)
    price_c_str = format_money(price_c)
    total_money_str = format_money(total_money)
    
    # Phương trình rút gọn: u_a * x + v_c * y = w_total
    pt_rutgon = '%sx + %sy = %s' % (u_a, v_c, w_total)
    
    # Nội dung câu hỏi (hệ viết dạng ngoặc nhọn nếu có trong câu hỏi/đáp án)
    noidungcauhoi = ('''Tại một rạp chiếu phim, giá vé người lớn là %s đồng/vé, vé trẻ em là %s đồng/vé. Một gia đình đi xem phim mua tổng cộng %s vé hết số tiền %s đồng. Gọi $x$ là số vé người lớn, $y$ là số vé trẻ em.''' % (price_a_str, price_c_str, total_tickets, total_money_str))
    
    ############################################################################# Nhận biết #################################################
    # a) Hệ phương trình biểu thị bài toán là { x + y = total_tickets; price_a_k*x + price_c_k*y = total_k } (với đơn vị nghìn đồng)
    # Đề yêu cầu hệ viết dạng ngoặc nhọn
    nb_da_1_d = '\\True Hệ phương trình biểu thị bài toán là $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$ (với đơn vị nghìn đồng)' % (total_tickets, price_a_k, price_c_k, total_k)
    nb_da_1_s = 'Hệ phương trình biểu thị bài toán là $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$ (với đơn vị nghìn đồng)' % (total_tickets, price_c_k, price_a_k, total_k)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì tổng số vé đã mua là %s vé nên ta có phương trình: $x + y = %s$. \\\\ Đổi %s đồng $= %s$ nghìn đồng. \\\\ Số tiền mua vé người lớn là $%s x$ (nghìn đồng), số tiền mua vé trẻ em là $%s y$ (nghìn đồng). \\\\ Ta có phương trình số tiền: $%sx + %sy = %s$. \\\\ Vậy hệ phương trình biểu thị bài toán là $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$ (với đơn vị nghìn đồng).''' % (total_tickets, total_tickets, total_money_str, total_k, price_a_k, price_c_k, price_a_k, price_c_k, total_k, total_tickets, price_a_k, price_c_k, total_k))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Phương trình số tiền rút gọn thành pt_rutgon
    w_wrong = w_total + 1
    th_da_1_d = '\\True Phương trình số tiền rút gọn thành $%s$' % (pt_rutgon)
    th_da_1_s = 'Phương trình số tiền rút gọn thành $%sx + %sy = %s$' % (u_a, v_c, w_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Phương trình số tiền là $%sx + %sy = %s$. \\\\ Chia cả hai vế của phương trình cho $%s$, ta được phương trình rút gọn: $%s$.''' % (price_a_k, price_c_k, total_k, gcd_k, pt_rutgon))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Gia đình đó gồm x0 người lớn và y0 trẻ em (Đúng)
    vd_da_1_d = '\\True Gia đình đó gồm %s người lớn và %s trẻ em' % (x0, y0)
    vd_da_1_s = 'Gia đình đó gồm %s người lớn và %s trẻ em' % (x0 + 1, y0 - 1)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$: \\\\ Nhân hai vế của phương trình thứ nhất với $%s$, ta được: $\\begin{cases} %sx + %sy = %s \\\\ %sx + %sy = %s \\end{cases}$. \\\\ Trừ từng vế hai phương trình: $(%s - %s)x = %s - %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$. \\\\ Thay $x = %s$ vào phương trình $x + y = %s$, ta được: $y = %s - %s = %s$. \\\\ Vậy gia đình đó gồm %s người lớn và %s trẻ em.''' % (total_tickets, u_a, v_c, w_total, v_c, v_c, v_c, v_c * total_tickets, u_a, v_c, w_total, u_a, v_c, w_total, v_c * total_tickets, u_a - v_c, w_total - v_c * total_tickets, x0, x0, total_tickets, total_tickets, x0, y0, x0, y0))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Gia đình đó gồm y0 người lớn và x0 trẻ em (Mệnh đề đảo thứ tự x và y là Sai)
    vdc_da_1_d = '\\True Nếu đổi lại mua %s vé người lớn và %s vé trẻ em thì tổng số tiền phải trả khác %s đồng' % (y0, x0, total_money_str)
    vdc_da_1_s = 'Gia đình đó gồm %s người lớn và %s trẻ em' % (y0, x0)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Vì số vé người lớn là $x = %s$ và số vé trẻ em là $y = %s$, nên khẳng định gia đình đó gồm %s người lớn và %s trẻ em là sai do đã đổi nhầm giữa số lượng vé người lớn và vé trẻ em.''' % (x0, y0, y0, x0))
    
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
