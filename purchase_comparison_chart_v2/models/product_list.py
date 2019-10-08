from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductListMods(models.Model):
    _inherit = 'product.list'

    categoria_id = fields.Many2one(
        'product.category',
        string="Contrato (estimación)",
        domain=[('x_contrato', '=', True)],
    )

    productos_a  = fields.Many2one("product.product", string="User", domain="[]")

    @api.onchange('categoria_id')
    @api.model
    def change_categoria(self):
        print("Cambiando",self.categoria_id.id)
        categorias = self.env['product.category'].search([('id', '=', self.categoria_id.id)])
        prod_list=[]
        for categoria in categorias:
            prod_list.append(categoria.id)
        
        lista=[1,2,3]
        print(prod_list)
        print(lista)
        return {'domain': {'productos_a': [('categ_id', 'in', prod_list)]}}
        #return {'domain': {'product': [('categ_id', 'in', prod_list)]}}


""" class ProductListLineasMods(models.Model):
    _inherit = 'product.list.line'

    product = fields.Many2one(
        'product.category',
        string="Contrato (estimación)",
        domain=[('x_contrato', '=', True)],
    ) """
