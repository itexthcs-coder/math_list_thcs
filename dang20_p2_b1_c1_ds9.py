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


def bt_dang20_p2_b1_c1_ds9(self):
    # Khai báo biến
    a, b, x, y = symbols('a b x y')
    
    # Dạng bài: Cho điểm P(x_P; y_P) và đường thẳng d: ax + by = 1
    # Trong ảnh gốc: P(2; -3), d: ax + by = 1
    # a) Nếu d đi qua P và có a = a_val thì b = b_val
    # b) Nếu d đi qua P và song song với Ox thì a = 0 và b = 1/y_P
    # c) Nếu d đi qua P và song song với Oy thì b = 0 và a = 1/x_P
    # d) Không có đường thẳng nào dạng d đi qua P mà đồng thời đi qua gốc toạ độ O (Đúng vì O(0; 0) => 0 = 1 vô lý)
    
    while True:
        x_P = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
        y_P = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
        if abs(x_P) != abs(y_P):
            # Chọn a_chosen sao cho b_val = (1 - a_chosen * x_P) / y_P là số nguyên đẹp
            # 1 - a_chosen * x_P = k * y_P
            candidates = []
            for a_cand in range(-5, 6):
                if a_cand != 0 and (1 - a_cand * x_P) % y_P == 0:
                    candidates.append((a_cand, (1 - a_cand * x_P) // y_P))
            if len(candidates) > 0:
                a_chosen, b_chosen = random.choice(candidates)
                break
    
    # Tính giá trị a, b theo lý thuyết:
    # Song song Ox: a = 0 => b * y_P = 1 => b = 1 / y_P
    b_ox = Rational(1, y_P)
    b_ox_latex = latex(b_ox)
    
    # Song song Oy: b = 0 => a * x_P = 1 => a = 1 / x_P
    a_oy = Rational(1, x_P)
    a_oy_latex = latex(a_oy)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho điểm $P(%s; %s)$ và đường thẳng $d: ax + by = 1$.''' % (x_P, y_P))
    
    ############################################################################# Nhận biết #################################################
    # a) Nếu d đi qua P và có a = a_chosen thì b = b_chosen
    b_chosen_wrong = b_chosen + random.choice([1, -1])
    nb_da_1_d = '\\True Nếu $d$ đi qua $P$ và có $a = %s$ thì $b = %s$' % (a_chosen, b_chosen)
    nb_da_1_s = 'Nếu $d$ đi qua $P$ và có $a = %s$ thì $b = %s$' % (a_chosen, b_chosen_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì đường thẳng $d$ đi qua điểm $P(%s; %s)$ nên toạ độ điểm $P$ thoả mãn phương trình của $d$: \\\\ $a \\cdot (%s) + b \\cdot (%s) = 1 \\Leftrightarrow %sa + %sb = 1$. \\\\ Khi $a = %s$, ta có: \\\\ %s \\cdot (%s) + %sb = 1 \\Leftrightarrow %s + %sb = 1 \\Leftrightarrow %sb = %s \\Leftrightarrow b = %s$.''' % (x_P, y_P, x_P, y_P, x_P, y_P, a_chosen, x_P, a_chosen, y_P, x_P * a_chosen, y_P, y_P, 1 - x_P * a_chosen, b_chosen))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Nếu d đi qua P và song song với trục Ox thì a = 0 và b = 1/y_P
    th_da_1_d = '\\True Nếu $d$ đi qua $P$ và song song với trục $Ox$ thì $a = 0$ và $b = %s$' % (b_ox_latex)
    th_da_1_s = 'Nếu $d$ đi qua $P$ và song song với trục $Ox$ thì $a = %s$ và $b = 0$' % (b_ox_latex)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Đường thẳng $d$ song song với trục hoành $Ox$ nên có phương trình dạng $y = c_0$ (tức là $a = 0$ và $b \\ne 0$). \\\\ Khi đó phương trình của $d$ trở thành $by = 1 \\Leftrightarrow y = \\dfrac{1}{b}$. \\\\ Do $d$ đi qua điểm $P(%s; %s)$ nên $y_P = \\dfrac{1}{b} \\Leftrightarrow %s = \\dfrac{1}{b} \\Leftrightarrow b = %s$. \\\\ Vậy $a = 0$ và $b = %s$.''' % (x_P, y_P, y_P, b_ox_latex, b_ox_latex))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Nếu d đi qua P và song song với trục Oy thì b = 0 và a = 1/x_P
    vd_da_1_d = '\\True Nếu $d$ đi qua $P$ và song song với trục $Oy$ thì $b = 0$ và $a = %s$' % (a_oy_latex)
    vd_da_1_s = 'Nếu $d$ đi qua $P$ và song song với trục $Oy$ thì $b = %s$ và $a = 0$' % (a_oy_latex)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Đường thẳng $d$ song song với trục tung $Oy$ nên có phương trình dạng $x = c_1$ (tức là $b = 0$ và $a \\ne 0$). \\\\ Khi đó phương trình của $d$ trở thành $ax = 1 \\Leftrightarrow x = \\dfrac{1}{a}$. \\\\ Do $d$ đi qua điểm $P(%s; %s)$ nên $x_P = \\dfrac{1}{a} \\Leftrightarrow %s = \\dfrac{1}{a} \\Leftrightarrow a = %s$. \\\\ Vậy $b = 0$ và $a = %s$.''' % (x_P, y_P, x_P, a_oy_latex, a_oy_latex))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Không có đường thẳng nào dạng ax + by = 1 đi qua gốc toạ độ O(0; 0)
    vdc_da_1_d = '\\True Không có đường thẳng nào dạng $d$ đi qua $P$ mà đồng thời đi qua gốc toạ độ $O$'
    vdc_da_1_s = 'Có duy nhất một đường thẳng dạng $d$ đi qua $P$ mà đồng thời đi qua gốc toạ độ $O$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Đường thẳng $d$ có phương trình $ax + by = 1$. \\\\ Nếu $d$ đi qua gốc toạ độ $O(0; 0)$ thì thay toạ độ $(0; 0)$ vào phương trình, ta được: \\\\ $a \\cdot 0 + b \\cdot 0 = 1 \\Leftrightarrow 0 = 1$ (điều này luôn vô lý với mọi $a, b$). \\\\ Do đó, đường thẳng $d$ không bao giờ đi qua gốc toạ độ $O$, tức là không có đường thẳng nào thuộc họ đường thẳng $d$ đi qua cả $P$ và gốc toạ độ $O$.''' )
    
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
