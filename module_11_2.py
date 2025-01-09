import inspect


def introspection_info(obj):
    obj_type = type(obj)
    attributes = dir(obj)
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = inspect.getmodule(introspection_info)
    # словарь с информацией об объекте
    info = {
        'Тип объекта': obj_type,
        'Атрибуты объекта': attributes,
        'Методы объекта': methods,
        'Модуль': module,
    }
    return info

number_info = introspection_info(42)
print(number_info)
