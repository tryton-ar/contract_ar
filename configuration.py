# This file is part of the contract_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Configuration']


class Configuration:
    __name__ = 'contract.configuration'
    __metaclass__ = PoolMeta

    pos = fields.Property(fields.Many2One('account.pos',
            'Point of sale', required=True, help='The point of sale to be '
            'used when the invoice is created.'))
