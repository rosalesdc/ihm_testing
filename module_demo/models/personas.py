# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models

class Persona(models.Model): #paquete.clase
    _name = 'persona.main_data' #por convencion nombre significativo.loque se va a guardar, name siempre se ha de poner
    name = fields.Char(
                       string="Nombre de la persona", #es una etiqueta
                       required=True,
                       help="Esta es la ayuda para el nombre de la persona",
                       index=True,
                       )

    edad = fields.Integer(
                          string="Edad de la persona",
                          default=15,
                          required=True,
                          )
    es_casado = fields.Boolean(
                               string="Es casado?",
                               )
    datos_personales = fields.Html(
                                   string="Datos personales",
                                   )
    informacion_adicional = fields.Text(
                                        string="Información adicional"
                                        )
    foto = fields.Binary(
                         string="Foto",
                         help="Agregue la foto de la persona"
                         )
    sexo = fields.Selection(
                            selection=[
                            ('femenino', 'Femenino'),
                            ('masculino', 'Masculino'),
                            ('otro', 'Otro')
                            ],
                            string="Sexo",
                            required=True,
                            default="otro"
                            )

    grado_estudio_id = fields.Many2one(#campo para relacion
                                       'personas.grados_estudio', #nombre del modelo con el que se relaciona
                                       string="Grado máximo de estudios",
                                       required=True,
                                       )

    dominios_email_ids = fields.Many2many(
                                          'personas.nombre_cuentas_email',
                                          string="Dominios de correo"
                                          )

    autos_ids = fields.One2many(
                                'personas.autos', #modelo al que se hace referencia
                                'persona_id', #un campo de regreso
		string="Autos"
		)#