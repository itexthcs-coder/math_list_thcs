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


def bt_dang14_p4_b2_c2_ds9(self):
    # Dạng 14: Bài toán quản lý tải trọng tàu vận tải hàng hóa
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tai_max = random.choice([400, 450, 500, 600])
        vlxd = random.choice([100, 120, 140])
        thuy_thu = random.choice([12, 15, 18])
        co_dinh = vlxd + thuy_thu
        cont = random.choice([16, 18, 20, 22])
        con_lai = tai_max - co_dinh
        max_cont = con_lai // cont
        kq_xap_xi = str(round(con_lai / cont, 2)).replace('.', ',')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một tàu vận tải đường thủy có trọng tải tối đa cho phép là $%d$ tấn. Trên tàu hiện đã có sẵn $%d$ tấn vật liệu xây dựng và thủy thủ đoàn cùng trang thiết bị nặng $%d$ tấn. Người ta muốn xếp thêm lên tàu các container hàng hóa giống nhau, mỗi container nặng $%d$ tấn. Hỏi tàu có thể chở thêm nhiều nhất bao nhiêu container hàng hóa để đảm bảo an toàn theo quy định?'''
                         % (tai_max, vlxd, thuy_thu, cont))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ ($x \\in \\mathbb{N}^*$) là số container hàng hóa xếp thêm lên tàu. \\\\
                   Tổng khối lượng hàng hóa và thiết bị trên tàu là: $%d + %d + %dx = %d + %dx$ (tấn). \\\\
                   Vì trọng tải tối đa là $%d$ tấn nên ta có bất đẳng thức:
                   $$%d + %dx \\le %d.$$
                   Cộng cả hai vế với $-%d$ ta được:
                   $$%dx \\le %d.$$
                   Nhân cả hai vế với số dương $\\dfrac{1}{%d} > 0$ ta được:
                   $$x \\le \\dfrac{%d}{%d} \\approx %s.$$
                   Vì $x \\in \\mathbb{N}^*$ nên tàu có thể chở thêm nhiều nhất $%d$ container hàng hóa.'''
                   % (vlxd, thuy_thu, cont, co_dinh, cont, tai_max,
                      co_dinh, cont, tai_max, co_dinh, cont, con_lai,
                      cont, con_lai, cont, kq_xap_xi, max_cont))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')


    return content
