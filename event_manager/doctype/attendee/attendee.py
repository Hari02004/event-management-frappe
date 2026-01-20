import frappe
from frappe.model.document import Document

class Attendee(Document):
    def before_insert(self):
        event = frappe.get_doc("Events1", self.event)
        if event.remaining_capacity <= 0:
            frappe.throw("Event capacity is full!")
