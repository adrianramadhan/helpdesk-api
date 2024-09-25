# TSG Helpdesk API

This project is designed to build a Helpdesk application for TSG using Odoo 16 for the backend, Docker for containerization, and Next.js for the frontend.

## Project Structure

- **addons/**: Custom Odoo modules
  - `hide_menu_user`: Custom module to hide menu items for certain users.
  - `odoo_website_helpdesk`: Helpdesk module to manage tickets via the Odoo website.
  - `odoo_website_helpdesk_dashboard`: Dashboard for visualizing Helpdesk ticket metrics.
  - `odoo_website_helpdesk_v2`: Second version of the Helpdesk module with additional features.
  
- **conf/**: Configuration files for Odoo.

- **docker-compose.yml**: Docker Compose configuration for setting up the Odoo backend environment.

## Requirements

Ensure you have the following installed on your local machine:

- Docker
- Docker Compose
- Git

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/adrianramadhan/helpdesk-api.git
   cd helpdesk-api
   ```
2. **Configure env and start Odoo using Docker**:
  ```bash
    touch cp env.example .env 
    <!-- update your avaliable port on env -->
   ```
   Use the docker-compose.yml file to start the Odoo server.
   ```bash
   docker-compose up -d
   ```
  This will launch Odoo 16, exposing it on port 1704. You can access the Odoo instance by visiting http://localhost:1704 in your browser.
3. **Accessing Odoo**: After the containers are running, visit the Odoo interface at http://localhost:1704 and log in using your admin credentials.
4. **Stopping and Removing Containers**: To stop and remove all running containers, use the following commands:
  ```bash
  docker-compose down
  ```
5. **Clean up Docker Containers and Volumes**: If you need to clean up all Docker volumes and containers completely, use:
   ```bash
   docker system prune --volumes
   ```

## Custom Modules
1. **hide_menu_user**
This module restricts certain menu options for specific user roles in Odoo.

2. **odoo_website_helpdesk**
This is the core Helpdesk module that allows users to submit, manage, and track tickets directly from the Odoo website.

3. **odoo_website_helpdesk_dashboard**
Provides a dashboard view of all Helpdesk tickets, giving an overview of key metrics such as ticket status and priority.

4. **odoo_website_helpdesk_v2**
The second version of the Helpdesk module that includes additional features and improvements over the first version.

