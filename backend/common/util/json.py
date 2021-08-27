import datetime
import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if obj is None:
            return None
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        elif isinstance(obj, set):
            return list(obj)
        elif isinstance(type(obj), type(datetime.datetime)):
            return str(obj)

        return json.JSONEncoder.default(self, obj)


def map_pynamo_item_to_python(item):
    if isinstance(item, list) or isinstance(item, set):
        sub_array = []
        for sub_item in item:
            sub_array.append(map_pynamo_item_to_python(sub_item))
        return sub_array
    elif hasattr(item, 'attribute_values'):
        sub_result = {}
        for k, v in item.attribute_values.items():
            sub_result[k] = map_pynamo_item_to_python(v)
        return sub_result

    return item


def dumps(content):
    return json.dumps(content, cls=ComplexEncoder)


def loads(s, decoder: json.JSONDecoder = None):
    return json.loads(s, cls=decoder)