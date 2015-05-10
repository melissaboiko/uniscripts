#!/bin/sh
set -e
cd `dirname "$0"`
set -x
for f in Scripts.txt ScriptExtensions.txt PropertyValueAliases.txt; do
  rm -f "$f"
  wget -q "http://ftp.unicode.org/Public/UNIDATA/$f"
done

./make_unidata.py > ../unidata.py
