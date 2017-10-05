# This file is part of the contract_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool, PoolMeta

__all__ = ['ContractConsumption']


class ContractConsumption:
    __name__ = 'contract.consumption'
    __metaclass__ = PoolMeta

    @classmethod
    def __setup__(cls):
        super(ContractConsumption, cls).__setup__()
        cls._error_messages.update({
                'missing_pos': ('Please, configure a point of sale before '
                    'creating contract invoices.'),
                })

    @classmethod
    def _invoice(cls, consumptions):
        invoices = super(ContractConsumption, cls)._invoice(consumptions)
        start_dates = []
        end_dates = []
        for invoice in invoices:
            invoice.set_pyafipws_concept()
            if invoice.pyafipws_concept in ['2', '3']:
                for line in invoice.lines:
                    start_dates.append(line.origin.start_date)
                    end_dates.append(line.origin.end_date)
                invoice.pyafipws_billing_start_date = start_dates[0]
                invoice.pyafipws_billing_end_date = end_dates[-1]
            invoice.save()
        return invoices

    @classmethod
    def _get_invoice(cls, keys):
        invoice = super(ContractConsumption, cls)._get_invoice(keys)
        Config = Pool().get('contract.configuration')
        pos = Config(1).pos
        if not pos:
            cls.raise_user_error('missing_pos')

        if invoice.pos is None:
            invoice.pos = pos
        invoice._set_invoice_type_sequence()
        return invoice
