# Sirius Odoo - Custom Modules

## Overview
This repository contains custom Odoo 18 modules for the Sirius project, developed for Quindicolor. This project is deployed on Odoo.sh.

## Modules

### sale_order
Custom sales module for Quindicolor with additional features:
- Custom delivery zones
- Improved salesperson tracking

### sirius_theme
Custom theme module providing:
- Customized backend appearance
- Company branding integration

### set_default_language
Module to set Spanish (Colombia) as the default language for all users.

## Deployment with Odoo.sh

### Prerequisites
- An active Odoo.sh subscription
- GitHub or Bitbucket account with access to this repository

### Deployment Steps
1. Log in to your Odoo.sh dashboard
2. Create a new project or select your existing project
3. Connect your GitHub/Bitbucket repository to Odoo.sh
4. Select the main branch for production deployment
5. Odoo.sh will automatically build and deploy your instance

## Development Workflow

### Branch Structure
- `production`: Stable code for production environment (protected)
- `staging`: Pre-production testing branch
- `development`: Active development branch

### Making Changes
1. Create a feature branch from development
2. Make your changes and commit them
3. Push your branch to the repository
4. Odoo.sh will automatically create a build for your branch
5. Test your changes in the Odoo.sh development environment
6. Create a pull request to merge into development branch

### Promoting to Production
1. Merge development into staging and test thoroughly
2. Once validated, merge staging into production
3. Odoo.sh will automatically deploy changes to production

## Accessing your Database
Access your different environments through the Odoo.sh dashboard:
- Production: https://your-project.odoo.sh
- Staging: https://staging-your-project.odoo.sh
- Development: https://development-your-project.odoo.sh

## License
This project is licensed under the LGPL-3 - see the LICENSE file for details.

## Team
Sirius Development Team - Let's win together!