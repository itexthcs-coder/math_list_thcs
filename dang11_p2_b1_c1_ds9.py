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


def bt_dang11_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Dạng bài: Cho phương trình x - b*y = c
    # Mẫu gốc: x - 3y = 2
    while True:
        b_val = random.choice([2, 3, 4, 5])
        c_val = random.choice([2, 3, 4, 5])
        y_test = random.choice([-2, -1, 1, 2])
        x_test = b_val * y_test + c_val
        if x_test != 0:
            break
    
    # Chuỗi phương trình
    lhs_str = 'x - %sy' % (b_val)
    # Biểu thức nghiệm tổng quát theo y: x = b_val * y + c_val
    expr_x_by_y = '%sy + %s' % (b_val, c_val) if c_val > 0 else '%sy - %s' % (b_val, abs(c_val))
    expr_x_wrong = '%sy - %s' % (b_val, c_val) if c_val > 0 else '%sy + %s' % (b_val, abs(c_val))
    
    # Khoảng cách từ O(0; 0) đến đường thẳng x - b*y - c = 0
    # d(O, d) = | -c | / sqrt(1 + b^2) = c / sqrt(1 + b^2)
    sum_sq = 1 + b_val**2
    d_latex = '\\dfrac{%s}{\\sqrt{%s}}' % (c_val, sum_sq)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho phương trình $%s = %s$.''' % (lhs_str, c_val))
    
    ############################################################################# Nhận biết #################################################
    # a) Nghiệm tổng quát của phương trình là (by + c; y) với y \in \mathbb{R} tuỳ ý
    nb_da_1_d = '\\True Nghiệm tổng quát của phương trình là $(%s; y)$ với $y \\in \\mathbb{R}$ tuỳ ý' % (expr_x_by_y)
    nb_da_1_s = 'Nghiệm tổng quát của phương trình là $(%s; y)$ với $y \\in \\mathbb{R}$ tuỳ ý' % (expr_x_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Từ phương trình $%s = %s$, ta biểu diễn $x$ theo $y$: \\\\ $%s = %s \\Leftrightarrow x = %s$. \\\\ Do đó, nghiệm tổng quát của phương trình là $(%s; y)$ với $y \\in \\mathbb{R}$ tuỳ ý.''' % (lhs_str, c_val, lhs_str, c_val, expr_x_by_y, expr_x_by_y))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Nếu y = y_test thì x = x_test
    x_test_wrong = x_test + random.choice([1, -1])
    th_da_1_d = '\\True Nếu $y = %s$ thì $x = %s$' % (y_test, x_test)
    th_da_1_s = 'Nếu $y = %s$ thì $x = %s$' % (y_test, x_test_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Thay $y = %s$ vào công thức nghiệm tổng quát $x = %s$, ta được: \\\\ $x = %s \\cdot (%s) + %s = %s$. \\\\ Vậy với $y = %s$ thì $x = %s$.''' % (y_test, expr_x_by_y, b_val, y_test, c_val, x_test, y_test, x_test))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Điểm N(x_test; y_test) nằm trên đường thẳng biểu diễn tập nghiệm của phương trình
    vd_da_1_d = '\\True Điểm $N(%s; %s)$ nằm trên đường thẳng biểu diễn tập nghiệm của phương trình' % (x_test, y_test)
    vd_da_1_s = 'Điểm $N(%s; %s)$ không nằm trên đường thẳng biểu diễn tập nghiệm của phương trình' % (x_test, y_test)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Thay toạ độ điểm $N(%s; %s)$ vào vế trái của phương trình, ta có: \\\\ $(%s) - %s \\cdot (%s) = %s - (%s) = %s = VP$. \\\\ Vì toạ độ điểm $N(%s; %s)$ thoả mãn phương trình nên điểm $N$ nằm trên đường thẳng biểu diễn tập nghiệm của phương trình.''' % (x_test, y_test, x_test, b_val, y_test, x_test, b_val * y_test, c_val, x_test, y_test))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Khoảng cách từ gốc toạ độ O(0; 0) đến đường thẳng x - by = c
    # Đúng: c / \sqrt{1 + b^2}
    # Sai: c (quên chia căn)
    vdc_da_1_d = '\\True Khoảng cách từ gốc toạ độ $O(0; 0)$ đến đường thẳng $%s = %s$ bằng $%s$' % (lhs_str, c_val, d_latex)
    vdc_da_1_s = 'Khoảng cách từ gốc toạ độ $O(0; 0)$ đến đường thẳng $%s = %s$ bằng $%s$' % (lhs_str, c_val, c_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Viết lại phương trình đường thẳng dưới dạng tổng quát: $x - %sy - %s = 0$. \\\\ Áp dụng công thức khoảng cách từ gốc toạ độ $O(0; 0)$ đến đường thẳng, ta có: \\\\ $d(O, \\Delta) = \\dfrac{|0 - %s \\cdot 0 - %s|}{\\sqrt{1^2 + (-%s)^2}} = \\dfrac{|-%s|}{\\sqrt{1 + %s}} = %s$. \\\\ Do đó khẳng định khoảng cách bằng $%s$ là sai.''' % (b_val, c_val, b_val, c_val, b_val, c_val, b_val**2, d_latex, c_val))
    
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
