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


def bt_dang8_p2_b3_c1_ds9(self):
    # Random diện tích và năng suất lúa
    S_moi = random.choice([50, 60, 70, 80])
    S_cu = random.choice([90, 100, 110, 120])
    S_tong = S_moi + S_cu
    
    x0 = random.choice([4, 5])       # năng suất lúa cũ (tấn/ha)
    y0 = x0 + random.choice([1, 2])  # năng suất lúa mới (tấn/ha)
    
    g_cu = random.randint(6, 9)
    g_moi = random.randint(6, 9)
    while g_moi * y0 <= g_cu * x0:
        g_moi += 1
    
    chenh = g_moi * y0 - g_cu * x0
    tong_thoc = S_cu * x0 + S_moi * y0
    
    noidungcauhoi = ('''Trên cánh đồng có diện tích $%s\\text{ ha}$ của một đơn vị sản xuất, người ta dành $%s\\text{ ha}$ để cấy thí điểm giống lúa mới, còn lại vẫn cấy giống lúa cũ. Khi thu hoạch, đầu tiên người ta gặt $%s\\text{ ha}$ giống lúa cũ và $%s\\text{ ha}$ giống lúa mới để đối chứng thì thấy $%s\\text{ ha}$ giống lúa mới cho thu hoạch nhiều hơn $%s\\text{ ha}$ giống lúa cũ là $%s\\text{ tấn}$ thóc. Biết tổng số thóc thu hoạch cả vụ trên $%s\\text{ ha}$ là $%s\\text{ tấn}$. Gọi $x$ (tấn/ha) là năng suất giống lúa cũ và $y$ (tấn/ha) là năng suất giống lúa mới ($x > 0, y > 0$).''' % (S_tong, S_moi, g_cu, g_moi, g_moi, g_cu, chenh, S_tong, tong_thoc))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Diện tích đất cấy giống lúa cũ trên cánh đồng là $%s\\text{ ha}$' % S_cu
    nb_da_1_s = 'Diện tích đất cấy giống lúa cũ trên cánh đồng là $%s\\text{ ha}$' % S_moi
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    
    loigiai_nb_1 = ('''Diện tích đất cấy giống lúa cũ là $%s - %s = %s\\text{ ha}$.''' % (S_tong, S_moi, S_cu))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Phương trình biểu diễn kết quả gặt đối chứng là $-%sx + %sy = %s$' % (g_cu, g_moi, chenh)
    th_da_1_s = 'Phương trình biểu diễn kết quả gặt đối chứng là $%sx - %sy = %s$' % (g_cu, g_moi, chenh)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    
    loigiai_th_1 = ('''Sản lượng của $%s\\text{ ha}$ lúa mới là $%sy$ (tấn), của $%s\\text{ ha}$ lúa cũ là $%sx$ (tấn). Vì lúa mới thu được nhiều hơn lúa cũ $%s\\text{ tấn}$ nên ta có $%sy - %sx = %s$ hay $-%sx + %sy = %s$.''' % (g_moi, g_moi, g_cu, g_cu, chenh, g_moi, g_cu, chenh, g_cu, g_moi, chenh))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Hệ phương trình biểu diễn bài toán là $\\begin{cases} -%sx + %sy = %s \\\\ %sx + %sy = %s \\end{cases}$' % (g_cu, g_moi, chenh, S_cu, S_moi, tong_thoc)
    vd_da_1_s = 'Hệ phương trình biểu diễn bài toán là $\\begin{cases} -%sx + %sy = %s \\\\ %sx + %sy = %s \\end{cases}$' % (g_cu, g_moi, chenh, S_moi, S_cu, tong_thoc)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    
    loigiai_vd_1 = ('''Tổng sản lượng cả cánh đồng cho ta phương trình $%sx + %sy = %s$. Kết hợp với kết quả đối chứng, ta có hệ $\\begin{cases} -%sx + %sy = %s \\\\ %sx + %sy = %s. \\end{cases}$''' % (S_cu, S_moi, tong_thoc, g_cu, g_moi, chenh, S_cu, S_moi, tong_thoc))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Năng suất giống lúa cũ là $%s\\text{ tấn/ha}$ và năng suất giống lúa mới là $%s\\text{ tấn/ha}$' % (x0, y0)
    vdc_da_1_s = 'Năng suất giống lúa cũ là $%s\\text{ tấn/ha}$ và năng suất giống lúa mới là $%s\\text{ tấn/ha}$' % (y0, x0)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    
    loigiai_vdc_1 = ('''Giải hệ phương trình trên, ta được $x = %s$ và $y = %s$ (thỏa mãn). Vậy năng suất giống lúa cũ là $%s\\text{ tấn/ha}$ và giống lúa mới là $%s\\text{ tấn/ha}$.''' % (x0, y0, x0, y0))
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
