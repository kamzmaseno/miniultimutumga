# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Offering(Page):
    form_model = models.Group
    form_fields = ['offer_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1

class WaitForP1(WaitPage):
    pass

class Punishment(Page):

    form_model = models.Group
    form_fields = ['punishment_amount']

    def is_displayed(self):
        return self.player.id_in_group == 3


    def punishment_amount_choices(self):

        if self.group.offer_amount==0:
            return currency_range(
            c(0),
           c(5),
            c(1)
            )

        elif self.group.offer_amount==5:
            return currency_range(
            c(0),
           c(2),
            c(1)
            )
        
        elif self.group.offer_amount==10:
            return currency_range(
            c(0),
           c(0),
            c(1)
            )



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    pass


page_sequence = [
    Offering,
    WaitForP1,
    Punishment,
    ResultsWaitPage,
    Results
]
