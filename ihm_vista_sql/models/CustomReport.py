
#from odoo import tools
from odoo import tools
from odoo import models, fields, api

class CustomReport(models.Model):
    _name = "my.report"
    _description = "my report"
    _auto = False

    name = fields.Integer(string='Nombre', readonly=True)
    name_product = fields.Char(string="Nombre Producto")
    name_crm = fields.Char(string='Nombre Oportunidad', readonly=True)
    
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW my_report as  
                        SELECT product_template.id, crm_lead.id as name, crm_lead.name as name_crm, product_template.name as name_product 
                        FROM crm_lead
                        FULL OUTER JOIN product_template
                        ON crm_lead.id_producto_inmueble=product_template.id
                        WHERE product_template.es_inmueble=TRUE AND product_template.es_bien_adicional=FALSE;
                        """)
        #result = self._cr.dictfetchall() # return the data into the list of dictionary format
        print("finalizando")

        
#    def primeraok(self):
#        tools.drop_view_if_exists(self._cr, self._table)
#        self._cr.execute("""CREATE or REPLACE VIEW my_report as  
#                        SELECT purchase_order.id, purchase_order.name as name,res_partner.name as partner_name
#                        FROM purchase_order 
#                        INNER JOIN res_partner 
#                        ON purchase_order.partner_id=res_partner.id;
                        #""")

