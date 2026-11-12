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


def bt_dang18_p2_b2_c1_ds9(self):
    # Khai báo biến
    x0 = random.choice([20, 25, 30])
    y0 = random.choice([10, 15, 20])
    while x0 == y0:
        y0 = random.choice([10, 15, 20])
    
    tong_nguoi = x0 + y0
    gia_nl = 50
    gia_te = 30
    tong_tien_nghin = gia_nl * x0 + gia_te * y0
    tiet_kiem_nghin = (gia_te * 20 // 100) * y0
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một đoàn khách du lịch gồm $%s\\text{ người}$ (bao gồm cả người lớn và trẻ em) đi tham quan một khu di tích lịch sử. Giá vé vào cổng cho mỗi người lớn là $%s\\,000\\text{ đồng}$ và mỗi trẻ em là $%s\\,000\\text{ đồng}$. Tổng số tiền vé mà cả đoàn phải thanh toán là $%s\\,000\\text{ đồng}$. Gọi $x$ là số người lớn và $y$ là số trẻ em trong đoàn ($x, y \\in \\mathbb{N}^*$). Xét tính đúng sai của các khẳng định sau:'''
                     % (latex(tong_nguoi), latex(gia_nl), latex(gia_te), latex(tong_tien_nghin)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Phương trình biểu thị tổng số người trong đoàn là $x + y = %s$' % (latex(tong_nguoi))
    nb_da_1_s = 'Phương trình biểu thị tổng số người trong đoàn là $x - y = %s$' % (latex(tong_nguoi))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tổng số người trong đoàn là $x + y = %s$.''' % (latex(tong_nguoi)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Phương trình biểu thị tổng số tiền vé (tính theo đơn vị nghìn đồng) là $%sx + %sy = %s$' % (latex(gia_nl), latex(gia_te), latex(tong_tien_nghin))
    th_da_1_s = 'Phương trình biểu thị tổng số tiền vé (tính theo đơn vị nghìn đồng) là $%sx + %sy = %s$' % (latex(gia_te), latex(gia_nl), latex(tong_tien_nghin))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Số tiền vé của $x$ người lớn là $%sx$ (nghìn đồng) và của $y$ trẻ em là $%sy$ (nghìn đồng), nên ta có phương trình $%sx + %sy = %s$.'''
                    % (latex(gia_nl), latex(gia_te), latex(gia_nl), latex(gia_te), latex(tong_tien_nghin)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Trong đoàn khách du lịch đó có $%s\\text{ người lớn}$ và $%s\\text{ trẻ em}$' % (latex(x0), latex(y0))
    vd_da_1_s = 'Trong đoàn khách du lịch đó có $%s\\text{ người lớn}$ và $%s\\text{ trẻ em}$' % (latex(y0), latex(x0))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx + %sy = %s \\end{cases}$, ta tìm được $x = %s$ và $y = %s$. Vậy đoàn có $%s\\text{ người lớn}$ và $%s\\text{ trẻ em}$.'''
                    % (latex(tong_nguoi), latex(gia_nl), latex(gia_te), latex(tong_tien_nghin), latex(x0), latex(y0), latex(x0), latex(y0)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Nếu khu di tích giảm giá vé trẻ em đi $20\\%%$ thì tổng số tiền vé cả đoàn tiết kiệm được là $%s\\,000\\text{ đồng}$' % (latex(tiet_kiem_nghin))
    vdc_da_1_s = 'Nếu khu di tích giảm giá vé trẻ em đi $20\\%%$ thì tổng số tiền vé cả đoàn tiết kiệm được là $%s\\,000\\text{ đồng}$' % (latex(tiet_kiem_nghin + 30))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Mỗi vé trẻ em được giảm $%s\\,000 \\cdot 20\\%% = %s\\,000\\text{ đồng}$. Với $%s\\text{ trẻ em}$, tổng số tiền vé tiết kiệm được là $%s \\cdot %s\\,000 = %s\\,000\\text{ đồng}$.'''
                     % (latex(gia_te), latex(gia_te * 20 // 100), latex(y0), latex(y0), latex(gia_te * 20 // 100), latex(tiet_kiem_nghin)))
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
