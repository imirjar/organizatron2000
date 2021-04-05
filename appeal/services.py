from docxtpl import DocxTemplate
import datetime
import pathlib

def appeal_generate_docx(appeal):
	date_today = datetime.date.today()
	doc = DocxTemplate("C:\\Users\\zadorov.aa\\Documents\\web\\organizatron2000\\static\\docs\\appeal.docx")

	appeal_num = appeal.appeal_num
	appeal_create_date = appeal.appeal_create_date
	appeal_owner_name = appeal.appeal_owner_name
	bsk_number = appeal.bsk_number

	answer = appeal.answer

	context = { 'appeal_num' : str(appeal_num), 'appeal_create_date' : str(appeal_create_date.strftime("%d.%m.%Y")), 'appeal_owner_name': str(appeal_owner_name), 'bsk_number': str(bsk_number), 'answer' : str(answer), 'date': date_today.strftime("%d.%m.%Y") }
	doc.render(context)
	pathlib.Path("C:\\Users\\zadorov.aa\\Documents\\web\\organizatron2000\\static\\appeal\\%s"%date_today.strftime("%d.%m.%Y")).mkdir(parents=True, exist_ok=True) 
	doc.save("C:\\Users\\zadorov.aa\\Documents\\web\\organizatron2000\\static\\appeal\\%s\\%s Отчет о рассмотрении обращения №%s %s.docx"%(date_today.strftime("%d.%m.%Y"),date_today.strftime("%d.%m.%Y"), appeal_num, appeal_owner_name))

def check_generated_file():
	pass