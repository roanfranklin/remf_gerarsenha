## REMF_GerarSenha :
[![Github All Releases](https://img.shields.io/badge/REMF_GerarSenha-versão%200.0.1-red)]()
[![Github All Releases](https://img.shields.io/badge/suporte-python%203.7%2F3.8%20%2B-brightgreen)]()
[![Github All Releases](https://img.shields.io/badge/platforma-windows%20%7C%20linux-lightgrey)]()

Gerar senha randomica informando os tipos de caracteres e qual o tamanho.

## Instalação :
Use o gerenciado de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar requisitos
```bash
cd remf_gerarsenha
python3 -m pip install -r requirements.txt
python3 remf_gerarsenha.py 
```

## Ajuda :
```bash
./remf_gerarsenha.py 1-6 [ TAMANHO ]
./remf_gerarsenha.py 0 [ TAMANHO ] "CARACTERES"
```
os tipos:

0 = PRECISA SETAR OS CARACTERES NO 3º CAMPO;\n
1 = ALFABETO + NUMEROS + CARACTERES ESPECIAIS;\n
2 = ALFABETO;\n
3 = ALFABETO + NUMEROS;\n
4 = ALFABETO + CARACTERES ESPECIAIS;\n
5 = NUMEROS + CARACTERES ESPECIAIS;\n
6 = CARACTERES ESPECIAIS;\n
\* = NUMEROS.

\* qualquer outro numero.

## Roan Franklin :
http://www.remf.com.br/
