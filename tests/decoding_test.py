"""Decodes toml and outputs it as tagged JSON"""

import datetime
import json
import sys
import math

# import toml_tools
import tomllib as toml_tools

if sys.version_info < (3,):
    _range = xrange  # noqa: F821
    iteritems = dict.iteritems
else:
    unicode = str
    _range = range
    basestring = str
    unichr = chr
    iteritems = dict.items
    long = int




def tag(value):
    if isinstance(value, dict):
        d = {}
        for k, v in iteritems(value):
            d[k] = tag(v)
        return d
    elif isinstance(value, list):
        return [tag(v) for v in value]
        a = []
        for v in value:
            a.append(tag(v))
        try:
            a[0]["value"]
        except KeyError:
            return a
        except IndexError:
            pass
        return {'type': 'array', 'value': a}
    elif isinstance(value, basestring):
        return {'type': 'string', 'value': value}
    elif isinstance(value, bool):
        return {'type': 'bool', 'value': str(value).lower()}
    elif isinstance(value, int):
        return {'type': 'integer', 'value': str(value)}
    elif isinstance(value, long):
        return {'type': 'integer', 'value': str(value)}
    elif isinstance(value, float):
        return {'type': 'float', 'value': repr(value)}
    elif isinstance(value, datetime.datetime):
        if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
            date_type_name = 'datetime-local'
        else:
            date_type_name = 'datetime'

        date_str = (value.isoformat() #timespec='milliseconds')
                               .replace('+00:00', 'Z'))

        if date_str.endswith('000'):
            date_str = date_str[:-3]
        if date_str.endswith('.000'):
            date_str = date_str[:-4]

        return {'type': date_type_name, 'value': date_str}
    elif isinstance(value, datetime.date):
        return {'type': 'date-local', 'value': value.isoformat()}
    elif isinstance(value, datetime.time):
        # datetime.time.strf time %f gives microsecond precision
        # toml-test only tests truncation to millisecond precision
        # time_str = value.strftime('%H:%M:%S.%f')[:-3]
        time_str = value.isoformat(timespec='milliseconds')
        if time_str.endswith('.000'):
            time_str = time_str[:-4]
        return {'type': 'time-local', 'value': time_str}
    assert False, 'Unknown type: %s' % type(value)


class FloatyMcFloatFace(float):
    def __eq__(self, x):
        # handles +inf and -inf too
        if math.isclose(x, self):
            return True
        if math.isnan(x) and math.isnan(self):
            return True
        return False



TAG_CONVERSIONS = {'string' : unicode,
                   'bool' : lambda x: x.lower() == 'true',
                   'integer' : int,
                   'float' : FloatyMcFloatFace,
                   'datetime-local' : datetime.datetime.fromisoformat,
                   'datetime' : datetime.datetime.fromisoformat,
                   'date-local': datetime.date.fromisoformat,
                   'time-local' : datetime.time.fromisoformat
                  }


def de_tag(val):
    if isinstance(val, str):
        print(f'{ord(val)=}')
        return str
    
    if isinstance(val, list):
        return [de_tag(item) for item in val]
    
    if isinstance(val, dict):
        if (len(val) == 2 and 'type' in val and 'value' in val):
            return TAG_CONVERSIONS[val['type']](val['value'])
        return {k: de_tag(v) for k, v in val.items()}
    
    raise TypeError('Unsupported type: %s for val: %s' % (type(val), val))



if __name__ == '__main__':
    tdata = toml_tools.loads(sys.stdin.read())
    tagged = tag(tdata)
    print(json.dumps(tagged))
