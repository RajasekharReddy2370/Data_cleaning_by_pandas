# import pandas as pd
# import pdfkit
# from jinja2 import Template
# # Read the HTML template
# with open('Template1.html') as file:
#     template_content = file.read()
# df=pd.read_excel(r"/home/rajashekar/Downloads/prac (1).xlsx")
# data = df.to_dict(orient='list')
#
# # pdfkit_config = pdfkit.configuration(wkhtmltopdf=r"/home/rajashekar/Downloads/wkhtmltox-0.12.6-1.msvc2015-win64.exe")
# # Iterate over the data and generate PDFs
# for i in range(len(df)):
#     # Render the template with current data
#     # rendered_content = Template(template_content).render({key: value[i] for key, value in data.items()})
#     # print('rendered_content',rendered_content)
#     # Output PDF file path
#     output_pdf_path = f"output_{i + 1}.pdf"
#     # Convert HTML to PDF using PDFKit
#     # pdfkit.from_string('Template1', output_path=output_pdf_path)
#     pdfkit.from_file('/home/rajashekar/WORK/voters_prac/Template1.html', output_path=output_pdf_path,css='/home/rajashekar/WORK/voters_prac/Template.css')
#     print(f"PDF {i + 1} generated successfully.")

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


import pandas as pd
from docx import Document
import os

# def generate_pdf(file_name, content):
#     pdf = SimpleDocTemplate(file_name, pagesize=letter, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
#
#     styles = getSampleStyleSheet()
#
#     # Modify the style with the desired font size
#     custom_style = styles["Normal"]
#     custom_style.fontSize = 11  # Adjust font size as needed
#
#     p = Paragraph(content.replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;').replace('\n', '<br/>'), custom_style)
#
#     pdf.build([p])

def generate_pdf(file_name, content):
    # pdf = SimpleDocTemplate(file_name, pagesize=letter, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
    pdf = SimpleDocTemplate(file_name, pagesize=letter, leftMargin=50, rightMargin=50, topMargin=35, bottomMargin=50)

    styles = getSampleStyleSheet()

    # Modify the style with the desired font size and line spacing
    custom_style = styles["Normal"]
    custom_style.fontSize = 11  # Adjust font size as needed
    custom_style.leading = 13 # Adjust line spacing as needed (16 is equivalent to 1.5 times font size)

    p = Paragraph(content.replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;').replace('\n', '<br/>'), custom_style)

    pdf.build([p])


df = pd.read_excel(r"/home/rajashekar/WORK/voters_prac/GTR.xlsx")

# Path to the Word document template
template_file_path = "/home/rajashekar/Downloads/FORM_NEW_12D (1).docx"

# Check if the template file exists
if not os.path.exists(template_file_path):
    print(f"Error: Template file '{template_file_path}' not found.")
else:
    try:
        # Read the Word document template
        template_doc = Document(template_file_path)

        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            print(row['Voter_id'])
            # if row['RLN_TYPE'] == 'F':
            #     row['RLN_TYPE'] = 'Father'
            # if row['RLN_TYPE'] == 'M':
            #     row['RLN_TYPE'] = 'Mother'
            # if row['RLN_TYPE'] == 'H':
            #     row['RLN_TYPE'] = 'Husband'
            rt_dict = {'M_F':'son','F_F':'daughter','M_H':'husband','F_H':'wife','M_M':'son','F_M':'daughter',
                       'M_G':'guardian','F_G':'guardian','M_L':'guardian','F_L':'guardian','M_O':'guardian',
                       'F_O':'guardian','M_W':'guardian','F_W':'guardian'}
            # print(str(row['G']+'_'+row['RLN_TYPE']))
            # Generate form text based on DataFrame values
            rel_type = rt_dict.get(str((row['G']+'_'+row['RLN_TYPE'])))
            if rel_type is None:
                rel_type = 'guardian'
            form_text = f'''\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b>FORM 12D</b> \n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b>[see rule 27-C]</b> \n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b>PART I</b> \n\n\t\t\t\t\t\t\t\t\t\tLetter of intimation to Assistant Returning Officer \n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t(for absentee voters) \n To \n\n  The Assistant Returning Officer \n\n (for the notified class of electors) \n\n <b>94_Guntur West</b> Parliamentary/Assembly constituency \n\n  ....................................(designation and address of ARO) \n 
                            Sir, \n\n I, <b>{row['Names']}</b> {rel_type} of <b>{row['RLN_FM_NM_EN']}</b>, resident of <b>{row['Address_eng']}</b> village/mohalla <b>Guntur</b> Town/city/tehsil <b>Guntur</b> District, <b>Andhrapradesh</b> (State) belong to the class of absentee voter and wish to cast my vote by post at the election to the House of the People/Legislative Assembly from the <b>94-Guntur West</b> Parliamentary/Assembly constituency. \n
                            My complete present postal address is as under:- \n\n  House/dwelling unit/tent number : <b>{row['House No']}</b> \n\n Camp/mohalla/village : <b>{row['Address_eng']}</b> \n\n Ward/town/tehsil : <b>Guntur</b> \n\n District : <b>Guntur</b> \n\n State : <b>Andhrapradesh</b>, PIN CODE : <b>522002</b>.\n
                            My name is entered at serial number <b>{int(row['S'])}</b> in part No <b>{row['B#']}</b> of the electoral roll for <b>94-Guntur West</b> \n\n Assembly constituency.\n\n I am working as ..................(Designation of the office held) in ................. \n\n (Name and full address of organization) \n\n                            
                            I will be on duty in the above-mentioned office on the day of poll for the above-mentioned election. \n\n  *On account of my official duties on the date of poll, I will not be in a position to be present in the \n\n polling station assigned to me on the day of poll. \n\n  or \n\n *I am <b>{row['Age']}</b> years of age/am a person with disability, and am not in a position to go to the polling station \n\n to cast vote. \n\n                                                                                                                                                                                                                                                                                                                                                                                                     
                            It is requested that postal ballot paper may be issued to me as absentee voter for the above election.\n\n
                            \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYours faithfully, \n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t .............................. \n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t(Full Name and Signature) \n\n 
                            \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t <b>PART 2</b>  \n\n\t\t\t\t(for absentee voter other than senior citizen or persons with disability) \n
                            Certificate by the nodal officer appointed by the Organization concerned.\n\n
                            It is hereby certified that the particulars given by the applicant in Part I are correct, and it is further \n\n certified that the applicant will be on official duty on the day of poll, and he/she will not be in a position \n\n to be present in the polling station on the day of poll. \n
                            \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t................................ \n\n
                            \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t (full signature of the attesting Officer) \n\n
                            \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t.............................(Name) \n\n
                            \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ............................(address) \n\n
                            \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t.................................(rubber stamp) \n\n
                            • Strike off whichever is not applicable and tick the relevant statement.\n\n
                            <b>Note-</b> This Application must reach RO within 5 days following the date of notification of election'''


            # generate_pdf(f'{row["B#"]}_{row["Names"]}.pdf', form_text)
            # generate_pdf(f'{row[]}.pdf', form_text)
            # Generate PDF
            generate_pdf(f'/home/rajashekar/Documents/conversion_files/{int(row["B#"])}_{row["Names"]}.pdf', form_text)
            # break

    except Exception as E:
        print(E)

