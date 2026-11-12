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


def bt_dang4_p2_b2_c1_ds9(self):
    # Khai báo biến
    a1 = random.choice([2, 3, 4])
    b1 = random.choice([3, 5, 7])
    while math.gcd(a1, b1) != 1:
        b1 = random.choice([3, 5, 7])
    
    # Tạo một nghiệm nguyên (x0; y0) để phương trình a1*x - b1*y = c1 có nghiệm nguyên đẹp
    x0 = random.choice([2, 3, 4, 5])
    y0 = random.choice([1, 2, 3])
    c1 = a1 * x0 - b1 * y0
    k = random.choice([-3, -2, 2, 3])
    
    pt1_str = latex(a1 * x - b1 * y) + '=' + latex(c1)
    pt2_str = latex(k * a1 * x - k * b1 * y) + '=' + latex(k * c1)
    y_tq = Rational(a1, b1) * x - Rational(c1, b1)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$. Xét tính đúng sai của các khẳng định sau:'''
                     % (pt1_str, pt2_str))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Chia hai vế của phương trình thứ hai cho $%s$, ta thu được phương trình trùng với phương trình thứ nhất' % (latex(k))
    nb_da_1_s = 'Chia hai vế của phương trình thứ hai cho $%s$, ta thu được phương trình $%s = %s$' % (latex(k), latex(a1 * x - b1 * y), latex(-c1))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Chia hai vế của phương trình thứ hai cho $%s$, ta được phương trình $%s$ trùng với phương trình thứ nhất của hệ.'''
                    % (latex(k), pt1_str))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Hệ phương trình đã cho có vô số nghiệm'
    th_da_1_s = 'Hệ phương trình đã cho vô nghiệm vì xuất hiện hệ thức $0x + 0y = 0$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Sau khi rút gọn phương trình thứ hai và trừ từng vế hai phương trình, ta được hệ thức $0x + 0y = 0$ luôn thỏa mãn với mọi giá trị tùy ý của $x$ và $y$. Vậy hệ phương trình đã cho có vô số nghiệm.''')
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Công thức nghiệm tổng quát của hệ phương trình đã cho là $\\left(x; %s\\right)$ với $x \\in \\mathbb{R}$ tùy ý' % (latex(y_tq))
    vd_da_1_s = 'Công thức nghiệm tổng quát của hệ phương trình đã cho là $\\left(x; %s\\right)$ với $x \\in \\mathbb{R}$ tùy ý' % (latex(Rational(a1, b1) * x + Rational(c1, b1)))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Với giá trị tùy ý của $x \\in \\mathbb{R}$, từ phương trình $%s$ ta tính được $y = %s$. Vậy nghiệm của hệ phương trình là $\\left(x; %s\\right)$ với $x \\in \\mathbb{R}$ tùy ý.'''
                    % (pt1_str, latex(y_tq), latex(y_tq)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Cặp số $(%s; %s)$ là một trong các nghiệm của hệ phương trình đã cho' % (latex(x0), latex(y0))
    vdc_da_1_s = 'Cặp số $(%s; %s)$ là một trong các nghiệm của hệ phương trình đã cho' % (latex(x0 + 1), latex(y0))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Thay $x = %s$ vào công thức nghiệm tổng quát, ta được $y = %s \\cdot %s - \\left(%s\\right) = %s$. Vậy cặp số $(%s; %s)$ là một nghiệm của hệ phương trình đã cho.'''
                     % (latex(x0), latex(Rational(a1, b1)), latex(x0), latex(Rational(c1, b1)), latex(y0), latex(x0), latex(y0)))
    list_vdc_2 = [loigiai_vdc_1]
    
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
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\n' '\\choiceTFn \n' '{' + str(shuffled_answers_nb[0]) + '}\n' '{' + str(shuffled_answers_th[0]) + '}\n' '{' + str(shuffled_answers_vd[0]) + '}\n' '{' + str(shuffled_answers_vdc[0]) + '}\n' '\\loigiai{ \n' '\\begin{enumEX}[a)]{1} \n' '\\item ' + str(shuffled_solutions_nb[0]) + '\n' '\\item ' + str(shuffled_solutions_th[0]) + '\n' '\\item ' + str(shuffled_solutions_vd[0]) + '\n' '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' '\\end{enumEX}} \n' '\\end{ex}\n \\end{minipage}\n\n')

    return content
