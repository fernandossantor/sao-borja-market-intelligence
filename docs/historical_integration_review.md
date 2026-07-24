# Revisão do mapeamento histórico

O mapeamento por metadados e nomes comparou as 33 fontes ativas do staging com os arquivos existentes em `processed`, `warehouse` e `exports`.

## Resultado observado

- 924 arquivos históricos-alvo;
- 923 arquivos potencialmente tabulares ou de banco de dados;
- 1 par candidato por similaridade forte de nome;
- 32 fontes do staging sem candidato nominal;
- nenhum par com SHA-256 idêntico;
- nenhum par com nome normalizado idêntico.

## Interpretação

A baixa correspondência nominal demonstra que os nomes dos arquivos históricos não são suficientes para relacionar o staging ao acervo existente. A próxima etapa deve examinar a organização interna do acervo e, depois, os esquemas estruturais dos formatos predominantes.

## Limitações

O mapeamento por nome não permite concluir duplicidade, complementaridade, conflito ou atualização metodológica. Nenhum arquivo histórico foi baixado, modificado ou promovido.
