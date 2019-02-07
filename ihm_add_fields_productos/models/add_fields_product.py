# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

import smtplib

class AddProductFields(models.Model):
    _inherit = 'product.template'
    
    #FUNCION PARA CALCULO DE ELEMENTOS
#    @api.one
#    @api.depends('invoice_line_ids.price_subtotal')
#    def _compute_total_elementos(self):
#        self.importe_total_elementos = sum(line.importe for line in self.x_asignacion_ids)

    @api.onchange('estatus') #Validaciones, si algún miembro no tiene correo, si hay servidores configurados
    def _envia_correos(self):
        print("Ejecutando enviar")
        if self.estatus=="Escriturado":
            print("El inmueble es escriturado, enviando correo...")
            
            servidor_salida=self.env['ir.mail_server'].search([], limit=1)
            
            proyecto = self.env['project.project'].search([('id', '=', self.x_proyecto_id.id)], limit=1)
            if not proyecto:
                print("Producto sin proyecto asignado")
            for miembros in proyecto.equipo_entrega:
                sender = servidor_salida.smtp_user
                #sender = 'drc@soluciones4g.com'
                receivers = miembros.email
                message = "Estimado(a) "+miembros.name+", el inmueble "+self.name+" ha cambiado su estatus a Escriturado"
                smtpObj = smtplib.SMTP(host=servidor_salida.smtp_host, port=servidor_salida.smtp_port)
                #smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.ehlo()
                smtpObj.login(user=servidor_salida.smtp_user, password=servidor_salida.smtp_pass)
                #smtpObj.login(user="drc@soluciones4g.com", password="S3nsusveri5")
                smtpObj.sendmail(sender, receivers, message)
            print ("Correo enviado")
        
    @api.one
    @api.depends('x_asignacion_ids.importe')
    def _compute_total_elementos(self):
        self.importe_total_elementos = sum(line.importe for line in self.x_asignacion_ids)
        
    @api.one
    def asignar_precio_inmueble(self):
        precio_calculado = float(self.importe_total_elementos)
        self.write({'list_price': precio_calculado})
    
    #Para relacionar los inmuebles de tipo "bien adicional" con un inmueble "normal"
    _parent_store = True
    parent_id     = fields.Many2one('product.template', string="Inmueble relacionado")
    parent_left   = fields.Integer('Parent Left', index=True)
    parent_right  = fields.Integer('Parent  Right', index=True)
    #child_ids = fields.One2many('product.tempĺate', 'parent_id')
    
    #características para los productos que son inmuebles y su proyecto relacionado
    es_inmueble = fields.Boolean(string="Es un inmueble")
    es_bien_adicional = fields.Boolean(string="Es un bien adicional")
    tipo_bien_adicional = fields.Selection(
                                           selection=[
                                           ('Cajon de Estacionamiento', 'Cajón de Estacionamiento'),
                                           ('Bodega', 'Bodega'),
                                           ],
                                           string="Tipo de bien adicional",
                                           default='Bodega',
                                           )
    caracteristicas = fields.Text(string="Características")
    numero = fields.Char(string="Número")
    estatus = fields.Selection(
                               selection=[
                               ('Disponible', 'Disponible'),
                               ('Apartado', 'Apartado'),
                               ('Vendido', 'Vendido'),
                               ('Escriturado', 'Escriturado'),
                               ('En Preparación', 'En preparación'),
                               ('Liberado', 'Liberado'),
                               ('Entregado', 'Entregado'),
                               ],
                               string="Estatus"
                               )
    x_proyecto_id = fields.Many2one('project.project', string='Proyecto')
    
    x_asignacion_ids = fields.One2many(
                                       'asignacion.elementos', #modelo al que se hace referencia
                                       'inmueble_id', #un campo de regreso
                                       string="Asignacion elementos"
                                       )
                                       
#CAMPO PARA EL CALCULO DE TOTAL DE LOS ELEMENTOS
    importe_total_elementos = fields.Float(string='Importe total elementos',
                                           #store=True, 
                                           readonly=True, 
                                           compute='_compute_total_elementos',
                                           )
        
    oportunidades_ids = fields.One2many(
                                        'crm.lead', #modelo al que se hace referencia
                                        'id_producto_inmueble', #un campo de regreso
                                        string="Oportunidad"
                                        )#
                                        
    cantidad_enganche = fields.Float(
                                     string="Cantidad Enganche"
                                     )
    garantia_id = fields.Many2one(
                                  'tipo.garantia',
                                  string="Tipo de garantia"
                                  )

#https://fundamentos-de-desarrollo-en-odoo.readthedocs.io/es/latest/capitulos/modelos-estructura-datos-aplicacion.html