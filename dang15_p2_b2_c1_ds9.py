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


def bt_dang15_p2_b2_c1_ds9(self):
    # Khai báo biến
    # Chọn bộ (S, x0, y0) để t_xuoi và t_nguoc đẹp
    bo_so = random.choice([
        (80, 20, 4),   # v_xuoi = 24, v_nguoc = 16 => t1 = 10/3, t2 = 5 => tong = 25/3, hieu = 5/3
        (60, 18, 2),   # v_xuoi = 20, v_nguoc = 16 => t1 = 3, t2 = 15/4 => tong = 27/4, hieu = 3/4
        (120, 25, 5)   # v_xuoi = 30, v_nguoc = 20 => t1 = 4, t2 = 6 => tong = 10, hieu = 2
    ])
    S_km, x0, y0 = bo_so
    v_xuoi = x0 + y0
    v_nguoc = x0 - y0
    t1 = Rational(S_km, v_xuoi)
    t2 = Rational(S_km, v_nguoc)
    tong_t = t1 + t2
    hieu_t = t2 - t1
    hieu_v = 2 * y0
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một chiếc tàu thủy chạy trên một khúc sông dài $%s\\text{ km}$. Cả đi và về mất $%s\\text{ giờ}$. Biết vận tốc của tàu thủy khi nước yên lặng là $x\\text{ (km/h)}$ và vận tốc dòng nước là $y\\text{ (km/h)}$ ($x > y > 0$), đồng thời vận tốc khi xuôi dòng lớn hơn vận tốc khi ngược dòng là $%s\\text{ km/h}$, và thời gian xuôi dòng ít hơn thời gian ngược dòng là $%s\\text{ giờ}$. Xét tính đúng sai của các khẳng định sau:'''
                     % (latex(S_km), latex(tong_t), latex(hieu_v), latex(hieu_t)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Vận tốc của tàu khi xuôi dòng là $x + y\\text{ (km/h)}$ và khi ngược dòng là $x - y\\text{ (km/h)}$'
    nb_da_1_s = 'Vận tốc của tàu khi xuôi dòng là $x - y\\text{ (km/h)}$ và khi ngược dòng là $x + y\\text{ (km/h)}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Khi xuôi dòng tàu được dòng nước đẩy thêm nên vận tốc là $x + y\\text{ (km/h)}$; khi ngược dòng tàu bị dòng nước cản lại nên vận tốc là $x - y\\text{ (km/h)}$.''')
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Từ giả thiết về hiệu vận tốc xuôi dòng và ngược dòng, ta có phương trình $2y = %s$, suy ra $y = %s\\text{ (km/h)}$' % (latex(hieu_v), latex(y0))
    th_da_1_s = 'Từ giả thiết về hiệu vận tốc xuôi dòng và ngược dòng, ta có phương trình $2x = %s$, suy ra $x = %s\\text{ (km/h)}$' % (latex(hieu_v), latex(y0))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $(x + y) - (x - y) = %s \\Leftrightarrow 2y = %s \\Leftrightarrow y = %s\\text{ (km/h)}$.'''
                    % (latex(hieu_v), latex(hieu_v), latex(y0)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Thời gian tàu chạy xuôi dòng hết khúc sông là $%s\\text{ giờ}$' % (latex(t1))
    vd_da_1_s = 'Thời gian tàu chạy xuôi dòng hết khúc sông là $%s\\text{ giờ}$' % (latex(t2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Gọi $t_1, t_2$ lần lượt là thời gian xuôi dòng và ngược dòng. Ta có hệ $\\begin{cases} t_1 + t_2 = %s \\\\ t_2 - t_1 = %s \\end{cases}$, giải ra được $t_1 = %s\\text{ giờ}$ và $t_2 = %s\\text{ giờ}$.'''
                    % (latex(tong_t), latex(hieu_t), latex(t1), latex(t2)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Vận tốc của tàu thủy khi nước yên lặng là $x = %s\\text{ km/h}$' % (latex(x0))
    vdc_da_1_s = 'Vận tốc của tàu thủy khi nước yên lặng là $x = %s\\text{ km/h}$' % (latex(v_xuoi))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vận tốc tàu khi xuôi dòng là $x + y = %s : %s = %s\\text{ (km/h)}$. Thay $y = %s$ vào ta được $x = %s - %s = %s\\text{ (km/h)}$.'''
                     % (latex(S_km), latex(t1), latex(v_xuoi), latex(y0), latex(v_xuoi), latex(y0), latex(x0)))
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
    
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\n' '\\choiceTFn \n' '{' + str(shuffled_answers_nb[0]) + '}\n' '{' + str(shuffled_answers_th[0]) + '}\n' '{' + str(shuffled_answers_vd[0]) + '}\n' '{' + str(shuffled_answers_vdc[0]) + '}\n' '\\loigiai{ \n' '\\begin{enumEX}[a)]{1} \n' '\\item ' + str(shuffled_solutions_nb[0]) + '\n' '\\item ' + str(shuffled_solutions_th[0]) + '\n' '\\item ' + str(shuffled_solutions_vd[0]) + '\n' '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' '\\end{enumEX}} \n' '\\end{ex}\n \\end{minipage}\n\n')

    return content
