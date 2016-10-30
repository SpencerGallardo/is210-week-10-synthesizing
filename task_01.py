#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 10 Task 1"""

import pprint


def sum_orders(customers, orders):
    """Combine two dictionaries into one.
    Args:
        Customers (dict): A dictionary of customers keyed by customer_id.
        Orders (dict): A dictionary of orders keyed by order id.
    Returns:
        A dictionary containing the combined data of name, email, orders, and
        total as a nested dictionary.
    Example:
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Person One',
             'email': 'email@one.com',
             'orders': 2,
             'total': 20}
         3: {'name': 'Person Two',
             'email': 'email@two.com',
             'orders': 1,
             'total': 15}}
    """
    cust_sum = {}
    order_tot = {}
    for value in orders.itervalues():
         customerkey = value['customer_id']
         cust_tot = {value['customer_id']: value['total']}
         if value['customer_id'] in order_tot:
             value['total'] += value['total']
         else:
             order_tot.update(cust_tot)
         for key, values in customers.iteritems():
             if key is customerkey:
                 cust_match = {customerkey: values}
                 cust_match.update(cust_tot)
         cust_sum.update(cust_match)
    pprint.pprint(cust_sum)
