# Farmácias/drogarias — revalidação de atividade — batch 04 — v001

**Data:** 22/09/2026  
**Geografia:** São Borja/RS  
**Objeto:** quarto e último bloco de 5 CNPJs do recorte de 20 farmácias/drogarias do inventário POM  
**Status:** cobertura dos 20 CNPJs concluída; consolidação CNES necessária antes de qualquer nova métrica de rede.

## 1. Resultados

### 1.1 Panvel — 92.665.611/0467-54

CNES 9921117.

O CNES/DATASUS registra **Panvel Loja 1**, CNPJ 92.665.611/0467-54, na Rua General Marques, 902, Centro, São Borja.

- última atualização CNES: **23/08/2026**;
- atualização local: 01/09/2025;
- horários de funcionamento informados.

O inventário antigo também associava esse mesmo CNPJ à Rua dos Andradas, 2161.

**Dado observado:** a associação corrente do CNPJ 92.665.611/0467-54 no CNES é General Marques, 902.

**Classificação:** `REGISTRO_CNES_ATUALIZADO_2026_COM_CORRECAO_DE_DUPLICIDADE`.

A linha Andradas, 2161 não deve mais ser tratada como segunda unidade desse CNPJ.

### 1.2 Droga Raia — 61.585.865/2878-50

CNES 4396235.

O CNES registra **Droga Raia Loja 1358**, CNPJ 61.585.865/2878-50, Rua Cândido Falcão, 868.

- última atualização CNES: **12/07/2026**;
- horários de funcionamento informados.

**Classificação:** `REGISTRO_CNES_ATUALIZADO_2026`.

### 1.3 Farmácia Fronteira — 94.963.576/0015-01

CNES 8245460.

A listagem corrente do CNES/DATASUS para São Borja inclui **Farmácia Fronteira**, CNPJ 94.963.576/0015-01.

Fonte cadastral secundária corrente também apresenta o CNPJ como ativo na Rua General Osório, 2229.

**Classificação:** `REGISTRO_CNES_CORRENTE`.

### 1.4 Farmácias Fronteira — 94.963.576/0013-31

CNES 8247994.

A listagem corrente do CNES inclui **Farmácias Fronteira**, CNPJ 94.963.576/0013-31, em São Borja.

Há ainda evidência municipal de contratação em março/2024 envolvendo diretamente esse CNPJ.

**Classificação:** `REGISTRO_CNES_CORRENTE_E_EVIDENCIA_MUNICIPAL_2024`.

### 1.5 Agafarma — 26.710.619/0001-83

A Agafarma São Borja possui sinais operacionais recentes: página de atividade comercial com publicações ao longo de 2026, inclusive em agosto, e anúncio de mudança de endereço a partir de 15/06/2026.

Fonte cadastral secundária corrente apresenta o CNPJ 26.710.619/0001-83 como ativo e ainda associado à Avenida Presidente Vargas, 2196.

Por outro lado, guia local recente aponta Agafarma na Avenida Presidente Vargas, 2311.

**Dado observado:** há evidência forte de continuidade operacional em 2026, mas o endereço corrente precisa ser reconciliado.

**Classificação:** `ATIVIDADE_OPERACIONAL_RECENTE_COM_ENDERECO_A_RECONCILIAR`.

O CNPJ não foi localizado na listagem CNES municipal consultada. Essa ausência, isoladamente, não autoriza concluir encerramento.

## 2. Cobertura concluída do recorte de 20 CNPJs

Com o batch 04, os **20 CNPJs únicos** do recorte de farmácias/drogarias foram examinados.

Nenhum registro produziu evidência suficiente para exclusão por encerramento.

Porém, a conclusão metodológica não é “20/20 ativos na RFB”.

O que se pode afirmar é:

- o recorte inteiro recebeu revalidação;
- a grande maioria possui presença em fonte institucional de saúde corrente;
- Agafarma possui sinais operacionais recentes e cadastro secundário ativo, com pendência de endereço;
- a situação cadastral RFB oficial permanece uma camada separada.

## 3. Achado novo: a revalidação expôs erro de completude do inventário

A revalidação não apenas conferiu os CNPJs existentes: ela revelou que a base antiga não representa adequadamente a configuração corrente.

No caso Panvel:

- o inventário repetia o CNPJ 92.665.611/0467-54 em General Marques, 902 e Andradas, 2161;
- o CNES corrente mantém 92.665.611/0467-54 em General Marques, 902;
- o CNES corrente registra **outro CNPJ Panvel — 92.665.611/0561-21 — na rede municipal**;
- fonte cadastral secundária corrente localiza 92.665.611/0561-21 na Rua dos Andradas, 2161.

Portanto, a antiga “duplicidade” Panvel escondia pelo menos uma unidade/CNPJ distinto que não entrou no universo de 20 CNPJs únicos.

## 4. Consequência para a métrica 85%

A métrica anterior:

- 20 CNPJs únicos;
- 7 raízes;
- 17/20 em raízes multi = 85%;
- maior raiz 7/20 = 35%;

continua válida **apenas como descrição do inventário POM processado naquele momento**.

Após a descoberta de unidades correntes não incorporadas, ela **não deve ser tratada como fotografia atual completa da oferta de farmácias/drogarias em São Borja**.

Antes de recalcular é necessário fechar um universo corrente, preferencialmente partindo do CNES e triangulando com CNAE/RFB.

## 5. Próxima etapa

Construir um **censo corrente CNES de estabelecimentos do tipo FARMÁCIA em São Borja**, com:

- CNES;
- CNPJ;
- nome;
- endereço;
- raiz CNPJ;
- presença/ausência no inventário POM;
- classificação de rede;
- validação CNAE/RFB quando disponível.

Só depois:

1. recalcular CNPJs únicos;
2. recalcular raízes;
3. identificar raízes multiunidade;
4. calcular unidades em raízes multi;
5. comparar POM × CNES corrente;
6. avaliar se há base madura para novo delta.

## 6. Artefato

- `docs/data_sources/farmacias_revalidacao_batch04_20260922_v001.csv`.

## 7. Status editorial

**BATCH DE REVALIDAÇÃO CONCLUÍDO, MAS MÉTRICA CORRENTE AINDA NÃO PROMOVÍVEL.**

A próxima decisão depende do censo corrente CNES.

## 8. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
