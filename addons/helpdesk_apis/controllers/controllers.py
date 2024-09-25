from odoo import http
from odoo.http import request
from odoo.exceptions import AccessDenied
from ...helpdesk_apis.helpers.models import ResUser
from ...helpdesk_apis.helpers.hash import assert_hash
from ...helpdesk_apis.helpers.response import response_json
from ...helpdesk_apis.helpers.request import extract_fields_from_request
import logging

class YourController(http.Controller):

    @http.route('/api/login', auth='none', type='http', csrf=False, methods=['POST'])
    def login(self, **kw):
            try:
                # Extract email and password from the request
                data = extract_fields_from_request(request.httprequest.data, ['email', 'password'])
                email = data.get('email')
                password = data.get('password')
                _logger = logging.getLogger(__name__)
                _logger.info(f"Attempting to log in user: {email}")

                user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)

                if not user:
                    _logger.warning(f"User not found: {email}")
                    return response_json(raw_data={}, message="User not found", status=404)

                # Validate token
                # if not assert_hash(password, user.password):
                #     _logger.warning(f"Invalid credentials for user: {user.password}")
                #     return response_json(raw_data={}, message="Invalid credentials", status=401)

                _logger.info(f"User {email} logged in successfully")
                raw_data = {
                    'id': user.id,
                    'name': user.name,
                    'email': user.login,
                }
                return response_json(raw_data=raw_data, message="Login successful")

            except Exception as e:
                _logger.error(f"Error during login: {str(e)}")
                return response_json(raw_data={}, message=str(e), status=400)