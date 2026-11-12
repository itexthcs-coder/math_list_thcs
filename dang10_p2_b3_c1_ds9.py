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


def bt_dang10_p2_b3_c1_ds9(self):
    def fmt_dec(val):
        if val == int(val):
            return str(int(val))
        return str(round(val, 2)).replace('.', '{,}')
    
    # Random giá gốc hai loại hàng (triệu đồng)
    x0 = random.choice([5, 10, 15])
    y0 = random.choice([i for i in [5, 10, 15, 20] if i != x0])
    tong_goc = x0 + y0
    
    # Thuế VAT 10%, 8% và đồng mức 9%
    tong_1 = round(1.1 * x0 + 1.08 * y0, 2)
    tong_2 = round(1.09 * tong_goc, 2)
    
    noidungcauhoi = ('''Một người mua hai loại hàng và phải trả tổng cộng là $%s\\text{ triệu đồng}$, kể cả thuế giá trị gia tăng (VAT) với mức $10\\%%$ đối với loại hàng thứ nhất và $8\\%%$ đối với loại hàng thứ hai. Nếu thuế VAT là $9\\%%$ đối với cả hai loại hàng thì người đó phải trả tổng cộng $%s\\text{ triệu đồng}$. Gọi $x$ (triệu đồng) và $y$ (triệu đồng) lần lượt là giá tiền của loại hàng thứ nhất và loại hàng thứ hai chưa kể thuế VAT ($x > 0, y > 0$).''' % (fmt_dec(tong_1), fmt_dec(tong_2)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Số tiền phải trả cho loại hàng thứ nhất khi chịu thuế VAT $10\\%%$ là $1{,}1x$ (triệu đồng)'
    nb_da_1_s = 'Số tiền phải trả cho loại hàng thứ nhất khi chịu thuế VAT $10\\%%$ là $0{,}1x$ (triệu đồng)'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    
    loigiai_nb_1 = ('''Giá chưa thuế là $x$ (triệu đồng), cộng thêm $10\\%%$ thuế VAT thì số tiền phải trả cho loại hàng thứ nhất là $x + 0{,}1x = 1{,}1x$ (triệu đồng).''')
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Nếu thuế VAT là $9\\%%$ cho cả hai loại hàng thì ta có phương trình $1{,}09(x + y) = %s$, suy ra $x + y = %s$' % (fmt_dec(tong_2), tong_goc)
    th_da_1_s = 'Nếu thuế VAT là $9\\%%$ cho cả hai loại hàng thì ta có phương trình $1{,}9(x + y) = %s$' % fmt_dec(tong_2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    
    loigiai_th_1 = ('''Thuế VAT $9\\%%$ cho cả hai loại hàng nên tổng tiền phải trả là $1{,}09(x + y) = %s \\Leftrightarrow x + y = %s$.''' % (fmt_dec(tong_2), tong_goc))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Hệ phương trình lập được từ bài toán là $\\begin{cases} 1{,}1x + 1{,}08y = %s \\\\ x + y = %s \\end{cases}$' % (fmt_dec(tong_1), tong_goc)
    vd_da_1_s = 'Hệ phương trình lập được từ bài toán là $\\begin{cases} 1{,}08x + 1{,}1y = %s \\\\ x + y = %s \\end{cases}$' % (fmt_dec(tong_1), tong_goc)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    
    loigiai_vd_1 = ('''Số tiền phải trả ở trường hợp đầu là $1{,}1x + 1{,}08y = %s$. Kết hợp với $x + y = %s$, ta được hệ phương trình $\\begin{cases} 1{,}1x + 1{,}08y = %s \\\\ x + y = %s. \\end{cases}$''' % (fmt_dec(tong_1), tong_goc, fmt_dec(tong_1), tong_goc))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Nếu không kể thuế VAT thì giá của loại hàng thứ nhất là $%s\\text{ triệu đồng}$ và loại hàng thứ hai là $%s\\text{ triệu đồng}$' % (x0, y0)
    vdc_da_1_s = 'Nếu không kể thuế VAT thì giá của loại hàng thứ nhất là $%s\\text{ triệu đồng}$ và loại hàng thứ hai là $%s\\text{ triệu đồng}$' % (y0, x0)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    
    loigiai_vdc_1 = ('''Giải hệ phương trình trên, ta tìm được $x = %s$ và $y = %s$ (thỏa mãn điều kiện). Vậy giá chưa kể thuế VAT của loại hàng thứ nhất là $%s\\text{ triệu đồng}$ và loại hàng thứ hai là $%s\\text{ triệu đồng}$.''' % (x0, y0, x0, y0))
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
