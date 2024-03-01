# SN Formatter

## Descrição
Este é um programa Python simples que formata uma sequência de números, inserindo uma vírgula a cada 9 dígitos. Ele foi projetado especificamente para formatar números de série (SN's) para atualização no Salesforce.

## Como usar
1. Execute o programa.
2. Quando solicitado, insira os números das notas.
3. O programa irá formatar os números, inserindo uma vírgula a cada 9 dígitos.
4. Se houver uma grande quantidade de SN's, o programa fará a divisão automática em grupos menores para serem inseridos separadamente no Salesforce.
5. Após a formatação, o programa abrirá automaticamente o Salesforce para edição.
6. Quando terminar, você pode escolher fechar o programa ou continuar formatando mais números.

## Observações
- Para grandes quantidades de SN's, o programa faz a divisão automática em grupos menores para serem inseridos separadamente no Salesforce.
- Cada um desses grupos deve ser colocado como ERP Document equals SN's do Grupo X, e deve ser adicionado uma Lógica nos filtros de acordo com o número de grupos.
- Por exemplo, para 3 grupos adicione a lógica, 1 OR 2 OR 3.

## Autoria
Este formatador foi feito por Pedro Aufieri. Qualquer dúvida, procure-o no Microsoft Teams.

## Código Aberto
Este projeto é de código aberto.
