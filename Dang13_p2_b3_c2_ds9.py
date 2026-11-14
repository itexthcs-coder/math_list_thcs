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


def bt_Dang13_p2_b3_c2_ds9(self):
    mo_cua = random.choice([12, 14, 15, 16])
    gia_km = random.choice([11, 12, 13, 14])
    tong_tien = random.choice([200, 220, 250, 300])
    while (tong_tien - mo_cua) % gia_km == 0:
        tong_tien += 10

    x_max_thuc = (tong_tien - mo_cua) / gia_km + 1
    x_lam_tron = round(x_max_thuc, 2)
    km_max = math.floor(x_max_thuc)

    noidungcauhoi = ('''Một hãng taxi quy định giá mở cửa là $%s$ nghìn đồng cho kilômét đầu tiên và giá cước cho mỗi kilômét tiếp theo là $%s$ nghìn đồng. Anh Minh có $%s$ nghìn đồng để đi taxi của hãng này. Gọi $x$ (km) là quãng đường anh Minh di chuyển ($x > 1$). Xét tính đúng sai của các khẳng định sau:''' % (mo_cua, gia_km, tong_tien))

    nb_da_1_d = '\\True Số tiền cước anh Minh phải trả cho quãng đường $x$ (km) là $%s + %s(x - 1)$ (nghìn đồng)' % (mo_cua, gia_km)
    nb_da_1_s = 'Số tiền cước anh Minh phải trả cho quãng đường $x$ (km) là $%s + %sx$ (nghìn đồng)' % (mo_cua, gia_km)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Kilômét đầu giá $%s$ nghìn đồng và $(x - 1)$ kilômét tiếp theo giá $%s(x - 1)$ nghìn đồng nên tổng cước là $%s + %s(x - 1)$ (nghìn đồng).''' % (mo_cua, gia_km, mo_cua, gia_km))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Bất phương trình biểu thị số tiền cước không vượt quá số tiền anh Minh có là $%s + %s(x - 1) \\le %s$' % (mo_cua, gia_km, tong_tien)
    th_da_1_s = 'Bất phương trình biểu thị số tiền cước không vượt quá số tiền anh Minh có là $%s + %s(x - 1) \\ge %s$' % (mo_cua, gia_km, tong_tien)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì số tiền cước không vượt quá $%s$ nghìn đồng nên ta có $%s + %s(x - 1) \\le %s$.''' % (tong_tien, mo_cua, gia_km, tong_tien))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Giải bất phương trình ta được $x \\le %.2f$ (làm tròn đến hàng phần trăm)' % (x_lam_tron)
    vd_da_1_s = 'Giải bất phương trình ta được $x \\ge %.2f$ (làm tròn đến hàng phần trăm)' % (x_lam_tron)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $%s + %s(x - 1) \\le %s \\Leftrightarrow %sx \\le %s \\Leftrightarrow x \\le %.2f$.''' % (mo_cua, gia_km, tong_tien, gia_km, tong_tien - mo_cua + gia_km, x_lam_tron))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Anh Minh có thể di chuyển được tối đa $%s\\text{ km}$ (làm tròn đến hàng đơn vị)' % (km_max)
    vdc_da_1_s = 'Anh Minh có thể di chuyển được tối đa $%s\\text{ km}$ (làm tròn đến hàng đơn vị)' % (km_max + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì $x \\le %.2f$ nên để không vượt quá số tiền hiện có, anh Minh di chuyển được tối đa $%s\\text{ km}$.''' % (x_lam_tron, km_max))
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
