from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class ComplexTests(TranspileTestCase):
    def test_conjugate(self):
        self.assertCodeExecution("""
            x = complex(1.5, 1)
            print(x.conjugate())
            """)

    def test_real_imag(self):
        self.assertCodeExecution("""
            x = complex(1, 2.0)
            print(x.real)
            print(x.imag)
            """)

    def test_equality_with_numbers_when_zero_imag(self):
        self.assertCodeExecution("""
            x = 2
            y = complex(2, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))

            x = 2.0
            y = complex(3, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))

            x = True
            y = complex(1, 0)
            print(x == y)
            print(y.__eq__(x))
            print(x != y)
            print(y.__ne__(x))
            """)


class UnaryComplexOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'complex'

    not_implemented = [
        'test_unary_not'
    ]


class BinaryComplexOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'complex'

    substitutions = {
        "(-161.18751321137705+195.77962956590406j)": [
            "(-161.18751321137705+195.77962956590403j)"
        ],
        "(2.6460893340172016e-18+0.04321391826377225j)": [
            "(2.6460019439688186e-18+0.04321391826377225j)"
        ],
        "(-9.8368221286278e-14-535.4916555247646j)": [
            "(-9.836497256617357e-14-535.4916555247646j)"
        ]
    }

    not_implemented = [
        'test_eq_class',
        'test_ge_class',
        'test_gt_class',
        'test_le_class',
        'test_lt_class',
        'test_ne_class',
    ]


class InplaceComplexOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'complex'

    not_implemented = [
        'test_add_bool',
        'test_add_complex',
        'test_add_float',
        'test_add_int',

        'test_floor_divide_None',
        'test_floor_divide_NotImplemented',
        'test_floor_divide_slice',
        'test_floor_divide_range',
        'test_floor_divide_bool',
        'test_floor_divide_bytearray',
        'test_floor_divide_bytes',
        'test_floor_divide_class',
        'test_floor_divide_dict',
        'test_floor_divide_float',
        'test_floor_divide_frozenset',
        'test_floor_divide_int',
        'test_floor_divide_list',
        'test_floor_divide_none',
        'test_floor_divide_set',
        'test_floor_divide_str',
        'test_floor_divide_tuple',

        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_slice',
        'test_modulo_range',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_none',
        'test_modulo_set',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_bool',
        'test_multiply_bytearray',
        'test_multiply_bytes',
        'test_multiply_complex',
        'test_multiply_float',
        'test_multiply_int',
        'test_multiply_list',
        'test_multiply_none',
        'test_multiply_str',
        'test_multiply_tuple',

        'test_or_class',
        'test_or_frozenset',

        'test_power_bool',
        'test_power_complex',
        'test_power_float',
        'test_power_int',

        'test_subtract_bool',
        'test_subtract_complex',
        'test_subtract_float',
        'test_subtract_int',

        'test_true_divide_bool',
        'test_true_divide_complex',
        'test_true_divide_float',
        'test_true_divide_int',
    ]
