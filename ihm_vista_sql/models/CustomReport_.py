
#from odoo import tools
from odoo import tools
from odoo import models, fields, api

class CustomReport(models.Model):
    _name = "my.report"
    _description = "my report"
    _auto = False

    name = fields.Integer(string='ID', readonly=True,default=0)
    nombre_inmueble = fields.Char(string="Nombre Inmueble", default="-")
    estatus = fields.Char(string="Estatus", default="-")
    precio = fields.Char(string='Precio SO', readonly=True, default="-")
    oportunidad = fields.Char(string='Oportunidad', readonly=True, default="-")
    tipo_credito = fields.Char(string='Tipo de credito', readonly=True, default="-")
    cantidad_cbancario = fields.Char(string='Cantidad C Bancario', readonly=True, default="-")
    cantidad_infornativ = fields.Char(string='Cantidad C Infonavit', readonly=True, default="-")
    cliente = fields.Char(string='Cliente', readonly=True, default="-") 
    orden = fields.Char(string='Orden', readonly=True, default="-")
    referencia_fecha = fields.Char(string='Referencia Fecha', readonly=True, default="-")
    referencia = fields.Char(string='Referencia', readonly=True, default="-")
    asesor = fields.Char(string='Asesor', readonly=True, default="-")
    entidad_financiera = fields.Char(string='Entidad Financiera', readonly=True, default="-")
    elementos_de_orden = fields.Char(string='Elementos en la Orden', readonly=True, default="-")
    proyecto = fields.Char(string='Proyecto', readonly=True, default="-")
    autorizacion_i_financera = fields.Char(string='Aut. I Financiera', readonly=True, default="-")
    autorizacion_avaluo = fields.Char(string='Aut. Avaluo', readonly=True, default="-")
    instruccion_i_financiera = fields.Char(string='Inst. I Financiera', readonly=True, default="-")
    escritura = fields.Char(string='Escritura', readonly=True, default="-")
    notaria = fields.Char(string='Notaría', readonly=True, default="-")
    fecha_escritura = fields.Char(string='Fecha Escritura', readonly=True, default="-")
    avaluo_fiscal=fields.Char(string='Avalúo Fiscal', readonly=True, default="-")
    ingreso_i_financiera=fields.Char(string='Ingreso I Financiera', readonly=True, default="-")
    fecha_completo=fields.Char(string='Expediente completo', readonly=True, default="-")
    categoria=fields.Char(string='Categoria', readonly=True, default="-")
    
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""CREATE or REPLACE VIEW my_report as  
                SELECT ROW_NUMBER() OVER (ORDER BY product_template.name) as id,
		product_template.id as name,
		product_template.name as nombre_inmueble,
                product_template.estatus as estatusx,
		
		crm_lead.name as oportunidad,
		res_partner.name as cliente, 
                sale_order.name as orden, 
		sale_order.tipo_credito as tipo_credito,
		sale_order.expediente_autorizacion_ifinanciera as autorizacion_i_financera,
		sale_order.expediente_avaluo as autorizacion_avaluo,
		sale_order.expediente_instruccion_ifinanciera as instruccion_i_financiera,
                sale_order.expediente_ingreso_ifinanciera as ingreso_i_financiera,
                sale_order.avaluo_fiscal as avaluo_fiscal,
                sale_order.expediente_fecha_completo as fecha_completo,
                crm_lead.fecha_entrega_referencia as referencia_fecha,
		numero_referencia.name as referencia,
		sale_order.nombre_asesor as asesor, 
		sale_order.amount_total as precio,
                
		res_bank.name as entidad_financiera,
		sale_order.cantidad_pagar_cbancario as cantidad_cbancario,
		sale_order.cantidad_pagar_infonavitfov as cantidad_infornativ,
                sale_order.productos_reporte as elementos_de_orden,
		project_project.name as proyecto,
                inmueble_escritura.name as escritura,
		inmueble_escritura.notaria as notaria,
		inmueble_escritura.fecha as fecha_escritura,
                product_category.name as categoria,
                
                CASE
                    WHEN (estatus = 'Disponible') THEN 'Disponible'
                    WHEN (estatus = 'Apartado') THEN 'Apartado'
                    WHEN (estatus = 'Vendido') THEN 'Vendido'
                    WHEN (estatus = 'Escriturado') THEN 'Escriturado'
                    WHEN (estatus = 'Preparacion') THEN 'Liberado'
                    WHEN (estatus = 'Entregado') THEN 'Entregado'
                    ELSE 'no especificado'
                    END AS estatus
		
		
    FROM product_template  
    FULL OUTER JOIN crm_lead ON product_template.id=crm_lead.id_producto_inmueble 
	FULL OUTER JOIN sale_order ON product_template.sale_order=sale_order.id
        FULL OUTER JOIN product_category ON product_template.categ_id=product_category.id 
	FULL OUTER JOIN res_partner ON res_partner.id=crm_lead.partner_id
	FULL OUTER JOIN numero_referencia ON sale_order.id_numero_referencia=numero_referencia.id
	FULL OUTER JOIN res_bank ON sale_order.id_entidad_financiera=res_bank.id
	FULL OUTER JOIN project_project ON product_template.x_proyecto_id=project_project.id 
    FULL OUTER JOIN inmueble_escritura ON sale_order.id=inmueble_escritura.orden_venta_id
	
    WHERE product_template.es_inmueble=TRUE AND product_category.name='DEPARTAMENTOS';
                        ;
                        """)
        print("finalizando")

#result = self._cr.dictfetchall() # return the data into the list of dictionary format
#    def primeraok(self):
#        tools.drop_view_if_exists(self._cr, self._table)
#        self._cr.execute("""CREATE or REPLACE VIEW my_report as  
#                        SELECT purchase_order.id, purchase_order.name as name,res_partner.name as partner_name
#                        FROM purchase_order 
#                        INNER JOIN res_partner 
#                        ON purchase_order.partner_id=res_partner.id;
                        #""")

