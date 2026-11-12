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


def bt_dang18_p2_b1_c2_ds9(self):
    # Khai báo biến
    x = symbols('x')
    
    x_ans = random.choice([3, 4, 5])
    canh_day = random.choice([10, 12, 14])
    canh_bia = canh_day + 2 * x_ans
    dt_day = canh_day**2
    gioi_han = canh_bia // 2
    
    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3.6,0);
    \\coordinate (C) at (3.6,3.6);
    \\coordinate (D) at (0,3.6);
    \\coordinate (E) at (0.8,0.8);
    \\coordinate (F) at (2.8,0.8);
    \\coordinate (G) at (2.8,2.8);
    \\coordinate (H) at (0.8,2.8);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\draw[line width=1pt, dashed] (E)--(F)--(G)--(H)--cycle;
    \\draw[line width=1pt] (0,0.8)--(0.8,0.8)--(0.8,0);
    \\draw[line width=1pt] (3.6,0.8)--(2.8,0.8)--(2.8,0);
    \\draw[line width=1pt] (3.6,2.8)--(2.8,2.8)--(2.8,3.6);
    \\draw[line width=1pt] (0,2.8)--(0.8,2.8)--(0.8,3.6);
    \\fill (A) circle (1pt);
    \\fill (B) circle (1pt);
    \\fill (C) circle (1pt);
    \\fill (D) circle (1pt);
    \\node[above] at (1.8,3.6) {$%s$};
    \\node[left] at (0,3.2) {$x$};
    \\node[above] at (0.4,3.6) {$x$};
    \\end{tikzpicture}
    \\end{center}''' % (latex(canh_bia)))
    
    noidungcauhoi = ('''Từ một tấm bìa hình vuông có cạnh bằng $%s\\text{ cm}$, người ta cắt bỏ ở bốn góc bốn hình vuông bằng nhau có cạnh là $x\\text{ (cm)}$ ($0 < x < %s$) rồi gấp lại thành một chiếc hộp hình hộp chữ nhật không có nắp như hình vẽ. Biết diện tích đáy của chiếc hộp tạo thành là $%s\\text{ cm}^2$. %s''' % (latex(canh_bia), latex(gioi_han), latex(dt_day), hinh_ve))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Đáy của chiếc hộp hình hộp chữ nhật là một hình vuông có cạnh $(%s - 2x)\\text{ cm}$' % (latex(canh_bia))
    nb_da_1_s = 'Đáy của chiếc hộp hình hộp chữ nhật là một hình vuông có cạnh $(%s - x)\\text{ cm}$' % (latex(canh_bia))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = ('''Mỗi cạnh của tấm bìa bị cắt bỏ hai đoạn bằng $x$ ở hai góc nên cạnh đáy chiếc hộp là $(%s - 2x)\\text{ cm}$.''' % (latex(canh_bia)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Phương trình biểu thị diện tích đáy của chiếc hộp là $(%s - 2x)^2 = %s$' % (latex(canh_bia), latex(dt_day))
    th_da_1_s = 'Phương trình biểu thị diện tích đáy của chiếc hộp là $(%s - x)^2 = %s$' % (latex(canh_bia), latex(dt_day))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Diện tích đáy hình vuông là $(%s - 2x)^2\\text{ (cm}^2)$, theo giả thiết ta có phương trình $(%s - 2x)^2 = %s$.''' % (latex(canh_bia), latex(canh_bia), latex(dt_day)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Phương trình trên quy về phương trình tích là $(%s - 2x)(%s - 2x) = 0$' % (latex(canh_bia - canh_day), latex(canh_bia + canh_day))
    vd_da_1_s = 'Phương trình trên quy về phương trình tích là $(%s - 2x)(%s + 2x) = 0$' % (latex(canh_bia - canh_day), latex(canh_bia + canh_day))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Ta có $(%s - 2x)^2 - %s^2 = 0$, áp dụng hằng đẳng thức hiệu hai bình phương được $(%s - 2x - %s)(%s - 2x + %s) = 0$ hay $(%s - 2x)(%s - 2x) = 0$.''' % (latex(canh_bia), latex(canh_day), latex(canh_bia), latex(canh_day), latex(canh_bia), latex(canh_day), latex(canh_bia - canh_day), latex(canh_bia + canh_day)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Chiều cao của chiếc hộp hình hộp chữ nhật là $%s\\text{ cm}$' % (latex(x_ans))
    vdc_da_1_s = 'Chiều cao của chiếc hộp hình hộp chữ nhật là $%s\\text{ cm}$' % (latex(canh_bia - x_ans))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Giải phương trình tích tìm được $x = %s$ (thoả mãn $0 < x < %s$) hoặc $x = %s$ (loại). Vì chiều cao chiếc hộp chính là cạnh hình vuông cắt bỏ nên chiều cao bằng $%s\\text{ cm}$.''' % (latex(x_ans), latex(gioi_han), latex(canh_bia - x_ans), latex(x_ans)))
    list_vdc_2 = [loigiai_vdc_1]
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
            break
    
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
    '\\choiceTFn \n'
    '{'+str(shuffled_answers_nb[0])+'}\n'
    '{'+str(shuffled_answers_th[0])+'}\n'
    '{'+str(shuffled_answers_vd[0])+'}\n'
    '{'+str(shuffled_answers_vdc[0])+'}\n'
    '\\loigiai{ \n'
    '\\begin{enumEX}[a)]{1} \n'
    '\\item '+str(shuffled_solutions_nb[0])+'\n'
    '\\item '+str(shuffled_solutions_th[0])+'\n'
    '\\item '+str(shuffled_solutions_vd[0])+'\n'
    '\\item '+str(shuffled_solutions_vdc[0])+'\n'
    '\\end{enumEX}} \n'
    '\\end{ex}\n \\end{minipage}\n\n')
    return content
