from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductListMods(models.Model):
    _inherit = 'product.list'

    @api.multi
    def write(self, vals):
        lista=super(ProductListMods, self).write(vals)
        if self.categoria_id:
            for producto in self.product_list_ids:
                if producto.product.categ_id != self.categoria_id:
                    raise UserError('Productos seleccionados no corresponden al contrato')
        return lista
    
    @api.model
    def create(self, vals):
        lista=super(ProductListMods, self).create(vals)
        if self.categoria_id:
            for producto in lista.product_list_ids:
                if producto.product.categ_id != lista.categoria_id:
                    raise UserError('Productos seleccionados no corresponden al contrato')
        return lista
 
    categoria_id = fields.Many2one(
        'product.category',
        string="Contrato (estimación)",
        domain=[('x_contrato', '=', True)],
    )


""" Se creó esto para la generación del dominio de forma dinámica, 
pero no funciona para el campo que está dentro del modelo de las líneas
en el campo productos_a sí lo hace correctamente
    productos_a  = fields.Many2one("product.product", string="User", domain="[]")

    @api.onchange('categoria_id')
    @api.model
    def change_categoria(self):
        print("Cambiando",self.categoria_id.id)
        categorias = self.env['product.category'].search([('id', '=', self.categoria_id.id)])
        prod_list=[]
        for categoria in categorias:
            prod_list.append(categoria.id)
        print(prod_list)
        return {'domain': {'productos_a': [('categ_id', 'in', prod_list)]}}
 """
