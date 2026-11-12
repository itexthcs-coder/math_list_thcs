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


def bt_dang18_p4_b6_c2_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        co_dinh_tr = random.choice([24, 28, 30])
        co_dinh_nghin = co_dinh_tr * 1000
        gia_von = random.choice([12, 14, 15])
        lai_ly = random.choice([18, 20, 22])
        gia_ban = gia_von + lai_ly
        loi_nhuan_tr = random.choice([18, 20, 24])
        loi_nhuan_nghin = loi_nhuan_tr * 1000
        x_thuc = (loi_nhuan_nghin + co_dinh_nghin) / lai_ly
        min_ly = math.ceil(x_thuc)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cửa hàng khởi nghiệp kinh doanh trà sữa có chi phí cố định hằng tháng (tiền thuê mặt bằng, điện nước, nhân viên) là $%s$ triệu đồng. Chi phí nguyên liệu để làm ra mỗi ly trà sữa là $%s$ nghìn đồng và giá bán mỗi ly là $%s$ nghìn đồng. Hỏi trung bình mỗi tháng cửa hàng cần bán ít nhất bao nhiêu ly trà sữa để thu được lợi nhuận từ $%s$ triệu đồng trở lên?'''
                         % (co_dinh_tr, gia_von, gia_ban, loi_nhuan_tr))
    
        # Nội dung lời giải
        loigiai = ('''Đổi $%s\\text{ triệu đồng} = %s\\text{ nghìn đồng}$ và $%s\\text{ triệu đồng} = %s\\text{ nghìn đồng}$.\\\\
        Gọi $x$ ($x \\in \\mathbb{N}^*$) là số ly trà sữa bán được trong tháng.\\\\
        Tiền lãi thu được trên mỗi ly trà sữa (chưa trừ chi phí cố định) là: $%s - %s = %s$ (nghìn đồng).\\\\
        Lợi nhuận thực tế hằng tháng của cửa hàng là: $%sx - %s$ (nghìn đồng).\\\\
        Để lợi nhuận đạt từ $%s$ triệu đồng trở lên, ta có bất phương trình:
        $$%sx - %s \\ge %s \\Leftrightarrow %sx \\ge %s \\Leftrightarrow x \\ge %.2f.$$
        Vì $x \\in \\mathbb{N}^*$ nên mỗi tháng cửa hàng cần bán ít nhất $%s$ ly trà sữa.'''
                   % (co_dinh_tr, co_dinh_nghin, loi_nhuan_tr, loi_nhuan_nghin,
                      gia_ban, gia_von, lai_ly,
                      lai_ly, co_dinh_nghin, loi_nhuan_tr,
                      lai_ly, co_dinh_nghin, loi_nhuan_nghin,
                      lai_ly, loi_nhuan_nghin + co_dinh_nghin, x_thuc, min_ly))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')

    return content
