# Placeholder API

A small application for testing only. It works like "[json-placeholder](https://jsonplaceholder.typicode.com/)" but locally.
You can use this project to lean new js frameworks o stuff like that.

## Stack Used

  - [docker-compose](https://docs.docker.com/compose/)
  - [FastApi](https://fastapi.tiangolo.com/)
  - [Faker](https://faker.readthedocs.io/en/master/)

## What do you get?

A set of endpoins to use in your test projects. You simply make a request and get some json data in return.

### Profiles

User profile related endpoins.

| method | endpoins  | description |
| --------------| ------------ | ------------- |
|GET |   /profile/get_profile|  Returns a json object with a series of attributes for a ***"basic user profile"***.|
|GET |  /profile/get_multiple_profiles/{cant}|Returns an amount N of "basic user profiles".|
|GET |  /profile/get_simple_profile_by_gender/{gender}|Returns A "basic user profile" with a specific gender. They can be ***M*** or ***F***.|
|GET  |  /profile/get_job_title|Returns a random profession.|
|GET |  /profile/get_multiple_job_titles/{cant}|Returns an amount ***N*** of random professions.|

### Utilities

Endpoints related to general topics.

| method | endpoins  | description |
| --------------| ------------ | ------------- |
|GET  | /utilities/validate_email/{email}|It allows to validate if an email is valid or not. Returns "***VALID EMAIL***" or "***INVALID EMAIL***".|
## How to Run this.
  
First you need to clone this project.

```
git clone https://github.com/TorrezMN/PlaceHolder_FA.git
```

then go in to "PlaceHolderApi"

```
cd PlaceHolder_FA/
```

then run the project with docker-compose:

```
sudo docker-compose up
```

go to your  [web browser](http://0.0.0.0:8000/docs) and enjoy.

```
http://0.0.0.0:8000/docs
```
