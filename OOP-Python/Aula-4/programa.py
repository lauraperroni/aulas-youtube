# Existem essas 3 formas de importar um namespace: (tire as aspas para testar cada uma!)

# A primeira forma ============================================

'''
import meu_namespace

print(meu_namespace.nome_de_usuario)
meu_namespace.funcao_do_namespace(mensagem='Bom dia!')
'''


# A segunda forma ============================================
'''
from meu_namespace import *

print(nome_de_usuario)
funcao_do_namespace(mensagem='Boa tarde')

'''


# A maneira mais correta: ====================================
'''
from meu_namespace import funcao_do_namespace

funcao_do_namespace(mensagem='Boa tarde')
'''
