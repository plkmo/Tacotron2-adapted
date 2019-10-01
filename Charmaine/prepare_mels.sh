#!/usr/bin/env bash

set -e

DATADIR="Charmaine"
FILELISTSDIR="filelists"

TESTLIST="$FILELISTSDIR/train.txt"
TRAINLIST="$FILELISTSDIR/train.txt"
VALLIST="$FILELISTSDIR/train.txt"

TESTLIST_MEL="$FILELISTSDIR/mels.txt"
TRAINLIST_MEL="$FILELISTSDIR/mels.txt"
VALLIST_MEL="$FILELISTSDIR/mels.txt"

mkdir -p "$DATADIR/mels"
if [ $(ls $DATADIR/mels | wc -l) -ne 13100 ]; then
    python preprocess_audio2mel.py --wav-files "$TRAINLIST" --mel-files "$TRAINLIST_MEL"	
fi	
