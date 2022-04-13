#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

import os
from pathlib import Path
from typing import Optional
from faker import Faker as F
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

#  IMPORTING SCHEMAS

#  IMPORTING ROUTERS
from routers import (profile_router)

#  IMPORTING METADATA
from api_metadata import api_metadata

app = FastAPI(title="PlaceHolder - API",
              description="A small api for testing proposites..",
              version="0.0.1",
              openapi_tags=api_metadata)

#  INCLUDING ROUTERS
app.include_router(profile_router.profile_router)

#  STATIC & TEMPLATES
BASE_DIR = Path(__file__).resolve().parent


@app.get('/', include_in_schema=False)
def api_home():
    return ('HOME PAGE!')
