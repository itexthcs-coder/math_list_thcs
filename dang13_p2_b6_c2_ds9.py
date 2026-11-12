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


def bt_dang13_p2_b6_c2_ds9(self):
    # Khai báo biến: Giá mở cửa M nghìn, mỗi km giá K nghìn, ngân sách S nghìn
    M = random.choice([12, 14, 15])
    K = random.choice([11, 12, 13])
    max_km = randint(12, 18)
    du_tien = randint(3, K - 1)
    S = M + K * max_km + du_tien
    phan_so = Rational(S - M, K)
    gia_tri_xap_xi = round(float(phan_so), 2)
    
    noidungcauhoi = ('''Một hãng taxi có giá mở cửa là $%s$ nghìn đồng và giá $%s$ nghìn đồng cho mỗi kilômét di chuyển. Một hành khách có $%s$ nghìn đồng để đi taxi của hãng này. Gọi $x$ ($\\text{km}$, $x > 0$) là quãng đường hành khách di chuyển.'''
                     % (M, K, S))
    
    # Mệnh đề a
    nb_da_1_d = '\\True Số tiền hành khách phải trả cho quãng đường $x$ ($\\text{km}$) là $%sx + %s$ (nghìn đồng).' % (K, M)
    nb_da_1_s = 'Số tiền hành khách phải trả cho quãng đường $x$ ($\\text{km}$) là $%sx + %s$ (nghìn đồng).' % (M, K)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tổng chi phí gồm giá mở cửa $%s$ nghìn đồng cộng với tiền cước $%sx$ nghìn đồng cho $x$ kilômét, tức là $%sx + %s$ (nghìn đồng).'''
                    % (M, K, K, M))
    
    # Mệnh đề b
    th_da_1_d = '\\True Bất phương trình biểu thị giới hạn chi tiêu của hành khách là $%sx + %s \\le %s$.' % (K, M, S)
    th_da_1_s = 'Bất phương trình biểu thị giới hạn chi tiêu của hành khách là $%sx + %s \\ge %s$.' % (K, M, S)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Số tiền phải trả không được vượt quá $%s$ nghìn đồng nên ta có $%sx + %s \\le %s$.''' % (S, K, M, S))
    
    # Mệnh đề c
    vd_da_1_d = '\\True Giải bất phương trình ta được $x \\le %s$.' % latex(phan_so)
    vd_da_1_s = 'Giải bất phương trình ta được $x \\le %s$.' % latex(Rational(S + M, K))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $%sx + %s \\le %s \\Leftrightarrow %sx \\le %s \\Leftrightarrow x \\le %s$.'''
                    % (K, M, S, K, S - M, latex(phan_so)))
    
    # Mệnh đề d
    vdc_da_1_d = '\\True Nếu tính theo số nguyên kilômét, hành khách có thể di chuyển tối đa $%s\\text{ km}$.' % max_km
    vdc_da_1_s = 'Nếu tính theo số nguyên kilômét, hành khách có thể di chuyển tối đa $%s\\text{ km}$.' % (max_km + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $x \\le %s \\approx %s$ nên nếu tính theo số nguyên kilômét, hành khách chỉ đi được tối đa $%s\\text{ km}$ (nếu đi $%s\\text{ km}$ sẽ vượt quá số tiền hiện có).'''
                     % (latex(phan_so), str(gia_tri_xap_xi).replace('.', ','), max_km, max_km + 1))
    
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
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
