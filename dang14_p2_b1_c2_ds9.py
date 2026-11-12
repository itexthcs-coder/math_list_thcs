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


def bt_dang14_p2_b1_c2_ds9(self):
    # Khai báo biến
    x = symbols('x')
    
    bo_so = random.choice([
        (36, 3, 15, Rational(9, 2), "4,5"),
        (48, 4, 20, 5, "5"),
        (60, 5, 25, 5, "5"),
        (30, 3, 12, Rational(16, 3), "\\dfrac{16}{3}")
    ])
    quang_duong, v_nuoc, v_cano, t_tong, t_tong_str = bo_so
    
    noidungcauhoi = ('''Một ca nô xuôi dòng từ bến $A$ đến bến $B$ cách nhau $%s\\text{ km}$, sau đó ngay lập tức quay ngược dòng từ $B$ về $A$. Biết vận tốc của dòng nước là $%s\\text{ km/h}$ và tổng thời gian cả đi lẫn về của ca nô là $%s\\text{ giờ}$. Gọi $x\\text{ (km/h)}$ là vận tốc riêng của ca nô khi nước yên lặng ($x > %s$).''' % (latex(quang_duong), latex(v_nuoc), t_tong_str, latex(v_nuoc)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Vận tốc của ca nô khi xuôi dòng là $(x + %s)\\text{ km/h}$ và khi ngược dòng là $(x - %s)\\text{ km/h}$' % (latex(v_nuoc), latex(v_nuoc))
    nb_da_1_s = 'Vận tốc của ca nô khi xuôi dòng là $(x - %s)\\text{ km/h}$ và khi ngược dòng là $(x + %s)\\text{ km/h}$' % (latex(v_nuoc), latex(v_nuoc))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = ('''Khi xuôi dòng, vận tốc ca nô cộng thêm vận tốc dòng nước nên bằng $(x + %s)\\text{ km/h}$; khi ngược dòng bị cản bởi dòng nước nên bằng $(x - %s)\\text{ km/h}$.''' % (latex(v_nuoc), latex(v_nuoc)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Thời gian ca nô đi xuôi dòng ít hơn thời gian ca nô đi ngược dòng'
    th_da_1_s = 'Thời gian ca nô đi xuôi dòng nhiều hơn thời gian ca nô đi ngược dòng'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Trên cùng quãng đường $%s\\text{ km}$, vận tốc xuôi dòng lớn hơn vận tốc ngược dòng nên thời gian đi xuôi dòng $\\dfrac{%s}{x + %s}$ ít hơn thời gian đi ngược dòng $\\dfrac{%s}{x - %s}$.''' % (latex(quang_duong), latex(quang_duong), latex(v_nuoc), latex(quang_duong), latex(v_nuoc)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Phương trình lập được của bài toán là $\\dfrac{%s}{x + %s} + \\dfrac{%s}{x - %s} = %s$' % (latex(quang_duong), latex(v_nuoc), latex(quang_duong), latex(v_nuoc), t_tong_str)
    vd_da_1_s = 'Phương trình lập được của bài toán là $\\dfrac{%s}{x + %s} - \\dfrac{%s}{x - %s} = %s$' % (latex(quang_duong), latex(v_nuoc), latex(quang_duong), latex(v_nuoc), t_tong_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Tổng thời gian cả đi lẫn về là $%s\\text{ giờ}$ nên ta có phương trình $\\dfrac{%s}{x + %s} + \\dfrac{%s}{x - %s} = %s$.''' % (t_tong_str, latex(quang_duong), latex(v_nuoc), latex(quang_duong), latex(v_nuoc), t_tong_str))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Vận tốc riêng của ca nô là $%s\\text{ km/h}$' % (latex(v_cano))
    vdc_da_1_s = 'Vận tốc riêng của ca nô là $%s\\text{ km/h}$' % (latex(v_cano + 3))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Quy đồng và khử mẫu phương trình trên, đưa về phương trình tích tìm được nghiệm dương $x = %s$ (thoả mãn $x > %s$). Vậy vận tốc riêng của ca nô là $%s\\text{ km/h}$.''' % (latex(v_cano), latex(v_nuoc), latex(v_cano)))
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
