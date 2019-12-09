from odoo import models, fields, api
from odoo.exceptions import UserError

class InmuebleAutomation(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def action_cancel(self):
        self.mapped('move_lines')._action_cancel()
        self.write({'is_locked': True})
        ############################################
        # Función para crear una instancia de inmuebles.helpdesk
        ############################################        
        inmueble = self.env['inmuebles.helpdesk'].search(['&',('product_id','=',self.product_id.id),('partner_id','=',self.partner_id.id)])
        inmueble.unlink()
        ############################################
        # Termina funcion para crear una instancia de inmuebles.helpdesk
        ############################################
        return True

    @api.multi
    def button_validate(self):        
        ############################################
        # Función para crear una instancia de inmuebles.helpdesk
        ############################################
        parent = super(InmuebleAutomation, self).button_validate()
        inmueble = self.env['inmuebles.helpdesk'] 
        data = {
                    'name':self.productos_related,
                    'partner_id':self.partner_id.id,
                    'product_id':self.product_id.id,
                    'picking_id':self.id,
                    'project_id':self.id_proyecto.id,
                }  
        inmueble.create(data)
        ############################################
        # Termina funcion para crear una instancia de inmuebles.helpdesk
        ############################################
        return parent
