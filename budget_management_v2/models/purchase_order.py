# -*- coding: utf-8 -*-

from odoo import fields, models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    product_list_id = fields.Many2one('product.list',string='Product List')
    
    @api.model
    def create(self, vals):
        # Override the original create function for the  model
        record = super(PurchaseOrder, self).create(vals)
        project_id = self.env['project.project'].search([('analytic_account_id','=',record.x_cuenta_analitica_id.id)])
        qty_rec_id = self.env['qty.budget'].search([('project_id','=',project_id.id)])
        if qty_rec_id:
            for line in record.order_line:
                rec_id = self.env['qty.budget'].search([('project_id','=',project_id.id),('name','=',line.product_id.id)])
                if not rec_id:
                    self.env['qty.budget'].create({
                        'name': line.product_id.id,
                        'category_id': line.product_id.categ_id.id,
                        'qty': line.product_qty,
                        'project_id' : project_id.id
        })
        else:
            for line in record.order_line:
                self.env['qty.budget'].create({
                    'name': line.product_id.id,
                    'category_id': line.product_id.categ_id.id,
                    'qty': line.product_qty,
                    'project_id' : project_id.id
        })
        return record

