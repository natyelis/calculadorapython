#!/bin/bash
echo "Digite um número:"
read num1
echo "Digite o segundo número:"
read num2
echo "Escolha uma operação (+ para somar, - para subtrair, * para multiplicar, / para dividir):"
read  op

if [ "$op" = "+" ]; then
  echo "Resultado: $(($num1 + $num2))"
elif [ "$op" = "-" ]; then
  echo "Resultado: $(($num1 - $num2))"
elif [ "$op" = "*" ]; then
  echo "Resultado: $(($num1 * $num2))"
elif [ "$op" = "/" ]; then
  echo "Resultado: $(($num1 / $num2))"

python3 calculadora.py
