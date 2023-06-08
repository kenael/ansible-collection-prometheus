# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.utils.display import Display

import datetime
import dateutil.parser
import time
import sys

display = Display()


class FilterModule(object):
    """
    """
    def filters(self):
        return {
            "expired": self.expired,
            "current_datetime": self.current_datetime,
        }

    def current_datetime(self, data, add_time):
        """
        """
        add_minutes = add_time.get("minutes", 10)
        add_hours = add_time.get("hours", 0)

        current_time = time.time()
        end_time = current_time + add_minutes
        current_date_time = datetime.datetime.utcfromtimestamp(current_time).isoformat()
        end_date_time = datetime.datetime.utcfromtimestamp(end_time).isoformat()

        return dict(
            begin = current_date_time,
            end = end_date_time
        )

    def expired(self, data):
        """
        """
        result = []

        if isinstance(data, list):
            for i in data:
                _id = i.get("id")
                _state = i.get("status", {}).get("state", None)

                if _state == "expired":
                    result.append(_id)

        return result
