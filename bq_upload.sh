#!/bin/bash
gcloud auth application-default login

bq load \
--source_format=NEWLINE_DELIMITED_JSON --autodetect \
skills_martinez.bills ./bills.jsonl 
