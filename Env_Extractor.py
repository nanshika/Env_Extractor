﻿# python Env_Extractor.py
# -*- coding: utf-8 -*-
import os
from datetime import datetime

with open("C:/Script/backup/" + datetime.now().strftime("%Y%m%d_%H%M%S") + "_Env_backup.csv",'w',encoding = "SJIS") as f2: #utf-8_sig
    for item in os.environ:
        f2.write(item + "," + os.environ[item] + "\n")
