# -*- coding: utf-8 -*-

#from odoo import tools
from odoo import tools
from odoo import models, fields, api

class ProjectMilestone(models.Model):
    _name = "project.milestone"
    _auto = False
    id = fields.Char(string='id')
    nombre = fields.Char(string='Nombre')
    rfc = fields.Char(string='Milestone')
 
    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'project_milestone')
        #tools.sql.drop_view_if_exists(self._cr, 'project_milestone')
        self._cr.execute("""
            CREATE OR REPLACE VIEW project_milestone AS (
                select color as id, name as nombre,vat as rfc from res_partner
            )""")
            
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            """
            CREATE OR REPLACE VIEW project_milestone AS (
                select color as id, name as nombre,vat as rfc from res_partner)
            """)
        
ProjectMilestone()