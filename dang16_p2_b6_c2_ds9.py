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


def bt_dang16_p2_b6_c2_ds9(self):
    # Khai báo biến: TB 3 bài là tb3, cần TB 4 bài >= tb4
    bo_so = [(6.7, 7.0, 8), (7.2, 7.5, 9), (6.5, 7.0, 9), (7.4, 7.8, 9), (6.8, 7.2, 9)]
    tb3, tb4, min_viet = random.choice(bo_so)
    tong3 = round(tb3 * 3, 1)
    tong4_can = round(tb4 * 4, 1)
    x_min_thuc = round(tong4_can - tong3, 1)
    
    noidungcauhoi = ('''Bạn Minh tham dự một kì kiểm tra năng lực ngoại ngữ gồm $4$ bài thi: Nghe, Nói, Đọc và Viết. Điểm mỗi bài thi là số nguyên từ $0$ đến $10$. Điểm trung bình của ba bài thi Nghe, Nói, Đọc của Minh là $%s$. Gọi $x$ ($x \\in \\mathbb{N}, 0 \\le x \\le 10$) là điểm bài thi Viết của Minh.'''
                     % str(tb3).replace('.', ','))
    
    # Mệnh đề a
    nb_da_1_d = '\\True Tổng điểm của ba bài thi Nghe, Nói, Đọc là $%s$.' % str(tong3).replace('.', ',')
    nb_da_1_s = 'Tổng điểm của ba bài thi Nghe, Nói, Đọc là $%s$.' % str(round(tb3*4, 1)).replace('.', ',')
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tổng điểm của $3$ bài thi Nghe, Nói, Đọc là $%s \\cdot 3 = %s$.'''
                    % (str(tb3).replace('.', ','), str(tong3).replace('.', ',')))
    
    # Mệnh đề b
    th_da_1_d = '\\True Điểm trung bình cả $4$ bài kiểm tra của Minh là $\\dfrac{%s + x}{4}$.' % str(tong3).replace('.', ',')
    th_da_1_s = 'Điểm trung bình cả $4$ bài kiểm tra của Minh là $\\dfrac{%s + x}{4}$.' % str(tb3).replace('.', ',')
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Điểm trung bình của $4$ bài thi bằng tổng điểm $4$ bài chia cho $4$, tức là $\\dfrac{%s + x}{4}$.'''
                    % (str(tong3).replace('.', ',')))
    
    # Mệnh đề c
    vd_da_1_d = '\\True Để điểm trung bình cả $4$ bài đạt từ $%s$ trở lên thì $x$ phải thỏa mãn $x \\ge %s$.' % (str(tb4).replace('.', ','), str(x_min_thuc).replace('.', ','))
    vd_da_1_s = 'Để điểm trung bình cả $4$ bài đạt từ $%s$ trở lên thì $x$ phải thỏa mãn $x \\le %s$.' % (str(tb4).replace('.', ','), str(x_min_thuc).replace('.', ','))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $\\dfrac{%s + x}{4} \\ge %s \\Leftrightarrow %s + x \\ge %s \\Leftrightarrow x \\ge %s$.'''
                    % (str(tong3).replace('.', ','), str(tb4).replace('.', ','), str(tong3).replace('.', ','), str(tong4_can).replace('.', ','), str(x_min_thuc).replace('.', ',')))
    
    # Mệnh đề d
    vdc_da_1_d = '\\True Vì điểm bài thi là số nguyên nên Minh cần đạt ít nhất $%s$ điểm ở bài thi Viết.' % min_viet
    vdc_da_1_s = 'Vì điểm bài thi là số nguyên nên Minh cần đạt ít nhất $%s$ điểm ở bài thi Viết.' % (min_viet - 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $x \\ge %s$ và $x \\in \\mathbb{N}$ nên Minh cần đạt tối thiểu $%s$ điểm ở bài thi Viết.'''
                     % (str(x_min_thuc).replace('.', ','), min_viet))
    
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
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
