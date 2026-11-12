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


def bt_dang4_p2_b3_c1_ds9(self):
    # Chọn bộ nghiệm đẹp (x0, y0) phút
    cases = [
        (120, 240, 80, 10, 12),   # 1/120 + 1/240 = 1/80; 10/120 + 12/240 = 2/15
        (100, 150, 60, 10, 15),   # 1/100 + 1/150 = 1/60; 10/100 + 15/150 = 1/5
        (150, 300, 100, 15, 20),  # 1/150 + 1/300 = 1/100; 15/150 + 20/300 = 1/6
        (180, 360, 120, 12, 18)   # 1/180 + 1/360 = 1/120; 12/180 + 18/360 = 7/60
    ]
    x0, y0, t_chung, t1, t2 = random.choice(cases)
    phan_be = Rational(t1, x0) + Rational(t2, y0)
    
    h = t_chung // 60
    m = t_chung % 60
    t_chung_str = f"{h}\\text{{ giờ }} {m}\\text{{ phút}}" if m > 0 else f"{h}\\text{{ giờ}}"
    
    noidungcauhoi = ('''Nếu hai vòi nước cùng chảy vào một bể không có nước thì bể sẽ đầy trong $%s$. Nếu mở riêng vòi thứ nhất trong $%s\\text{ phút}$ và vòi thứ hai trong $%s\\text{ phút}$ thì chỉ được $%s$ bể nước. Gọi $x$ (phút) và $y$ (phút) lần lượt là thời gian vòi thứ nhất và vòi thứ hai chảy một mình đầy bể ($x > 0, y > 0$).''' % (t_chung_str, t1, t2, latex(phan_be)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Đổi $%s = %s\\text{ phút}$, do đó trong $1\\text{ phút}$ cả hai vòi cùng chảy được $\\dfrac{1}{%s}$ bể' % (t_chung_str, t_chung, t_chung)
    nb_da_1_s = 'Đổi $%s = %s\\text{ phút}$, do đó trong $1\\text{ phút}$ cả hai vòi cùng chảy được $\\dfrac{1}{%s}$ bể' % (t_chung_str, t_chung + 20, t_chung + 20)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    
    loigiai_nb_1 = ('''Ta có $%s = %s\\text{ phút}$. Hai vòi cùng chảy trong $%s\\text{ phút}$ thì đầy bể nên trong $1\\text{ phút}$ cả hai vòi cùng chảy được $\\dfrac{1}{%s}$ bể.''' % (t_chung_str, t_chung, t_chung, t_chung))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Trong $%s\\text{ phút}$ vòi thứ nhất chảy được $\\dfrac{%s}{x}$ bể, trong $%s\\text{ phút}$ vòi thứ hai chảy được $\\dfrac{%s}{y}$ bể' % (t1, t1, t2, t2)
    th_da_1_s = 'Trong $%s\\text{ phút}$ vòi thứ nhất chảy được $\\dfrac{x}{%s}$ bể, trong $%s\\text{ phút}$ vòi thứ hai chảy được $\\dfrac{y}{%s}$ bể' % (t1, t1, t2, t2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    
    loigiai_th_1 = ('''Mỗi phút vòi thứ nhất chảy được $\\dfrac{1}{x}$ bể, vòi thứ hai chảy được $\\dfrac{1}{y}$ bể. Vậy sau $%s\\text{ phút}$ vòi thứ nhất chảy được $\\dfrac{%s}{x}$ bể và sau $%s\\text{ phút}$ vòi thứ hai chảy được $\\dfrac{%s}{y}$ bể.''' % (t1, t1, t2, t2))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Hệ phương trình lập được là $\\begin{cases} \\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{%s} \\\\ \\dfrac{%s}{x} + \\dfrac{%s}{y} = %s \\end{cases}$' % (t_chung, t1, t2, latex(phan_be))
    vd_da_1_s = 'Hệ phương trình lập được là $\\begin{cases} \\dfrac{1}{x} + \\dfrac{1}{y} = %s \\\\ \\dfrac{%s}{x} + \\dfrac{%s}{y} = %s \\end{cases}$' % (t_chung, t1, t2, latex(phan_be))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    
    loigiai_vd_1 = ('''Từ các dữ kiện đề bài, ta có hệ phương trình biểu diễn bài toán là $\\begin{cases} \\dfrac{1}{x} + \\dfrac{1}{y} = \\dfrac{1}{%s} \\\\ \\dfrac{%s}{x} + \\dfrac{%s}{y} = %s. \\end{cases}$''' % (t_chung, t1, t2, latex(phan_be)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Nếu mở riêng từng vòi thì vòi thứ nhất chảy đầy bể trong $%s\\text{ phút}$ và vòi thứ hai chảy đầy bể trong $%s\\text{ phút}$' % (x0, y0)
    vdc_da_1_s = 'Nếu mở riêng từng vòi thì vòi thứ nhất chảy đầy bể trong $%s\\text{ phút}$ và vòi thứ hai chảy đầy bể trong $%s\\text{ phút}$' % (y0, x0)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    
    loigiai_vdc_1 = ('''Đặt $u = \\dfrac{1}{x}$ và $v = \\dfrac{1}{y}$, giải hệ bậc nhất hai ẩn ta được $u = \\dfrac{1}{%s}$ và $v = \\dfrac{1}{%s}$, suy ra $x = %s$ và $y = %s$ (thỏa mãn).''' % (x0, y0, x0, y0))
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
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' '\\choiceTFn \n' '{'+str(shuffled_answers_nb[0])+'}\n' '{'+str(shuffled_answers_th[0])+'}\n' '{'+str(shuffled_answers_vd[0])+'}\n' '{'+str(shuffled_answers_vdc[0])+'}\n' '\\loigiai{ \n' '\\begin{enumEX}[a)]{1} \n' '\\item '+str(shuffled_solutions_nb[0])+'\n' '\\item '+str(shuffled_solutions_th[0])+'\n' '\\item '+str(shuffled_solutions_vd[0])+'\n' '\\item '+str(shuffled_solutions_vdc[0])+'\n' '\\end{enumEX}} \n' '\\end{ex}\n \\end{minipage}\n\n')

    return content
