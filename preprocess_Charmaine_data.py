# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:18:29 2019

@author: plkmo
"""
import pandas as pd
import re
from tqdm import tqdm
import logging

tqdm.pandas(desc="prog_bar")
logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', \
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logger = logging.getLogger('__file__')

def preprocess_for_taco2(transcripts_path="./data/Charmaine/prompt.txt", out_path="./data/Charmaine/train.txt"):
    
    with open(transcripts_path, "r", encoding="utf8") as f:
        text = f.readlines()
    
    lines = []
    for sent in text:
        filename = re.findall("charmaine_[\d]+", sent)[0]
        transcript = re.findall("\".+\"", sent)[0]
        transcript = re.sub("[\"\']", "", transcript)
        line = "Charmaine/wavs/" + filename + ".wav|" + transcript
        lines.append(line)
    
    with open(out_path, "w", encoding="utf8") as f:
        for line in lines:
            f.write(line + "\n")
        
    return lines

if __name__ == "__main__":
    lines = preprocess_for_taco2()
