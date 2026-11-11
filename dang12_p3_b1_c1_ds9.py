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


def bt_dang12_p3_b1_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Lãi suất hai mã cổ phiếu r1 và r2 (đơn vị %) với r1 < r2
        r1 = randint(4, 7)
        r2 = r1 + randint(2, 4)
        
        # Số tiền đầu tư vào mỗi mã (triệu đồng), làm tròn theo bước nhảy 50 hoặc 100
        buoc = 50
        tien_ma2 = randint(4, 16) * buoc
        tien_ma1 = randint(4, 16) * buoc
        tong_von = tien_ma1 + tien_ma2
        
        # Tổng số tiền lãi thu được (triệu đồng)
        # Để lãi là số nguyên, ta đảm bảo các phép nhân chia hết
        # Nếu chưa chia hết cho 100, nhân hệ số hoặc điều chỉnh
        while (tien_ma1 * r1 + tien_ma2 * r2) % 100 != 0:
            tien_ma2 = randint(4, 16) * buoc
            tien_ma1 = randint(4, 16) * buoc
            tong_von = tien_ma1 + tien_ma2
            
        tong_lai = (tien_ma1 * r1 + tien_ma2 * r2) // 100
        
        # Giả sử toàn bộ số tiền đầu tư vào mã có lãi suất r1%
        lai_neu_toan_ma1 = (tong_von * r1) // 100
        chenh_lech_lai = tong_lai - lai_neu_toan_ma1
        chenh_lech_ti_le = r2 - r1
        
        # Kết quả cần tìm: số tiền đầu tư vào mã lãi suất r2%
        kq = tien_ma2
        kq_str = str(kq)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một nhà đầu tư dùng %s triệu đồng để đầu tư vào $2$ mã cổ phiếu với mức sinh lời dự kiến lần lượt là %s\\%%/năm và %s\\%%/năm. Hết một năm, tổng số tiền lãi nhà đầu tư thu được là %s triệu đồng. Hỏi người đó đã đầu tư bao nhiêu triệu đồng vào mã có lãi suất %s\\%%?'''
                         %(str(tong_von),
                           str(r1),
                           str(r2),
                           str(tong_lai),
                           str(r2)
                         ))
    
        # Nội dung lời giải
        loigiai = ('''Giả sử nhà đầu tư dùng toàn bộ $%s$ triệu đồng để đầu tư vào mã cổ phiếu có mức sinh lời $%s\\%%$/năm thì sau một năm số tiền lãi thu được là: \\\\
    $%s \\cdot %s\\%% = %s$ (triệu đồng). \\\\
    Số tiền lãi thực tế thu được nhiều hơn số tiền lãi theo giả thiết là: \\\\
    $%s - %s = %s$ (triệu đồng). \\\\
    Mỗi trăm triệu đồng đầu tư vào mã có mức sinh lời $%s\\%%$/năm mang lại nhiều hơn mã $%s\\%%$/năm số tiền lãi tương ứng với tỉ lệ là: \\\\
    $%s\\%% - %s\\%% = %s\\%%$. \\\\
    Số tiền nhà đầu tư đã đầu tư vào mã có lãi suất $%s\\%%$ là: \\\\
    $%s : %s\\%% = %s$ (triệu đồng). \\\\
    Vậy số tiền đầu tư vào mã có lãi suất $%s\\%%$ là $%s$ triệu đồng.'''
                   %(str(tong_von), str(r1),
                     str(tong_von), str(r1), str(lai_neu_toan_ma1),
                     str(tong_lai), str(lai_neu_toan_ma1), str(chenh_lech_lai),
                     str(r2), str(r1),
                     str(r2), str(r1), str(chenh_lech_ti_le),
                     str(r2),
                     str(chenh_lech_lai), str(chenh_lech_ti_le), str(kq_str),
                     str(r2), str(kq_str)
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
