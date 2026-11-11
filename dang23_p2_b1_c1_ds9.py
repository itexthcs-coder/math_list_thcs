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


def bt_dang23_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Dạng bài: Bài toán cổ chia cam, quýt
    # Mẫu gốc:
    # "Quýt, cam mười bảy quả tươi / Đem chia cho một trăm người cùng vui / Chia ba mỗi quả quýt rồi / Còn cam, mỗi quả chia mười vừa xinh"
    # Gọi x là số quả cam và y là số quả quýt
    # Cam chia c_pieces miếng (mẫu là 10), quýt chia q_pieces miếng (mẫu là 3)
    
    while True:
        x_cam = random.choice([5, 6, 7, 8, 9])
        y_quyt = random.choice([6, 7, 8, 9, 10, 11, 12])
        if x_cam != y_quyt:
            c_pieces = random.choice([8, 10])
            q_pieces = random.choice([3, 4])
            total_fruits = x_cam + y_quyt
            total_people = c_pieces * x_cam + q_pieces * y_quyt
            break
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Trong bài toán cổ: "Quýt, cam %s quả tươi / Đem chia cho %s người cùng vui / Chia %s mỗi quả quýt rồi / Còn cam, mỗi quả chia %s vừa xinh". Gọi $x$ là số quả cam và $y$ là số quả quýt.''' % (total_fruits, total_people, q_pieces, c_pieces))
    
    ############################################################################# Nhận biết #################################################
    # a) Tổng số quả cam và quýt được mô tả bởi phương trình x + y = total_fruits
    total_fruits_wrong = total_fruits + random.choice([1, -1])
    nb_da_1_d = '\\True Tổng số quả cam và quýt được mô tả bởi phương trình $x + y = %s$' % (total_fruits)
    nb_da_1_s = 'Tổng số quả cam và quýt được mô tả bởi phương trình $x + y = %s$' % (total_fruits_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì tổng số quả cam và quýt là %s quả nên ta có phương trình: $x + y = %s$.''' % (total_fruits, total_fruits))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Tổng số miếng chia được mô tả bởi phương trình c_pieces*x + q_pieces*y = total_people
    # (Đề mẫu gốc ghi nhầm hệ số: q_pieces*x + c_pieces*y = total_people -> Sai)
    th_da_1_d = '\\True Tổng số miếng chia được mô tả bởi phương trình $%sx + %sy = %s$' % (c_pieces, q_pieces, total_people)
    th_da_1_s = 'Tổng số miếng chia được mô tả bởi phương trình $%sx + %sy = %s$' % (q_pieces, c_pieces, total_people)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Mỗi quả cam chia thành %s miếng nên $x$ quả cam có $%sx$ miếng. \\\\ Mỗi quả quýt chia thành %s miếng nên $y$ quả quýt có $%sy$ miếng. \\\\ Tổng số miếng chia cho %s người (mỗi người một miếng) là %s miếng nên phương trình đúng phải là $%sx + %sy = %s$. \\\\ Khẳng định phương trình là $%sx + %sy = %s$ là nhầm lẫn giữa số miếng của cam và quýt.''' % (c_pieces, c_pieces, q_pieces, q_pieces, total_people, total_people, c_pieces, q_pieces, total_people, q_pieces, c_pieces, total_people))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Hệ phương trình mô tả bài toán cổ viết dạng ngoặc nhọn
    vd_da_1_d = '\\True Hệ phương trình mô tả bài toán cổ là $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$' % (total_fruits, c_pieces, q_pieces, total_people)
    vd_da_1_s = 'Hệ phương trình mô tả bài toán cổ là $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$' % (total_fruits, q_pieces, c_pieces, total_people)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Kết hợp phương trình tổng số quả và phương trình tổng số miếng, ta có hệ phương trình: \\\\ $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$ (với $x, y \\in \\mathbb{N}^*$).''' % (total_fruits, c_pieces, q_pieces, total_people))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Cặp số x = x_cam (cam) và y = y_quyt (quýt) là đáp án đúng của bài toán cổ
    vdc_da_1_d = '\\True Cặp số $x = %s$ (cam) và $y = %s$ (quýt) là đáp án đúng của bài toán cổ' % (x_cam, y_quyt)
    vdc_da_1_s = 'Cặp số $x = %s$ (cam) và $y = %s$ (quýt) là đáp án đúng của bài toán cổ' % (y_quyt, x_cam)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$: \\\\ Nhân hai vế phương trình thứ nhất với $%s$, ta được: $\\begin{cases} %sx + %sy = %s \\\\ %sx + %sy = %s \\end{cases}$. \\\\ Trừ từng vế hai phương trình: $(%s - %s)x = %s - %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$. \\\\ Thay $x = %s$ vào $x + y = %s$, ta được: $y = %s - %s = %s$. \\\\ Vậy số quả cam là $x = %s$ và số quả quýt là $y = %s$.''' % (total_fruits, c_pieces, q_pieces, total_people, q_pieces, q_pieces, q_pieces, q_pieces * total_fruits, c_pieces, q_pieces, total_people, c_pieces, q_pieces, total_people, q_pieces * total_fruits, c_pieces - q_pieces, total_people - q_pieces * total_fruits, x_cam, x_cam, total_fruits, total_fruits, x_cam, y_quyt, x_cam, y_quyt))
    
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
