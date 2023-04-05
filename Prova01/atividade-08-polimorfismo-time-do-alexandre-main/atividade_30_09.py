import requests
import json
r =requests.get('http://universities.hipolabs.com/search?country=United+States')
universidades = json.loads(r.text)



class simples:
    def __init__(self,name,country,alpha_two_code):
        self.name = name
        self.country = country
        self.alpha_two_code = alpha_two_code
    def printaatributo_simples(self):
        print(self.name)

class compostos(simples):
    def __init__(self, domains, web_pages):
        self.domains = domains
        self.web_pages = web_pages
    def printaatributo_composto(self):
        print(f"Domains: {self.domains[0]} Qtd =  {len(self.domains)}")


vaar = False
lista1 = []


for uni in universidades:
    if vaar:
        objeto_2 = simples(uni['name'], uni['country'], uni['alpha_two_code'])
        #objeto_2.printaatributo_simples()
        vaar = False
        lista1.append(objeto_2)
    else:
        objeto_3 = compostos(uni['domains'], uni['web_pages'])
        #objeto_3.printaatributo_composto()
        vaar = True
        lista1.append(objeto_3)

    print("-----------")
print(lista1)



    """
    PARTICIPANTES
    ALEXANDRE
    VINICIUS AURELIO
    PEDRO FONTES
    """

