from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def add_page_break(doc):
    doc.add_page_break()

def set_cell_border(cell, **kwargs):
    """
    Set cell borders
    """
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        if edge in kwargs:
            edge_data = kwargs.get(edge)
            edge_el = OxmlElement(f'w:{edge}')
            edge_el.set(qn('w:val'), 'single')
            edge_el.set(qn('w:sz'), '4')
            edge_el.set(qn('w:space'), '0')
            edge_el.set(qn('w:color'), '000000')
            tcBorders.append(edge_el)
    tcPr.append(tcBorders)

# Create document
doc = Document()

# Set margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# ==================== COVER PAGE ====================
# Title
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('A PROJECT REPORT')
run.bold = True
run.font.size = Pt(16)

doc.add_paragraph()

# Project Title
project_title = doc.add_paragraph()
project_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = project_title.add_run('ON')
run.font.size = Pt(14)

doc.add_paragraph()

main_title = doc.add_paragraph()
main_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = main_title.add_run('"OFFICE EMPLOYEE MANAGEMENT SYSTEM (OEMS)"')
run.bold = True
run.font.size = Pt(18)
run.font.color.rgb = RGBColor(0, 0, 0)

doc.add_paragraph()
doc.add_paragraph()

# Submitted details
submitted = doc.add_paragraph()
submitted.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = submitted.add_run('Submitted in partial fulfillment of the requirements for the award of the degree of')
run.font.size = Pt(12)

doc.add_paragraph()

degree = doc.add_paragraph()
degree.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = degree.add_run('BACHELOR IN COMPUTER APPLICATION (BCA)')
run.bold = True
run.font.size = Pt(14)

doc.add_paragraph()

# Submitted By
submitted_by = doc.add_paragraph()
submitted_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = submitted_by.add_run('Submitted By:')
run.bold = True
run.font.size = Pt(12)

name = doc.add_paragraph()
name.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = name.add_run('Kiran Barode')
run.bold = True
run.font.size = Pt(14)

enrollment = doc.add_paragraph()
enrollment.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = enrollment.add_run('Enrollment No: R23CA1CA0042')
run.font.size = Pt(12)

roll = doc.add_paragraph()
roll.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = roll.add_run('Roll No: AU230190')
run.font.size = Pt(12)

doc.add_paragraph()
doc.add_paragraph()

# Under Guidance
guidance = doc.add_paragraph()
guidance.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = guidance.add_run('Under the Guidance of:')
run.bold = True
run.font.size = Pt(12)

guide = doc.add_paragraph()
guide.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = guide.add_run('Mr. Shashikant Upadhyay')
run.bold = True
run.font.size = Pt(14)

designation = doc.add_paragraph()
designation.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = designation.add_run('Assistant Professor, Department of Computer Science & Application')
run.font.size = Pt(11)

doc.add_paragraph()
doc.add_paragraph()

# University
university = doc.add_paragraph()
university.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = university.add_run('RABINDRANATH TAGORE UNIVERSITY')
run.bold = True
run.font.size = Pt(14)

location = doc.add_paragraph()
location.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = location.add_run('BHOPAL (M.P.)')
run.bold = True
run.font.size = Pt(14)

doc.add_paragraph()

year = doc.add_paragraph()
year.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = year.add_run('2024-2025')
run.bold = True
run.font.size = Pt(14)

# Page Break
add_page_break(doc)

# ==================== CERTIFICATE PAGE ====================
cert_title = doc.add_paragraph()
cert_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = cert_title.add_run('CERTIFICATE')
run.bold = True
run.font.size = Pt(16)
run.underline = True

doc.add_paragraph()

cert_text = doc.add_paragraph()
cert_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('This is to certify that the project report entitled "OFFICE EMPLOYEE MANAGEMENT SYSTEM (OEMS)" '
        'submitted by Kiran Barode (Enrollment No: R23CA1CA0042, Roll No: AU230190) in partial fulfillment '
        'of the requirements for the award of the degree of Bachelor in Computer Application (BCA) from '
        'Rabindranath Tagore University, Bhopal (M.P.) is a bonafide record of work carried out by her under '
        'my guidance and supervision.')
run = cert_text.add_run(text)
run.font.size = Pt(12)

doc.add_paragraph()
doc.add_paragraph()
doc.add_paragraph()

# Signatures
sig_table = doc.add_table(rows=1, cols=2)
sig_table.autofit = False
sig_table.allow_autofit = False

left_cell = sig_table.rows[0].cells[0]
right_cell = sig_table.rows[0].cells[1]

left_para = left_cell.paragraphs[0]
left_para.add_run('Project Guide:\n\n\n').font.size = Pt(11)
left_para.add_run('Mr. Shashikant Upadhyay\n').bold = True
left_para.add_run('Assistant Professor\n').font.size = Pt(10)
left_para.add_run('Department of CSA').font.size = Pt(10)

right_para = right_cell.paragraphs[0]
right_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
right_para.add_run('Head of Department:\n\n\n').font.size = Pt(11)
right_para.add_run('Dr. [HOD Name]\n').bold = True
right_para.add_run('Professor & HOD\n').font.size = Pt(10)
right_para.add_run('Department of CSA').font.size = Pt(10)

doc.add_paragraph()
doc.add_paragraph()

date_place = doc.add_paragraph()
date_place.add_run('Date: _______________\n').font.size = Pt(11)
date_place.add_run('Place: Bhopal').font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== ACKNOWLEDGEMENT ====================
ack_title = doc.add_paragraph()
ack_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = ack_title.add_run('ACKNOWLEDGEMENT')
run.bold = True
run.font.size = Pt(16)
run.underline = True

doc.add_paragraph()

ack_text = doc.add_paragraph()
ack_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('I would like to express my sincere gratitude to all those who have contributed to the successful '
        'completion of this project on "Office Employee Management System (OEMS)".\n\n'
        'First and foremost, I am deeply thankful to my project guide, Mr. Shashikant Upadhyay, Assistant Professor, '
        'Department of Computer Science & Application, for his invaluable guidance, continuous support, and '
        'encouragement throughout the development of this project.\n\n'
        'I would also like to extend my heartfelt thanks to Netlink Software Group India Pvt. Ltd. for providing '
        'me with the opportunity to undergo industrial training as a Python Full Stack Trainee for 4-5 months. '
        'This training has been instrumental in enhancing my technical skills in Frontend Technologies (HTML, CSS, '
        'JavaScript, Bootstrap), Backend Development (Core Python, Django Framework), and Database Management (SQL). '
        'The practical exposure and hands-on experience gained during this training have significantly contributed '
        'to my understanding of real-world software development.\n\n'
        'I am grateful to the faculty members of the Department of Computer Science & Application and the '
        'management of Rabindranath Tagore University, Bhopal, for providing the necessary facilities and '
        'academic environment.\n\n'
        'Last but not least, I would like to thank my family and friends for their constant support and motivation '
        'throughout this journey.')
run = ack_text.add_run(text)
run.font.size = Pt(12)

doc.add_paragraph()
doc.add_paragraph()

signature = doc.add_paragraph()
signature.alignment = WD_ALIGN_PARAGRAPH.RIGHT
run = signature.add_run('Kiran Barode\n')
run.bold = True
run.font.size = Pt(12)
run = signature.add_run('R23CA1CA0042')
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== TABLE OF CONTENTS ====================
toc_title = doc.add_paragraph()
toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = toc_title.add_run('TABLE OF CONTENTS')
run.bold = True
run.font.size = Pt(16)
run.underline = True

doc.add_paragraph()

# TOC Table
toc_data = [
    ('Chapter No.', 'Title', 'Page No.'),
    ('1', 'INTRODUCTION', '1'),
    ('1.1', 'Project Overview', '1'),
    ('1.2', 'Objectives', '2'),
    ('1.3', 'Scope of the Project', '2'),
    ('2', 'LITERATURE REVIEW / BACKGROUND STUDY', '3'),
    ('2.1', 'Existing Systems', '3'),
    ('2.2', 'Technology Stack Overview', '4'),
    ('3', 'SYSTEM ANALYSIS AND DESIGN', '5'),
    ('3.1', 'System Requirements', '5'),
    ('3.2', 'System Architecture', '6'),
    ('3.3', 'Database Design', '7'),
    ('4', 'IMPLEMENTATION', '8'),
    ('4.1', 'Major Project: OEMS', '8'),
    ('4.2', 'Frontend Application: Personal Developer Portfolio', '9'),
    ('4.3', 'Academic Project: AI Stock Market Prediction', '10'),
    ('5', 'INDUSTRIAL TRAINING EXPERIENCE', '11'),
    ('5.1', 'Training at Netlink Software Group', '11'),
    ('5.2', 'Skills Acquired', '12'),
    ('6', 'TESTING AND VALIDATION', '13'),
    ('7', 'CONCLUSION AND FUTURE SCOPE', '14'),
    ('7.1', 'Conclusion', '14'),
    ('7.2', 'Future Enhancements', '14'),
    ('', 'REFERENCES', '15'),
    ('', 'APPENDIX', '16'),
]

toc_table = doc.add_table(rows=len(toc_data), cols=3)
toc_table.style = 'Table Grid'

for i, (chapter, title, page) in enumerate(toc_data):
    row = toc_table.rows[i]
    row.cells[0].text = chapter
    row.cells[1].text = title
    row.cells[2].text = page
    
    for cell in row.cells:
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(11)
                if i == 0:
                    run.bold = True

# Page Break
add_page_break(doc)

# ==================== CHAPTER 1: INTRODUCTION ====================
ch1_title = doc.add_paragraph()
run = ch1_title.add_run('CHAPTER 1')
run.bold = True
run.font.size = Pt(14)

ch1_subtitle = doc.add_paragraph()
run = ch1_subtitle.add_run('INTRODUCTION')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

# 1.1 Project Overview
section_1_1 = doc.add_paragraph()
run = section_1_1.add_run('1.1 Project Overview')
run.bold = True
run.font.size = Pt(12)

overview_text = doc.add_paragraph()
overview_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('The Office Employee Management System (OEMS) is a comprehensive web-based application developed using '
        'the Django framework. This system is designed to automate and streamline the management of employee-related '
        'data in an office environment. The primary focus of OEMS is to efficiently handle three critical aspects '
        'of employee management:\n\n'
        '• Daily Attendance Tracking: Automated recording and monitoring of employee attendance\n'
        '• Leave Management: Systematic handling of leave applications, approvals, and tracking\n'
        '• Payroll Management: Automated calculation and management of employee salary details\n\n'
        'The system aims to reduce manual paperwork, minimize errors, and provide a centralized platform for '
        'managing all employee-related operations. By leveraging modern web technologies, OEMS offers a user-friendly '
        'interface that can be accessed from any device with an internet connection.')
run = overview_text.add_run(text)
run.font.size = Pt(11)

doc.add_paragraph()

# 1.2 Objectives
section_1_2 = doc.add_paragraph()
run = section_1_2.add_run('1.2 Objectives')
run.bold = True
run.font.size = Pt(12)

objectives_text = doc.add_paragraph()
objectives_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('The main objectives of the Office Employee Management System are:\n\n'
        '1. To develop a centralized system for managing employee information and records\n'
        '2. To automate the attendance tracking process and generate accurate attendance reports\n'
        '3. To streamline the leave application and approval workflow\n'
        '4. To automate payroll calculations based on attendance, leaves, and other parameters\n'
        '5. To provide role-based access control for administrators, managers, and employees\n'
        '6. To generate comprehensive reports for management decision-making\n'
        '7. To ensure data security and maintain confidentiality of employee information\n'
        '8. To create a scalable and maintainable system using industry-standard technologies')
run = objectives_text.add_run(text)
run.font.size = Pt(11)

doc.add_paragraph()

# 1.3 Scope
section_1_3 = doc.add_paragraph()
run = section_1_3.add_run('1.3 Scope of the Project')
run.bold = True
run.font.size = Pt(12)

scope_text = doc.add_paragraph()
scope_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('The scope of this project encompasses:\n\n'
        '• Development of a fully functional web application using Django framework\n'
        '• Implementation of user authentication and authorization mechanisms\n'
        '• Design and implementation of database schema for storing employee data\n'
        '• Creation of intuitive user interfaces for different user roles\n'
        '• Integration of attendance tracking modules with biometric or manual entry options\n'
        '• Development of leave management workflow with approval hierarchy\n'
        '• Implementation of payroll calculation algorithms\n'
        '• Generation of various reports in PDF and Excel formats\n'
        '• Responsive design for accessibility across different devices\n\n'
        'The project is currently under development and focuses on core functionalities. Future enhancements '
        'may include advanced analytics, mobile applications, and integration with third-party services.')
run = scope_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== CHAPTER 2: LITERATURE REVIEW ====================
ch2_title = doc.add_paragraph()
run = ch2_title.add_run('CHAPTER 2')
run.bold = True
run.font.size = Pt(14)

ch2_subtitle = doc.add_paragraph()
run = ch2_subtitle.add_run('LITERATURE REVIEW / BACKGROUND STUDY')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

# 2.1 Existing Systems
section_2_1 = doc.add_paragraph()
run = section_2_1.add_run('2.1 Existing Systems')
run.bold = True
run.font.size = Pt(12)

existing_text = doc.add_paragraph()
existing_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('Employee management systems have evolved significantly over the years. Traditional systems relied heavily '
        'on manual record-keeping and paper-based processes, which were time-consuming and prone to errors. '
        'Modern employee management systems leverage web technologies to provide automated solutions.\n\n'
        'Several commercial and open-source employee management systems exist in the market, including:\n\n'
        '• BambooHR: A comprehensive HR management platform\n'
        '• Zoho People: Cloud-based HR management software\n'
        '• Keka: Payroll and HR management system\n'
        '• OrangeHRM: Open-source HR management solution\n\n'
        'However, many of these systems are either expensive for small to medium-sized organizations or lack '
        'customization options specific to Indian business requirements. This project aims to develop a cost-effective, '
        'customizable solution tailored to the needs of local organizations.')
run = existing_text.add_run(text)
run.font.size = Pt(11)

doc.add_paragraph()

# 2.2 Technology Stack
section_2_2 = doc.add_paragraph()
run = section_2_2.add_run('2.2 Technology Stack Overview')
run.bold = True
run.font.size = Pt(12)

tech_text = doc.add_paragraph()
tech_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('The Office Employee Management System is built using the following technology stack:\n\n'
        'Backend Technologies:\n'
        '• Python: A versatile, high-level programming language known for its simplicity and readability\n'
        '• Django: A high-level Python web framework that encourages rapid development and clean design\n'
        '• Django ORM: Object-Relational Mapping for database operations\n\n'
        'Frontend Technologies:\n'
        '• HTML5: Markup language for structuring web content\n'
        '• CSS3: Styling language for designing responsive and attractive interfaces\n'
        '• JavaScript: Programming language for interactive and dynamic web features\n'
        '• Bootstrap: CSS framework for responsive and mobile-first web development\n\n'
        'Database:\n'
        '• SQL (SQLite/PostgreSQL/MySQL): Relational database management system for data storage\n\n'
        'Development Tools:\n'
        '• Git: Version control system\n'
        '• VS Code: Integrated Development Environment\n'
        '• Django Admin: Built-in administration interface')
run = tech_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== CHAPTER 3: SYSTEM ANALYSIS AND DESIGN ====================
ch3_title = doc.add_paragraph()
run = ch3_title.add_run('CHAPTER 3')
run.bold = True
run.font.size = Pt(14)

ch3_subtitle = doc.add_paragraph()
run = ch3_subtitle.add_run('SYSTEM ANALYSIS AND DESIGN')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

# 3.1 System Requirements
section_3_1 = doc.add_paragraph()
run = section_3_1.add_run('3.1 System Requirements')
run.bold = True
run.font.size = Pt(12)

req_text = doc.add_paragraph()
req_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('Hardware Requirements:\n'
        '• Processor: Intel Core i3 or higher\n'
        '• RAM: Minimum 4GB (8GB recommended)\n'
        '• Storage: Minimum 500MB free space\n'
        '• Network: Internet connection for web access\n\n'
        'Software Requirements:\n'
        '• Operating System: Windows 10/11, Linux, or macOS\n'
        '• Python: Version 3.8 or higher\n'
        '• Django: Version 4.x or higher\n'
        '• Database: SQLite (development) / PostgreSQL or MySQL (production)\n'
        '• Web Browser: Chrome, Firefox, Safari, or Edge (latest versions)\n\n'
        'Functional Requirements:\n'
        '• User authentication and authorization\n'
        '• Employee profile management\n'
        '• Attendance tracking and reporting\n'
        '• Leave application and approval workflow\n'
        '• Payroll calculation and management\n'
        '• Report generation (PDF, Excel)\n'
        '• Dashboard with key metrics and analytics\n\n'
        'Non-Functional Requirements:\n'
        '• Security: Secure authentication, data encryption\n'
        '• Performance: Fast response time, efficient database queries\n'
        '• Scalability: Ability to handle growing number of users\n'
        '• Usability: Intuitive and user-friendly interface\n'
        '• Reliability: High availability and data integrity')
run = req_text.add_run(text)
run.font.size = Pt(11)

doc.add_paragraph()

# 3.2 System Architecture
section_3_2 = doc.add_paragraph()
run = section_3_2.add_run('3.2 System Architecture')
run.bold = True
run.font.size = Pt(12)

arch_text = doc.add_paragraph()
arch_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('The Office Employee Management System follows the Model-View-Template (MVT) architecture pattern, '
        'which is the standard architecture for Django applications:\n\n'
        'Model Layer:\n'
        '• Defines the data structure and database schema\n'
        '• Handles database operations through Django ORM\n'
        '• Includes models for Employee, Attendance, Leave, Payroll, etc.\n\n'
        'View Layer:\n'
        '• Contains the business logic of the application\n'
        '• Processes user requests and returns appropriate responses\n'
        '• Handles form validation and data processing\n\n'
        'Template Layer:\n'
        '• Defines the presentation layer (HTML templates)\n'
        '• Uses Django template language for dynamic content rendering\n'
        '• Integrates with Bootstrap for responsive design\n\n'
        'The system also includes:\n'
        '• URL Dispatcher: Maps URLs to appropriate views\n'
        '• Middleware: Handles cross-cutting concerns like authentication\n'
        '• Static Files: CSS, JavaScript, and image files\n'
        '• Admin Interface: Django\'s built-in administration panel')
run = arch_text.add_run(text)
run.font.size = Pt(11)

doc.add_paragraph()

# 3.3 Database Design
section_3_3 = doc.add_paragraph()
run = section_3_3.add_run('3.3 Database Design')
run.bold = True
run.font.size = Pt(12)

db_text = doc.add_paragraph()
db_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('The database design includes the following main entities:\n\n'
        '1. User/Employee Table:\n'
        '   - Employee ID (Primary Key)\n'
        '   - Name, Email, Phone\n'
        '   - Department, Designation\n'
        '   - Date of Joining\n'
        '   - Role (Admin/Manager/Employee)\n\n'
        '2. Attendance Table:\n'
        '   - Attendance ID (Primary Key)\n'
        '   - Employee ID (Foreign Key)\n'
        '   - Date, Check-in Time, Check-out Time\n'
        '   - Status (Present/Absent/Half-day)\n\n'
        '3. Leave Table:\n'
        '   - Leave ID (Primary Key)\n'
        '   - Employee ID (Foreign Key)\n'
        '   - Leave Type, Start Date, End Date\n'
        '   - Reason, Status (Pending/Approved/Rejected)\n'
        '   - Approved By (Foreign Key to Manager)\n\n'
        '4. Payroll Table:\n'
        '   - Payroll ID (Primary Key)\n'
        '   - Employee ID (Foreign Key)\n'
        '   - Month, Year\n'
        '   - Basic Salary, Allowances, Deductions\n'
        '   - Net Salary\n\n'
        'Relationships:\n'
        '• One-to-Many: Employee to Attendance\n'
        '• One-to-Many: Employee to Leave\n'
        '• One-to-Many: Employee to Payroll\n'
        '• Many-to-One: Leave to Approver (Manager)')
run = db_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== CHAPTER 4: IMPLEMENTATION ====================
ch4_title = doc.add_paragraph()
run = ch4_title.add_run('CHAPTER 4')
run.bold = True
run.font.size = Pt(14)

ch4_subtitle = doc.add_paragraph()
run = ch4_subtitle.add_run('IMPLEMENTATION')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

intro_text = doc.add_paragraph()
intro_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('This chapter describes the implementation details of various projects undertaken during the course of study, '
        'including the major project (OEMS), frontend applications, and academic projects.')
run = intro_text.add_run(text)
run.font.size = Pt(11)

doc.add_paragraph()

# 4.1 Major Project: OEMS
section_4_1 = doc.add_paragraph()
run = section_4_1.add_run('4.1 Major Project: Office Employee Management System (OEMS)')
run.bold = True
run.font.size = Pt(12)

oems_text = doc.add_paragraph()
oems_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('Status: Under Development\n\n'
        'Objective:\n'
        'The primary objective of OEMS is to efficiently track and manage employee attendance, leave applications, '
        'and payroll details in an automated manner. The system aims to eliminate manual processes and provide '
        'real-time access to employee data for administrators and managers.\n\n'
        'Technology Stack:\n'
        '• Backend: Django (Python Framework)\n'
        '• Frontend: HTML, CSS, JavaScript, Bootstrap\n'
        '• Database: SQL (SQLite for development, PostgreSQL for production)\n'
        '• Version Control: Git\n\n'
        'Key Features Implemented:\n\n'
        '1. User Authentication Module:\n'
        '   - Login/Logout functionality\n'
        '   - Role-based access control (Admin, Manager, Employee)\n'
        '   - Password reset and change functionality\n\n'
        '2. Employee Management Module:\n'
        '   - Add, edit, and delete employee records\n'
        '   - View employee profiles with complete details\n'
        '   - Department and designation management\n\n'
        '3. Attendance Management Module:\n'
        '   - Daily attendance marking (manual/automated)\n'
        '   - Attendance reports (daily, weekly, monthly)\n'
        '   - Late arrival and early departure tracking\n\n'
        '4. Leave Management Module:\n'
        '   - Leave application submission by employees\n'
        '   - Leave approval/rejection workflow\n'
        '   - Leave balance tracking\n'
        '   - Different leave types (Casual, Sick, Earned)\n\n'
        '5. Payroll Module (In Progress):\n'
        '   - Salary structure definition\n'
        '   - Automated salary calculation based on attendance\n'
        '   - Payslip generation\n\n'
        '6. Dashboard and Reports:\n'
        '   - Admin dashboard with key metrics\n'
        '   - Employee dashboard with personal information\n'
        '   - Export reports in PDF and Excel formats\n\n'
        'Implementation Challenges:\n'
        '• Designing an efficient database schema to handle complex relationships\n'
        '• Implementing secure authentication and authorization mechanisms\n'
        '• Creating responsive UI that works across different devices\n'
        '• Handling date and time calculations for attendance and payroll\n\n'
        'Current Status:\n'
        'The core modules (Authentication, Employee Management, Attendance, and Leave Management) have been '
        'implemented and are undergoing testing. The Payroll module is currently under development.')
run = oems_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# 4.2 Frontend Application
section_4_2 = doc.add_paragraph()
run = section_4_2.add_run('4.2 Frontend Application: Personal Developer Portfolio')
run.bold = True
run.font.size = Pt(12)

portfolio_text = doc.add_paragraph()
portfolio_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('Objective:\n'
        'To create a professional and responsive portfolio website that showcases frontend development and UI/UX '
        'capabilities. The portfolio serves as a platform to display projects, skills, and professional information.\n\n'
        'Technology Stack:\n'
        '• HTML5: For semantic markup and structure\n'
        '• CSS3: For styling, animations, and responsive design\n'
        '• JavaScript: For interactive features and dynamic content\n'
        '• Bootstrap: For responsive grid system and components\n\n'
        'Key Features:\n\n'
        '1. Home Section:\n'
        '   - Professional introduction and tagline\n'
        '   - Animated text effects\n'
        '   - Call-to-action buttons\n\n'
        '2. About Section:\n'
        '   - Personal and professional background\n'
        '   - Skills showcase with progress bars\n'
        '   - Education and certification details\n\n'
        '3. Projects Section:\n'
        '   - Showcase of completed projects\n'
        '   - Project cards with hover effects\n'
        '   - Links to live demos and source code\n\n'
        '4. Mini Projects Integrated:\n'
        '   a) To-Do List Application:\n'
        '      - Add, edit, and delete tasks\n'
        '      - Mark tasks as complete\n'
        '      - Local storage for data persistence\n'
        '      - Filter tasks (All, Active, Completed)\n\n'
        '   b) Working Calculator:\n'
        '      - Basic arithmetic operations (+, -, ×, ÷)\n'
        '      - Clear and delete functionality\n'
        '      - Keyboard support\n'
        '      - Responsive design\n\n'
        '5. Contact Section:\n'
        '   - Contact form with validation\n'
        '   - Social media links\n'
        '   - Email and phone information\n\n'
        'Design Principles Applied:\n'
        '• Mobile-first responsive design\n'
        '• Clean and modern UI with consistent color scheme\n'
        '• Smooth scrolling and animations\n'
        '• Cross-browser compatibility\n'
        '• Optimized images and assets for fast loading\n\n'
        'Learning Outcomes:\n'
        '• Mastery of HTML5 semantic elements\n'
        '• Advanced CSS techniques (Flexbox, Grid, Animations)\n'
        '• DOM manipulation with vanilla JavaScript\n'
        '• Responsive design principles\n'
        '• Bootstrap framework utilization')
run = portfolio_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# 4.3 Academic Project
section_4_3 = doc.add_paragraph()
run = section_4_3.add_run('4.3 Academic Project: AI Stock Market Prediction')
run.bold = True
run.font.size = Pt(12)

ai_text = doc.add_paragraph()
ai_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('Context:\n'
        'This project was completed as part of the Artificial Intelligence course in the 5th semester of BCA program.\n\n'
        'Objective:\n'
        'To develop a machine learning model that analyzes historical stock market data and predicts future stock '
        'prices. The project aims to demonstrate the application of AI and machine learning algorithms in financial '
        'forecasting.\n\n'
        'Technology Stack:\n'
        '• Python: Primary programming language\n'
        '• Pandas: Data manipulation and analysis\n'
        '• NumPy: Numerical computations\n'
        '• Scikit-learn: Machine learning algorithms\n'
        '• Matplotlib/Seaborn: Data visualization\n\n'
        'Machine Learning Algorithms Used:\n'
        '• Linear Regression: For basic trend prediction\n'
        '• Multiple Regression: Considering multiple features\n'
        '• Time Series Analysis: For temporal pattern recognition\n\n'
        'Project Workflow:\n\n'
        '1. Data Collection:\n'
        '   - Historical stock price data from Yahoo Finance or similar sources\n'
        '   - Features: Open, High, Low, Close prices, Volume\n'
        '   - Time period: Multiple years of historical data\n\n'
        '2. Data Preprocessing:\n'
        '   - Handling missing values\n'
        '   - Data normalization and scaling\n'
        '   - Feature engineering (moving averages, RSI, etc.)\n'
        '   - Train-test split (80-20 ratio)\n\n'
        '3. Model Development:\n'
        '   - Implementation of regression models\n'
        '   - Training models on historical data\n'
        '   - Hyperparameter tuning\n\n'
        '4. Model Evaluation:\n'
        '   - Performance metrics: MSE, RMSE, MAE, R² Score\n'
        '   - Comparison of different algorithms\n'
        '   - Visualization of predictions vs actual values\n\n'
        '5. Prediction:\n'
        '   - Forecasting future stock prices\n'
        '   - Confidence intervals for predictions\n\n'
        'Key Findings:\n'
        '• Linear regression models can capture general trends in stock prices\n'
        '• Multiple features improve prediction accuracy\n'
        '• Stock market prediction is challenging due to high volatility and external factors\n'
        '• Model performs better for short-term predictions than long-term forecasts\n\n'
        'Learning Outcomes:\n'
        '• Understanding of machine learning concepts and algorithms\n'
        '• Practical experience with Python data science libraries\n'
        '• Data preprocessing and feature engineering techniques\n'
        '• Model evaluation and performance metrics\n'
        '• Real-world application of AI in financial domain\n\n'
        'Limitations:\n'
        '• Stock prices are influenced by many external factors not captured in historical data\n'
        '• Model accuracy decreases for longer prediction horizons\n'
        '• Requires continuous retraining with new data')
run = ai_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== CHAPTER 5: INDUSTRIAL TRAINING ====================
ch5_title = doc.add_paragraph()
run = ch5_title.add_run('CHAPTER 5')
run.bold = True
run.font.size = Pt(14)

ch5_subtitle = doc.add_paragraph()
run = ch5_subtitle.add_run('INDUSTRIAL TRAINING EXPERIENCE')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

# 5.1 Training at Netlink
section_5_1 = doc.add_paragraph()
run = section_5_1.add_run('5.1 Training at Netlink Software Group India Pvt. Ltd.')
run.bold = True
run.font.size = Pt(12)

netlink_text = doc.add_paragraph()
netlink_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('Organization: Netlink Software Group India Pvt. Ltd.\n'
        'Position: Python Full Stack Trainee\n'
        'Duration: 4-5 Months\n'
        'Training Period: [Start Date] to [End Date / Ongoing]\n\n'
        'Overview:\n'
        'I had the privilege of undergoing comprehensive industrial training at Netlink Software Group India Pvt. Ltd., '
        'a leading software development company. This training program was designed to provide hands-on experience in '
        'full-stack web development using Python and modern web technologies.\n\n'
        'Training Structure:\n\n'
        'Phase 1: Frontend Development (Weeks 1-6)\n'
        '• HTML5: Semantic markup, forms, multimedia elements\n'
        '• CSS3: Styling, layouts (Flexbox, Grid), animations, transitions\n'
        '• JavaScript: ES6+ features, DOM manipulation, event handling, AJAX\n'
        '• Bootstrap: Responsive design, grid system, components, utilities\n'
        '• Practical Projects: Responsive landing pages, interactive forms, UI components\n\n'
        'Phase 2: Backend Development - Core Python (Weeks 7-10)\n'
        '• Python Fundamentals: Data types, control structures, functions\n'
        '• Object-Oriented Programming: Classes, inheritance, polymorphism\n'
        '• File Handling: Reading/writing files, CSV, JSON operations\n'
        '• Exception Handling: Try-except blocks, custom exceptions\n'
        '• Modules and Packages: Standard library, third-party packages\n'
        '• Practical Exercises: Console applications, data processing scripts\n\n'
        'Phase 3: Database Management - SQL (Week 11)\n'
        '• Database Concepts: RDBMS, normalization, relationships\n'
        '• SQL Basics: SELECT, INSERT, UPDATE, DELETE operations\n'
        '• Table Creation: Data types, constraints, primary/foreign keys\n'
        '• Joins: INNER JOIN, LEFT JOIN, RIGHT JOIN\n'
        '• Basic Queries: WHERE, ORDER BY, GROUP BY, HAVING\n'
        '• Database Integration: Connecting Python with databases\n\n'
        'Phase 4: Django Framework (Weeks 12-18)\n'
        '• Django Basics: Project structure, MVT architecture, settings\n'
        '• Models: ORM, model fields, relationships, migrations\n'
        '• Views: Function-based views, class-based views, request/response\n'
        '• Templates: Template language, filters, tags, template inheritance\n'
        '• Forms: Form handling, validation, ModelForms\n'
        '• Admin Interface: Customization, model registration\n'
        '• Authentication: User authentication, permissions, decorators\n'
        '• Static Files: CSS, JavaScript, images management\n'
        '• Deployment Basics: Production settings, WSGI\n\n'
        'Projects Developed During Training:\n'
        '1. Blog Application: Multi-user blogging platform with CRUD operations\n'
        '2. E-commerce Product Catalog: Product listing with search and filter\n'
        '3. Student Management System: Basic CRUD application for student records\n'
        '4. Office Employee Management System (OEMS): Major project (ongoing)\n\n'
        'Training Methodology:\n'
        '• Instructor-led sessions with live coding demonstrations\n'
        '• Hands-on practical exercises and assignments\n'
        '• Code reviews and feedback sessions\n'
        '• Peer learning and collaborative projects\n'
        '• Industry best practices and coding standards\n'
        '• Agile development methodology introduction')
run = netlink_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# 5.2 Skills Acquired
section_5_2 = doc.add_paragraph()
run = section_5_2.add_run('5.2 Skills Acquired')
run.bold = True
run.font.size = Pt(12)

skills_text = doc.add_paragraph()
skills_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('Technical Skills:\n\n'
        'Frontend Development:\n'
        '• Proficiency in HTML5, CSS3, and JavaScript\n'
        '• Responsive web design using Bootstrap framework\n'
        '• Cross-browser compatibility and optimization\n'
        '• Modern CSS techniques (Flexbox, Grid, Animations)\n'
        '• JavaScript ES6+ features and best practices\n'
        '• DOM manipulation and event handling\n\n'
        'Backend Development:\n'
        '• Strong foundation in Python programming\n'
        '• Object-oriented programming concepts\n'
        '• Django framework for web application development\n'
        '• RESTful API design principles\n'
        '• Session management and authentication\n'
        '• File handling and data processing\n\n'
        'Database Management:\n'
        '• SQL query writing and optimization\n'
        '• Database design and normalization\n'
        '• Django ORM for database operations\n'
        '• Understanding of relationships and joins\n'
        '• Data migration and schema management\n\n'
        'Development Tools:\n'
        '• Version control with Git\n'
        '• Integrated Development Environments (VS Code, PyCharm)\n'
        '• Command-line interface proficiency\n'
        '• Debugging and troubleshooting techniques\n'
        '• Package management (pip, npm)\n\n'
        'Soft Skills:\n'
        '• Problem-solving and analytical thinking\n'
        '• Time management and meeting deadlines\n'
        '• Team collaboration and communication\n'
        '• Adaptability to new technologies\n'
        '• Code documentation and commenting\n'
        '• Attention to detail and code quality\n\n'
        'Professional Development:\n'
        '• Understanding of software development lifecycle\n'
        '• Exposure to industry-standard coding practices\n'
        '• Experience with real-world project requirements\n'
        '• Client communication and requirement gathering\n'
        '• Code review and quality assurance processes\n\n'
        'Impact on Academic Project:\n'
        'The training at Netlink Software Group has been instrumental in the development of the Office Employee '
        'Management System (OEMS). The practical knowledge gained during the training has enabled me to:\n'
        '• Design and implement a scalable database architecture\n'
        '• Develop secure authentication and authorization mechanisms\n'
        '• Create responsive and user-friendly interfaces\n'
        '• Follow industry best practices and coding standards\n'
        '• Debug and troubleshoot complex issues efficiently\n'
        '• Manage project timeline and deliverables effectively\n\n'
        'The hands-on experience with Django framework and full-stack development has significantly enhanced my '
        'technical capabilities and prepared me for professional software development roles.')
run = skills_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== CHAPTER 6: TESTING ====================
ch6_title = doc.add_paragraph()
run = ch6_title.add_run('CHAPTER 6')
run.bold = True
run.font.size = Pt(14)

ch6_subtitle = doc.add_paragraph()
run = ch6_subtitle.add_run('TESTING AND VALIDATION')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

testing_text = doc.add_paragraph()
testing_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('Testing is a critical phase in software development to ensure the application functions correctly and meets '
        'the specified requirements. The Office Employee Management System has undergone various levels of testing.\n\n'
        'Testing Approach:\n\n'
        '1. Unit Testing:\n'
        '   - Testing individual components and functions\n'
        '   - Django\'s built-in testing framework\n'
        '   - Test cases for models, views, and forms\n'
        '   - Code coverage analysis\n\n'
        '2. Integration Testing:\n'
        '   - Testing interaction between different modules\n'
        '   - Database operations and ORM queries\n'
        '   - Form submission and validation\n'
        '   - Authentication and authorization flow\n\n'
        '3. Functional Testing:\n'
        '   - Testing complete user workflows\n'
        '   - Employee registration and login\n'
        '   - Attendance marking and reporting\n'
        '   - Leave application and approval process\n'
        '   - Report generation\n\n'
        '4. User Interface Testing:\n'
        '   - Responsive design across different devices\n'
        '   - Browser compatibility (Chrome, Firefox, Safari, Edge)\n'
        '   - Form validation and error messages\n'
        '   - Navigation and user experience\n\n'
        '5. Security Testing:\n'
        '   - Authentication and authorization mechanisms\n'
        '   - SQL injection prevention\n'
        '   - Cross-Site Scripting (XSS) protection\n'
        '   - CSRF token validation\n'
        '   - Password encryption and security\n\n'
        'Test Cases:\n\n'
        'Module: User Authentication\n'
        '• Test Case 1: Valid login credentials - Expected: Successful login\n'
        '• Test Case 2: Invalid credentials - Expected: Error message\n'
        '• Test Case 3: Password reset - Expected: Reset link sent\n'
        '• Test Case 4: Unauthorized access - Expected: Redirect to login\n\n'
        'Module: Attendance Management\n'
        '• Test Case 1: Mark attendance - Expected: Record saved successfully\n'
        '• Test Case 2: Duplicate attendance - Expected: Error message\n'
        '• Test Case 3: Generate report - Expected: Correct data displayed\n'
        '• Test Case 4: Date range filter - Expected: Filtered results\n\n'
        'Module: Leave Management\n'
        '• Test Case 1: Submit leave application - Expected: Application submitted\n'
        '• Test Case 2: Approve leave - Expected: Status updated to approved\n'
        '• Test Case 3: Reject leave - Expected: Status updated to rejected\n'
        '• Test Case 4: Check leave balance - Expected: Correct balance displayed\n\n'
        'Testing Tools:\n'
        '• Django Test Framework: For unit and integration testing\n'
        '• Browser Developer Tools: For frontend debugging\n'
        '• Postman: For API testing (if applicable)\n'
        '• Manual Testing: For user experience validation\n\n'
        'Issues Identified and Resolved:\n'
        '• Date format inconsistencies in different browsers\n'
        '• Form validation errors not displaying properly\n'
        '• Attendance report calculation errors\n'
        '• Responsive design issues on mobile devices\n'
        '• Session timeout handling\n\n'
        'Testing Results:\n'
        '• All critical functionalities are working as expected\n'
        '• Security vulnerabilities have been addressed\n'
        '• User interface is responsive and user-friendly\n'
        '• Performance is satisfactory for expected user load\n\n'
        'Future Testing Plans:\n'
        '• Load testing for concurrent users\n'
        '• Automated testing with Selenium\n'
        '• User acceptance testing (UAT)\n'
        '• Performance optimization based on test results')
run = testing_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== CHAPTER 7: CONCLUSION ====================
ch7_title = doc.add_paragraph()
run = ch7_title.add_run('CHAPTER 7')
run.bold = True
run.font.size = Pt(14)

ch7_subtitle = doc.add_paragraph()
run = ch7_subtitle.add_run('CONCLUSION AND FUTURE SCOPE')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

# 7.1 Conclusion
section_7_1 = doc.add_paragraph()
run = section_7_1.add_run('7.1 Conclusion')
run.bold = True
run.font.size = Pt(12)

conclusion_text = doc.add_paragraph()
conclusion_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('The Office Employee Management System (OEMS) project has been a comprehensive learning experience that '
        'has significantly enhanced my understanding of full-stack web development using Django framework. The project '
        'successfully demonstrates the practical application of concepts learned during academic coursework and '
        'industrial training at Netlink Software Group India Pvt. Ltd.\n\n'
        'Key Achievements:\n'
        '• Successfully designed and implemented a functional employee management system\n'
        '• Developed core modules for attendance tracking, leave management, and employee records\n'
        '• Created a secure authentication and authorization system\n'
        '• Implemented responsive user interfaces using Bootstrap\n'
        '• Gained hands-on experience with Django ORM and database management\n'
        '• Applied industry best practices and coding standards\n\n'
        'The project has met its primary objectives of automating employee management processes and providing a '
        'centralized platform for managing employee data. The system is capable of handling daily attendance, '
        'leave applications, and generating comprehensive reports.\n\n'
        'Learning Outcomes:\n'
        'Throughout this project, I have gained valuable experience in:\n'
        '• Full-stack web development with Python and Django\n'
        '• Database design and SQL operations\n'
        '• Frontend development with HTML, CSS, JavaScript, and Bootstrap\n'
        '• Software development lifecycle and project management\n'
        '• Problem-solving and debugging techniques\n'
        '• Testing and quality assurance\n\n'
        'The industrial training at Netlink Software Group has been instrumental in providing practical knowledge '
        'and real-world exposure to software development. The combination of academic learning and industrial training '
        'has prepared me well for professional software development roles.\n\n'
        'Challenges Overcome:\n'
        '• Understanding and implementing complex database relationships\n'
        '• Handling date and time calculations for attendance and payroll\n'
        '• Creating responsive designs that work across different devices\n'
        '• Implementing secure authentication mechanisms\n'
        '• Managing project timeline and deliverables\n\n'
        'Overall, the project has been successful in achieving its goals and has provided a solid foundation for '
        'future enhancements and professional development.')
run = conclusion_text.add_run(text)
run.font.size = Pt(11)

doc.add_paragraph()

# 7.2 Future Scope
section_7_2 = doc.add_paragraph()
run = section_7_2.add_run('7.2 Future Enhancements')
run.bold = True
run.font.size = Pt(12)

future_text = doc.add_paragraph()
future_text.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
text = ('The Office Employee Management System has significant potential for future enhancements and expansions:\n\n'
        'Short-term Enhancements:\n'
        '• Complete implementation of the Payroll module with tax calculations\n'
        '• Advanced reporting with charts and graphs using libraries like Chart.js\n'
        '• Email notifications for leave approvals and important updates\n'
        '• Export functionality for reports (PDF, Excel, CSV)\n'
        '• Employee self-service portal for updating personal information\n'
        '• Mobile-responsive improvements for better mobile experience\n\n'
        'Medium-term Enhancements:\n'
        '• Integration with biometric devices for automated attendance\n'
        '• Performance appraisal and review management module\n'
        '• Document management system for employee documents\n'
        '• Task and project management features\n'
        '• Calendar integration for leave and holiday management\n'
        '• Multi-language support for diverse user base\n'
        '• Advanced analytics and dashboard with predictive insights\n\n'
        'Long-term Enhancements:\n'
        '• Mobile application (Android/iOS) for on-the-go access\n'
        '• RESTful API development for third-party integrations\n'
        '• Integration with accounting software for payroll\n'
        '• AI-based attendance pattern analysis and anomaly detection\n'
        '• Chatbot for employee queries and support\n'
        '• Cloud deployment for scalability and accessibility\n'
        '• Multi-tenant architecture for serving multiple organizations\n'
        '• Advanced security features like two-factor authentication\n'
        '• Recruitment and onboarding module\n'
        '• Training and development tracking\n\n'
        'Technical Improvements:\n'
        '• Implementation of caching for improved performance\n'
        '• Microservices architecture for better scalability\n'
        '• Containerization using Docker\n'
        '• Continuous Integration/Continuous Deployment (CI/CD) pipeline\n'
        '• Comprehensive automated testing suite\n'
        '• Performance optimization and load balancing\n\n'
        'Business Expansion:\n'
        '• Customization options for different industries\n'
        '• White-label solution for reselling\n'
        '• SaaS model for subscription-based access\n'
        '• Integration marketplace for third-party plugins\n\n'
        'The modular architecture of the system allows for easy integration of these enhancements without major '
        'restructuring. The future scope demonstrates the scalability and extensibility of the current implementation.')
run = future_text.add_run(text)
run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== REFERENCES ====================
ref_title = doc.add_paragraph()
run = ref_title.add_run('REFERENCES')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

references = [
    'Django Documentation. (2024). Django Web Framework. Retrieved from https://docs.djangoproject.com/',
    'Python Software Foundation. (2024). Python Documentation. Retrieved from https://docs.python.org/',
    'Mozilla Developer Network. (2024). Web Development Documentation. Retrieved from https://developer.mozilla.org/',
    'Bootstrap Documentation. (2024). Bootstrap Framework. Retrieved from https://getbootstrap.com/docs/',
    'W3Schools. (2024). HTML, CSS, JavaScript Tutorials. Retrieved from https://www.w3schools.com/',
    'Stack Overflow. (2024). Programming Q&A Community. Retrieved from https://stackoverflow.com/',
    'Real Python. (2024). Python Tutorials and Articles. Retrieved from https://realpython.com/',
    'Django for Beginners by William S. Vincent',
    'Python Crash Course by Eric Matthes',
    'Web Development with Django by Ben Shaw, Saurabh Badhwar, Andrew Bird, Bharath Chandra K S',
]

for i, ref in enumerate(references, 1):
    ref_para = doc.add_paragraph()
    ref_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = ref_para.add_run(f'{i}. {ref}')
    run.font.size = Pt(11)

# Page Break
add_page_break(doc)

# ==================== APPENDIX ====================
app_title = doc.add_paragraph()
run = app_title.add_run('APPENDIX')
run.bold = True
run.font.size = Pt(14)
run.underline = True

doc.add_paragraph()

# Appendix A: Code Snippets
app_a = doc.add_paragraph()
run = app_a.add_run('Appendix A: Sample Code Snippets')
run.bold = True
run.font.size = Pt(12)

doc.add_paragraph()

code_intro = doc.add_paragraph()
run = code_intro.add_run('1. Django Model Example (Employee Model):')
run.font.size = Pt(11)
run.bold = True

code1 = doc.add_paragraph()
code1.alignment = WD_ALIGN_PARAGRAPH.LEFT
code_text = '''from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10, unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name()}"'''
run = code1.add_run(code_text)
run.font.name = 'Courier New'
run.font.size = Pt(9)

doc.add_paragraph()

code_intro2 = doc.add_paragraph()
run = code_intro2.add_run('2. Django View Example (Attendance View):')
run.font.size = Pt(11)
run.bold = True

code2 = doc.add_paragraph()
code2.alignment = WD_ALIGN_PARAGRAPH.LEFT
code_text2 = '''from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from datetime import date

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        employee = request.user.employee
        today = date.today()
        
        attendance, created = Attendance.objects.get_or_create(
            employee=employee,
            date=today,
            defaults={'status': 'Present'}
        )
        
        if created:
            messages.success(request, 'Attendance marked successfully!')
        else:
            messages.warning(request, 'Attendance already marked for today.')
        
        return redirect('dashboard')
    
    return render(request, 'attendance/mark_attendance.html')'''
run = code2.add_run(code_text2)
run.font.name = 'Courier New'
run.font.size = Pt(9)

doc.add_paragraph()
doc.add_paragraph()

# Appendix B: Screenshots
app_b = doc.add_paragraph()
run = app_b.add_run('Appendix B: System Screenshots')
run.bold = True
run.font.size = Pt(12)

screenshot_note = doc.add_paragraph()
run = screenshot_note.add_run('[Screenshots of the application interface would be included here, showing:]\n\n'
                              '• Login Page\n'
                              '• Admin Dashboard\n'
                              '• Employee List\n'
                              '• Attendance Marking Interface\n'
                              '• Leave Application Form\n'
                              '• Reports Page\n'
                              '• Employee Profile Page')
run.font.size = Pt(11)
run.italic = True

doc.add_paragraph()
doc.add_paragraph()

# Appendix C: Training Certificate
app_c = doc.add_paragraph()
run = app_c.add_run('Appendix C: Industrial Training Certificate')
run.bold = True
run.font.size = Pt(12)

cert_note = doc.add_paragraph()
run = cert_note.add_run('[Training certificate from Netlink Software Group India Pvt. Ltd. would be attached here]')
run.font.size = Pt(11)
run.italic = True

doc.add_paragraph()
doc.add_paragraph()

# Appendix D: Project Timeline
app_d = doc.add_paragraph()
run = app_d.add_run('Appendix D: Project Timeline')
run.bold = True
run.font.size = Pt(12)

timeline_table = doc.add_table(rows=7, cols=3)
timeline_table.style = 'Table Grid'

timeline_data = [
    ('Phase', 'Activity', 'Duration'),
    ('1', 'Requirement Analysis and Planning', '2 weeks'),
    ('2', 'Database Design and Setup', '1 week'),
    ('3', 'Authentication Module Development', '2 weeks'),
    ('4', 'Attendance Module Development', '3 weeks'),
    ('5', 'Leave Management Module Development', '3 weeks'),
    ('6', 'Testing and Bug Fixes', 'Ongoing'),
]

for i, (phase, activity, duration) in enumerate(timeline_data):
    row = timeline_table.rows[i]
    row.cells[0].text = phase
    row.cells[1].text = activity
    row.cells[2].text = duration
    
    for cell in row.cells:
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(10)
                if i == 0:
                    run.bold = True

# Save document
doc.save('/vercel/sandbox/OEMS_Project_Report_Kiran_Barode.docx')
print("Project report created successfully!")
print("File saved as: OEMS_Project_Report_Kiran_Barode.docx")
