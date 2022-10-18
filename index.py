from copy import copy
import csv

from order import Order

import jinja2


headers = []
rows = []

qnt_categories = input("How many categories exists in this event? ")

categories = []

for n in range(0, int(qnt_categories)):
  name = input(f'Please, set category name ({n+1}): ')
  categories.append(name)

with open("./test.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    info = {}
    categories_info = {}

    headers = csvreader.fieldnames
    # final_header =  {'Qual o seu nome completo?': {'new_name': 'Nome', 'category': '0'}, 'Marguerita': {'new_name': 'Margerita', 'category': '1'}, 'Calabresa': {'category': '1'}, 'Presunto e Mussarela': {'category': '1'}, 'Marguerita e Calabresa': {'category': '1'}, 'Marguerita e Presunto/Mussarela': {'category': '1'}, 'Calabresa e Presunto/Mussarela': {'category': '1'}, 'Brigadeiro': {'category': '2'}, 'Leite Ninho': {'category': '2'}, 'Mulatinho': {'category': '2'}, 'Misto ': {'category': '2'}, 'Pavê de Chocolate': {'category': '2'}}

    print("Escolha qual informação deve ir para o pedido. Você também pode renomeá-lo.\n")

    choices = [f'{index} - {item}' for index, item in enumerate(headers)]
    choices = '\n'.join(choices)

    print(f'Informações:\n{choices}\n')
    name = int(input('Qual dessas informações representa o nome da pessoa que realizou o pedido? '))
    for category in categories:
      category_choice = input(f'Quais dessas informações fazem parte da categoria {category}? (ex.: 1,2,3,4)\n')
      categories_info[category] = category_choice.split(',')

    # for info in headers:
    #   new_info = {}
    #   print(f"Informação: {info}")

    #   keep = input("Deseja manter essa informação? (y/N)")

    #   if not keep or keep.lower() == 'n':
    #     continue
      
    #   print("Você decidiu manter esta informação\n")
    #   rename = input("Deseja renomea-la? (y/N) ")

    #   if rename.lower() == 'y':
    #     new_name = input("Digite o nome desejado para esta info: ")
    #     new_info['new_name'] = new_name.lstrip()
      
    #   category = input("Categorias: \n 0 - Nome \n 1 - Pedido principal \n 2 - Doces\n Escolha uma categoria para esta info: ")
    #   new_info['category'] = category
    #   final_header[info.lstrip()] = new_info
    
    # print(f"Informações: {final_header}")


    orders = []
    for row in csvreader:
      orders.append(Order(row, categories_info, name))
    
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "test.html.jinja2"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render({'informations':orders, 'categories':categories})

with open('finalFile.html', 'w') as final:
  final.write(outputText)