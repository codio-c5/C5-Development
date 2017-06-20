#!/bin/bash
#
echo "WDNH PH RXW WR WKH EDOO JDPH WDNH PH RXW ZLWK WKH FURZG EXB PH VRPH SHDQXWV DQG FUDFNHUMDFNVL GRQW FDUH LI L QHYHU JHW EDFN OHW PH URRW" | \
sed -e 's/\s//g' | \
fold -w1 | \
sort | \
uniq -c | sort -rn | head -7
