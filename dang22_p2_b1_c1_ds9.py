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


def bt_dang22_p2_b1_c1_ds9(self):
    # Khai báo biến
    x, y = symbols('x y')
    
    # Dạng bài: Bài toán thực tế chu vi hình chữ nhật
    # Mẫu gốc: Chu vi 48 m, nửa chu vi 24 m, pt x + y = 24
    # Điều kiện thực tế: x > y > 0
    while True:
        # Nửa chu vi p chẵn để dễ chọn các kích thước đẹp
        half_perim = random.choice([20, 24, 28, 30, 32, 36, 40])
        perim = 2 * half_perim
        
        # Chọn cặp kích thước hợp lý: x_true > y_true > 0 và x_true + y_true = half_perim
        diff = random.choice([4, 6, 8, 10])
        if (half_perim + diff) % 2 == 0:
            x_true = (half_perim + diff) // 2
            y_true = (half_perim - diff) // 2
            if x_true > y_true > 0:
                # Cặp kích thước đảo ngược (chiều dài nhỏ hơn chiều rộng): (y_true, x_true)
                x_inv = y_true
                y_inv = x_true
                break
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Bác An rào một mảnh vườn hình chữ nhật có chu vi là %s m. Gọi chiều dài vườn là $x$ (m) và chiều rộng vườn là $y$ (m).''' % (perim))
    
    ############################################################################# Nhận biết #################################################
    # a) Nửa chu vi của mảnh vườn là half_perim m
    half_perim_wrong = half_perim + random.choice([2, -2])
    nb_da_1_d = '\\True Nửa chu vi của mảnh vườn là %s m' % (half_perim)
    nb_da_1_s = 'Nửa chu vi của mảnh vườn là %s m' % (half_perim_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Nửa chu vi của mảnh vườn hình chữ nhật là: \\\\ $%s : 2 = %s$ m.''' % (perim, half_perim))
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ############################################################################# Thông hiểu #################################################
    # b) Mối liên hệ giữa chiều dài và chiều rộng được biểu diễn bởi phương trình x + y = half_perim
    th_da_1_d = '\\True Mối liên hệ giữa chiều dài và chiều rộng được biểu diễn bởi phương trình $x + y = %s$' % (half_perim)
    th_da_1_s = 'Mối liên hệ giữa chiều dài và chiều rộng được biểu diễn bởi phương trình $x + y = %s$' % (perim)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Vì nửa chu vi hình chữ nhật bằng tổng chiều dài và chiều rộng nên ta có mối liên hệ: \\\\ $x + y = %s$.''' % (half_perim))
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ############################################################################# Vận dụng #################################################
    # c) Cặp số (x_true; y_true) thoả mãn kích thước thực tế của mảnh vườn (x > y > 0)
    vd_da_1_d = '\\True Cặp số $(%s; %s)$ thoả mãn kích thước thực tế của mảnh vườn ($x > y > 0$)' % (x_true, y_true)
    vd_da_1_s = 'Cặp số $(%s; %s)$ không thoả mãn kích thước thực tế của mảnh vườn ($x > y > 0$)' % (x_true, y_true)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Với cặp số $(%s; %s)$, ta có $x = %s$ m và $y = %s$ m. \\\\ Kiểm tra các điều kiện: \\\\ + Tổng chiều dài và chiều rộng: $%s + %s = %s$ m (thoả mãn nửa chu vi). \\\\ + Chiều dài lớn hơn chiều rộng và các kích thước dương: $%s > %s > 0$ (thoả mãn điều kiện thực tế). \\\\ Do đó, cặp số $(%s; %s)$ hoàn toàn thoả mãn bài toán thực tế.''' % (x_true, y_true, x_true, y_true, x_true, y_true, half_perim, x_true, y_true, x_true, y_true))
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ############################################################################# Vận dụng cao #################################################
    # d) Cặp số (x_inv; y_inv) không phải là cặp kích thước hợp lý vì chiều dài < chiều rộng
    vdc_da_1_d = '\\True Cặp số $(%s; %s)$ không phải là một cặp kích thước hợp lý của chiều dài và chiều rộng mảnh vườn' % (x_inv, y_inv)
    vdc_da_1_s = 'Cặp số $(%s; %s)$ là một cặp kích thước hợp lý của chiều dài và chiều rộng mảnh vườn' % (x_inv, y_inv)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Trong hình chữ nhật, chiều dài $x$ bắt buộc phải lớn hơn chiều rộng $y$ ($x > y$). \\\\ Nếu lấy cặp số $(%s; %s)$ thì $x = %s$ và $y = %s$, khi đó $x < y$ (chiều dài lại nhỏ hơn chiều rộng), điều này không hợp lý trong thực tế. \\\\ Do đó, cặp số $(%s; %s)$ không phải là cặp kích thước hợp lý của mảnh vườn.''' % (x_inv, y_inv, x_inv, y_inv, x_inv, y_inv, x_inv, y_inv))
    
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
