# Time_equals

A classe `Time_equals` é usada para comparar a hora atual com horas específicas e retornar uma mensagem correspondente.

## Uso

Para utilizar a classe `Time_equals`, siga estes passos:

1. Importe a classe `Time_equals` do módulo onde ela está definida.

   ```python
   from datetime import datetime, timedelta
   from time_equals import Time_equals

2. Crie uma instância da classe Time_equals.

    ```python
    time = Time_equals()

3. Chame o método time_equal() para comparar a hora atual com as horas específicas.

    ```
    resultado = time.time_equal()
    print(resultado)

# Métodos
## time_equal()
Este método compara a hora atual com as horas específicas e retorna uma mensagem correspondente. Os possíveis valores de retorno são:

* `'Horario XX'`: se os minutos e horas atuais coincidirem com a hora especificada.
* `'Dif 5minutes'`: se os minutos atuais estiverem dentro de 5 minutos após a hora especificada.
* `'Fora de horario'`: caso contrário, quando a hora atual não coincidir com as horas específicas.
catch_minutes()
Este método obtém os minutos atuais e retorna um valor inteiro.

### catch_hours()
Este método obtém as horas atuais e retorna um valor inteiro.

### diff_5minutes()
Este método calcula a hora correspondente a 5 horas após a hora atual e retorna o valor da hora.

# Exemplo
Aqui está um exemplo de uso da classe Time_equals:
```
from datetime import datetime, timedelta
from time_equals import Time_equals

# Cria uma instância da classe
time = Time_equals()

# Obtém a mensagem correspondente para a hora atual
resultado = time.time_equal()

# Imprime o resultado
print(resultado)
```
Neste exemplo, a mensagem correspondente à hora atual será impressa no console.

