#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from typing import Optional

from faker import Faker as F
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def read_root():
    return RedirectResponse(url='/docs')


#  PROFILE
@app.get('/profile')
def profile():
    """Returns a single profile."""
    return {'data': F().profile()}


@app.get('/profile/{quantity}')
def profiles(quantity: int):
    """Returns a set of profiles."""
    return {'data': [F().profile() for i in range(0, quantity)]}


#  RANDOM SHIT
@app.get('/address')
def addres():
    """Returns a single addres."""
    return {'address': F().address()}


@app.get('/address/{quantity}')
def addresses(quantity: int):
    """Return's a set of addresses matching the number requested."""
    return {'data': [F().address() for i in range(0, quantity)]}
