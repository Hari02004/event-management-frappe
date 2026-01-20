import frappe
from frappe.model.document import Document

class Events1(Document):
    def on_update(self):
        tickets = frappe.db.count("Ticket", {"event": self.name})
        self.tickets_sold = tickets
        self.remaining_capacity = self.capacity - tickets
