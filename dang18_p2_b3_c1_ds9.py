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


def bt_dang18_p2_b3_c1_ds9(self):
    # Random cánh tay đòn OA, OB và khối lượng vật x0, y0 sao cho x0 * OA = y0 * OB
    cases = [
        (40, 60, 2, 3, 9, 6),    # 2x = 3y; x=9, y=6
        (30, 60, 1, 2, 10, 5),   # x = 2y; x=10, y=5
        (40, 100, 2, 5, 15, 6),  # 2x = 5y; x=15, y=6
        (50, 75, 2, 3, 12, 8)    # 2x = 3y; x=12, y=8
    ]
    oa, ob, p, q, x0, y0 = random.choice(cases)
    tong_m = x0 + y0
    
    noidungcauhoi = ('''Một thanh cứng đồng chất $AB$ có trọng lượng không đáng kể, đặt trên điểm tựa $O$ sao cho $OA = %s\\text{ cm}$ và $OB = %s\\text{ cm}$. Khi treo hai vật có khối lượng lần lượt là $x\\text{ (kg)}$ tại $A$ và $y\\text{ (kg)}$ tại $B$ ($x > 0, y > 0$) thì thanh $AB$ nằm thăng bằng (biết điều kiện cân bằng là $x \\cdot OA = y \\cdot OB$). Biết tổng khối lượng của hai vật là $%s\\text{ kg}$.''' % (oa, ob, tong_m))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Tổng khối lượng hai vật cho ta phương trình $x + y = %s$' % tong_m
    nb_da_1_s = 'Tổng khối lượng hai vật cho ta phương trình $x - y = %s$' % tong_m
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    
    loigiai_nb_1 = ('''Tổng khối lượng hai vật treo ở hai đầu thanh là $%s\\text{ kg}$ nên $x + y = %s$.''' % (tong_m, tong_m))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Điều kiện cân bằng của đòn bẩy cho ta phương trình $%sx = %sy$ hay $%sx - %sy = 0$' % (oa, ob, p if p != 1 else '', q)
    th_da_1_s = 'Điều kiện cân bằng của đòn bẩy cho ta phương trình $%sx = %sy$ hay $%sx - %sy = 0$' % (ob, oa, q, p if p != 1 else '')
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    
    loigiai_th_1 = ('''Theo điều kiện cân bằng $x \\cdot OA = y \\cdot OB$, ta có $%sx = %sy \\Leftrightarrow %sx - %sy = 0$.''' % (oa, ob, p if p != 1 else '', q))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Khối lượng vật treo tại đầu $A$ là $%s\\text{ kg}$ và vật treo tại đầu $B$ là $%s\\text{ kg}$' % (x0, y0)
    vd_da_1_s = 'Khối lượng vật treo tại đầu $A$ là $%s\\text{ kg}$ và vật treo tại đầu $B$ là $%s\\text{ kg}$' % (y0, x0)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    
    loigiai_vd_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ %sx - %sy = 0 \\end{cases}$ ta được $x = %s\\text{ kg}$ và $y = %s\\text{ kg}$ (thỏa mãn).''' % (tong_m, p if p != 1 else '', q, x0, y0))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Nếu tăng khối lượng vật tại $B$ thêm $%s\\text{ kg}$ thì để thanh vẫn cân bằng, cần tăng khối lượng vật tại $A$ thêm $%s\\text{ kg}$' % (p, q)
    vdc_da_1_s = 'Nếu tăng khối lượng vật tại $B$ thêm $%s\\text{ kg}$ thì để thanh vẫn cân bằng, cần tăng khối lượng vật tại $A$ thêm $%s\\text{ kg}$' % (q, p)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    
    loigiai_vdc_1 = ('''Vì $%s \\cdot \\Delta x = %s \\cdot \\Delta y$, nên khi $\\Delta y = %s\\text{ kg}$ thì $\\Delta x = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ kg}$.''' % (p if p != 1 else '', q, p, q, p, p, q))
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
