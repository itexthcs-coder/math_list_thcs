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


def bt_dang1_p1_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        tam_giac = random.choice([
            ('A', 'B', 'C', 'a', 'b', 'c'),
            ('M', 'N', 'P', 'm', 'n', 'p'),
            ('D', 'E', 'F', 'd', 'e', 'f')
        ])
        A, B, C, a, b, c = tam_giac
        chon_canh = random.choice(['b', 'c'])

        if chon_canh == 'b':
            du = [f"${b} = {a} \\cdot \\sin {B}$", f"${b} = {a} \\cdot \\cos {C}$"]
            da = random.choice(du)
            s = [
                f"${b} = {a} \\cdot \\cos {B}$",
                f"${b} = {a} \\cdot \\sin {C}$",
                f"${b} = {a} \\cdot \\tan {B}$",
                f"${b} = {a} \\cdot \\cot {B}$",
                f"${b} = {c} \\cdot \\sin {B}$"
            ]
            gt_dung = f"${b} = {a} \\cdot \\sin {B} = {a} \\cdot \\cos {C}$"
        else:
            du = [f"${c} = {a} \\cdot \\sin {C}$", f"${c} = {a} \\cdot \\cos {B}$"]
            da = random.choice(du)
            s = [
                f"${c} = {a} \\cdot \\cos {C}$",
                f"${c} = {a} \\cdot \\sin {B}$",
                f"${c} = {a} \\cdot \\tan {C}$",
                f"${c} = {a} \\cdot \\cot {C}$",
                f"${c} = {b} \\cdot \\sin {C}$"
            ]
            gt_dung = f"${c} = {a} \\cdot \\sin {C} = {a} \\cdot \\cos {B}$"

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        hinh_tikz = (
            r"\begin{center}" + "\n"
            r"\begin{tikzpicture}[scale=0.8]" + "\n"
            f"\\coordinate ({A}) at (0,0);\n"
            f"\\coordinate ({B}) at (4,0);\n"
            f"\\coordinate ({C}) at (0,2.6);\n"
            f"\\draw[thick] ({A}) -- ({B}) node[midway, below] {{${c}$}} -- ({C}) node[midway, above right] {{${a}$}} -- cycle node[midway, left] {{${b}$}};\n"
            f"\\draw ({A}) rectangle ++(0.3,0.3);\n"
            f"\\node[below left] at ({A}) {{${A}$}};\n"
            f"\\node[below right] at ({B}) {{${B}$}};\n"
            f"\\node[above left] at ({C}) {{${C}$}};\n"
            r"\end{tikzpicture}" + "\n"
            r"\end{center}"
        )

        noidungcauhoi = f"Cho tam giác ${A}{B}{C}$ vuông tại ${A}$ có cạnh huyền ${B}{C} = {a}$ và các cạnh góc vuông ${A}{C} = {b}$, ${A}{B} = {c}$ (như hình vẽ). Khẳng định nào sau đây là \\textbf{{đúng}}?{hinh_tikz}"

        da_d = "\\True " + str(da)
        da_s1, da_s2, da_s3 = str(das1), str(das2), str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = (
            f"Theo Định lí 1: Trong tam giác vuông, mỗi cạnh góc vuông bằng cạnh huyền nhân với $\\sin$ góc đối hoặc nhân với $\\cos$ góc kề.\\\\"
            f"Trong tam giác ${A}{B}{C}$ vuông tại ${A}$, ta có {gt_dung}.\\\\"
            f"Vậy chọn đáp án {da}."
        )

    # Xuất câu trắc nghiệm
    content = (r"\begin{minipage}{\textwidth}" + "\n"
               r"\begin{ex}" + "\n" + str(noidungcauhoi) + r"\choice" + "\n"
               "{" + str(list_1[1]) + "}\n"
               "{" + str(list_1[2]) + "}\n"
               "{" + str(list_1[3]) + "}\n"
               "{" + str(list_1[0]) + "}\n"
               r"\loigiai{" + str(loigiai) + "}\n"
               r"\end{ex}" + "\n" + r"\end{minipage}" + "\n\n")

    return content
