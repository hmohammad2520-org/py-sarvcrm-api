from .accounts import Accounts
from .aos_contracts import AosContracts
from .aos_invoices import AosInvoices
from .aos_pdf_templates import AosPdfTemplates
from .aos_product_categories import AosProductCategories
from .aos_products import AosProducts
from .aos_quotes import AosQuotes
from .appointments import Appointments
from .approval import Approval
from .asol_project import AsolProject
from .branches import Branches
from .bugs import Bugs
from .calls import Calls
from .cases import Cases
from .communications import Communications
from .communications_target import CommunicationsTarget
from .communications_template import CommunicationsTemplate
from .campaigns import Campaigns
from .contacts import Contacts
from .deposits import Deposits
from .documents import Documents
from .emails import Emails
from .knowledge_base import KnowledgeBase
from .knowledge_base_categories import KnowledgeBaseCategories
from .leads import Leads
from .meetings import Meetings
from .notes import Notes
from .obj_conditions import ObjConditions
from .obj_indicators import ObjIndicators
from .obj_objectives import ObjObjectives
from .opportunities import Opportunities
from .payments import Payments
from .purchase_order import PurchaseOrder
from .sc_competitor import ScCompetitor
from .sc_contract import ScContract
from .sc_contract_management import ScContractManagement
from .service_centers import ServiceCenters
from .tasks import Tasks
from .timesheet import Timesheet
from .vendors import Vendors


module_map = {
    'Accounts': Accounts, 
    'AOS_Contracts': AosContracts, 
    'AOS_Invoices': AosInvoices, 
    'AOS_PDF_Templates': AosPdfTemplates, 
    'AOS_Product_Categories': AosProductCategories, 
    'AOS_Products': AosProducts, 
    'AOS_Quotes': AosQuotes, 
    'Appointments': Appointments, 
    'Approval': Approval, 
    'asol_Project': AsolProject, 
    'Branches': Branches, 
    'Bugs': Bugs, 
    'Calls': Calls, 
    'Cases': Cases, 
    'Communications': Communications, 
    'Communications_Target': CommunicationsTarget, 
    'Communications_Template': CommunicationsTemplate, 
    'Campaigns': Campaigns, 
    'Contacts': Contacts, 
    'Deposits': Deposits, 
    'Documents': Documents, 
    'Emails': Emails, 
    'Knowledge_Base': KnowledgeBase, 
    'Knowledge_Base_Categories': KnowledgeBaseCategories, 
    'Leads': Leads, 
    'Meetings': Meetings, 
    'Notes': Notes, 
    'OBJ_Conditions': ObjConditions, 
    'OBJ_Indicators': ObjIndicators, 
    'OBJ_Objectives': ObjObjectives, 
    'Opportunities': Opportunities, 
    'Payments': Payments, 
    'Purchase_Order': PurchaseOrder, 
    'sc_competitor': ScCompetitor, 
    'sc_Contract': ScContract, 
    'sc_contract_management': ScContractManagement, 
    'Service_Centers': ServiceCenters, 
    'Tasks': Tasks, 
    'Timesheet': Timesheet, 
    'Vendors': Vendors, 
    }


__all__ = [
    'module_map'
]