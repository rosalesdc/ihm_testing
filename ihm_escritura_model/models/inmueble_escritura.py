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
    
    def _envia_correos(self,prod_inmueble): #Validaciones, si algún miembro no tiene correo, si hay servidores configurados
        print("Ejecutando enviar")
        if prod_inmueble.estatus=="Escriturado":
            #print("El inmueble es escriturado, enviando correo...")
            
            servidor_salida=self.env['ir.mail_server'].search([], limit=1)
            
            #obtener el proyecto para llamar al equipo de entrega
            proyecto = self.env['project.project'].search([('id', '=', prod_inmueble.x_proyecto_id.id)], limit=1)
            
            #obtener todos los productos del proyecto
            inmuebles_escriturados=self.env['product.template'].search([('x_proyecto_id.id', '=', proyecto.id),(('estatus', '=', "Escriturado"))])
            listado_proyectos="--- Listado de inmuebles escriturados en: "+proyecto.name+" ---\n"
            for inmuebles in inmuebles_escriturados:
                listado_proyectos += (inmuebles.name+"\n")
            #print(listado_proyectos)
            
            if not proyecto:
                print("Producto sin proyecto asignado")
            for miembros in proyecto.equipo_entrega:
                sender = servidor_salida.smtp_user
                receivers = miembros.email
                message = "Estimado(a) "+miembros.name+", el inmueble "+prod_inmueble.name+" ha cambiado su estatus a Escriturado \n"+listado_proyectos
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
        oportunidad = self.env['crm.lead'].search([('id_numero_referencia.name', '=', escritura.orden_venta_id.id_numero_referencia.name)], limit=1)
        producto_inmueble = self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
        if producto_inmueble.estatus == "Vendido":
            producto_inmueble.estatus="Escriturado"
            self._envia_correos(producto_inmueble)
        else:
            raise ValidationError('El producto no estaba en estatus: Vendido'+producto_inmueble.name)
        return escritura
        
