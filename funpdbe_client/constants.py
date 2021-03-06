#!/usr/bin/env python3

# Copyright 2018 EMBL - European Bioinformatics Institute
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the
# License.

# These are the URLs of the API of the FunPDBe deposition system
    # internal EBI test URL
# API_URL = "http://wp-p1m-3c.ebi.ac.uk/pdbe/funpdbe/funpdbe_deposition/entries/"
    # local test URL
API_URL = "http://127.0.0.1:8000/funpdbe_deposition/entries/"

# This is the file name of the log file that the client generates
LOG_FILENAME = 'client.log'

# This is the regular expression pattern for a PDB identifier
PDB_ID_PATTERN = "[0-9][a-z][a-z0-9]{2}"

# These are the valid resource name in FunPDBe
RESOURCES = (
    "cath-funsites",
    "3dligandsite",
    "nod",
    "popscomp",
    "14-3-3-pred",
    "dynamine",
    "cansar",
    "credo"
)
