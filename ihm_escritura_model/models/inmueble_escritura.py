# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import UserError, ValidationError

import smtplib

class InmuebleEscritura(models.Model): 
    _name = 'inmueble.escritura'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Número de Escritura")
    notaria = fields.Char(string="Notaría")
    fecha = fields.Datetime(
                            string="Fecha de Escritura"
                            )
    
    orden_venta_id = fields.Many2one(
                                     'sale.order',
                                     string="Orden"
                                     )
    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "En número de escritura debe ser único"),
        ]
    
    def _envia_correos(self,prod_inmueble): #Validaciones, si algún miembro no tiene correo, si hay servidores configurados
        print("Ejecutando enviar")
        if prod_inmueble.estatus=="Escriturado":
            #print("El inmueble es escriturado, enviando correo...")
            
            servidor_salida=self.env['ir.mail_server'].search([], limit=1)
            
            #obtener el proyecto para llamar al equipo de entrega
            proyecto = self.env['project.project'].search([('id', '=', prod_inmueble.x_proyecto_id.id)], limit=1)
            
            #obtener todos los productos del proyecto
            inmuebles_escriturados=self.env['product.product'].search([('x_proyecto_id.id', '=', proyecto.id),(('estatus', '=', "Escriturado"))])
            listado_proyectos="--- Listado de inmuebles escriturados en: "+proyecto.name+" ---\n"
            for inmuebles in inmuebles_escriturados:
                listado_proyectos += (inmuebles.name+"\n")
            #print(listado_proyectos)
            
            if not proyecto:
                print("Producto sin proyecto asignado")
            for miembros in proyecto.equipo_entrega:
                sender = servidor_salida.smtp_user
                receivers = miembros.email
                message = "Estimado(a) "+miembros.name+", el inmueble "+prod_inmueble.name+" ha sido escriturado, por favor, tome las acciones necesarias correspondientes para liberar dicho inmueble, muchas gracias.\n"+listado_proyectos
                smtpObj = smtplib.SMTP(host=servidor_salida.smtp_host, port=servidor_salida.smtp_port)
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.ehlo()
                smtpObj.login(user=servidor_salida.smtp_user, password=servidor_salida.smtp_pass)
                smtpObj.sendmail(sender, receivers, message)
            print ("Correo enviado")
    
    @api.model
    def create(self, vals):
        #CAMBIA EL ESTATUS DEL INMUEBLE A ESCRITURADO
        print("CREATING VALUES:::::::::::::::::::::::::")
        escritura = super(InmuebleEscritura, self).create(vals)
        #oportunidad = self.env['crm.lead'].search([('id_numero_referencia.name', '=', escritura.orden_venta_id.id_numero_referencia.name)], limit=1)
        
        so=self.env['sale.order'].search([('id_numero_referencia.name', '=', escritura.orden_venta_id.id_numero_referencia.name)], limit=1)
        
        #producto_inmueble = self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
        print("Verificar si se puede escriturar")
        for lines in so.order_line:
            print(lines.product_id.estatus)
            if lines.product_id.estatus == "Vendido":
                #print("Cambiando -- Vendido")
                lines.product_id.write({'estatus': 'Escriturado'})
                self._envia_correos(lines.product_id)
                #print("Inmueble Escriturado")
            else:
                raise ValidationError('Producto(s) no en estatus Vendido ')
#        if producto_inmueble.estatus == "Vendido":
#            producto_inmueble.estatus="Escriturado"
#            self._envia_correos(producto_inmueble)
#        else:
#            raise ValidationError('El producto no estaba en estatus: Vendido'+producto_inmueble.name)

###COPIA EL NOMBRE DE LA ESCRITURA A LA SO
        
        print (self.orden_venta_id.name)
            
        
        
        return escritura
        
