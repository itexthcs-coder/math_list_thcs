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


def bt_dang16_p4_b2_c2_ds9(self):
    # Dạng 16: Bài toán điểm hòa vốn và mục tiêu lợi nhuận trong kinh doanh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        von_ly = random.choice([10, 12, 15])          # nghìn đồng
        lai_ly = random.choice([15, 20, 25])          # nghìn đồng
        gia_ban = von_ly + lai_ly
        co_dinh = random.choice([1200, 1400, 1500])   # nghìn đồng
        min_ly = randint(95, 140)
        lai_muc_tieu = lai_ly * min_ly - co_dinh
        while lai_muc_tieu < 800:
            min_ly += 10
            lai_muc_tieu = lai_ly * min_ly - co_dinh
        tong_can = lai_muc_tieu + co_dinh
    
        def fmt_t(nghin):
            return f"{nghin * 1000:,}".replace(",", "\\,")
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cửa hàng kinh doanh cà phê có chi phí cố định hằng ngày (tiền thuê mặt bằng, nhân công, điện nước) là $%s$ đồng. Chi phí nguyên liệu để pha chế mỗi ly cà phê là $%s$ đồng và giá bán ra là $%s$ đồng/ly. Hỏi mỗi ngày cửa hàng cần bán được ít nhất bao nhiêu ly cà phê để thu được lợi nhuận (doanh thu trừ đi tổng chi phí) đạt từ $%s$ đồng trở lên?'''
                         % (fmt_t(co_dinh), fmt_t(von_ly), fmt_t(gia_ban), fmt_t(lai_muc_tieu)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ ($x \\in \\mathbb{N}^*$) là số ly cà phê cửa hàng bán được trong một ngày. \\\\
                   Doanh thu trong ngày là $%sx$ (đồng); tổng chi phí trong ngày là $%s + %sx$ (đồng). \\\\
                   Lợi nhuận thu được trong ngày là: $%sx - (%s + %sx) = %sx - %s$ (đồng). \\\\
                   Để lợi nhuận đạt từ $%s$ đồng trở lên, ta có bất đẳng thức:
                   $$%sx - %s \\ge %s.$$
                   Cộng cả hai vế với $%s$ ta được:
                   $$%sx \\ge %s.$$
                   Nhân cả hai vế với số dương $\\dfrac{1}{%s} > 0$ ta được:
                   $$x \\ge %d.$$
                   Vậy mỗi ngày cửa hàng cần bán được ít nhất $%d$ ly cà phê.'''
                   % (fmt_t(gia_ban), fmt_t(co_dinh), fmt_t(von_ly),
                      fmt_t(gia_ban), fmt_t(co_dinh), fmt_t(von_ly), fmt_t(lai_ly), fmt_t(co_dinh),
                      fmt_t(lai_muc_tieu), fmt_t(lai_ly), fmt_t(co_dinh), fmt_t(lai_muc_tieu),
                      fmt_t(co_dinh), fmt_t(lai_ly), fmt_t(tong_can), fmt_t(lai_ly), min_ly, min_ly))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')


    return content
