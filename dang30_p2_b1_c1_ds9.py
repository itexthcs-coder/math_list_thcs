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


def bt_dang30_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Hàm định dạng số thập phân dùng dấu phẩy
    def format_dec(val):
        val_float = float(val)
        if val_float.is_integer():
            return str(int(val_float))
        return str(val_float).replace('.', ',')
    
    # Dạng bài: Hai bạn thu gom giấy vụn kế hoạch nhỏ, tổng cộng total_kg kg.
    # Số giấy Bình gấp k_ratio lần Cường (trong mẫu gốc: gấp rưỡi = 1,5 lần = 3/2).
    # x là số giấy của Bình, y là số giấy của Cường: x = k_ratio * y <=> x - k_ratio*y = 0.
    # x + y = total_kg => y*(1 + k_ratio) = total_kg.
    while True:
        # Chọn tỉ lệ đẹp: 1.5 (gấp rưỡi), 2 (gấp đôi), 2.5 (gấp 2,5 lần), 3 (gấp ba)
        k_choice = random.choice([
            (1.5, 'gấp rưỡi (1,5 lần)'),
            (2.0, 'gấp đôi (2 lần)'),
            (2.5, 'gấp hai lần rưỡi (2,5 lần)'),
            (3.0, 'gấp ba (3 lần)')
        ])
        k_ratio, k_ratio_text = k_choice
        
        # Chọn y (số giấy của Cường) là số nguyên dương đẹp
        y_cuong = random.choice([10, 12, 14, 15, 16, 18, 20])
        x_binh_float = k_ratio * y_cuong
        if x_binh_float.is_integer():
            x_binh = int(x_binh_float)
            total_kg = x_binh + y_cuong
            break
    
    k_ratio_str = format_dec(k_ratio)
    pt_lienhe = 'x - %sy = 0' % (k_ratio_str)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Hai bạn Bình và Cường cùng tham gia một đợt thu gom giấy vụn kế hoạch nhỏ của trường, tổng cộng gom được %s kg giấy vụn. Biết số giấy vụn Bình gom được %s số giấy của Cường. Gọi $x, y$ (kg) lần lượt là số giấy vụn Bình và Cường gom được.''' % (total_kg, k_ratio_text))
    
    ############################################################################# Nhận biết #################################################
    # a) Phương trình biểu thị tổng khối lượng giấy là x + y = total_kg
    total_kg_wrong = total_kg + random.choice([5, -5, 10])
    nb_da_1_d = '\\True Phương trình biểu thị tổng khối lượng giấy là $x + y = %s$' % (total_kg)
    nb_da_1_s = 'Phương trình biểu thị tổng khối lượng giấy là $x + y = %s$' % (total_kg_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì tổng khối lượng giấy vụn hai bạn Bình và Cường gom được là %s kg nên ta có phương trình: $x + y = %s$.''' % (total_kg, total_kg))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Phương trình biểu thị mối liên hệ giữa số giấy của hai bạn là x - k_ratio*y = 0
    pt_lienhe_wrong = 'y - %sx = 0' % (k_ratio_str)
    th_da_1_d = '\\True Phương trình biểu thị mối liên hệ giữa số giấy của hai bạn là $%s$' % (pt_lienhe)
    th_da_1_s = 'Phương trình biểu thị mối liên hệ giữa số giấy của hai bạn là $%s$' % (pt_lienhe_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Số giấy vụn Bình gom được gấp %s số giấy của Cường nên ta có: \\\\ $x = %s y \\Leftrightarrow %s$.''' % (k_ratio_str, k_ratio_str, pt_lienhe))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Cường thu gom được y_cuong kg giấy vụn
    y_cuong_wrong = y_cuong + random.choice([2, -2, 4])
    vd_da_1_d = '\\True Cường thu gom được %s kg giấy vụn' % (y_cuong)
    vd_da_1_s = 'Cường thu gom được %s kg giấy vụn' % (y_cuong_wrong)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Từ hai phương trình trên ta có hệ phương trình: $\\begin{cases} x + y = %s \\\\ %s \\end{cases}$. \\\\ Thay $x = %s y$ vào phương trình thứ nhất, ta được: \\\\ $%s y + y = %s \\Leftrightarrow %s y = %s \\Leftrightarrow y = %s$. \\\\ Vậy Cường thu gom được %s kg giấy vụn.''' % (total_kg, pt_lienhe, k_ratio_str, k_ratio_str, total_kg, format_dec(k_ratio + 1), total_kg, y_cuong, y_cuong))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Bình thu gom được x_binh kg giấy vụn
    x_binh_wrong = x_binh + random.choice([2, -2, 5])
    vdc_da_1_d = '\\True Bình thu gom được %s kg giấy vụn' % (x_binh)
    vdc_da_1_s = 'Bình thu gom được %s kg giấy vụn' % (x_binh_wrong)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Thay $y = %s$ vào phương trình $x + y = %s$, ta được: \\\\ $x = %s - %s = %s$. \\\\ Vậy Bình thu gom được %s kg giấy vụn.''' % (y_cuong, total_kg, total_kg, y_cuong, x_binh, x_binh))
    
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
