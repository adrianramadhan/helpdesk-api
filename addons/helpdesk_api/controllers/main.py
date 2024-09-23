# controllers/main.py
import json
from odoo import http
from odoo.http import request

class HelpdeskAPI(http.Controller):
    
    @http.route('/api/login', auth='public', type='json', methods=['POST'], csrf=False)
    def login(self, **kwargs):
        """Login method to authenticate the user and start a session"""
        login = kwargs.get('login')
        password = kwargs.get('password')

        if not login or not password:
            return json.dumps({'error': 'Login and password are required'})

        # Authenticate the user and start a session
        try:
            request.session.authenticate(request.env.cr.dbname, login, password)
            user_id = request.env.user.id
            if user_id:
                return json.dumps({'success': 'Logged in successfully', 'user_id': user_id})
            else:
                return json.dumps({'error': 'Invalid credentials'})
        except Exception as e:
            return json.dumps({'error': str(e)})


    @http.route('/api/logout', auth='user', type='json', methods=['POST'], csrf=False)
    def logout(self):
        """Logout method to destroy the current user session"""
        try:
            request.session.logout()
            return json.dumps({'success': 'Logged out successfully'})
        except Exception as e:
            return json.dumps({'error': str(e)})

    @http.route('/api/my/tickets', type='json', auth='user', methods=['GET'])
    def get_my_tickets(self, page=1, limit=10):
        domain = [('customer_id', '=', request.env.user.partner_id.id)]
        tickets = request.env['help.ticket'].search(domain, limit=limit, offset=(page - 1) * limit)

        ticket_data = []
        for ticket in tickets:
            ticket_data.append({
                'id': ticket.id,
                'name': ticket.name,
                'subject': ticket.subject,
                'description': ticket.description,
                'status': ticket.stage_id.name,
                'priority': ticket.priority,
                'assigned_user': ticket.assigned_user.name if ticket.assigned_user else None,
                'creation_date': ticket.create_date,
            })

        total_count = request.env['help.ticket'].search_count(domain)
        return {
            'status': 200,
            'message': 'Success',
            'tickets': ticket_data,
            'total_count': total_count,
            'page': page,
            'limit': limit,
        }
