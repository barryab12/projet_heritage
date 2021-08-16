# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TaskInheritProject(models.Model):
    _inherit = "project.task"

    nom = fields.Char(string='Nom')
    buy = fields.Boolean(string='Achat')
