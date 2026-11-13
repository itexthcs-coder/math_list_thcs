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


def bt_dang18_p2_b1_c3_ds9(self):
    # Khai báo biến
    S = random.choice([2, 3, 4, 5])
    pi_val = 3.1416
    R_val = math.sqrt(S / pi_val)
    d_val = 2 * R_val
    R_tron = round(R_val, 2)
    d_tron = round(d_val, 2)
    str_R = f"{R_tron:.2f}".replace('.', ',')
    str_R_sai = f"{round(R_tron + 0.03, 2):.2f}".replace('.', ',')
    str_d = f"{d_tron:.2f}".replace('.', ',')
    str_d_sai = f"{round(d_tron + 0.04, 2):.2f}".replace('.', ',')

    # Nội dung câu hỏi
    noidungcauhoi = (f"Để trang trí khuôn viên trường học, nhà trường xây dựng một bồn hoa hình tròn có diện tích $S = {S}\\text{{ m}}^2$ (lấy $\\pi \\approx 3,1416$). Xét tính đúng, sai của các khẳng định sau:")

    # ######################################################################## Nhận biết ############################################
    nb_da_1_d = r'\True Bán kính $R$ của bồn hoa được tính theo công thức $R = \sqrt{\dfrac{S}{\pi}}.$'
    nb_da_1_s = 'Bán kính $R$ của bồn hoa được tính theo công thức $R = \dfrac{S}{\sqrt{\pi}}.$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1_d = 'Từ công thức diện tích hình tròn $S = \pi R^2$ ($R > 0$) suy ra $R^2 = \dfrac{S}{\pi} \Rightarrow R = \sqrt{\dfrac{S}{\pi}}.$'
    loigiai_nb_1_s = 'Sai. Từ $S = \pi R^2$ ($R > 0$) ta suy ra $R = \sqrt{\dfrac{S}{\pi}}.$'

    # ######################################################################## Thông hiểu ############################################
    th_da_1_d = r'\True Đường kính $d$ của bồn hoa được biểu diễn bởi công thức $d = 2\sqrt{\dfrac{S}{\pi}}.$'
    th_da_1_s = 'Đường kính $d$ của bồn hoa được biểu diễn bởi công thức $d = \sqrt{\dfrac{2S}{\pi}}.$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1_d = 'Vì đường kính gấp đôi bán kính nên $d = 2R = 2\sqrt{\dfrac{S}{\pi}}.$'
    loigiai_th_1_s = 'Sai. Đường kính là $d = 2R = 2\sqrt{\dfrac{S}{\pi}}$ (hệ số $2$ nằm ngoài dấu căn).'

    # ######################################################################## Vận dụng ############################################
    vd_da_1_d = f'\\True Bán kính của bồn hoa (làm tròn đến chữ số thập phân thứ hai) là ${str_R}\\text{{ m}}$.'
    vd_da_1_s = f'Bán kính của bồn hoa (làm tròn đến chữ số thập phân thứ hai) là ${str_R_sai}\\text{{ m}}$.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1_d = f'Ta có $R = \\sqrt{{\\dfrac{{{S}}}{{3,1416}}}} \\approx {R_val:.4f}\\dots \\approx {str_R}\\text{{ m}}$.'
    loigiai_vd_1_s = f'Sai. Ta có $R = \\sqrt{{\\dfrac{{{S}}}{{3,1416}}}} \\approx {R_val:.4f}\\dots \\approx {str_R}\\text{{ m}}$.'

    # ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = f'\\True Với độ chính xác $0,005$, đường kính của bồn hoa ước lượng khoảng ${str_d}\\text{{ m}}$.'
    vdc_da_1_s = f'Với độ chính xác $0,005$, đường kính của bồn hoa ước lượng khoảng ${str_d_sai}\\text{{ m}}$.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1_d = f'Làm tròn với độ chính xác $0,005$ là làm tròn đến hàng phần trăm: $d = 2\\sqrt{{\\dfrac{{{S}}}{{3,1416}}}} \\approx {d_val:.4f}\\dots \\approx {str_d}\\text{{ m}}$.'
    loigiai_vdc_1_s = f'Sai. Ta có $d = 2\\sqrt{{\\dfrac{{{S}}}{{3,1416}}}} \\approx {d_val:.4f}\\dots$, làm tròn với độ chính xác $0,005$ được ${str_d}\\text{{ m}}$.'

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
