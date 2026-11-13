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


def bt_dang5_p2_b1_c3_ds9(self):
    # Khai báo biến
    a = random.randint(2, 5)
    nghiem = random.randint(4, 9)
    b = a * nghiem
    bt = b - a * x
    x_ngoai = nghiem + 1
    gt_ngoai = b - a * x_ngoai
    so_nguyen_khong_am = nghiem + 1

    # Nội dung câu hỏi
    noidungcauhoi = (f'''Cho biểu thức $B = \\sqrt{{{latex(bt)}}}$. Xét tính đúng, sai của các khẳng định sau:''')

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = f'\\True Biểu thức $B$ có nghĩa khi ${latex(bt)} \\ge 0$.'
    nb_da_1_s = f'Biểu thức $B$ có nghĩa khi ${latex(bt)} \\le 0$.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1_d = f'Căn thức bậc hai $\\sqrt{{M}}$ có nghĩa khi $M \\ge 0$, tức là ${latex(bt)} \\ge 0$.'
    loigiai_nb_1_s = f'Sai. Biểu thức $B$ có nghĩa khi biểu thức dưới dấu căn không âm: ${latex(bt)} \\ge 0$.'

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = f'\\True Điều kiện xác định của $B$ là $x \\le {nghiem}$.'
    th_da_1_s = f'Điều kiện xác định của $B$ là $x \\ge {nghiem}$.'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1_d = f'Ta có ${latex(bt)} \\ge 0 \\Leftrightarrow {b} \\ge {a}x \\Leftrightarrow x \\le {nghiem}$.'
    loigiai_th_1_s = f'Sai. Khi chia hai vế bất phương trình $-{a}x \\ge -{b}$ cho số âm $-{a}$ ta phải đổi chiều: $x \\le {nghiem}$.'

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = f'\\True Tại $x = {x_ngoai}$, biểu thức $B$ không xác định.'
    vd_da_1_s = f'Tại $x = {x_ngoai}$, giá trị của biểu thức $B$ bằng $\\sqrt{{{gt_ngoai}}}$.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1_d = f'Tại $x = {x_ngoai} > {nghiem}$, ta có ${b} - {a}\\cdot {x_ngoai} = {gt_ngoai} < 0$ nên $B$ không xác định.'
    loigiai_vd_1_s = f'Sai. Vì tại $x = {x_ngoai}$ thì ${b} - {a}\\cdot {x_ngoai} = {gt_ngoai} < 0$, số âm không có căn bậc hai.'

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = f'\\True Có đúng ${so_nguyen_khong_am}$ giá trị nguyên không âm của $x$ để biểu thức $B$ có nghĩa.'
    vdc_da_1_s = f'Có đúng ${nghiem}$ giá trị nguyên không âm của $x$ để biểu thức $B$ có nghĩa.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1_d = f'Các giá trị nguyên không âm của $x$ thoả mãn $0 \\le x \\le {nghiem}$ là $x \\in \\{{0; 1; 2; \\dots; {nghiem}\\}}$, gồm ${so_nguyen_khong_am}$ giá trị.'
    loigiai_vdc_1_s = f'Sai. Các số nguyên không âm thoả mãn $0 \\le x \\le {nghiem}$ là $0; 1; \\dots; {nghiem}$, gồm ${so_nguyen_khong_am}$ giá trị (tính cả số $0$).'

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

    loigiai_nb_1 = loigiai_nb_1_d if '\\True' in nb_da_1 else loigiai_nb_1_s
    loigiai_th_1 = loigiai_th_1_d if '\\True' in th_da_1 else loigiai_th_1_s
    loigiai_vd_1 = loigiai_vd_1_d if '\\True' in vd_da_1 else loigiai_vd_1_s
    loigiai_vdc_1 = loigiai_vdc_1_d if '\\True' in vdc_da_1 else loigiai_vdc_1_s

    # Xuất câu hỏi
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
