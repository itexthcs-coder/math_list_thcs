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


def bt_dang12_p2_b1_c2_ds9(self):
    # Khai báo biến
    x = symbols('x')
    
    x_ans = random.choice([2, 3, 4])
    canh_nha = random.choice([10, 12, 14])
    rong = canh_nha + x_ans
    dai = rong + 2
    dt_nha = canh_nha**2
    dt_tong = dai * rong
    dt_vuon = dt_tong - dt_nha
    x_loai = rong + canh_nha
    
    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (4.2,0);
    \\coordinate (C) at (4.2,3.4);
    \\coordinate (D) at (0,3.4);
    \\coordinate (E) at (3.0,0);
    \\coordinate (F) at (3.0,2.7);
    \\coordinate (G) at (0,2.7);
    \\coordinate (P1) at (-0.3,2.7);
    \\coordinate (P2) at (-0.3,3.4);
    \\coordinate (Q1) at (3.0,-0.3);
    \\coordinate (Q2) at (4.2,-0.3);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\draw[line width=1pt] (E)--(F)--(G);
    \\draw[line width=1pt, <->] (P1)--(P2);
    \\draw[line width=1pt, <->] (Q1)--(Q2);
    \\fill (A) circle (1pt);
    \\fill (B) circle (1pt);
    \\fill (C) circle (1pt);
    \\fill (D) circle (1pt);
    \\fill (E) circle (1pt);
    \\fill (F) circle (1pt);
    \\fill (G) circle (1pt);
    \\node[above] at (2.1,3.4) {$%s$};
    \\node[right] at (4.2,1.7) {$%s$};
    \\node[left] at (-0.3,3.05) {$x$};
    \\node[below] at (3.6,-0.3) {$x + 2$};
    \\node at (1.5,1.35) {Nhà};
    \\node at (2.5,3.05) {Sân vườn};
    \\end{tikzpicture}
    \\end{center}''' % (latex(dai), latex(rong)))
    
    noidungcauhoi = ('''Bác An có một mảnh đất hình chữ nhật với chiều dài $%s\\text{ m}$ và chiều rộng $%s\\text{ m}$. Bác dự định xây nhà trên mảnh đất đó và dành một phần diện tích đất để làm sân vườn như hình vẽ (với $0 < x < %s$). Biết diện tích đất làm nhà là $%s\\text{ m}^2$. %s''' % (latex(dai), latex(rong), latex(rong), latex(dt_nha), hinh_ve))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Chiều dài và chiều rộng của phần đất làm nhà lần lượt là $%s - (x + 2)$ và $%s - x$ (mét)' % (latex(dai), latex(rong))
    nb_da_1_s = 'Chiều dài và chiều rộng của phần đất làm nhà lần lượt là $%s - x$ và $%s - (x + 2)$ (mét)' % (latex(dai), latex(rong))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = ('''Quan sát hình vẽ, chiều dài phần đất làm nhà là $%s - (x + 2)$ (mét) và chiều rộng là $%s - x$ (mét).''' % (latex(dai), latex(rong)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Phần đất dùng để làm nhà có dạng hình vuông cạnh $(%s - x)\\text{ m}$' % (latex(rong))
    th_da_1_s = 'Phần đất dùng để làm nhà có dạng hình chữ nhật với chiều dài lớn hơn chiều rộng $2\\text{ m}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Ta có $%s - (x + 2) = %s - x$, nên chiều dài và chiều rộng phần đất làm nhà bằng nhau và bằng $(%s - x)\\text{ m}$, tức là phần đất làm nhà có dạng hình vuông.''' % (latex(dai), latex(rong), latex(rong)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Giá trị của $x$ tìm được bằng $%s\\text{ m}$' % (latex(x_ans))
    vd_da_1_s = 'Phương trình tính $x$ giải ra được hai giá trị là $x = %s$ và $x = %s$, cả hai đều thoả mãn bài toán' % (latex(x_ans), latex(x_loai))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Ta có $(%s - x)^2 = %s$, biến đổi thành $(%s - x)(%s - x) = 0$. Giải ra được $x = %s$ (thoả mãn) hoặc $x = %s$ (loại vì $x < %s$). Vậy $x = %s\\text{ m}$.''' % (latex(rong), latex(dt_nha), latex(rong - canh_nha), latex(rong + canh_nha), latex(x_ans), latex(x_loai), latex(rong), latex(x_ans)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Diện tích phần đất bác An dành để làm sân vườn là $%s\\text{ m}^2$' % (latex(dt_vuon))
    vdc_da_1_s = 'Diện tích phần đất bác An dành để làm sân vườn là $%s\\text{ m}^2$' % (latex(dt_tong))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Diện tích cả mảnh đất là $%s \\cdot %s = %s\\text{ (m}^2)$. Diện tích phần đất làm sân vườn là $%s - %s = %s\\text{ (m}^2)$.''' % (latex(dai), latex(rong), latex(dt_tong), latex(dt_tong), latex(dt_nha), latex(dt_vuon)))
    list_vdc_2 = [loigiai_vdc_1]
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
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
    
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
    '\\choiceTFn \n'
    '{'+str(shuffled_answers_nb[0])+'}\n'
    '{'+str(shuffled_answers_th[0])+'}\n'
    '{'+str(shuffled_answers_vd[0])+'}\n'
    '{'+str(shuffled_answers_vdc[0])+'}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item '+str(shuffled_solutions_nb[0])+'\n'
    '\\item '+str(shuffled_solutions_th[0])+'\n'
    '\\item '+str(shuffled_solutions_vd[0])+'\n'
    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    return content
