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


def bt_dang16_p2_b1_c3_ds9(self):
    # Khai báo biến
    ty_so = random.choice([30, 40, 50, 60])
    S_cao = round(4.9 * ty_so, 1)
    str_S_cao = str(S_cao).replace('.', ',')
    t_thu = random.choice([3, 4])
    S_thu = round(4.9 * (t_thu**2), 1)
    str_S_thu = str(S_thu).replace('.', ',')
    t_cham = math.sqrt(ty_so)
    t_tron1 = round(t_cham, 1)
    str_t_tron1 = f"{t_tron1:.1f}".replace('.', ',')
    str_t_sai = f"{round(t_tron1 + 0.1, 1):.1f}".replace('.', ',')

    # Nội dung câu hỏi
    noidungcauhoi = (f'''Trong Vật lí, quãng đường $S$ (tính bằng mét) của một vật rơi tự do được cho bởi công thức $S = 4,9t^2$, trong đó $t$ là thời gian rơi (tính bằng giây). Một viên bi được thả rơi tự do từ độ cao ${str_S_cao}\\text{{ m}}$ xuống mặt đất (bỏ qua sức cản không khí). Xét tính đúng, sai của các khẳng định sau:''')

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Thời gian $t$ (giây) để vật rơi được quãng đường $S$ (mét) tính theo công thức $t = \\sqrt{\\dfrac{S}{4,9}}$ (với $S \\ge 0$).'
    nb_da_1_s = 'Thời gian $t$ (giây) để vật rơi được quãng đường $S$ (mét) tính theo công thức $t = \\dfrac{\\sqrt{S}}{4,9}$ (với $S \\ge 0$).'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1_d = 'Từ $S = 4,9t^2$ suy ra $t^2 = \\dfrac{S}{4,9}$. Vì $t \\ge 0$ nên $t = \\sqrt{\\dfrac{S}{4,9}}$.'
    loigiai_nb_1_s = 'Sai. Từ $t^2 = \\dfrac{S}{4,9}$ ($t \\ge 0$) ta lấy căn bậc hai số học cả hai vế được $t = \\sqrt{\\dfrac{S}{4,9}}$.'

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = f'\\True Sau ${t_thu}\\text{{ giây}}$, viên bi rơi được quãng đường là ${str_S_thu}\\text{{ m}}$.'
    th_da_1_s = f'Sau ${t_thu}\\text{{ giây}}$, viên bi rơi được quãng đường là ${str(round(4.9 * t_thu, 1)).replace(".", ",")}\\text{{ m}}$.'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1_d = f'Thay $t = {t_thu}$ vào công thức ta được $S = 4,9 \\cdot {t_thu}^2 = {str_S_thu}\\text{{ m}}$.'
    loigiai_th_1_s = f'Sai. Quãng đường rơi sau ${t_thu}\\text{{ giây}}$ là $S = 4,9 \\cdot {t_thu}^2 = {str_S_thu}\\text{{ m}}$.'

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = f'\\True Thời gian để viên bi chạm đất từ độ cao ${str_S_cao}\\text{{ m}}$ là $\\sqrt{{{ty_so}}}\\text{{ giây}}$.'
    vd_da_1_s = f'Thời gian để viên bi chạm đất từ độ cao ${str_S_cao}\\text{{ m}}$ là ${ty_so}\\text{{ giây}}$.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1_d = f'Thay $S = {str_S_cao}$ vào công thức $t = \\sqrt{{\\dfrac{{S}}{{4,9}}}}$ ta được $t = \\sqrt{{\\dfrac{{{str_S_cao}}}{{4,9}}}} = \\sqrt{{{ty_so}}}\\text{{ giây}}$.'
    loigiai_vd_1_s = f'Sai. Thời gian chạm đất là $t = \\sqrt{{\\dfrac{{{str_S_cao}}}{{4,9}}}} = \\sqrt{{{ty_so}}}\\text{{ giây}}$.'

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = f'\\True Nếu làm tròn đến chữ số thập phân thứ nhất thì sau khoảng ${str_t_tron1}\\text{{ giây}}$ viên bi sẽ chạm đất.'
    vdc_da_1_s = f'Nếu làm tròn đến chữ số thập phân thứ nhất thì sau khoảng ${str_t_sai}\\text{{ giây}}$ viên bi sẽ chạm đất.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1_d = f'Sử dụng máy tính cầm tay ta có $\\sqrt{{{ty_so}}} \\approx {t_cham:.4f}\\dots \\approx {str_t_tron1}\\text{{ giây}}$.'
    loigiai_vdc_1_s = f'Sai. Ta có $\\sqrt{{{ty_so}}} \\approx {t_cham:.4f}\\dots$, làm tròn đến chữ số thập phân thứ nhất được ${str_t_tron1}\\text{{ giây}}$.'

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

    loigiai_nb_1 = loigiai_nb_1_d if '\\True' in nb_da_1 else loigiai_nb_1_s
    loigiai_th_1 = loigiai_th_1_d if '\\True' in th_da_1 else loigiai_th_1_s
    loigiai_vd_1 = loigiai_vd_1_d if '\\True' in vd_da_1 else loigiai_vd_1_s
    loigiai_vdc_1 = loigiai_vdc_1_d if '\\True' in vdc_da_1 else loigiai_vdc_1_s

    # Xuất câu hỏi
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
