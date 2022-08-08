# django_cstomuser
## _DRY - No need to create new user app from scratch_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Features:
- ##### Model
- ##### Registration/Login/Logout
- ##### Urls
```sh
 git clone --depth 1 https://www.github.com/moriire/django_customuser
```
```sh
 cd django_customuser
```
## Well documented and easy to use for beginners
Open models.py

```sh
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from .base import CustomBaseUser

class CustomUser(CustomBaseUser):
    pass # Leave this way if you require normal django auth data
    """
    Other models methods:
    - CharField
    - IntegerField
    - BooleanField
    - ImageField
    - DateTimeField
    
    """
    
```
