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


def bt_dang3_p2_b2_c1_ds9(self):
    # Khai báo biến
    def fmt_tp(val):
        return str(val).replace('.', ',')
    
    while True:
        x0 = random.choice([-3, -2, -1, 1, 2, 3])
        y0 = random.choice([-3, -2, -1, 1, 2, 3])
        a1 = random.choice([3, 4, 5, 6])
        b1 = random.choice([4, 5, 6, 7])
        a2 = random.choice([2, 4, 5, 8])
        b2 = random.choice([3, 5, 7, 9])
        if a1 * b2 + a2 * b1 != 0 and x0 != y0:
            break
    
    c1 = a1 * x0 + b1 * y0
    c2 = a2 * x0 - b2 * y0
    
    a1_s = fmt_tp(a1 / 10)
    b1_s = fmt_tp(b1 / 10)
    c1_s = fmt_tp(c1 / 10)
    a2_s = fmt_tp(a2 / 10)
    b2_s = fmt_tp(b2 / 10)
    c2_s = fmt_tp(c2 / 10)
    mc1_s = fmt_tp(-c1 / 10)
    
    pt1_tp = '%sx + %sy = %s' % (a1_s, b1_s, c1_s)
    pt2_tp = '%sx - %sy = %s' % (a2_s, b2_s, c2_s)
    pt1_ng = latex(a1 * x + b1 * y) + '=' + latex(c1)
    pt2_ng = latex(a2 * x - b2 * y) + '=' + latex(c2)
    tong_bp = x0**2 + y0**2
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$. Xét tính đúng sai của các khẳng định sau:'''
                     % (pt1_tp, pt2_tp))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Nhân hai vế của cả hai phương trình với $10$, ta đưa được hệ về dạng hệ số nguyên là $\\begin{cases} %s \\\\ %s \\end{cases}$' % (pt1_ng, pt2_ng)
    nb_da_1_s = 'Nhân hai vế của cả hai phương trình với $10$, ta đưa được hệ về dạng hệ số nguyên là $\\begin{cases} %s \\\\ %s = %s \\end{cases}$' % (pt1_ng, latex(a2 * x + b2 * y), latex(c2))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Nhân hai vế của mỗi phương trình với $10$ để khử số thập phân, ta được hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$.'''
                    % (pt1_ng, pt2_ng))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Khi giải hệ bằng máy tính cầm tay, ta nhập bộ hệ số hàng thứ nhất là $(%s; %s; %s)$' % (a1_s, b1_s, c1_s)
    th_da_1_s = 'Khi giải hệ bằng máy tính cầm tay, ta nhập bộ hệ số hàng thứ nhất là $(%s; %s; %s)$' % (a1_s, b1_s, mc1_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Hệ phương trình đã ở dạng chuẩn $\\begin{cases} a_1x + b_1y = c_1 \\\\ a_2x + b_2y = c_2 \\end{cases}$ nên bộ hệ số hàng thứ nhất cần nhập là $(%s; %s; %s)$.'''
                    % (a1_s, b1_s, c1_s))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Hệ phương trình đã cho có nghiệm duy nhất là $(%s; %s)$' % (latex(x0), latex(y0))
    vd_da_1_s = 'Hệ phương trình đã cho có nghiệm duy nhất là $(%s; %s)$' % (latex(-x0), latex(-y0))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Giải hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$ bằng phương pháp cộng đại số, ta tìm được $x = %s$ và $y = %s$. Vậy nghiệm của hệ là $(%s; %s)$.'''
                    % (pt1_ng, pt2_ng, latex(x0), latex(y0), latex(x0), latex(y0)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Tổng bình phương hai thành phần nghiệm của hệ là $x_0^2 + y_0^2 = %s$' % (latex(tong_bp))
    vdc_da_1_s = 'Tổng bình phương hai thành phần nghiệm của hệ là $x_0^2 + y_0^2 = %s$' % (latex(tong_bp - 2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $x_0^2 + y_0^2 = (%s)^2 + (%s)^2 = %s$.'''
                     % (latex(x0), latex(y0), latex(tong_bp)))
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
