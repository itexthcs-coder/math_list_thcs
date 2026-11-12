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


def bt_dang17_p2_b2_c1_ds9(self):
    # Khai báo biến
    def fmt_tp(val):
        return str(val).replace('.', ',')
    
    x0 = random.choice([200, 300])
    y0 = random.choice([300, 400])
    while x0 == y0:
        y0 = random.choice([300, 400])
    
    tong_tien = x0 + y0
    rA = 5
    rB = 6
    lai_A = (x0 * rA) // 100
    lai_B = (y0 * rB) // 100
    tong_lai = lai_A + lai_B
    chenh_lech = abs(y0 - x0)
    
    hsA_tp = fmt_tp(rA / 100)
    hsB_tp = fmt_tp(rB / 100)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Bác Lan có tổng cộng $%s\\text{ triệu đồng}$ và chia làm hai khoản gửi tiết kiệm ở hai ngân hàng khác nhau với kì hạn $1\\text{ năm}$. Khoản thứ nhất gửi ở ngân hàng $A$ với lãi suất $%s\\%%/\\text{năm}$, khoản thứ hai gửi ở ngân hàng $B$ với lãi suất $%s\\%%/\\text{năm}$. Sau một năm, tổng số tiền lãi bác Lan nhận được từ cả hai ngân hàng là $%s\\text{ triệu đồng}$. Gọi $x$ (triệu đồng) là số tiền gửi ở ngân hàng $A$ và $y$ (triệu đồng) là số tiền gửi ở ngân hàng $B$ ($x, y > 0$). Xét tính đúng sai của các khẳng định sau:'''
                     % (latex(tong_tien), latex(rA), latex(rB), latex(tong_lai)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Hệ phương trình biểu diễn mối quan hệ giữa $x$ và $y$ là $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$' % (latex(tong_tien), hsA_tp, hsB_tp, latex(tong_lai))
    nb_da_1_s = 'Hệ phương trình biểu diễn mối quan hệ giữa $x$ và $y$ là $\\begin{cases} x + y = %s \\\\ 0,5x + 0,6y = %s \\end{cases}$' % (latex(tong_tien), latex(tong_lai))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tổng số tiền gửi là $x + y = %s$. Tiền lãi sau một năm ở hai ngân hàng là $%sx + %sy = %s$. Ta có hệ $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$.'''
                    % (latex(tong_tien), hsA_tp, hsB_tp, latex(tong_lai), latex(tong_tien), hsA_tp, hsB_tp, latex(tong_lai)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Số tiền bác Lan gửi ở ngân hàng $A$ là $%s\\text{ triệu đồng}$' % (latex(x0))
    th_da_1_s = 'Số tiền bác Lan gửi ở ngân hàng $A$ là $%s\\text{ triệu đồng}$' % (latex(y0))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Giải hệ phương trình trên, ta tìm được $x = %s\\text{ (triệu đồng)}$ và $y = %s\\text{ (triệu đồng)}$. Vậy số tiền gửi ở ngân hàng $A$ là $%s\\text{ triệu đồng}$.'''
                    % (latex(x0), latex(y0), latex(x0)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Số tiền lãi bác Lan nhận được từ ngân hàng $B$ sau một năm là $%s\\text{ triệu đồng}$' % (latex(lai_B))
    vd_da_1_s = 'Số tiền lãi bác Lan nhận được từ ngân hàng $B$ sau một năm là $%s\\text{ triệu đồng}$' % (latex(lai_A))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Số tiền lãi nhận được từ ngân hàng $B$ sau một năm là $%s \\cdot %s\\%% = %s\\text{ (triệu đồng)}$.'''
                    % (latex(y0), latex(rB), latex(lai_B)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Khoản tiền gửi ở ngân hàng $B$ nhiều hơn khoản tiền gửi ở ngân hàng $A$ là $%s\\text{ triệu đồng}$' % (latex(y0 - x0))
    vdc_da_1_s = 'Khoản tiền gửi ở ngân hàng $A$ nhiều hơn khoản tiền gửi ở ngân hàng $B$ là $%s\\text{ triệu đồng}$' % (latex(chenh_lech + 50))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $y - x = %s - %s = %s\\text{ (triệu đồng)}$.'''
                     % (latex(y0), latex(x0), latex(y0 - x0)))
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
