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


def bt_dang19_p2_b3_c1_ds9(self):
    def fmt_num(val):
        return f"{val:,}".replace(',', '\\,')
    
    # Random năng suất hai dây chuyền (hộp/giờ)
    x0 = random.choice([300, 350, 400])
    y0 = random.choice([450, 500, 550])
    while x0 == y0:
        y0 = random.choice([450, 500, 550])
    
    t1_1, t2_1 = 4, 3
    t1_2, t2_2 = 3, 5
    
    sp_1 = t1_1 * x0 + t2_1 * y0
    sp_2 = t1_2 * x0 + t2_2 * y0
    chenh_ns = y0 - x0
    tong_2h = 2 * (x0 + y0)
    
    noidungcauhoi = ('''Một xưởng sản xuất có hai dây chuyền đóng gói tự động. Trong một ca làm việc, dây chuyền I hoạt động trong $%s\\text{ giờ}$ và dây chuyền II hoạt động trong $%s\\text{ giờ}$ thì đóng gói được tất cả $%s\\text{ hộp}$ bánh. Trong một ca khác, dây chuyền I hoạt động trong $%s\\text{ giờ}$ và dây chuyền II hoạt động trong $%s\\text{ giờ}$ thì đóng gói được tất cả $%s\\text{ hộp}$ bánh. Gọi $x$ (hộp/giờ) và $y$ (hộp/giờ) lần lượt là năng suất đóng gói của dây chuyền I và dây chuyền II ($x, y \\in \\mathbb{N}^*$).''' % (t1_1, t2_1, fmt_num(sp_1), t1_2, t2_2, fmt_num(sp_2)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Hệ phương trình biểu diễn bài toán là $\\begin{cases} %sx + %sy = %s \\\\ %sx + %sy = %s \\end{cases}$' % (t1_1, t2_1, fmt_num(sp_1), t1_2, t2_2, fmt_num(sp_2))
    nb_da_1_s = 'Hệ phương trình biểu diễn bài toán là $\\begin{cases} %sx + %sy = %s \\\\ %sx + %sy = %s \\end{cases}$' % (t2_1, t1_1, fmt_num(sp_1), t2_2, t1_2, fmt_num(sp_2))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    
    loigiai_nb_1 = ('''Từ số sản phẩm đóng gói được trong hai ca làm việc, ta lập được hệ phương trình $\\begin{cases} %sx + %sy = %s \\\\ %sx + %sy = %s. \\end{cases}$''' % (t1_1, t2_1, fmt_num(sp_1), t1_2, t2_2, fmt_num(sp_2)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Năng suất của dây chuyền I là $%s\\text{ hộp/giờ}$ và dây chuyền II là $%s\\text{ hộp/giờ}$' % (x0, y0)
    th_da_1_s = 'Năng suất của dây chuyền I là $%s\\text{ hộp/giờ}$ và dây chuyền II là $%s\\text{ hộp/giờ}$' % (y0, x0)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    
    loigiai_th_1 = ('''Giải hệ phương trình trên bằng phương pháp cộng đại số, ta tìm được $x = %s$ và $y = %s$ (thỏa mãn điều kiện).''' % (x0, y0))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Mỗi giờ dây chuyền II đóng gói nhiều hơn dây chuyền I là $%s\\text{ hộp}$' % chenh_ns
    vd_da_1_s = 'Mỗi giờ dây chuyền II đóng gói nhiều hơn dây chuyền I là $%s\\text{ hộp}$' % (chenh_ns + 50)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    
    loigiai_vd_1 = ('''Mỗi giờ dây chuyền II đóng gói nhiều hơn dây chuyền I là $y - x = %s - %s = %s\\text{ (hộp)}$.''' % (y0, x0, chenh_ns))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Nếu cả hai dây chuyền cùng hoạt động liên tục trong $2\\text{ giờ}$ thì đóng gói được $%s\\text{ hộp}$ bánh' % fmt_num(tong_2h)
    vdc_da_1_s = 'Nếu cả hai dây chuyền cùng hoạt động liên tục trong $2\\text{ giờ}$ thì đóng gói được $%s\\text{ hộp}$ bánh' % fmt_num(tong_2h - 100)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    
    loigiai_vdc_1 = ('''Trong $2\\text{ giờ}$, cả hai dây chuyền đóng gói được $2(x + y) = 2(%s + %s) = %s\\text{ (hộp)}$.''' % (x0, y0, fmt_num(tong_2h)))
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
