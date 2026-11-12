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


def bt_dang13_p4_b2_c2_ds9(self):
    # Dạng 13: Bài toán so sánh hai gói cước điện thoại di động
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cuoc_1 = random.choice([700, 800, 900])
        cuoc_2 = random.choice([1100, 1200, 1300])
        hieu_cuoc = cuoc_2 - cuoc_1
        phut_hoa = randint(90, 160)
        thue_bao = phut_hoa * hieu_cuoc
    
        def fmt_n(so):
            return f"{so:,}".replace(",", "\\,")
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một nhà mạng viễn thông đưa ra hai gói cước gọi nội mạng trong một tháng như sau:
                         \\begin{itemize}
                             \\item \\textit{Gói cước 1:} Phí thuê bao cố định $%s$ đồng/tháng và tính cước $%s$ đồng cho mỗi phút gọi.
                             \\item \\textit{Gói cước 2:} Không mất phí thuê bao cố định, tính cước $%s$ đồng cho mỗi phút gọi.
                         \\end{itemize}
                         Hỏi nếu một khách hàng gọi bao nhiêu phút trong một tháng thì chọn Gói cước 1 sẽ tiết kiệm hơn Gói cước 2?'''
                         % (fmt_n(thue_bao), fmt_n(cuoc_1), fmt_n(cuoc_2)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ ($x > 0$, tính theo phút) là thời gian gọi nội mạng trong một tháng của khách hàng. \\\\
                   Chi phí khi dùng Gói cước 1 là $%s + %sx$ (đồng); chi phí khi dùng Gói cước 2 là $%sx$ (đồng). \\\\
                   Để Gói cước 1 tiết kiệm hơn Gói cước 2, ta có bất đẳng thức:
                   $$%s + %sx < %sx.$$
                   Cộng cả hai vế với $-%sx$ ta được:
                   $$%s < %sx \\iff %sx > %s.$$
                   Nhân cả hai vế với số dương $\\dfrac{1}{%s} > 0$ ta được:
                   $$x > %d.$$
                   Vậy nếu khách hàng gọi trên $%d$ phút (tức là từ $%d$ phút trở lên nếu tính theo số nguyên phút) trong một tháng thì chọn Gói cước 1 sẽ tiết kiệm hơn.'''
                   % (fmt_n(thue_bao), fmt_n(cuoc_1), fmt_n(cuoc_2),
                      fmt_n(thue_bao), fmt_n(cuoc_1), fmt_n(cuoc_2),
                      fmt_n(cuoc_1), fmt_n(thue_bao), fmt_n(hieu_cuoc), fmt_n(hieu_cuoc), fmt_n(thue_bao),
                      fmt_n(hieu_cuoc), phut_hoa, phut_hoa, phut_hoa + 1))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')



    return content
