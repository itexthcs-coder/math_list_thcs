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


def bt_dang6_p2_b2_c1_ds9(self):
    # Khai báo biến
    # Đường thẳng Delta1: x + b1*y = c1 đi qua C(0; yC) và D(xD; 0) với xD = b1*yC
    # Giao điểm M(xM; yM) với 0 < yM < yC và xM = c1 - b1*yM
    b1 = random.choice([2, 3])
    yC = random.choice([2, 3, 4])
    xD = b1 * yC
    c1 = xD
    
    yM = random.randint(1, yC - 1)
    xM = c1 - b1 * yM
    
    # Đường thẳng Delta2: a2*x - y = c2 đi qua M(xM; yM) và A(0; -c2)
    a2 = random.choice([2, 3])
    c2 = a2 * xM - yM
    yA = -c2
    
    pt1_str = latex(x + b1 * y) + '=' + latex(c1)
    pt2_str = latex(a2 * x - y) + '=' + latex(c2)
    
    # Diện tích tam giác MCD = S_OCD - S_OMD = 1/2 * xD * (yC - yM)
    dien_tich = Rational(1, 2) * xD * (yC - yM)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, xét hai đường thẳng $\\Delta_1: %s$ và $\\Delta_2: %s$. Xét tính đúng sai của các khẳng định sau:'''
                     % (pt1_str, pt2_str))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Đường thẳng $\\Delta_1$ cắt trục tung tại điểm $C(0; %s)$ và cắt trục hoành tại điểm $D(%s; 0)$' % (latex(yC), latex(xD))
    nb_da_1_s = 'Đường thẳng $\\Delta_1$ cắt trục tung tại điểm $C(0; %s)$ và cắt trục hoành tại điểm $D(%s; 0)$' % (latex(xD), latex(yC))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Cho $x = 0$ vào phương trình $\\Delta_1$ ta được $y = %s$, nên $\\Delta_1$ cắt trục tung tại $C(0; %s)$. Cho $y = 0$ ta được $x = %s$, nên $\\Delta_1$ cắt trục hoành tại $D(%s; 0)$.'''
                    % (latex(yC), latex(yC), latex(xD), latex(xD)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Đường thẳng $\\Delta_2$ đi qua điểm $A(0; %s)$ và điểm $B(1; %s)$' % (latex(yA), latex(a2 - c2))
    th_da_1_s = 'Đường thẳng $\\Delta_2$ đi qua điểm $A(0; %s)$ và điểm $B(1; %s)$' % (latex(yA), latex(a2 + c2))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Thay $x = 0$ vào phương trình $\\Delta_2$ ta được $y = %s$; thay $x = 1$ ta được $y = %s \\cdot 1 - (%s) = %s$. Vậy $\\Delta_2$ đi qua $A(0; %s)$ và $B(1; %s)$.'''
                    % (latex(yA), latex(a2), latex(c2), latex(a2 - c2), latex(yA), latex(a2 - c2)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Hai đường thẳng $\\Delta_1$ và $\\Delta_2$ cắt nhau tại điểm $M(%s; %s)$' % (latex(xM), latex(yM))
    vd_da_1_s = 'Hai đường thẳng $\\Delta_1$ và $\\Delta_2$ cắt nhau tại điểm $M(%s; %s)$' % (latex(yM), latex(xM))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Giải hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$, ta tìm được nghiệm duy nhất là $(%s; %s)$. Do đó $\\Delta_1$ và $\\Delta_2$ cắt nhau tại $M(%s; %s)$.'''
                    % (pt1_str, pt2_str, latex(xM), latex(yM), latex(xM), latex(yM)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Diện tích tam giác $MCD$ bằng $%s$ (đơn vị diện tích)' % (latex(dien_tich))
    vdc_da_1_s = 'Diện tích tam giác $MCD$ bằng $%s$ (đơn vị diện tích)' % (latex(dien_tich + 2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $M(%s; %s)$ nằm trên đoạn thẳng $CD$ nên diện tích tam giác $MCD$ bằng hiệu diện tích hai tam giác vuông $OCD$ và $OMD$: \\\\
                     $S_{\\Delta MCD} = S_{\\Delta OCD} - S_{\\Delta OMD} = \\frac{1}{2} \\cdot OD \\cdot y_C - \\frac{1}{2} \\cdot OD \\cdot y_M = \\frac{1}{2} \\cdot %s \\cdot (%s - %s) = %s$.'''
                     % (latex(xM), latex(yM), latex(xD), latex(yC), latex(yM), latex(dien_tich)))
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
