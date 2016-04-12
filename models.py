# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Martin Kamundi'

doc = """
"""


class Constants(BaseConstants):
    name_in_url = 'mini'
    players_per_group = 3
    num_rounds = 1

    endowment = c(10)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    offer_amount = models.CurrencyField(
    	choices=currency_range(0, Constants.endowment, c(5)),
    	)
    punishment_amount = models.CurrencyField()

    def set_payoffs(self):
    	p1 = self.get_player_by_id(1)
    	p2 = self.get_player_by_id(2)
    	p3 = self.get_player_by_id(3)
    	p1.payoff = Constants.endowment - (self.offer_amount + (self.punishment_amount*2))
    	p2.payoff = Constants.endowment + self.offer_amount
    	p3.payoff = Constants.endowment - self.punishment_amount





class Player(BasePlayer):
    pass