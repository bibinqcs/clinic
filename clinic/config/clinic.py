from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {
                        "label": _("Clinic Forms"),
                        "icon": "fa fa-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "BMI Form",
                                        "description": _("BMI Form"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Emergency Information and Contact",
                                        "description": _("Emergency Information and Contact"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Family History Collection Form",
                                        "description": _("Family History Collection Form"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "First Aid Administration Form",
                                        "description": _("First Aid Administration Form"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Glucometer Quality Test",
                                        "description": _("Glucometer Quality Test"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Immunization Schedule",
                                        "description": _("Immunization Schedule"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Infection Control Checklist",
                                        "description": _("Infection Control Checklist"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Medication Administration Record",
                                        "description": _("Medication Administration Record"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Oxygen Cylinder Log",
                                        "description": _("Oxygen Cylinder Log"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "School Health Service Report",
                                        "description": _("School Health Service Report"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Screen Log",
                                        "description": _("Screen Log"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Student Incident Form",
                                        "description": _("Student Incident Form"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Incident Report Form",
                                        "description": _("Incident Report Form"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Rounds Reports",
                                        "description": _("Rounds Reports"),
                                },
                        ]
                },
		]
