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


def bt_dang13_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Điểm cộng cho mỗi câu đúng và điểm trừ cho mỗi câu sai/không làm
        diem_dung = randint(4, 6)
        diem_tru = randint(1, 3)
        
        # Tổng số câu hỏi n
        tong_cau = randint(15, 30)
        
        # Số câu đúng (x) và số câu sai (y)
        cau_dung = randint(tong_cau // 2, tong_cau - 2)
        cau_sai = tong_cau - cau_dung
        
        # Tổng số điểm đạt được
        tong_diem = cau_dung * diem_dung - cau_sai * diem_tru
        
        # Giả sử tất cả các câu đều làm đúng
        diem_neu_dung_het = tong_cau * diem_dung
        # Số điểm bị giảm đi so với tối đa
        diem_giam = diem_neu_dung_het - tong_diem
        # Mỗi câu làm sai/không trả lời làm mất đi số điểm là:
        diem_mat_moi_cau = diem_dung + diem_tru
        
        # Kết quả cần tìm: số câu trả lời đúng
        kq = cau_dung
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một bài thi đánh giá năng lực gồm %s câu hỏi. Mỗi câu trả lời đúng được cộng %s điểm, mỗi câu trả lời sai (hoặc không trả lời) bị trừ %s điểm. Một thí sinh làm bài và đạt được tổng số %s điểm. Hỏi thí sinh đó đã trả lời đúng bao nhiêu câu?'''
                         %(str(tong_cau),
                           str(diem_dung),
                           str(diem_tru),
                           str(tong_diem)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Giả sử thí sinh trả lời đúng tất cả $%s$ câu hỏi thì số điểm đạt được tối đa là: \\\\
    $%s \\cdot %s = %s$ (điểm). \\\\
    Số điểm bị giảm đi so với khi làm đúng hết là: \\\\
    $%s - %s = %s$ (điểm). \\\\
    Thay vì được cộng $%s$ điểm, mỗi câu trả lời sai (hoặc không trả lời) lại bị trừ $%s$ điểm nên mỗi câu sai làm giảm đi số điểm là: \\\\
    $%s + %s = %s$ (điểm). \\\\
    Số câu thí sinh trả lời sai (hoặc không trả lời) là: \\\\
    $%s : %s = %s$ (câu). \\\\
    Số câu thí sinh đã trả lời đúng là: \\\\
    $%s - %s = %s$ (câu). \\\\
    Vậy thí sinh đó đã trả lời đúng $%s$ câu.'''
                   %(str(tong_cau),
                     str(tong_cau), str(diem_dung), str(diem_neu_dung_het),
                     str(diem_neu_dung_het), str(tong_diem), str(diem_giam),
                     str(diem_dung), str(diem_tru),
                     str(diem_dung), str(diem_tru), str(diem_mat_moi_cau),
                     str(diem_giam), str(diem_mat_moi_cau), str(cau_sai),
                     str(tong_cau), str(cau_sai), str(kq_str),
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
