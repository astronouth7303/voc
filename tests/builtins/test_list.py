from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class ListTests(TranspileTestCase):
    pass


class BuiltinListFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["list"]

    substitutions = {
        "[1, 2.3456, 'another']": [
            "[1, 'another', 2.3456]",
            "[2.3456, 1, 'another']",
            "[2.3456, 'another', 1]",
            "['another', 1, 2.3456]",
            "['another', 2.3456, 1]",
        ]
    }

    not_implemented = [
        'test_bytearray',
    ]
