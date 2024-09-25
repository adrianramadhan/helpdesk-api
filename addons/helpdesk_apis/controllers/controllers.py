# -*- coding: utf-8 -*-
from odoo import http
from ..helpers.request import extract_fields_from_request, extract_multipart_fields
from ..helpers.response import response_json
from odoo.http import request


class HelpdeskApis(http.Controller):
    @http.route('/helpdesk_apis/helpdesk_apis', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/helpdesk_apis/helpdesk_apis/objects', auth='public')
    def list(self, **kw):
        return http.request.render('helpdesk_apis.listing', {
            'root': '/helpdesk_apis/helpdesk_apis',
            'objects': http.request.env['helpdesk_apis.helpdesk_apis'].search([]),
        })

    @http.route('/helpdesk_apis/helpdesk_apis/objects/<model("helpdesk_apis.helpdesk_apis"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('helpdesk_apis.object', {
            'object': obj
        })

    @http.route('/api/login', auth='none', type='http', csrf=False, methods=['POST'])
    def login(self, **kw):
        try:
            data = extract_fields_from_request(request.httprequest.data, ['email', 'password'])
            email = data.get('email')
    
            # Menyiapkan pesan dan data untuk respons
            message = "Request processed successfully"
            raw_data = {
                'email': email,
                # 'password': data.get('password')  # Hindari mengirimkan password
            }
            
            # Mengembalikan respons JSON
            return response_json(raw_data=raw_data, message=message)
        except Exception as e:
            return response_json(raw_data={}, message=f"{e}", status=400)
   