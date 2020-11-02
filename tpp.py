#!/usr/bin/env python3                                                                                                                                                                                                                                                                                        #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filename: tpp.py
# TTP Tradutor Pessoal de PDFs
# Brasilia, Brasil maio de 2020
# @Author Clesio Maxuel
# @Mail clesiorki2014@gmail.com
#                                                                   
# tentei manter os nomes de funções e nomes de variáveis em inglês, mas como
# sou apenas um eterno estudante... 
                                   
import PyPDF2                        # Biblioteca para extrair os textos de ar-
                                     # quivos PDFs
import string                        # Biblioteca que possui constantes que se-
                                     # rão úteis
import re                            # Biblioteca de expressões regulares
from googletrans import Translator   # Tradutor Python com API do Google
import sys                           # Biblioteca de sistema utilizada para ma-
                                     # nipular os argumentos de linha de comando
import time                                


class TradutorPessoalPdf(object):
    def __init__(self,argv):
        self.argv = argv
        self.wordlist_file_path = None
        self.pdf_file_path = None
        self.output_file_path = None
        self.not_translate = False
        self.words = False
        self.pdf_words_set = None
        self.wordlist = None
        self.unknow_words = None
        self.translator = Translator()
        self.words_translateds = {}
        self.parse_args(self.argv)
        self.proccess_items()


    def parse_args(self,argv):
        args_valids_by_arg = {'wordlist':['--wordlist','-w'],\
                                'pdf':['--pdf', '-p'],\
                                'output':['--output','-o'],\
                                'not_translate':['--not-translate','-n'],\
                                'words':['--words','-W'],\
                                'help':['--help','-h']}
        args_valids = []
        for key, value in args_valids_by_arg.items():
            for item in value:
                args_valids.append(item)

        if len(argv) == 1:
            self.help()
        else: 
            for index in range(len(argv)):
                try:
                    if argv[index] in args_valids_by_arg['wordlist']:
                        if args[index+1] in args_valids:
                            self.help()
                        else:
                            self.wordlist_file_path = args[index+1]
                    elif argv[index] in args_valids_by_arg['pdf']:
                        if args[index+1] in args_valids:
                            self.help()
                        else:
                            self.pdf_file_path = argv[index+1]
                    elif argv[index] in args_valids_by_arg['help']:
                        self.help()
                    elif argv[index] in args_valids_by_arg['output']:
                        if args[index+1] in args_valids:
                            self.help()
                        else:
                            self.output_file_path = args[index+1]
                    elif argv[index] in args_valids_by_arg['not_translate']:
                        self.not_translate = True
                    elif argv[index] in args_valids_by_arg['words']:
                        self.words = True
                except:
                    self.help()


    def proccess_items(self):
        if self.wordlist_file_path == None and not self.words:
            self.help()
        if self.pdf_file_path == None:
            self.help()
        
        self.pdf_words_set = self.load_pdf_words(self.pdf_file_path)
        if not self.words:
            self.wordlist = self.load_know_words(self.wordlist_file_path)
            self.unknow_words = self.pdf_words_set - self.wordlist
            self.unknow_words = list(self.unknow_words)
            self.pdf_words_set = list(self.pdf_words_set)
            self.wordlist = list(self.wordlist)
            self.unknow_words.sort()
            self.pdf_words_set.sort()
            self.wordlist.sort()
            if not self.not_translate:
                self.translate()
        self.output()


    def output(self):
        if self.output_file_path == None:
            if self.not_translate:
                print(type(self.unknow_words))
                for word in self.unknow_words:
                    print(word)
                return
            if self.words:
                for word in self.pdf_words_set:
                    print(word)
                return
            if self.not_translate:
                for word in self.unknow_words:
                    print(word)
                return
            for word, result in self.words_translateds.items():
                print(word,result)
        else:
            with open(self.output_file_path, 'w') as out:
                if self.not_translate:
                    print(type(self.unknow_words))
                    for word in self.unknow_words:
                        out.write(word+'\n')
                    return
                if self.words:
                    for word in self.pdf_words_set:
                        out.write(word+'\n')
                    return
                if self.not_translate:
                    for word in self.unknow_words:
                        out.write(word+'\n')
                    return
                for word, result in self.words_translateds.items():
                    out.write(word+' '+result+'\n')


    def translate(self):
        count = 0
        for word in self.unknow_words:
            count += 1
            word = self.translator.translate(word,src='en',dest='pt')
            #print(word.origin,word.text)
            self.words_translateds[word.origin] = word.text
            time.sleep(0.1)
            #if count >= 5:
                #print(self.words_translateds)
                #break

        

    # Esta função retorna um conjunto de palavras extraídas de um arquivo
    # recebe como parâmetro o nome do arquivo, percorre o arquivo considerando cada 
    # linha como uma palavra.
    # Nesta implementação básica apenas foram adicionadas possíveis terminações para
    # considerar palavras singulares e plurais, não havendo nenhuma implementação
    # robusta neste sentido ainda...
    def load_know_words(self,path_file_know_words):

        know_words = set()  # O "set" do Python é uma classe que não permite dados 
                            # duplicados.
            
        try:
            file_know_words = open(path_file_know_words,'r')
            
            for row in file_know_words.readlines():
                for word in row.split():
                    word = (word.lower().strip())
                    know_words.add(word)
                    know_words.add(word+'s')
                    know_words.add(word+'rs')
                    know_words.add(word+'ers')

            for caracter in string.ascii_lowercase:
                know_words.add(caracter)

            file_know_words.close()

        except:
            print('[erro!] Falha ao abrir o arquivo: %s'%path_file_know_words)
            sys.exit(1)

        return know_words


    # Esta função recebe o nome do arquivo PDF como parâmetro e retorna um conjunto
    # de palavras encontradas no PDF.
    def load_pdf_words(self,pdf_file_path):
        pdf_file = None
        wordlist = set()
        pdf_file = PyPDF2.PdfFileReader(pdf_file_path)
        
        for page in range (pdf_file.getNumPages()):
            words = self.clear_text(pdf_file.getPage(page).extractText())
            for word in words:
                wordlist.add(word)
        
        return wordlist                                                                             


    # Esta função faz o tratamento em um texto recebido como parâmetro e retorna um
    # conjunto com as palavras "normalizadas".
    def clear_text(self,text):

        # Remove todos os dígitos de 0 a 9.
        raw_text = re.sub("\d","",text)                                           

        # Transforma todas as letras para caixa baixa.
        raw_text = raw_text.lower()

        # Preserva apenas as letras de 'a' a 'z' e os espaços em branco.
        raw_text = re.sub("[^a-z|\s]|\|","", raw_text)

        # Remove os espaços em branco em excesso.
        raw_text = raw_text.strip()

        # Subistitui cada quebra de linha por um espaço em branco.
        raw_text = str(raw_text.replace("\n"," "))

        # Divide o texto em palavras, ordena alfabeticamente, e remove as duplicadas
        words_set = raw_text.split()
        words_set.sort()
        words_set = set(words_set)                                               

        return words_set                           

    # Função para mostrar ajuda ao usuário    
    def help(self):
        program_name = self.argv[0]
        print()
        print('Modo de uso: %s [opções] [arquivo pdf]'%program_name)
        print('Opções:')
        print('\tOpção\t\tAbreviatura\tArgumento\t\tDescrição')
        print('\t--help\t\t-h\t\t\t\t\tExibe esta ajuda.')
        print('\t--pdf\t\t-p\t\t<arquivo pdf>\t\tEspecifica o arquivo PDF para extrair as palavras.')
        print('\t--wordlist\t-w\t\t<arquivo de lista>\tEspecifica o a lista de palavras conhecidas ao usuário.')
        print('\t--output\t-o\t\t<arquivo de saída>\tEspecifica o arquivo de saída, se não especificado a saída é exibida na tela.')
        print('\t--not-translate\t-n\t\t\t\t\tNão traduz as as palavras apenas exibe as palavras em inglês desconhecidas ao vocabulário do usuário.')
        print('\t--words\t\t-W\t\t\t\t\tNão traduz e não processa as  palavras do vocabulario, apenas extrai todas as palavras do PDF.')
        print()
        print('Exemplos:')
        print('\tRetorna as palavras do PDF desconhecidas ao vocabulário e as traduz.')
        print('\t\t$%s -p book.pdf --w wordlist.txt')
        print()
        print('\tRetorna as palavras do PDF desconhecidas ao vocabulário.')
        print('\t\t$%s --pdf paper.pdf --wordlist wordlist.txt -n'%program_name)
        print()
        quit()



if __name__ == "__main__":

    args = sys.argv
    ttp = TradutorPessoalPdf(args)
