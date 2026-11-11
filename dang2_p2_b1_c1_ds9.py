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


def bt_dang2_p2_b1_c1_ds9(self):
    # Khai báo biến và hằng số
    x, y = symbols('x y')
    
    # Dạng bài: Cho phương trình bậc nhất hai ẩn: 0x + b*y = c (với b != 0, a = 0)
    # Nghiệm y = c / b, đường thẳng y = y0 song song với Ox (hoặc trùng Ox nếu y0 = 0)
    # Trong ảnh gốc: 0x + 3y = -9 => a = 0, b = 3, c = -9 => y = -3
    
    while True:
        b_val = random.choice([2, 3, 4, 5, -2, -3, -4, -5])
        # Chọn y0 nguyên khác 0
        y0_val = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        c_val = b_val * y0_val
        x_test = random.choice([1, 2, 3, 4, 5, 6, 7])
        if c_val != 0:
            break
    
    a_val = 0
    
    # Chuỗi phương trình vế trái dạng 0x + b*y hoặc 0x - |b|y
    if b_val > 0:
        lhs_str = '0x + %sy' % (b_val)
    else:
        lhs_str = '0x - %sy' % (abs(b_val))
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho phương trình bậc nhất hai ẩn $%s = %s$.''' % (lhs_str, c_val))
    
    ############################################################################# Nhận biết #################################################
    # Ý a: Nhận biết các hệ số a, b, c
    nb_da_1_d = '\\True Phương trình đã cho là phương trình bậc nhất hai ẩn với $a = %s$, $b = %s$, $c = %s$' % (a_val, b_val, c_val)
    nb_da_1_s = 'Phương trình đã cho là phương trình bậc nhất hai ẩn với $a = %s$, $b = %s$, $c = %s$' % (b_val, a_val, c_val)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Phương trình bậc nhất hai ẩn có dạng tổng quát là $ax + by = c$, trong đó $a$ và $b$ không đồng thời bằng $0$. \\\\ Đối chiếu với phương trình $%s = %s$, ta có: $a = %s$, $b = %s$, $c = %s$.''' % (lhs_str, c_val, a_val, b_val, c_val))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # Ý b: Cặp số (x_test; y0) là một nghiệm của phương trình
    y_wrong = -y0_val if y0_val != 0 else y0_val + 1
    th_da_1_d = '\\True Cặp số $(%s; %s)$ là một nghiệm của phương trình' % (x_test, y0_val)
    th_da_1_s = 'Cặp số $(%s; %s)$ là một nghiệm của phương trình' % (x_test, y_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của phương trình, ta được: \\\\ $0 \\cdot %s + (%s) \\cdot (%s) = %s = VP$. \\\\ Do đó, cặp số $(%s; %s)$ là một nghiệm của phương trình đã cho.''' % (x_test, y0_val, x_test, b_val, y0_val, c_val, x_test, y0_val))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # Ý c: Tập nghiệm của phương trình được biểu diễn bởi đường thẳng song song hoặc trùng với Ox (không phải song song với Oy)
    vd_da_1_d = '\\True Tập nghiệm của phương trình được biểu diễn bởi đường thẳng song song với trục hoành $Ox$'
    vd_da_1_s = 'Tập nghiệm của phương trình được biểu diễn bởi đường thẳng song song với trục tung $Oy$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Ta có: $%s = %s \\Leftrightarrow %sy = %s \\Leftrightarrow y = %s$. \\\\ Đường thẳng $y = %s$ là đường thẳng vuông góc với trục tung $Oy$ tại điểm $(0; %s)$ và song song với trục hoành $Ox$. \\\\ Do đó, khẳng định đường thẳng song song với trục tung $Oy$ là sai.''' % (lhs_str, c_val, b_val, c_val, y0_val, y0_val, y0_val))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # Ý d: Mọi điểm nằm trên đường thẳng biểu diễn tập nghiệm đều có tung độ bằng y0_val
    vdc_da_1_d = '\\True Mọi điểm nằm trên đường thẳng biểu diễn tập nghiệm đều có tung độ bằng $%s$' % (y0_val)
    vdc_da_1_s = 'Mọi điểm nằm trên đường thẳng biểu diễn tập nghiệm đều có hoành độ bằng $%s$' % (y0_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Phương trình $%s = %s \\Leftrightarrow y = %s$ thoả mãn với mọi giá trị $x \\in \\mathbb{R}$. \\\\ Do đó, tập nghiệm của phương trình là $S = \\{(x; %s) \\mid x \\in \\mathbb{R}\\}$. \\\\ Như vậy, mọi điểm thuộc đường thẳng biểu diễn tập nghiệm đều có tung độ bằng $%s$.''' % (lhs_str, c_val, y0_val, y0_val, y0_val))
    
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
