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


def bt_Dang19_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ti_le = random.choice([4, 9])
        can_tl = int(math.sqrt(ti_le))
        rong = randint(8, 16)
        dai = ti_le * rong
        S = ti_le * (rong**2)
        chu_vi = 2 * (rong + dai)
        cong = random.choice([4, 5, 6])
        chieu_dai_rao = chu_vi - cong
        don_gia = random.choice([1200000, 1500000])
        tong_tien = chieu_dai_rao * don_gia

        def fmt_tien(val):
            return f"{val:,}".replace(",", "\\,")

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một khu đất hình chữ nhật có chiều dài gấp $%s$ lần chiều rộng và có diện tích bằng $%s\text{ m}^2$.\\
                         a) Tính chiều rộng và chiều dài của khu đất đó.\\
                         b) Người ta muốn xây tường rào bao quanh khu đất, trừ ra một cổng ra vào rộng $%s\text{ m}$. Tính chi phí xây tường rào biết giá xây mỗi mét dài tường rào là $%s\text{ đồng}$.'''
                         % (latex(ti_le), latex(S), latex(cong), fmt_tien(don_gia)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                      \item Gọi $x$ ($\text{m}$, $x > 0$) là chiều rộng của khu đất hình chữ nhật. Khi đó chiều dài khu đất là $%sx$ ($\text{m}$). Vì diện tích khu đất bằng $%s\text{ m}^2$ nên ta có:
                      $$x \cdot %sx = %s \Leftrightarrow %sx^2 = %s \Leftrightarrow x^2 = \dfrac{%s}{%s} \Leftrightarrow x = \dfrac{\sqrt{%s}}{\sqrt{%s}} = \dfrac{%s}{%s} = %s\text{ (m)}.$$
                      Chiều dài của khu đất là $%s \cdot %s = %s$ ($\text{m}$).
                      \item Chu vi của khu đất là $2(%s + %s) = %s$ ($\text{m}$).
                      Chiều dài tường rào cần xây (sau khi trừ cổng) là $%s - %s = %s$ ($\text{m}$).
                      Tổng chi phí xây tường rào là $%s \cdot %s = %s\text{ (đồng)}$.
                      \\end{enumEX}'''
                   % (latex(ti_le), latex(S), latex(ti_le), latex(S), latex(ti_le), latex(S),
                      latex(S), latex(ti_le), latex(S), latex(ti_le), latex(can_tl * rong), latex(can_tl), latex(rong),
                      latex(ti_le), latex(rong), latex(dai),
                      latex(rong), latex(dai), latex(chu_vi),
                      latex(chu_vi), latex(cong), latex(chieu_dai_rao),
                      latex(chieu_dai_rao), fmt_tien(don_gia), fmt_tien(tong_tien)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
