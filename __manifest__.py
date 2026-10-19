
{
    "name": "Hello Odoo",
    "version": "19.0.1.0.0",
    "summary": "Simple Notes Management",
    "description": "A simple application to manage notes.",
    "category": "Productivity",
    "author": "Abdullah",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/hello_odoo_note_views.xml",
    ],
    "installable": True,
    "application": True,
}
