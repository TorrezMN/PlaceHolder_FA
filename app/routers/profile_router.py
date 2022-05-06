#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from faker import Faker
from fastapi import APIRouter, Depends, HTTPException
from schemas.base_schema import API_RESPONSE

fake = Faker()

profile_router = APIRouter(
    prefix="/profile",
    tags=["profile"],
)


@profile_router.get('/')
def profile_home():
    API_RESPONSE['data'] = "test data!"
    return (API_RESPONSE)


@profile_router.get('/get_profile')
def get_profile():
    """Returns a single FAKE profile."""
    API_RESPONSE['data'] = fake.profile()
    return (API_RESPONSE)


@profile_router.get('/get_multiple_profiles/{cant}')
def get_multiple_profiles(cant: int):
    if (isinstance(cant, int) and cant > 0):
        API_RESPONSE['data'] = [fake.profile() for i in range(0, cant)]
    else:
        error = f'The quantity required:{cant}. The required amount must be an INTEGER greater than zero.'
        raise HTTPException(
            status_code=404,
            detail=error,
            headers={"X-Error": error},
        )
        API_RESPONSE['DATA'] = {"cant": cant}
    return (API_RESPONSE)


@profile_router.get('/get_simple_profile_by_gender/{gender}')
def get_simple_profile_by_gender(gender: str):
    """Returns a simple profile with the gender specified values. M / F"""
    if(len(gender)==1 and gender.istitle and gender in ['M','F']):
        API_RESPONSE['data'] = fake.simple_profile(sex=gender) 
    else:
        error = f'Gender must be a single capital letter. Only options M / F.'
        raise HTTPException(
            status_code=404,
            detail=error,
            headers={"X-Error": error},
        )
        API_RESPONSE['DATA'] = {"cant": cant}

    return (API_RESPONSE)

@profile_router.get('/get_job_title')
def get_job_title():
    """Returns a simple job title."""
    API_RESPONSE['data'] = fake.job() 

    return (API_RESPONSE)


@profile_router.get('/get_multiple_job_titles/{cant}')
def get_multiple_job_titles(cant:int):
    """Returns multiple job titles."""
    if(isinstance(cant,int) and cant>0):
        API_RESPONSE['data'] = [fake.job() for i in range(0,cant)]
    else:
        error = f'cant must be an Integer greather than Zero.'


        raise HTTPException(
            status_code=404,
            detail=error,
            headers={"X-Error": error},
        )
    return (API_RESPONSE)




#  first_name() → str
#  first_name_female() → str
#  first_name_male() → str
#  first_name_nonbinary() → str
#  language_name() → str
#  last_name() → str
#  last_name_female() → str
#  last_name_male() → str
#  last_name_nonbinary() → str
#  name() → str
#  name_female() → str
#  name_male() → str
#  name_nonbinary() → str
#  prefix() → str
#  prefix_female() → str
#  prefix_male() → str
#  prefix_nonbinary() → str
#  suffix() → str
#  suffix_female() → str
#  suffix_male() → str
#  suffix_nonbinary() → str
