from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class IdTests(TranspileTestCase):
    pass


class BuiltinIdFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["id"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_set',
        'test_str',
        'test_tuple',
    ]
