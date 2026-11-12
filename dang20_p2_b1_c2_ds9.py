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


def bt_dang20_p2_b1_c2_ds9(self):
    # Khai báo biến
    x = symbols('x')
    
    bo_so = random.choice([
        (Rational(3, 2), "1,5", 9, 2, 10, Rational(1, 6)),
        (Rational(3, 2), "1,5", 12, 3, 21, Rational(1, 8)),
        (2, "2", 10, 3, 12, Rational(1, 5)),
        (Rational(3, 2), "1,5", 6, 2, 6, Rational(1, 4))
    ])
    h_coc, h_coc_str, h_cot, bong_coc, x_ans, ti_so = bo_so
    
    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (0,2.8);
    \\coordinate (C) at (4.5,0);
    \\coordinate (D) at (3.0,0);
    \\coordinate (E) at (3.0,0.93);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt] (D)--(E);
    \\fill (A) circle (1pt) node[below] {$A$};
    \\fill (B) circle (1pt) node[above] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\fill (E) circle (1pt) node[above right] {$E$};
    \\node[left] at (0,1.4) {$%s\\text{ m}$};
    \\node[left] at (3.0,0.45) {$%s\\text{ m}$};
    \\node[below] at (1.5,0) {$x\\text{ m}$};
    \\node[below] at (3.75,0) {$%s\\text{ m}$};
    \\end{tikzpicture}
    \\end{center}''' % (latex(h_cot), h_coc_str, latex(bong_coc)))
    
    noidungcauhoi = ('''Để đo chiều cao của một cột cờ $AB$ tại sân trường, một học sinh cắm một chiếc cọc $DE$ thẳng đứng cao $%s\\text{ m}$ cách chân cột cờ một khoảng $AD = x\\text{ (m)}$ ($x > 0$). Tại cùng một thời điểm nắng chiếu, bóng của đỉnh cột cờ và bóng của đỉnh cọc trùng nhau tại điểm $C$ trên mặt đất cách chân cọc $CD = %s\\text{ m}$. Biết chiều cao cột cờ là $AB = %s\\text{ m}$ (như hình vẽ). %s''' % (h_coc_str, latex(bong_coc), latex(h_cot), hinh_ve))
    
    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Khoảng cách từ điểm bóng trùng nhau $C$ đến chân cột cờ $A$ là $(x + %s)\\text{ m}$' % (latex(bong_coc))
    nb_da_1_s = 'Khoảng cách từ điểm bóng trùng nhau $C$ đến chân cột cờ $A$ là $(x - %s)\\text{ m}$' % (latex(bong_coc))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = ('''Vì điểm $D$ nằm giữa $A$ và $C$ nên $AC = AD + DC = (x + %s)\\text{ m}$.''' % (latex(bong_coc)))
    list_nb_2 = [loigiai_nb_1]
    
    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Áp dụng định lí Thalès, ta lập được tỉ lệ thức $\\dfrac{%s}{%s} = \\dfrac{%s}{x + %s}$' % (h_coc_str, latex(h_cot), latex(bong_coc), latex(bong_coc))
    th_da_1_s = 'Áp dụng định lí Thalès, ta lập được tỉ lệ thức $\\dfrac{%s}{%s} = \\dfrac{x}{x + %s}$' % (h_coc_str, latex(h_cot), latex(bong_coc))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = ('''Vì $DE // AB$ (cùng vuông góc với mặt đất $AC$), áp dụng định lí Thalès trong tam giác $ABC$ ta có $\\dfrac{DE}{AB} = \\dfrac{CD}{CA}$ hay $\\dfrac{%s}{%s} = \\dfrac{%s}{x + %s}$.''' % (h_coc_str, latex(h_cot), latex(bong_coc), latex(bong_coc)))
    list_th_2 = [loigiai_th_1]
    
    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Phương trình chứa ẩn ở mẫu tìm được là $\\dfrac{%s}{x + %s} = %s$' % (latex(bong_coc), latex(bong_coc), latex(ti_so))
    vd_da_1_s = 'Phương trình chứa ẩn ở mẫu tìm được là $\\dfrac{%s}{x + %s} = %s$' % (latex(bong_coc), latex(bong_coc), latex(Rational(1, ti_so)))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = ('''Rút gọn tỉ số $\\dfrac{%s}{%s} = %s$, ta thu được phương trình $\\dfrac{%s}{x + %s} = %s$.''' % (h_coc_str, latex(h_cot), latex(ti_so), latex(bong_coc), latex(bong_coc), latex(ti_so)))
    list_vd_2 = [loigiai_vd_1]
    
    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Chiếc cọc được cắm cách chân cột cờ một khoảng là $%s\\text{ m}$' % (latex(x_ans))
    vdc_da_1_s = 'Chiếc cọc được cắm cách chân cột cờ một khoảng là $%s\\text{ m}$' % (latex(x_ans + bong_coc))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = ('''Quy đồng và khử mẫu phương trình $\\dfrac{%s}{x + %s} = %s$ (với $x > 0$), ta được $x + %s = %s$, suy ra $x = %s$ (thoả mãn). Vậy cọc cách chân cột cờ $%s\\text{ m}$.''' % (latex(bong_coc), latex(bong_coc), latex(ti_so), latex(bong_coc), latex(x_ans + bong_coc), latex(x_ans), latex(x_ans)))
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
