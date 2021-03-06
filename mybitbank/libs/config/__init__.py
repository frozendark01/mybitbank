from django.utils.translation import ugettext_noop as _


MainConfig = {
              'globals' : {
                    'site_brand': "",  # change this to whatever you want
                    'confirmation_limit': 5,
               },
                  
              'site_sections' : [
                    {'name': 'dashboard', 'path':"/dashboard", 'title': _('Dashboard')},
                    {'name': 'accounts', 'path':"/accounts", 'title': _("Accounts"), 'subsections': 
                     [
                         {'name': 'all', 'path':"/accounts", 'title': _('All')},
                         {'name': 'add', 'path':"/accounts/create", 'title': _('Create account')},
                         {'name': 'details', 'path':"/accounts/details", 'title': _('Account details')},
                     ]
                    },
                    {'name': 'transactions', 'path':"/transactions/", 'title': _("Transactions"), 'subsections':
                     [
                         {'name': 'pages', 'path':"/transactions/", 'title': _('Pages')},
                     ]
                    },
                    {'name': 'transfer', 'path':"/transfer", 'title': _("Transfer"), 'subsections': 
                     [
                         # {'name': 'transfer', 'path':"/transfer/", 'title': 'All transactions'}
                     ]
                    },
                    {'name': 'addressbook', 'path':"/addressbook", 'title': _("Addressbook"), 'subsections': 
                     [
                        {'name': 'add', 'path':"/addressbook/add", 'title': _('Add address')},
                     
                     ]},
                    {'name': 'network', 'path':"/network", 'title': _("Network"), 'subsections': 
                     [
                        # {'name': 'add', 'path':"/addressbook/add", 'title': _('Add address')},
                     
                     ]},
               ]
              }
