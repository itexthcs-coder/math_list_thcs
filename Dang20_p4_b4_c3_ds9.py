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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_Dang20_p4_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hanh_tinh, T_val = random.choice([
            ("Sao Mộc", 11.86),
            ("Sao Thổ", 29.46),
            ("Sao Thiên Vương", 84.01)
        ])
        a_val = (T_val**2)**(1/3)
        a_2 = str(Decimal(float(a_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        T_str = str(T_val).replace('.', ',')
        he_so_a = random.choice([4, 9, 16])
        can_a = int(he_so_a**(1/2))
        T_tieu_hanh_tinh = can_a**3

        noidungcauhoi = ('''Theo định luật III Kepler, chu kì quay $T$ (tính bằng năm Trái Đất) của một hành tinh quanh Mặt Trời và bán trục lớn $a$ (tính bằng đơn vị thiên văn $\text{AU}$) của quỹ đạo hành tinh đó liên hệ với nhau bởi công thức $T^2 = a^3$, hay $a = \sqrt[3]{T^2}$. \\
        a) Biết %s có chu kì quay quanh Mặt Trời là $T \approx %s$ năm. Hãy tính khoảng cách trung bình $a$ từ %s đến Mặt Trời (làm tròn kết quả đến chữ số thập phân thứ hai). \\
        b) Một tiểu hành tinh có khoảng cách trung bình đến Mặt Trời gấp $%s$ lần khoảng cách từ Trái Đất đến Mặt Trời (biết khoảng cách từ Trái Đất đến Mặt Trời là $1\text{ AU}$). Hỏi chu kì quay của tiểu hành tinh đó quanh Mặt Trời là bao nhiêu năm?'''
                         % (hanh_tinh, T_str, hanh_tinh, he_so_a))

        loigiai = ('''\\begin{enumEX}[a)]{1} \n
        \\item Khoảng cách trung bình từ %s đến Mặt Trời là: \\
        $a = \sqrt[3]{%s^2} \approx %s \approx %s\text{ (AU)}$. \n
        \\item Với tiểu hành tinh có $a = %s\text{ AU}$, ta có $T^2 = %s^3 = %s \Rightarrow T = %s$ (năm) (vì $T > 0$). \n
        \\end{enumEX} \n'''
                   % (hanh_tinh, T_str, str(round(a_val, 5)).replace('.', ','), a_2,
                      he_so_a, he_so_a, he_so_a**3, T_tieu_hanh_tinh))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
