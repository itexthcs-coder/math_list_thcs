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


def bt_dang10_p2_b1_c1_ds9(self):
    # Khai báo biến
    m, x, y = symbols('m x y')
    
    # Dạng bài: Cho hệ phương trình:
    # pt 1: (m - k0)x + y = c
    # pt 2: k_val*x + k_val*y = k_val*c
    # với m là tham số
    while True:
        k0 = random.choice([1, 2, 3, -1, -2])
        c_val = random.choice([2, 3, 4, 5])
        k_val = random.choice([2, 3])
        
        # Giá trị m để hệ có vô số nghiệm: m - k0 = 1 => m_inf = k0 + 1
        m_inf = k0 + 1
        # Giá trị m để hệ có nghiệm duy nhất (chọn m_uniq != m_inf)
        m_uniq = m_inf + random.choice([1, 2])
        # Giá trị m kiểm tra tính vô nghiệm (thực chất có nghiệm duy nhất)
        m_diff = k0
        if m_inf != 0:
            break
    
    # Hệ số pt2
    a2 = k_val
    b2 = k_val
    c2 = k_val * c_val
    
    # Biểu diễn biểu thức (m - k0)
    if k0 > 0:
        str_m = 'm - %s' % (k0)
    elif k0 < 0:
        str_m = 'm + %s' % (abs(k0))
    else:
        str_m = 'm'
    
    # Nội dung câu hỏi (hệ phương trình viết dạng ngoặc nhọn \begin{cases} ... \end{cases})
    noidungcauhoi = ('''Cho hệ phương trình: $\\begin{cases} (%s)x + y = %s \\\\ %sx + %sy = %s \\end{cases}$ với $m$ là tham số.''' % (str_m, c_val, a2, b2, c2))
    
    ############################################################################# Nhận biết #################################################
    # a) Khi m = m_inf, hệ phương trình có vô số nghiệm
    nb_da_1_d = '\\True Khi $m = %s$, hệ phương trình có vô số nghiệm' % (m_inf)
    nb_da_1_s = 'Khi $m = %s$, hệ phương trình vô nghiệm' % (m_inf)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Rút gọn phương trình thứ hai bằng cách chia cả hai vế cho $%s$, ta được $x + y = %s$. \\\\ Khi $m = %s$, phương trình thứ nhất trở thành: $(%s - (%s))x + y = %s \\Leftrightarrow x + y = %s$. \\\\ Khi đó cả hai phương trình của hệ đều là $x + y = %s$, do đó hệ phương trình có vô số nghiệm.''' % (k_val, c_val, m_inf, m_inf, k0, c_val, c_val, c_val))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Khi m = m_uniq, hệ phương trình có nghiệm duy nhất
    m_uniq_coef = m_uniq - k0
    th_da_1_d = '\\True Khi $m = %s$, hệ phương trình có nghiệm duy nhất' % (m_uniq)
    th_da_1_s = 'Khi $m = %s$, hệ phương trình có vô số nghiệm' % (m_uniq)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Khi $m = %s$, hệ phương trình trở thành: $\\begin{cases} %sx + y = %s \\\\ x + y = %s \\end{cases}$. \\\\ Trừ hai phương trình vế theo vế, ta được: $%sx = 0 \\Leftrightarrow x = 0 \\Rightarrow y = %s$. \\\\ Do đó, hệ phương trình có nghiệm duy nhất là $(0; %s)$.''' % (m_uniq, m_uniq_coef, c_val, c_val, m_uniq_coef - 1, c_val, c_val))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Khi m = m_diff, hệ phương trình vô nghiệm (Mệnh đề sai vì hệ có nghiệm duy nhất (0; c_val))
    m_diff_coef = m_diff - k0
    vd_da_1_d = '\\True Khi $m = %s$, hệ phương trình có nghiệm duy nhất' % (m_diff)
    vd_da_1_s = 'Khi $m = %s$, hệ phương trình vô nghiệm' % (m_diff)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Khi $m = %s$, phương trình thứ nhất trở thành: $0x + y = %s \\Leftrightarrow y = %s$. \\\\ Thay $y = %s$ vào phương trình thứ hai $x + y = %s$, ta được $x = 0$. \\\\ Hệ có nghiệm duy nhất là $(0; %s)$, do đó khẳng định hệ phương trình vô nghiệm là sai.''' % (m_diff, c_val, c_val, c_val, c_val, c_val))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Với mọi giá trị của m, cặp số (x_fix; y_fix) luôn là nghiệm của hệ phương trình
    # Nghiệm cố định thỏa mãn mọi m là (0; c_val) vì (m - k0)*0 + c_val = c_val đúng với mọi m.
    # Nếu lấy (1; c_val - 1) thì chỉ đúng khi m = m_inf.
    vdc_da_1_d = '\\True Với mọi giá trị của $m$, cặp số $(0; %s)$ luôn là nghiệm của hệ phương trình' % (c_val)
    vdc_da_1_s = 'Với mọi giá trị của $m$, cặp số $(1; %s)$ luôn là nghiệm của hệ phương trình' % (c_val - 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Thay $x = 1$ và $y = %s$ vào phương trình thứ nhất: $(%s) \\cdot 1 + %s = %s + %s$. \\\\ Để cặp số $(1; %s)$ là nghiệm của hệ thì cần $m - %s + %s = %s \\Leftrightarrow m = %s$. \\\\ Như vậy cặp số $(1; %s)$ chỉ là nghiệm khi $m = %s$, không phải với mọi giá trị của $m$. \\\\ (Thực chất cặp số cố định là nghiệm với mọi $m$ phải là $(0; %s)$).''' % (c_val - 1, str_m, c_val - 1, str_m, c_val - 1, c_val - 1, k0, c_val - 1, c_val, m_inf, c_val - 1, m_inf, c_val))
    
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
