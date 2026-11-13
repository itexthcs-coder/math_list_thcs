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


def bt_Dang16_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        P0 = random.choice([100, 144, 225, 400])
        R0 = random.choice([4, 9, 16])
        U0 = int(math.sqrt(P0 * R0))

        k_P = random.choice([8, 18, 32])
        k_R = 2
        tich_heso = k_P // k_R
        ti_so_U = int(math.sqrt(tich_heso))

        noidungcauhoi = ('''Công suất $P$ ($\text{W}$), hiệu điện thế $U$ ($\text{V}$), điện trở $R$ ($\Omega$) trong đoạn mạch một chiều liên hệ với nhau theo công thức $U = \sqrt{PR}$. Xét tính đúng sai của các mệnh đề sau:''')

        nb_da_1_d = '\\True Khi $P = %s\text{ W}$ và $R = %s\ \Omega$, hiệu điện thế trong mạch là $U = %s\text{ V}$' % (latex(P0), latex(R0), latex(U0))
        nb_da_1_s = 'Khi $P = %s\text{ W}$ và $R = %s\ \Omega$, hiệu điện thế trong mạch là $U = %s\text{ V}$' % (latex(P0), latex(R0), latex(U0 * 2))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Thay $P = %s$ và $R = %s$ vào công thức, ta được $U = \sqrt{%s \cdot %s} = \sqrt{%s} \cdot \sqrt{%s} = %s \cdot %s = %s\text{ (V)}$.'''
                        % (latex(P0), latex(R0), latex(P0), latex(R0), latex(P0), latex(R0), latex(int(math.sqrt(P0))), latex(int(math.sqrt(R0))), latex(U0)))

        th_da_1_d = '\\True Nếu giữ nguyên điện trở $R$ và tăng công suất $P$ lên $4$ lần thì hiệu điện thế $U$ tăng lên $2$ lần'
        th_da_1_s = 'Nếu giữ nguyên điện trở $R$ và tăng công suất $P$ lên $4$ lần thì hiệu điện thế $U$ tăng lên $4$ lần'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Khi $P' = 4P$ và $R' = R$, ta có $U' = \sqrt{4PR} = \sqrt{4} \cdot \sqrt{PR} = 2U$. Vậy hiệu điện thế tăng lên $2$ lần.''')

        vd_da_1_d = '\\True Nếu công suất $P$ tăng gấp $%s$ lần và điện trở $R$ giảm đi $%s$ lần thì tích $P\'R\'$ bằng $%sPR$' % (latex(k_P), latex(k_R), latex(tich_heso))
        vd_da_1_s = 'Nếu công suất $P$ tăng gấp $%s$ lần và điện trở $R$ giảm đi $%s$ lần thì tích $P\'R\'$ bằng $%sPR$' % (latex(k_P), latex(k_R), latex(k_P * k_R))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Ta có $P' = %sP$ và $R' = \dfrac{R}{%s}$, suy ra $P'R' = %sP \cdot \dfrac{R}{%s} = %sPR$.'''
                        % (latex(k_P), latex(k_R), latex(k_P), latex(k_R), latex(tich_heso)))

        vdc_da_1_d = '\\True Khi công suất tăng gấp $%s$ lần và điện trở giảm $%s$ lần, tỉ số giữa hiệu điện thế lúc đó và hiệu điện thế ban đầu bằng $%s$' % (latex(k_P), latex(k_R), latex(ti_so_U))
        vdc_da_1_s = 'Khi công suất tăng gấp $%s$ lần và điện trở giảm $%s$ lần, tỉ số giữa hiệu điện thế lúc đó và hiệu điện thế ban đầu bằng $%s$' % (latex(k_P), latex(k_R), latex(tich_heso))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Hiệu điện thế lúc đó là $U' = \sqrt{P'R'} = \sqrt{%sPR} = \sqrt{%s} \cdot \sqrt{PR} = %sU$. Vậy tỉ số $\dfrac{U'}{U} = %s$.'''
                         % (latex(tich_heso), latex(tich_heso), latex(ti_so_U), latex(ti_so_U)))

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

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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
