from docxtpl import DocxTemplate
import datetime

def get_appeal_answer(appeal):
	print(appeal)
	return 1
	"""date_today = datetime.date.today()
	doc = DocxTemplate("appeal.docx")

	appeal_num = input('Номер обращения: ')
	appeal_create_date = input('Дата обращения: ')
	appeal_owner_name = input('ФИО: ')
	bsk_number = input('Номер БСК: ')

	answer = 'отложенный платеж успешно активирован 30.03.2021 на станции метро "Ленинский проспект".'

	context = { 'appeal_num' : str(appeal_num), 'appeal_create_date' : str(appeal_create_date), 'appeal_owner_name': str(appeal_owner_name), 'bsk_number': str(bsk_number), 'answer' : str(answer), 'date': date_today.strftime("%d.%m.%Y") }
	doc.render(context)

	doc.save("%s Отчет о рассмотрении обращения №%s %s.docx"%(date_today.strftime("%d.%m.%Y"), appeal_num, appeal_owner_name))"""