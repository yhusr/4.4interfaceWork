import re


class HandleRe:
    @classmethod
    def re_data(cls, re_args, data):

        if re.search(r'{no_exist_phone}', data):
            result = re.sub(r'{no_exist_phone}', re_args, data)
            return result
        else:
            return data
