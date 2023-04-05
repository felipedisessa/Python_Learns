from django.db import models

class Produto(models.Model):
	id_prod = models.CharField(max_length=20)
	nome = models.CharField(max_length=20)
	preco= models.CharField(max_length=20)
	validade = models.CharField(max_length=20)
	lote = models.CharField(max_length=20)

class vendas(models.Model):
	id_vendas = models.CharField(max_length=20)
	id_produto = models.CharField(max_length=20)
	data = models.CharField(max_length=20)
	produto = models.CharField(max_length=20)
	cod = models.CharField(max_length=20)

class vendedor(models.Model):
	id_vendedor = models.CharField(max_length=20)
	nome = models.CharField(max_length=20)
	cpf = models.CharField(max_length=20)
	telefone = models.CharField(max_length=20)
	cargo = models.CharField(max_length=20)  
 
 
v1 = vendedor(id_vendedor='1', nome='fernando',cpf='43267876544',telefone='33423456' ,cargo='vendedor')
v2 = vendedor(id_vendedor='2', nome='luis',cpf='4272345679',telefone='33433012' ,cargo='vendedor')

p1 = Produto(id_prod='10' ,nome='arroz', preco='30', validade='15/10/2022',lote='15')
p2 = Produto(id_prod='20' ,nome='feijao', preco='40', validade='17/10/2022',lote='25')
p3 = Produto(id_prod='30' ,nome='aovo', preco='10', validade='19/10/2022',lote='65')

vendas1 = vendas(id_vendas='20', id_produto='10', data='14/10/2022', produto='arroz', cod='3456')
vendas2 = vendas(id_vendas='30', id_produto='15', data='13/10/2022', produto='feijao', cod='3267')
vendas3 = vendas(id_vendas='40', id_produto='20', data='12/10/2022', produto='carne', cod='1298')
vendas4 = vendas(id_vendas='50', id_produto='50', data='11/10/2022', produto='ovo', cod='2376')
vendas5 = vendas(id_vendas='60', id_produto='60', data='10/10/2022', produto='bolacha', cod='7654')

p1.id_prod = '30'
p1.save

p2.id_prod = '90'
p1.save

p3.id_prod = '340'
p1.save


