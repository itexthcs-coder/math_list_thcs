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


def bt_dang18_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Tốc độ in của máy A (v_A) và máy B (v_B) (trang/phút)
        v_B = randint(2, 4)
        v_A = v_B + randint(1, 2)
        
        # Thời gian hoạt động của máy A và máy B (phút)
        t_A = randint(15, 40)
        t_B = randint(15, 40)
        
        # Tổng thời gian và tổng số trang in được
        tong_t = t_A + t_B
        tong_trang = v_A * t_A + v_B * t_B
        
        # Giả sử cả tong_t phút đều là máy B hoạt động
        trang_neu_toan_B = tong_t * v_B
        # Số trang in dôi ra
        trang_doi_ra = tong_trang - trang_neu_toan_B
        # Mỗi phút máy A in nhiều hơn máy B số trang là
        chenh_lech_toc_do = v_A - v_B
        
        # Kết quả cần tìm: thời gian máy A hoạt động (phút)
        kq = t_A
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong xưởng in, máy A có tốc độ in %s trang/phút, máy B in được %s trang/phút. Tổng thời gian hoạt động của hai máy là %s phút và tổng số trang in được là %s trang. Hỏi máy A đã hoạt động trong bao nhiêu phút?'''
                         %(str(v_A),
                           str(v_B),
                           str(tong_t),
                           str(tong_trang)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Giả sử trong toàn bộ $%s$ phút chỉ có máy B hoạt động thì tổng số trang in được là: \\\\
    $%s \\cdot %s = %s$ (trang). \\\\
    Số trang in thực tế nhiều hơn số trang in theo giả thiết là: \\\\
    $%s - %s = %s$ (trang). \\\\
    Trong mỗi phút, máy A in được nhiều hơn máy B số trang là: \\\\
    $%s - %s = %s$ (trang). \\\\
    Thời gian máy A đã hoạt động là: \\\\
    $%s : %s = %s$ (phút). \\\\
    Vậy máy A đã hoạt động trong $%s$ phút.'''
                   %(str(tong_t),
                     str(tong_t), str(v_B), str(trang_neu_toan_B),
                     str(tong_trang), str(trang_neu_toan_B), str(trang_doi_ra),
                     str(v_A), str(v_B), str(chenh_lech_toc_do),
                     str(trang_doi_ra), str(chenh_lech_toc_do), str(kq_str),
                     str(kq_str)
                   ))
    
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage} \n\n')
    return content
