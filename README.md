# personal-pdf-translator
	Esta  é uma ferramenta criada para ajudar o estudante a
dominar o inglês lendo PDFs originalmente em inglês. O objetivo da ferramenta
não é simplismente tradizir o documento inteiro, o objetivo desta ferramenta é
aumentar o vocabulário do estudante pois a ferramenta extrai somente as palavras
desconhecidas ao estudante e as traduz para que o estudante possa fazer uma rápida
consulta sem precisar ficar procurando traduzir o texto na íntegra, ou consultar
um dicionário.

	A ferramenta está sendo desenvolvida utilizando a linguagem Python, 
com o código fote aberto sob a lincensa livre do MIT.

	Para a execução é necessário a criação de uma lista de palavras conhecidas
ao estudante pois a ferramenta irá ignorar as palavras desta lista e traduzir somente
as palavras de um dado documento. É uma tarefa massante porém o resultado é
interessante. Um bom início é pegar uma lista das palavras mais comums em inglês
e deletar as palavras desconhecidas, pode-se utilizar a lista de 3000 palavras
que está no github do projeto. Uma estratégia que pode-se usar é percorrer 200
palavras por dia que resulta em 15 dias, cada lista é pessoal para cada estudante
para manter o objetivo de aumentar o vocabulario do estudante.

	Caso hipotético: Marcela precisa ler vários artigos científicos e livros
originalmente em inglês durante seu curso, e ela precisa dominar o inglês para 
sua carreira e vida pessoal. Ela entende que é mais fácil aumentar seu vocabulário
do que ter que ficar traduzindo todos os documentos que precisa, então ela decide
usar essa ferramenta.

	Ela começa criando sua lista de palavras utilizando como base a lista disponível
no github, originalmente ela deleta aproximadamente 1000 palavras desconhecidas, 
ficando com apenas aoproximadamente 2000 palavras em seu vocabulário. A primeira execução
sobre um artigo gerou 1200 palavras muitas das quais ela já conhecia então ela salvou essa 
lista, retirou as palavras desconhecidas e anexou ao seu vocabulario.txt. A segunda execução gerou uma
lista de apenas 150 palavras e suas traduções.

	Porceba que conforme ela vai aprendendo novas palavras e adicionando a
sua lista de palavras conhecidas, a cada execução a ferramenta traz somente aquelas
traduções realmente necessárias para a Marcela compreender aquele texto. Conforme
o tempo e o domínio de novas palavras a lista de palavras tende a "zero".
