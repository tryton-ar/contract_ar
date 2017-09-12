# This file is part of the contract_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import contract
from . import configuration


def register():
    Pool.register(
        contract.ContractConsumption,
        configuration.Configuration,
        module='contract_ar', type_='model')
