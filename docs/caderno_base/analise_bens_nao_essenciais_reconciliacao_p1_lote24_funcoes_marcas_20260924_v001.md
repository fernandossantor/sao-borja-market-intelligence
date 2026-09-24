# Bens não essenciais — reconciliação P1 — lote 24 — funções físicas e marcas — 24/09/2026

## 1. Objeto

Segundo lote dirigido à fila **P1**, priorizando casos em que a principal incerteza era transformar corretamente:

- estabelecimento jurídico em storefront — ou não;
- CNPJ adicional de raiz em unidade comercial — ou não;
- marca operacional em CNPJ correto;
- uma linha do inventário que conflava duas unidades atuais.

Foram tratados sete casos:

- M.H. Moda Íntima — matriz adicional da raiz 05.823.159;
- Brasil Free Shop — filial adicional 32.195.385/0011-58;
- RM2S — filial adicional 58.434.608/0015-00;
- João e Maria Pet — matriz 59.205.031/0001-21;
- Barraca Missões — filial 92.293.703/0011-45;
- Requinte — filial 93.202.695/0002-56;
- Lins Ferrão — reconciliação Pompéia/Gang.

Governança preservada:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhum indicador canônico recalculado.

## 2. M.H. Moda Íntima — raiz 05.823.159

### Dados observados

O site oficial em 2026 utiliza:

- CNPJ `05.823.159/0001-20`;
- endereço institucional/e-commerce em Rua General Osório, 2298.

A página oficial “Nossas Lojas” apresenta **uma loja em São Borja**, na Rua General Marques, 1014.

O CNPJ `05.823.159/0004-72`, já presente no inventário, permanece filial ativa em endereço cadastral na BR-287.

### Interpretação

A raiz possui mais de um estabelecimento jurídico em São Borja, mas a evidência de primeira parte não sustenta dois storefronts físicos independentes.

### Decisão provisória

- manter **uma operação M.H. Moda Íntima** no cenário-base exploratório;
- não adicionar `/0001-20` como segundo storefront;
- rebaixar a pendência para P2 de mapeamento CNPJ ↔ loja física.

## 3. Brasil Free Shop — 32.195.385/0011-58

### Dados observados

A Receita Estadual/RS lista oficialmente o CNPJ `32.195.385/0011-58` entre as **Lojas Francas de Fronteira Terrestre** de São Borja.

Fonte cadastral atual apresenta:

- situação ativa;
- abertura em 09/06/2025;
- CNAE principal de lojas francas;
- Rua Vereador Eurico Batista da Silva, 925.

A mesma lista oficial inclui também `/0006-90` e `/0012-39` no município.

### Decisão provisória

Classificar `/0011-58` como **storefront distinto autorizado** e incorporar ao cenário-base exploratório, preservando a raiz comum.

## 4. RM2S — 58.434.608/0015-00

### Dados observados

O CNPJ `58.434.608/0015-00` está ativo, aberto em 19/06/2026, em Rua General Marques, 1112.

Não foi encontrada marca/fachada varejista própria associada à unidade.

O mesmo endereço permanece publicamente associado à agência Itaú 0343 em 2026.

A raiz RM2S já possui outra filial em São Borja, `58.434.608/0010-03`, na Rua General Osório, 2251.

### Decisão provisória

- não adicionar `/0015-00` como storefront incremental no cenário-base;
- manter como unidade jurídica ativa em sensibilidade;
- reabrir apenas se surgir evidência operacional própria.

## 5. João e Maria Pet — raiz 59.205.031

### Dados observados

A matriz `59.205.031/0001-21`:

- está ativa;
- atua no varejo pet;
- localiza-se em 10A Rua Borges do Canto, 385, sala 101;
- não apresenta fantasia cadastral.

A filial `59.205.031/0002-02`:

- foi aberta em 20/03/2026;
- possui fantasia **João e Maria Pet e Rações**;
- está em Rua Coronel Aparício Mariense, 2287.

### Decisão provisória

- manter a filial `/0002-02` como operação-base;
- não adicionar a matriz `/0001-21` como segundo storefront sem evidência operacional própria;
- preservar a matriz na camada jurídica/sensibilidade.

## 6. Barraca Missões — raiz 92.293.703

### Dados observados

A filial `92.293.703/0011-45` está ativa, com fantasia Barraca Missões, em Avenida Bernardo de Mello, 150.

O site oficial da Barraca Missões informa atualmente **sete lojas** e inclui São Borja uma única vez.

Diretório operacional atual localiza a loja São Borja na Rua Engenheiro Manoel Luís Fagundes, 1372 — endereço do CNPJ `92.293.703/0005-05`, já presente no inventário.

### Decisão provisória

- manter `/0005-05` como storefront-base da marca em São Borja;
- não contar `/0011-45` como segunda loja no cenário-base;
- manter `/0011-45` como filial jurídica em sensibilidade.

## 7. Requinte — raiz 93.202.695

### Dados observados

O CNPJ `93.202.695/0002-56`:

- está ativo;
- atua no varejo de vestuário;
- localiza-se em Avenida Presidente Vargas, 2055, sala 1;
- possui telefone comercial próprio.

O CNPJ `93.202.695/0006-80`:

- está ativo;
- corresponde à **Requinte Modas**;
- está em Rua General Osório, 2051;
- possui endereço e telefone diferentes.

### Interpretação

Há dois estabelecimentos comerciais distintos da mesma raiz em São Borja.

A marca da unidade `/0002-56` não foi identificada.

### Decisão provisória

- incorporar `/0002-56` como **storefront distinto**;
- não atribuir a marca Requinte à unidade sem evidência explícita;
- preservar a raiz comum para análises de rede/concentração.

## 8. Lins Ferrão — Pompéia e Gang

Este é o principal achado estrutural do lote.

### Dados observados

O CNPJ `87.345.021/0033-04`:

- está ativo;
- localiza-se em Rua General Marques, 1196;
- diretórios operacionais atuais identificam **Lojas Pompéia** nesse endereço.

O CNPJ `87.345.021/0122-14`, usado pelo inventário como Pompéia:

- também está ativo;
- localiza-se em Rua Cândido Falcão, 1057;
- diretórios operacionais atuais identificam **Gang — São Borja** nesse endereço.

### Interpretação

O inventário conflava duas operações:

- `/0033-04` = Pompéia;
- `/0122-14` = Gang.

São dois storefronts distintos sob a mesma raiz Lins Ferrão.

### Decisão provisória

- manter `87.345.021/0122-14`, mas corrigir a marca da linha original para **Gang**;
- incorporar `87.345.021/0033-04` como **Lojas Pompéia**;
- preservar a raiz comum para análises de rede;
- não tratar a correção como simples substituição de CNPJ: trata-se de **desdobramento de uma linha que conflava duas unidades atuais**.

## 9. Resultado do lote

### Dados observados

- Brasil Free Shop `/0011-58`, Requinte `/0002-56` e Pompéia `/0033-04` possuem evidência suficiente de storefront distinto;
- M.H. `/0001-20`, RM2S `/0015-00`, João e Maria `/0001-21` e Barraca Missões `/0011-45` permanecem unidades jurídicas sem evidência suficiente para adicionar storefront incremental;
- o CNPJ original Lins Ferrão `/0122-14` deve ser reinterpretado como Gang, não Pompéia.

### Decisões calculadas

Dos sete casos:

- **3 CNPJs adicionais entram como storefronts distintos**: Brasil Free Shop, Requinte e Pompéia;
- **4 CNPJs adicionais não acrescentam storefront ao cenário-base**: M.H., RM2S, João e Maria e Barraca Missões;
- a linha Lins Ferrão original continua presente, mas com marca corrigida para Gang.

## 10. Efeito esperado sobre a fila

Os sete casos deixam P1 como bloqueios de storefront.

A próxima versão da fila deverá concentrar P1 principalmente em:

- sucessões;
- homonímias;
- vínculos marca↔CNPJ;
- operadores atuais sem identidade jurídica corrente.

## 11. Próxima etapa

Prosseguir com:

- Amei Presentes Criativos;
- Veterinária São Francisco;
- Excêntrica;
- Rilu;
- Ka Lopes Fitness;
- Marco Relojoeiro;
- Bella Cestas & Presentes;
- 7 Povos Confecções;
- Marlin Fashion;
- Bicho Mimado;
- Pet House.

## 12. Artefato

`docs/data_sources/bens_nao_essenciais_reconciliacao_p1_lote24_funcoes_marcas_20260924_v001.csv`
