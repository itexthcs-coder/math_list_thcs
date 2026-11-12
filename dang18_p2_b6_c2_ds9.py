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


def bt_dang18_p2_b6_c2_ds9(self):
    # Khai báo biến: Lương cứng L triệu, hoa hồng p%, mục tiêu thu nhập M triệu
    L = random.choice([6, 7, 8])
    p = random.choice([4, 5])
    p_dec = round(p / 100, 2)
    dt_min = random.choice([200, 250, 300])
    M = int(L + p_dec * dt_min)
    dt_thieu = dt_min - 30
    thu_nhap_thieu = round(L + p_dec * dt_thieu, 1)
    
    noidungcauhoi = ('''Một nhân viên kinh doanh được hưởng mức lương cơ bản là $%s$ triệu đồng/tháng và nhận thêm tiền hoa hồng bằng $%s\\%%$ tổng doanh thu bán hàng trong tháng đó. Gọi $x$ (triệu đồng, $x \\ge 0$) là doanh thu bán hàng của nhân viên trong một tháng.'''
                     % (L, p))
    
    # Mệnh đề a
    nb_da_1_d = '\\True Tổng thu nhập hằng tháng của nhân viên đó được biểu diễn bởi biểu thức $%s + %sx$ (triệu đồng).' % (L, str(p_dec).replace('.', ','))
    nb_da_1_s = 'Tổng thu nhập hằng tháng của nhân viên đó được biểu diễn bởi biểu thức $%s + %sx$ (triệu đồng).' % (L, p)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tiền hoa hồng bằng $%s\\%% \\cdot x = %sx$ (triệu đồng), cộng thêm lương cơ bản $%s$ triệu đồng nên tổng thu nhập là $%s + %sx$ (triệu đồng).'''
                    % (p, str(p_dec).replace('.', ','), L, L, str(p_dec).replace('.', ',')))
    
    # Mệnh đề b
    th_da_1_d = '\\True Để tổng thu nhập trong tháng đạt ít nhất $%s$ triệu đồng, bất phương trình cần lập là $%s + %sx \\ge %s$.' % (M, L, str(p_dec).replace('.', ','), M)
    th_da_1_s = 'Để tổng thu nhập trong tháng đạt ít nhất $%s$ triệu đồng, bất phương trình cần lập là $%s + %sx \\le %s$.' % (M, L, str(p_dec).replace('.', ','), M)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Thu nhập ít nhất là $%s$ triệu đồng nghĩa là tổng thu nhập $\\ge %s$, do đó $%s + %sx \\ge %s$.'''
                    % (M, M, L, str(p_dec).replace('.', ','), M))
    
    # Mệnh đề c
    vd_da_1_d = '\\True Nhân viên đó cần đạt doanh thu tối thiểu là $%s$ triệu đồng để nhận được mức thu nhập như mong muốn.' % dt_min
    vd_da_1_s = 'Nhân viên đó cần đạt doanh thu tối thiểu là $%s$ triệu đồng để nhận được mức thu nhập như mong muốn.' % (dt_min + 50)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $%s + %sx \\ge %s \\Leftrightarrow %sx \\ge %s \\Leftrightarrow x \\ge %s$. Vậy doanh thu tối thiểu là $%s$ triệu đồng.'''
                    % (L, str(p_dec).replace('.', ','), M, str(p_dec).replace('.', ','), M - L, dt_min, dt_min))
    
    # Mệnh đề d
    vdc_da_1_d = '\\True Nếu trong tháng nhân viên bán được $%s$ triệu đồng tiền hàng thì tổng thu nhập chưa đạt mức $%s$ triệu đồng.' % (dt_thieu, M)
    vdc_da_1_s = 'Nếu trong tháng nhân viên bán được $%s$ triệu đồng tiền hàng thì tổng thu nhập sẽ vượt mức $%s$ triệu đồng.' % (dt_thieu, M)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Với $x = %s$ triệu đồng, tổng thu nhập là $%s + %s \\cdot %s = %s < %s$ (triệu đồng), chưa đạt mức mong muốn.'''
                     % (dt_thieu, L, str(p_dec).replace('.', ','), dt_thieu, str(thu_nhap_thieu).replace('.', ','), M))
    
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
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
