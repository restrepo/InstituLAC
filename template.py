import pandas as pd

#Initialize the Output Excel File
writer = pd.ExcelWriter('template.xlsx', engine='xlsxwriter')


#Global variables
abstract_text='VERIFICACIÓN DE INFORMACIÓN PARA OTORGAR AVAL A LOS GRUPOS DE INVESTIGACIÓN  E INVESTIGADORES PARA SU PARTICIPACIÓN EN LA CONVOCATORIA 894 DE 2021 DE MINCIENCIAS'
instructions='''Los grupos de investigación e investigadores de la Universidad de Antioquia que deseen participar en la Convocatoria Nacional para el reconocimiento y medición de grupos de investigación, desarrollo tecnológico o de innovación y para el reconocimiento de investigadores del Sistema Nacional de Ciencia, Tecnología e Innovación - SNCTI, 894 de 2021, deben presentar la información actualizada en las plataformas CvLAC y GrupLAC validada por el Centro de Investigación en el presente formato, y respaldada en el repositorio digital de evidencias dispuesto para este fin, para la obtención del aval institucional por parte de la Vicerrectoría de Investigación. 

La información a validar corresponde a los años 2019-2020 y aquella que entra en la ventana de observación y debe ser modificada según el Modelo de medición de grupos. La validación comprende:

1. Verificación de la vinculación de los integrantes a la Universidad de Antioquia y al grupo de investigación.  Diligenciar los campos solicitados. 

2. Verificación de la producción de GNC, DTeI, ASC y FRH, en los campos habilitados en cada hoja de este formato. Las evidencias requeridas para los productos deben ser anexadas al repositorio digital asignado al grupo y se deben enlazar a cada producto.  

Este documento debe ser diligenciado en línea.

De antemano, la Vicerrectoría de Investigación agradece su participación en este ejercicio, que resulta de vital importancia para llevar a buen término la Convocatoria de Reconocimiento y Medición de Grupos de Investigación
'''
#Final part of the first sheet
datos=pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vTp7cVkcQYoLvuPgs04O6_DeC_klRtPVhzLJ1VLxCek6MchPpoAmUCr-5wuJ3Lc9C9JwhxmxdmYy7E5/pub?output=xlsx')
#Example of Table → Like the one generated by the Scrapping
table=pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vTp7cVkcQYoLvuPgs04O6_DeC_klRtPVhzLJ1VLxCek6MchPpoAmUCr-5wuJ3Lc9C9JwhxmxdmYy7E5/pub?output=xlsx',
                     sheet_name='4.ART y N').fillna('')

#Capture xlsxwriter object 
# IMPORTANT → workbook is the same object used in the official document at https://xlsxwriter.readthedocs.io
workbook=writer.book
#***************
#Styles as explained in https://xlsxwriter.readthedocs.io
general=workbook.add_format({'text_wrap':True})
title=workbook.add_format({'font_size':28,'center_across':True})
subtitle=workbook.add_format({'font_size':24,'center_across':True})
abstract=workbook.add_format({'font_size':20,'center_across':True,'text_wrap':True})
normal=workbook.add_format({'font_size':12,'text_wrap':True})
merge_format = workbook.add_format({
    'bold': 1,
    'border':1,
    'text_wrap': True,    
    'align': 'center',
    'valign': 'vcenter',
    'font_color': 'blue'})
fmt_header = workbook.add_format({
    'bold': True,
    'align': 'center',    
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#33A584',
    'font_color': '#FFFFFF',
    'border': 1})
#***************
#Creates the first work-sheet
#IMPORTANT → worksheet is the same object  used in the official document at https://xlsxwriter.readthedocs.io
worksheet=workbook.add_worksheet("1.Presentación")
#Prepare image insertion: See → https://xlsxwriter.readthedocs.io/example_images.html
worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)
worksheet.insert_image('A1', 'img/udea.jpeg')
#Prepare text insertion: See  → https://xlsxwriter.readthedocs.io/example_images.html
worksheet.set_column('C:C', 140,general)
worksheet.set_row_pixels(0, 60)
#Texts
worksheet.write('C1', 'UNIVERSIDAD DE ANTIOQUIA',title)
worksheet.set_row_pixels(2, 60)
worksheet.write('C3', 'VICERRECTORÍA DE INVESTIGACIÓN',subtitle)
worksheet.set_row_pixels(5, 100)
worksheet.write('C6', abstract_text,abstract)
worksheet.set_row_pixels(8, 40)
worksheet.write('C9','PRESENTACIÓN DEL EJERCICIO',
                workbook.add_format({'font_size':18,'center_across':True}) )
worksheet.set_row_pixels(10, 320)
worksheet.write('C11',instructions,normal )
#*** ADD PANDAS DATAFRAME IN SPECIFIC POSITION ****
#Add a data Frame in some specific position. See → https://stackoverflow.com/a/43510881/2268280
#                                       See also → https://xlsxwriter.readthedocs.io/working_with_pandas.html
writer.sheets["1.Presentación"]=worksheet
datos.to_excel(writer,sheet_name="1.Presentación",startrow=12,startcol=2,index=False)
#**************************************************
#Fix columns heights for long text
worksheet.set_row_pixels(17, 40)
worksheet.set_row_pixels(18, 40)
worksheet.set_row_pixels(19, 40)
worksheet.set_row_pixels(20, 40)
worksheet.set_row_pixels(22, 40)

#Creates second work-sheet
# "4.ART y N" → work-sheet
worksheet2=workbook.add_worksheet("4.ART y N")
# See Merger Columns → https://xlsxwriter.readthedocs.io/example_merge1.html
worksheet2.merge_range('C1:I1', 'Información suministrada por la Vicerrectoría de Investigación', merge_format)
worksheet2.merge_range('J1:M1', 'Validación del Centro, Instituto o Corporación', merge_format)
#Add a data Frame in some specific position. See → https://stackoverflow.com/a/43510881/2268280
#                                       See also → https://xlsxwriter.readthedocs.io/working_with_pandas.html
writer.sheets["4.ART y N"]=worksheet2
table.to_excel(writer,sheet_name="4.ART y N",startrow=1,startcol=2,index=False)
worksheet2.set_row_pixels(1, 60)
#Overwrite the header row of the table with the proper format
#...See → https://link.medium.com/fniEH6hMxfb
for col , value in enumerate(table.columns.values):
    worksheet2.write(1, col+2, value, fmt_header)
#Increase the width of a specific column and add some formatting    
worksheet2.set_column('C:C',30,general)
# Add extra headers
worksheet2.write(1, 0, 'VoBo de VRI', merge_format)
#New columns
extra_url='Si no tiene URL o DOI agregue una evidencia en el repositorio digital y genere un hipervínculo en este campo'
cols=['DOI',extra_url,'¿El producto cumple con los requisitos para ser avalado?']
for col , value in enumerate(cols):
    worksheet2.write(1, col+2+table.columns.size, value, fmt_header)
worksheet2.set_column('L:L',20)
worksheet2.set_column('M:M',20)
#Creates a set of cells with a drop-down menu Sí/No. See → https://xlsxwriter.readthedocs.io/working_with_data_validation.html
worksheet2.data_validation('M3:M{}'.format(table.shape[0]+2), {'validate': 'list',
                                  'source': ['Sí', 'No']})


workbook.close()
