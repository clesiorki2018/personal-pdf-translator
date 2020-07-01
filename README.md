	Esta ferramenta está sendo desenvolvida  para ajudar o estudante a dominar o inglês lendo documentos PDFs
	originalmente em inglês. O objetivo da ferramenta não é simplesmente traduzir o documento inteiro, o objetivo
	desta ferramenta é aumentar o vocabulário do estudante pois a ferramenta extrai somente as palavras desconhe-
	cidas ao estudante e as traduz para que o estudante possa fazer uma rápida consulta sem precisar ficar procu-
	rando traduzir o texto na íntegra, ou consultar um dicionário.

	A ferramenta está sendo desenvolvida utilizando a linguagem Python na versão 3.x, com o código fonte aberto e
	livre sob a licença livre do MIT.

	Para a execução faz-se necessário a instalação das dependências e  a criação de uma lista de palavras conhe-
	cidas ao estudante, pois a ferramenta irá ignorar as palavras desta lista e traduzir somente as palavras des-
	conhecidas de um dado documento. Formar esta lista é uma tarefa massante porém o resultado é interessante e 
	gratificante. Um bom início é pegar uma lista das palavras mais comuns em inglês e deletar as palavras desco-
	nhecidas, pode-se utilizar a lista de 3000 palavras que está no github do projeto. Uma estratégia que pode-se
	usar é percorrer 200 palavras por dia que resulta em 15 dias, cada lista é pessoal para cada estudante para 
	manter o objetivo de aumentar o vocabulário do estudante.
	
	o arquivo example.php é apenas uma página do ebook "2018_Book_ResearchMethodsForTheDigitalHu.pdf" que foi 
	disponibilizado gratuitamente pela editora durante a pandemia do COVID-19

	As dependências são as bibliotecas PyPDF2 e googletrans para isso na linha de comando do seu sistema operacio-
	nal execute os seguintes comandos:
	
	$ pip3 install pyPDF2
	$ pip3 install googletrans
