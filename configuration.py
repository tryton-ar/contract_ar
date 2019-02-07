# This file is part of the contract_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelSQL, fields
from trytond.model import ValueMixin
from trytond.pool import PoolMeta
from trytond import backend
from trytond.tools.multivalue import migrate_property

__all__ = ['Configuration', 'ConfigurationPos']

pos = fields.Many2One('account.pos', 'Point Of Sales',
    help="The default point of sales for new invoices.")


class Configuration:
    __name__ = 'contract.configuration'
    __metaclass__ = PoolMeta

    pos = fields.MultiValue(pos)


class _ConfigurationValue(ModelSQL):

    _configuration_value_field = None

    @classmethod
    def __register__(cls, module_name):
        TableHandler = backend.get('TableHandler')
        exist = TableHandler.table_exist(cls._table)

        super(_ConfigurationValue, cls).__register__(module_name)

        if not exist:
            cls._migrate_property([], [], [])

    @classmethod
    def _migrate_property(cls, field_names, value_names, fields):
        field_names.append(cls._configuration_value_field)
        value_names.append(cls._configuration_value_field)
        migrate_property(
            'contract.configuration', field_names, cls, value_names,
            fields=fields)


class ConfigurationPos(_ConfigurationValue, ModelSQL, ValueMixin):
    'Contract Configuration Pos'
    __name__ = 'contract.configuration.pos'
    pos = pos
    _configuration_value_field = 'pos'
