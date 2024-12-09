from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def calcular(request):
    resultado = None
    if request.method == 'POST':  #Usei o método post para enviar os dados que o usuário colocou nos inputs. 
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operacao = request.POST.get('operacao')

            if operacao == 'adicao':
                resultado = num1 + num2
            elif operacao == 'subtracao':
                resultado = num1 - num2
            elif operacao == 'multiplicacao':
                resultado = num1 * num2
            elif operacao == 'divisao':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = 'Erro: Divisão por zero'
            else:
                resultado = 'Operação inválida'
        except ValueError:
            resultado = 'Erro: Insira valores válidos'
    
    return render(request, 'calculadora/calculadora.html', {'resultado': resultado})
