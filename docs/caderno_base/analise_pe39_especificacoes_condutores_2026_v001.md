# PE 39/2026 — normalização técnica dos 18 condutores prioritários — v001

## 1. Objetivo

Transformar os 18 itens prioritários de condutores em um conjunto menor de **especificações técnicas distintas** para o próximo gate de catálogo/estoque.

A Prefeitura confirma oficialmente o PE39, seu objeto, julgamento por item e sessão. As descrições técnicas abaixo continuam provenientes de espelho secundário do processo, que também indexa os arquivos `EDITAL_E_ANEXOS_PCE_39_2026.7z` e `FASE_PREPARAT_RIA_PCE_39_2026.7z`.

Fonte oficial de existência/objeto:
https://antigo.saoborja.rs.gov.br/index.php/licitacoes-e-contratos/itemlist/category/25-pregao-eletronico

Fonte secundária item a item:
https://mabus.com.br/licitacao/3630558/pregao-eletronico-municipio-de-sao-borja-sao-borja-rs

**Controle:** a normalização é provisória até reconciliação com edital/TR oficial.

## 2. Resultado

Os **18 itens** podem ser reduzidos a **9 clusters técnicos** quando:

- cores do mesmo cabo são consolidadas;
- itens com descrição e preço unitário idênticos são somados;
- bitolas/tensões/material diferentes continuam separados.

Isso reduz em **50%** o número de verificações de produto sem eliminar nenhuma especificação materialmente distinta observada no espelho.

| Cluster | Especificação | Quantidade | Valor estimado | % dos condutores |
|---|---|---:|---:|---:|
| T01 | Fio plastichumbo em cobre 2 x 4,0 mm 450/750V - norma ABNT | 4.200 m | R$ 26.208,00 | 4,92% |
| T02 | Fio plastichumbo em cobre 2 x 2,5 mm 450/750V - norma ABNT | 4.200 m | R$ 27.468,00 | 5,15% |
| T03 | Cabo flexível 16,00 mm² 0,6/1kV - ATOX | 6.500 m | R$ 117.520,00 | 22,04% |
| T04 | Cabo PP 2 x 2,5 mm 1kV | 3.600 m | R$ 19.836,00 | 3,72% |
| T05 | Cabo PP 4 x 10,00 mm 1kV | 2.820 m | R$ 103.353,00 | 19,38% |
| T06 | Cabo multiplex 4 x 16,00 mm 1kV - alumínio | 3.820 m | R$ 45.534,40 | 8,54% |
| T07 | Cabo flexível de cobre 6mm com isolamento em PVC 70C sem alumínio | 12.000 m | R$ 50.520,00 | 9,47% |
| T08 | Cabo flexível de cobre 10mm com isolamento em PVC 70C sem alumínio | 7.500 m | R$ 68.850,00 | 12,91% |
| T09 | Cabo flexível de cobre 25mm com isolamento em PVC 70C sem alumínio | 3.900 m | R$ 73.905,00 | 13,86% |

Controle de soma:
**R$ 533.194,40 = R$ 533.194,40**.

## 3. Três grandes arquiteturas técnicas

### A. Cabos com construção/especificação especial

- plastichumbo em cobre 450/750V, com menção explícita a norma ABNT;
- cabo flexível 16 mm² 0,6/1kV ATOX;
- cabos PP 1kV;
- cabo multiplex 4x16 mm² 1kV em alumínio.

Esses grupos exigem validação por **construção, tensão, seção e material**, não apenas “mesma bitola”.

### B. Cabos flexíveis de cobre PVC 70°C

Os itens de 6, 10 e 25 mm² são explicitamente descritos como cobre, isolamento em PVC 70°C e sem alumínio, variando por seção e cor.

Aqui a equivalência de catálogo tende a ser mais simples de verificar documentalmente, mas ainda depende da íntegra do TR.

### C. Cor como subespecificação

Vários itens diferem apenas por cor. Para capacidade de abastecimento, podem ser testados como um cluster técnico; para aderência ao edital, cada cor deve continuar sendo verificada.

## 4. Padrão 75%/25% nos itens 35 e 36

Os itens 35 e 36 possuem:

- mesma descrição: **Cabo PP 4 x 10,00 mm 1kV**;
- mesmo valor unitário de referência: **R$ 36,65**;
- quantidades: **2.115 m** e **705 m**;
- total: **2.820 m**.

Cálculo:

- 2.115 / 2.820 = **75,00%**;
- 705 / 2.820 = **25,00%**.

### Hipótese

O padrão é **compatível** com desenho de cota principal + cota reservada, comum em tratamento favorecido a ME/EPP.

### Limite

Isso é apenas **hipótese documental**. Não classificar item 36 como cota reservada nem inferir vantagem regulatória para fornecedor local antes de ler o edital/TR oficial.

## 5. Implicação para o gate da Iluminar

A pergunta de catálogo deixa de exigir checagem de 18 linhas independentes. O próximo formulário pode verificar 9 especificações:

1. plastichumbo cobre 2x4,0 mm 450/750V ABNT;
2. plastichumbo cobre 2x2,5 mm 450/750V ABNT;
3. flexível 16 mm² 0,6/1kV ATOX;
4. PP 2x2,5 mm 1kV;
5. PP 4x10 mm 1kV;
6. multiplex 4x16 mm² 1kV alumínio;
7. flexível cobre 6 mm² PVC 70°C;
8. flexível cobre 10 mm² PVC 70°C;
9. flexível cobre 25 mm² PVC 70°C.

Para cada cluster, registrar:

`produto equivalente? → marca/modelo → norma/certificação → estoque imediato → quantidade disponível → lead time → fornecedor upstream → preço entregue`.

## 6. Priorização dentro dos nove clusters

Por valor estimado:

1. flexível 16 mm² ATOX — R$117.520,00;
2. PP 4x10 mm² 1kV — R$103.353,00;
3. flexível cobre 25 mm² PVC 70°C — R$73.905,00;
4. flexível cobre 10 mm² PVC 70°C — R$68.850,00;
5. plastichumbo 2x2,5 — R$27.468,00;
6. plastichumbo 2x4 — R$26.208,00;
7. flexível cobre 6 mm² PVC 70°C — R$50.520,00;
8. multiplex 4x16 alumínio — R$45.534,40;
9. PP 2x2,5 — R$19.836,00.

**Nota:** a ordem acima deve ser lida pelo valor individual; a lista narrativa não substitui a tabela/CSV calculada.

## 7. Próxima ação

1. obter ou materializar a íntegra oficial do edital/TR;
2. confirmar as 9 especificações e o significado do split 75/25;
3. somente depois executar o gate de catálogo da Iluminar;
4. itens sem equivalência documental não avançam para preço/estoque;
5. manter resultado PE39 separado — ainda não publicado segundo indexador secundário consultado.

## 8. Limitações

- especificações ainda vêm de espelho secundário;
- ATOX, PVC 70°C, tensão e composição não podem ser simplificados como equivalentes entre si;
- cor pode ser irrelevante economicamente, mas continua requisito de item;
- split 75/25 não prova cota ME/EPP;
- preço de referência não é preço homologado.

## 9. Governança

- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
