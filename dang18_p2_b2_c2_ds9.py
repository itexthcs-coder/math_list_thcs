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


def bt_dang18_p2_b2_c2_ds9(self):
    # Dạng 18: Tính điểm trung bình xét danh hiệu học sinh
    bo_diem = random.choice([
        ([7, 8, 8, 9], 8.5, 49, 23), # 72 - 49 = 23 => x >= 7.67
        ([8, 8, 8, 9], 8.5, 50, 22), # 72 - 50 = 22 => x >= 7.33
        ([7, 7, 8, 9], 8.5, 48, 24)  # 72 - 48 = 24 => x >= 8.0
    ])
    tx, gk, tong_hs, can_3x = bo_diem
    gk_str = str(gk).replace('.', ',')
    
    noidungcauhoi = '''Để đạt danh hiệu Học sinh Giỏi môn Toán trong học kì I, điểm trung bình môn Toán (chưa xét làm tròn) phải đạt từ $8,0$ trở lên. Bạn An đã có $4$ cột điểm đánh giá thường xuyên lần lượt là $%d; %d; %d; %d$ (hệ số 1) và điểm đánh giá giữa kì là $%s$ (hệ số 2). Gọi $x$ ($0 \\le x \\le 10$) là điểm đánh giá cuối kì (hệ số 3) của bạn An. Biết điểm trung bình môn được tính bằng tổng điểm có hệ số chia cho tổng các hệ số ($1 + 1 + 1 + 1 + 2 + 3 = 9$). Xét tính đúng sai của các khẳng định sau:''' % (tx[0], tx[1], tx[2], tx[3], gk_str)
    
    # Mệnh đề 1
    nb_da_1_d = '\\True Tổng điểm có hệ số của An trước khi thi cuối kì là $%d$.' % tong_hs
    nb_da_1_s = 'Tổng điểm có hệ số của An trước khi thi cuối kì là $%d$.' % (tong_hs - 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = '''Tổng điểm có hệ số trước khi thi cuối kì là: $%d + %d + %d + %d + %s \\cdot 2 = %d$.''' % (tx[0], tx[1], tx[2], tx[3], gk_str, tong_hs)
    
    # Mệnh đề 2
    th_da_1_d = '\\True Để đạt điểm trung bình từ $8,0$ trở lên, điểm $x$ phải thỏa mãn $\\dfrac{%d + 3x}{9} \\ge 8,0$.' % tong_hs
    th_da_1_s = 'Để đạt điểm trung bình từ $8,0$ trở lên, điểm $x$ phải thỏa mãn $\\dfrac{%d + 3x}{9} > 8,0$.' % tong_hs
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = '''Điểm trung bình môn là $\\dfrac{%d + 3x}{9}$. Yêu cầu đạt từ $8,0$ trở lên được biểu diễn bởi bất đẳng thức $\\dfrac{%d + 3x}{9} \\ge 8,0$.''' % (tong_hs, tong_hs)
    
    # Mệnh đề 3
    vd_da_1_d = '\\True Từ bất đẳng thức ở ý b, suy ra $3x \\ge %d$.' % can_3x
    vd_da_1_s = 'Từ bất đẳng thức ở ý b, suy ra $3x \\ge %d$.' % (can_3x - 2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = '''Nhân cả hai vế của $\\dfrac{%d + 3x}{9} \\ge 8,0$ với $9 > 0$ được $%d + 3x \\ge 72$. Cộng hai vế với $-%d$ ta được $3x \\ge %d$.''' % (tong_hs, tong_hs, tong_hs, can_3x)
    
    # Mệnh đề 4
    min_x = round(can_3x / 3, 2)
    sai_x = round(min_x - 0.5, 1)
    if can_3x % 3 == 0:
        vdc_da_1_d = '\\True Bạn An cần đạt ít nhất $%d$ điểm trong bài thi cuối kì để có điểm trung bình từ $8,0$ trở lên.' % (can_3x // 3)
        vdc_da_1_s = 'Bạn An chỉ cần đạt $%s$ điểm trong bài thi cuối kì thì điểm trung bình đã đạt từ $8,0$ trở lên.' % str(sai_x).replace('.', ',')
        loigiai_vdc_1 = '''Nhân hai vế của $3x \\ge %d$ với $\\dfrac{1}{3} > 0$ ta được $x \\ge %d$. Vậy An cần đạt ít nhất $%d$ điểm.''' % (can_3x, can_3x // 3, can_3x // 3)
    else:
        diem_le = math.ceil(can_3x / 3 * 4) / 4
        vdc_da_1_d = '\\True Nếu bài thi cuối kì được tính điểm lẻ đến $0,25$ thì An cần đạt ít nhất $%s$ điểm.' % str(diem_le).replace('.', ',')
        vdc_da_1_s = 'Bạn An chỉ cần đạt $%s$ điểm trong bài thi cuối kì thì điểm trung bình đã đạt từ $8,0$ trở lên.' % str(sai_x).replace('.', ',')
        loigiai_vdc_1 = '''Nhân hai vế của $3x \\ge %d$ với $\\dfrac{1}{3} > 0$ ta được $x \\ge \\dfrac{%d}{3} \\approx %s$. Nếu điểm lẻ đến $0,25$ thì An cần đạt ít nhất $%s$ điểm.''' % (can_3x, can_3x, str(min_x).replace('.', ','), str(diem_le).replace('.', ','))
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    
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
    
    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]
    
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
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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
