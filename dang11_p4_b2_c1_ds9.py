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


def bt_dang11_p4_b2_c1_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            x0 = random.choice([40, 50, 60, 70])
            y0 = random.choice([10, 12, 15, 18])
            dx1 = random.choice([6, 8, 10])
            dy1 = random.choice([2, 3, 4])
            dx2 = random.choice([4, 5])
            dy2 = random.choice([2, 3])
            if y0 > dy1 and x0 > dx2 and (-dy1 * dx2 + dx1 * dy2) != 0:
                break
    
        giam_cay = x0 * y0 - (x0 + dx1) * (y0 - dy1)
        tang_cay = (x0 - dx2) * (y0 + dy2) - x0 * y0
        vp1 = -giam_cay + dx1 * dy1
        vp2 = tang_cay + dx2 * dy2
    
        pt1_rg = latex(-dy1 * x + dx1 * y) + '=' + latex(vp1)
        pt2_rg = latex(dy2 * x - dx2 * y) + '=' + latex(vp2)
    
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một mảnh vườn được đánh thành nhiều luống, mỗi luống trồng cùng một số cây cải bắp. Hãy tính số cây cải bắp được trồng trên mảnh vườn đó, biết rằng: \\\\
                         $\\bullet$ Nếu tăng thêm $%s$ luống, nhưng mỗi luống trồng ít đi $%s$ cây cải bắp thì số cải bắp của cả vườn sẽ ít đi $%s$ cây; \\\\
                         $\\bullet$ Nếu giảm đi $%s$ luống, nhưng mỗi luống trồng tăng thêm $%s$ cây thì số cải bắp cả vườn sẽ tăng thêm $%s$ cây.'''
                         % (latex(dx1), latex(dy1), latex(giam_cay), latex(dx2), latex(dy2), latex(tang_cay)))
    
        # Nội dung lời giải
        loigiai = ('''Gọi $x$ là số luống trong vườn và $y$ là số cây cải bắp trồng ở mỗi luống ($x, y \\in \\mathbb{N}^*$). \\\\
                   Tổng số cây cải bắp ban đầu được trồng trên mảnh vườn là $xy$ (cây). \\\\
                   Nếu tăng thêm $%s$ luống và mỗi luống trồng ít đi $%s$ cây thì số cải bắp cả vườn ít đi $%s$ cây, nên ta có phương trình: \\\\
                   $(x + %s)(y - %s) = xy - %s \\Leftrightarrow xy - %sx + %sy - %s = xy - %s \\Leftrightarrow %s$. \\\\
                   Nếu giảm đi $%s$ luống và mỗi luống trồng tăng thêm $%s$ cây thì số cải bắp cả vườn tăng thêm $%s$ cây, nên ta có phương trình: \\\\
                   $(x - %s)(y + %s) = xy + %s \\Leftrightarrow xy + %sx - %sy - %s = xy + %s \\Leftrightarrow %s$. \\\\
                   Từ đó ta có hệ phương trình $\\begin{cases} %s \\\\ %s \\end{cases}$. \\\\
                   Giải hệ phương trình trên bằng phương pháp cộng đại số, ta tìm được $x = %s$ và $y = %s$ (thỏa mãn điều kiện). \\\\
                   Vậy tổng số cây cải bắp được trồng trên mảnh vườn đó là $%s \\cdot %s = %s$ (cây).'''
                   % (latex(dx1), latex(dy1), latex(giam_cay),
                      latex(dx1), latex(dy1), latex(giam_cay), latex(dy1), latex(dx1), latex(dx1 * dy1), latex(giam_cay), pt1_rg,
                      latex(dx2), latex(dy2), latex(tang_cay),
                      latex(dx2), latex(dy2), latex(tang_cay), latex(dy2), latex(dx2), latex(dx2 * dy2), latex(tang_cay), pt2_rg,
                      pt1_rg, pt2_rg,
                      latex(x0), latex(y0), latex(x0), latex(y0), latex(x0 * y0)))
    
    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n' '\\end{ex}\n \\end{minipage} \n\n')

    return content
