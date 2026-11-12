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


def bt_dang20_p2_b2_c1_ds9(self):
    # Khai báo biến
    while True:
        x0 = random.choice([15, 16, 18, 20])
        y0 = random.choice([10, 12, 14])
        dx = random.choice([3, 4, 5])
        dy = random.choice([2, 3])
        if x0 > y0 > dy and (x0 + dx) * (y0 - dy) > x0 * y0:
            break
    
    nua_cv = x0 + y0
    chu_vi = 2 * nua_cv
    tang_dt = (x0 + dx) * (y0 - dy) - x0 * y0
    vp_dt = tang_dt + dx * dy
    dt_goc = x0 * y0
    
    pt_dt_rg = latex(-dy * x + dx * y) + '=' + latex(vp_dt)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một mảnh đất hình chữ nhật có chu vi bằng $%s\\text{ m}$. Nếu giảm chiều rộng đi $%s\\text{ m}$ và tăng chiều dài thêm $%s\\text{ m}$ thì diện tích mảnh đất tăng thêm $%s\\text{ m}^2$. Gọi $x\\text{ (m)}$ là chiều dài và $y\\text{ (m)}$ là chiều rộng ban đầu của mảnh đất ($x > y > %s$). Xét tính đúng sai của các khẳng định sau:'''
                     % (latex(chu_vi), latex(dy), latex(dx), latex(tang_dt), latex(dy)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Nửa chu vi của mảnh đất hình chữ nhật là $%s\\text{ m}$, do đó ta có phương trình $x + y = %s$' % (latex(nua_cv), latex(nua_cv))
    nb_da_1_s = 'Nửa chu vi của mảnh đất hình chữ nhật là $%s\\text{ m}$, do đó ta có phương trình $x + y = %s$' % (latex(nua_cv), latex(chu_vi))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Nửa chu vi của hình chữ nhật bằng $%s : 2 = %s\\text{ (m)}$, nên ta có phương trình $x + y = %s$.'''
                    % (latex(chu_vi), latex(nua_cv), latex(nua_cv)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Phương trình biểu diễn sự thay đổi diện tích của mảnh đất là $(x + %s)(y - %s) = xy + %s$, rút gọn thành $%s$' % (latex(dx), latex(dy), latex(tang_dt), pt_dt_rg)
    th_da_1_s = 'Phương trình biểu diễn sự thay đổi diện tích của mảnh đất là $(x + %s)(y - %s) = xy + %s$, rút gọn thành $%s = %s$' % (latex(dx), latex(dy), latex(tang_dt), latex(-dy * x + dx * y), latex(tang_dt - dx * dy))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $(x + %s)(y - %s) = xy + %s \\Leftrightarrow xy - %sx + %sy - %s = xy + %s \\Leftrightarrow %s$.'''
                    % (latex(dx), latex(dy), latex(tang_dt), latex(dy), latex(dx), latex(dx * dy), latex(tang_dt), pt_dt_rg))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Chiều dài ban đầu của mảnh đất là $%s\\text{ m}$ và chiều rộng ban đầu là $%s\\text{ m}$' % (latex(x0), latex(y0))
    vd_da_1_s = 'Chiều dài ban đầu của mảnh đất là $%s\\text{ m}$ và chiều rộng ban đầu là $%s\\text{ m}$' % (latex(x0 + 2), latex(y0 - 2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ %s \\end{cases}$, ta tìm được $x = %s\\text{ (m)}$ và $y = %s\\text{ (m)}$.'''
                    % (latex(nua_cv), pt_dt_rg, latex(x0), latex(y0)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Diện tích ban đầu của mảnh đất hình chữ nhật đó là $%s\\text{ m}^2$' % (latex(dt_goc))
    vdc_da_1_s = 'Diện tích ban đầu của mảnh đất hình chữ nhật đó là $%s\\text{ m}^2$' % (latex(dt_goc + 16))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Diện tích ban đầu của mảnh đất hình chữ nhật đó là $S = x \\cdot y = %s \\cdot %s = %s\\text{ (m}^2\\text{)}$.'''
                     % (latex(x0), latex(y0), latex(dt_goc)))
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
