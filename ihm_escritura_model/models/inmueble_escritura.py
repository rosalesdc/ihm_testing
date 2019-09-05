# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import UserError, ValidationError
import re

import smtplib

class InmuebleEscritura(models.Model):
    _name = 'inmueble.escritura'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Número de Escritura")
    notaria = fields.Char(string="Notaría")
    fecha = fields.Datetime(
                            string="Fecha de Escritura"
                            )
    id_notaria = fields.Many2one(
                                string="Notaría ID"
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
                receivers=""
                sender = servidor_salida.smtp_user
                receivers = miembros.email
                if receivers != False:
                    print("receiver registrado: "+receivers)
                    receivers = receivers.encode('ascii', 'ignore').decode('ascii')
                    print("receiver codificado: "+receivers)
                    if (re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',receivers.lower())):
                        print ("Correo correcto validado con expresion "+receivers)
                        message = "Estimado(a) "+miembros.name+", el inmueble "+prod_inmueble.name+" ha sido escriturado, por favor, tome las acciones necesarias correspondientes para liberar dicho inmueble, muchas gracias.\n"+listado_proyectos
                        message = message.encode('ascii', 'ignore').decode('ascii')
                        #message = "Estimado, inmueble escriturado"
                        smtpObj = smtplib.SMTP(host=servidor_salida.smtp_host, port=servidor_salida.smtp_port)
                        print("paso1")
                        smtpObj.ehlo()
                        print("paso2")
                        smtpObj.starttls()
                        print("paso3")
                        smtpObj.ehlo()
                        print("paso4")
                        smtpObj.login(user=servidor_salida.smtp_user, password=servidor_salida.smtp_pass)
                        print("paso5")
                        smtpObj.sendmail(sender, receivers, message)
                        print ("Correo enviado")
                    else:
                        print ("Correo incorrecto")


    @api.model
    def create(self, vals):
        #CAMBIA EL ESTATUS DEL INMUEBLE A ESCRITURADO
        print("CREATING VALUES:::::::::::::::::::::::::")
        num_lineas=0
        escritura = super(InmuebleEscritura, self).create(vals)
        #oportunidad = self.env['crm.lead'].search([('id_numero_referencia.name', '=', escritura.orden_venta_id.id_numero_referencia.name)], limit=1)

        so=self.env['sale.order'].search([('id_numero_referencia.name', '=', escritura.orden_venta_id.id_numero_referencia.name)], limit=1)

        #producto_inmueble = self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)

        ##Checar el saldo del cliente en la liquidación debe ser 0 o menor a 0
        if so.saldo_cliente>0:
            raise ValidationError('El saldo del cliente en la liquidación debe ser 0 o menor a 0 ')

        print("Verificar si se puede escriturar")
        for lines in so.order_line:
            num_lineas+=1;
            print(lines.product_id.estatus)
            if lines.product_id.estatus == "Vendido":
                #print("Cambiando -- Vendido")
                lines.product_id.write({'estatus': 'Escriturado'})
                self._envia_correos(lines.product_id)
                #print("Inmueble Escriturado")
            else:
                raise ValidationError('Producto(s) no en estatus Vendido ')
        if num_lineas==0:
            raise ValidationError('No hay lineas en la orden')
#        if producto_inmueble.estatus == "Vendido":
#            producto_inmueble.estatus="Escriturado"
#            self._envia_correos(producto_inmueble)
#        else:
#            raise ValidationError('El producto no estaba en estatus: Vendido'+producto_inmueble.name)

        
        so.escritura=escritura.name
###COPIA EL NOMBRE DE LA ESCRITURA A LA SO
        so.x_fecha_escritura=escritura.fecha
        #print (escritura.name)
        entrega=self.env['stock.picking'].search([('sale_id', '=', so.id)], limit=1)
        entrega.estado_id=1 #ESCRITRUADO


        return escritura
