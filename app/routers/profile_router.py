#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, APIRouter
from schemas.base_schema import API_RESPONSE

profile_router = APIRouter(
    prefix="/profile",
    tags=["profile"],
)


@profile_router.get('/')
def get_all_dose():
    API_RESPONSE['data'] = "test data!"
    return (API_RESPONSE)
