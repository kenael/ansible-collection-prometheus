#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) 2022-2023, Bodo Schulz <bodo@boone-schulz.de>

from __future__ import absolute_import, division, print_function

import requests


class Alertmanager():
    """
    """
    module = None

    def __init__(self, module):
        """
        """
        self.module = module

        self.state = module.params.get("state")
        self.verbose = module.params.get("verbose")
        self.url = module.params.get("url")

    def status(self):
        """
        """
        path = "api/v2/status"

        code, status = self.__call_url(
            method='GET',
            path=path
        )

        return code, status

    def silences(self):
        """
        """
        path = "api/v2/silences"

        code, status = self.__call_url(
            method='GET',
            path=path,
        )

        return code, status

    def silence(self, payload=None):
        """
        """
        path = "api/v2/silences"

        if not payload:
            method = 'GET'
        else:
            method = 'POST'

        code, status = self.__call_url(
            method=method,
            path=path,
            data=payload,
        )

        return code, status

    def delete_silence(self, silence_id):
        """
        """
        path = f"api/v2/silence/{silence_id}"

        code, status = self.__call_url(
            method="DELETE",
            path=path
        )

        return code, status

    def __call_url(self, method='GET', path=None, data=None, headers=None):
        """
        """
        if headers is None:
            headers = {'Accept': 'application/json'}

        url = f"{self.url}/{path}"

        try:
            if method == 'GET':
                ret = requests.get(
                    url,
                    verify=False
                )
                ret.raise_for_status()

            elif method == 'POST':
                ret = requests.post(
                    url,
                    json=data,
                    verify=False
                )

                ret.raise_for_status()

            elif method == "DELETE":
                ret = requests.delete(
                    url,
                    verify=False
                )

                ret.raise_for_status()

            else:
                self.module.log(msg=f"unsupported: {method}")

                return 500, f"Unsupported method '{method}'"

            # ret.raise_for_status()
            # self.module.log(msg="------------------------------------------------------------------")
            # self.module.log(msg=f" text    : {type(ret.text)} / {ret.text}")
            # self.module.log(msg=f" headers : {type(ret.headers)} / {ret.headers}")
            # self.module.log(msg=f" code    : {type(ret.status_code)} / {ret.status_code}")
            # self.module.log(msg="------------------------------------------------------------------")

            return ret.status_code, ret.text  # json.loads(ret.text)

        except Exception as e:
            self.module.log(msg=f"{str(e)}")

            return 500, str(e)
