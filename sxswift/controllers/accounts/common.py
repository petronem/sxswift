'''
Copyright (C) 2015-2016 Skylable Ltd. <info-copyright@skylable.com>
License: Apache 2.0, see LICENSE for more details.
'''

import bottle

from sxswift.http_helpers.validators import validate_api_version
from sxswift.lib.validators import account_name_is_valid


def _validate_account(api_ver, account):
    validate_api_version(api_ver)

    if not account_name_is_valid(account):
        msg = 'Account name %s is invalid' % account
        raise bottle.HTTPError(400, msg)
