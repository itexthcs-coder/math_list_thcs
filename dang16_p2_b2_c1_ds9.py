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


def bt_dang16_p2_b2_c1_ds9(self):
    # Khai báo biến
    # Đội A làm gấp rưỡi (3/2) đội B => x = 3/2 y => x + y = 5/2 y = 1/T_chung
    # Chọn T_chung chia hết cho 2: T_chung in [12, 18, 24]
    T_chung = random.choice([12, 18, 24])
    T_A = (5 * T_chung) // 3
    T_B = (5 * T_chung) // 2
    
    x0 = Rational(1, T_A)
    y0 = Rational(1, T_B)
    ns_chung = Rational(1, T_chung)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Hai đội công nhân cùng làm một đoạn đường trong $%s\\text{ ngày}$ thì xong. Mỗi ngày, phần việc đội $A$ làm được nhiều gấp rưỡi (tức bằng $\\frac{3}{2}$) phần việc của đội $B$. Gọi $x$ (công việc/ngày) là năng suất làm việc một ngày của đội $A$ và $y$ (công việc/ngày) là năng suất làm việc một ngày của đội $B$ ($x, y > 0$). Xét tính đúng sai của các khẳng định sau:'''
                     % (latex(T_chung)))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Trong $1\\text{ ngày}$, cả hai đội làm chung được $%s$ công việc, nên ta có phương trình $x + y = %s$' % (latex(ns_chung), latex(ns_chung))
    nb_da_1_s = 'Trong $1\\text{ ngày}$, cả hai đội làm chung được $%s$ công việc, nên ta có phương trình $x + y = %s$' % (latex(T_chung), latex(T_chung))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì hai đội làm chung trong $%s\\text{ ngày}$ thì xong toàn bộ công việc (quy ước là $1$) nên mỗi ngày hai đội làm chung được $%s$ công việc. Ta có phương trình $x + y = %s$.'''
                    % (latex(T_chung), latex(ns_chung), latex(ns_chung)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Vì năng suất đội $A$ gấp rưỡi đội $B$ nên ta có phương trình $2x - 3y = 0$'
    th_da_1_s = 'Vì năng suất đội $A$ gấp rưỡi đội $B$ nên ta có phương trình $3x - 2y = 0$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Mỗi ngày đội $A$ làm được bằng $\\frac{3}{2}$ phần việc của đội $B$ nên $x = \\frac{3}{2}y \\Leftrightarrow 2x - 3y = 0$.''')
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Năng suất làm việc mỗi ngày của đội $B$ là $y = %s$ công việc' % (latex(y0))
    vd_da_1_s = 'Năng suất làm việc mỗi ngày của đội $B$ là $y = %s$ công việc' % (latex(x0))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Giải hệ phương trình $\\begin{cases} x + y = %s \\\\ 2x - 3y = 0 \\end{cases}$, ta tìm được $x = %s$ và $y = %s$.'''
                    % (latex(ns_chung), latex(x0), latex(y0)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Nếu làm một mình thì đội $A$ hoàn thành toàn bộ đoạn đường đó trong $%s\\text{ ngày}$' % (latex(T_A))
    vdc_da_1_s = 'Nếu làm một mình thì đội $A$ hoàn thành toàn bộ đoạn đường đó trong $%s\\text{ ngày}$' % (latex(T_B))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì mỗi ngày đội $A$ làm được $x = %s$ công việc nên nếu làm một mình, đội $A$ hoàn thành toàn bộ công việc trong $1 : %s = %s\\text{ (ngày)}$.'''
                     % (latex(x0), latex(x0), latex(T_A)))
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
