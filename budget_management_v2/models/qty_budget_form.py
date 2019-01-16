# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields,api,_

from odoo.exceptions import UserError, ValidationError

class QuantityBudget(models.Model):
    _name = 'qty.budget'
    _description = 'Quantity Budget'
    
    name = fields.Many2one("product.product",string="Product",required=True)
    category_id = fields.Many2one(related="name.categ_id",string="Category",store=True)
    qty = fields.Float("Quantity",required=True)
    uom_id = fields.Many2one("uom.uom",string="UOM",required=True)
    project_id = fields.Many2one("project.project",string="Project")
    cantidad_total=fields.Float(string="Presupuesto",default=0.0)
    executed = fields.Float(compute="_compute_values",string="Executed Qty")
    executed_cost = fields.Float(compute="_compute_values",string="Executed Amount")
    percentage_qty = fields.Float(compute="_compute_values",string="% Executed Qty")
    percentage_amt = fields.Float(compute="_compute_values",string="% Executed Amount")
    remaining_amt = fields.Float(compute="_compute_values",string="Remaining Amount")
    remaining_qty = fields.Float(compute="_compute_values",string="Remaining Qty")
    
    
    @api.multi
    @api.depends('name')
    def _compute_values(self):
        for line in self:
            qty_id = self.env['purchase.order.line'].search([
                ('product_id','=',line.name.id),
                ('order_id.x_cuenta_analitica_id','=',line.project_id.analytic_account_id.id),
                ('order_id.state','=','purchase')
            ])
            total = executed_cost=0.0
            for res in qty_id:
                if res.state == 'purchase':
                    total += res.product_qty
                    executed_cost += res.price_subtotal
            line.executed = total
            line.executed_cost = executed_cost

            if line.qty > 0 and total > 0:
                line.percentage_qty = (total / line.qty)*100
            else:
                line.percentage_qty = 0.0
                
            if line.cantidad_total > 0 and executed_cost > 0:
                line.percentage_amt = (executed_cost / line.cantidad_total)*100
            else:
                line.percentage_amt = 0.0
            
            line.remaining_amt = line.qty-line.executed
            line.remaining_qty = line.cantidad_total-line.executed_cost
            
    @api.model
    def create(self, vals):

        rec=super(QuantityBudget, self).create(vals)
        total=self.search_count([('name', '=', rec.name.id), ('project_id', '=', rec.project_id.id)])
        if total>1:
            raise ValidationError(_('Product Category should not be repeat!'))
        return rec
    
    @api.onchange('name')
    def _onchange_category(self):
            if self.name:
                self.category_id=self.name.categ_id.id
        
