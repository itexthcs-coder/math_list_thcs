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


def bt_dang15_p4_b2_c2_ds9(self):
    # Dạng 15: Bài toán lập kế hoạch tiết kiệm và trả góp mua xe máy điện
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tra_truoc = random.choice([5500, 6000, 6500, 7000]) # nghìn đồng
        moi_thang = random.choice([1200, 1250, 1500])       # nghìn đồng
        so_thang = randint(10, 16)
        no_lai = moi_thang * so_thang
        gia_xe = tra_truoc + no_lai
    
        def fmt_t(nghin):
            return f"{nghin * 1000:,}".replace(",", "\\,")
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc xe máy điện có giá niêm yết là $%s$ đồng. Cửa hàng áp dụng hình thức mua trả góp: khách hàng trả trước $%s$ đồng, phần còn lại trả góp đều trong các tháng tiếp theo, mỗi tháng trả $%s$ đồng (lãi suất $0\\%%$). Hỏi sau ít nhất bao nhiêu tháng trả góp thì khách hàng thanh toán xong toàn bộ tiền mua xe?'''
                         % (fmt_t(gia_xe), fmt_t(tra_truoc), fmt_t(moi_thang)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ ($x \\in \\mathbb{N}^*$) là số tháng khách hàng trả góp. \\\\
                   Tổng số tiền khách hàng đã thanh toán sau $x$ tháng là: $%s + %sx$ (đồng). \\\\
                   Để thanh toán xong toàn bộ tiền mua xe, ta có bất đẳng thức:
                   $$%s + %sx \\ge %s.$$
                   Cộng cả hai vế với $-%s$ ta được:
                   $$%sx \\ge %s.$$
                   Nhân cả hai vế với số dương $\\dfrac{1}{%s} > 0$ ta được:
                   $$x \\ge %d.$$
                   Vậy sau ít nhất $%d$ tháng trả góp thì khách hàng sẽ thanh toán xong toàn bộ tiền mua xe.'''
                   % (fmt_t(tra_truoc), fmt_t(moi_thang),
                      fmt_t(tra_truoc), fmt_t(moi_thang), fmt_t(gia_xe),
                      fmt_t(tra_truoc), fmt_t(moi_thang), fmt_t(no_lai),
                      fmt_t(moi_thang), so_thang, so_thang))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')


    return content
