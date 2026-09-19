# PMSB — exposição territorial das compras/contratações — interpretação e sensibilidades — v001

**Status:** exploratório — não canônico.  
**Período dos pagamentos:** 01/01/2026 a 18/09/2026.  
**Fonte dos pagamentos:** Portal da Transparência da Prefeitura Municipal de São Borja.  
**Fonte cadastral:** Receita Federal do Brasil — Dados Abertos CNPJ, competência 2026-08.  
**Limitação de transporte:** nesta execução, os arquivos RFB foram obtidos por espelho do snapshot agosto/2026 devido a timeout do host oficial. Portanto, os resultados permanecem exploratórios até reconciliação de hash ou reexecução pela fonte oficial.

## 1. Resultado principal

No universo de **R$ 72.039.491,18** de pagamentos enquadrados em rubricas compatíveis com aquisição/contratação:

- CNPJ credor **ativo e registrado em São Borja**: **R$ 43.751.499,71 = 60,73%**;
- CNPJ externo cuja **mesma raiz possui estabelecimento ativo em São Borja**: **R$ 10.184.036,91 = 14,14%**;
- presença operacional local ampliada: **R$ 53.935.536,62 = 74,87%**;
- CNPJ sem estabelecimento ativo local na raiz, incluindo os raros casos não ativos no snapshot: **R$ 18.103.465,56 = 25,13%**;
- nenhum CNPJ do núcleo ficou sem correspondência cadastral.

Isto mede **exposição territorial de primeira ordem do pagamento**, não retenção econômica final.

## 2. Controle temporal

Três CNPJs do núcleo, somando apenas **R$ 489,00**, estavam registrados em São Borja, mas não ativos no snapshot RFB de agosto/2026. Eles permanecem separados porque podem ter recebido pagamentos anteriormente no ano e encerrado a situação cadastral antes da competência RFB.

Dois registros externos não ativos no snapshot somam **R$ 9.950,00**.

## 3. Efeito da Fundação Ivan Goulart

A Fundação Ivan Goulart recebeu **R$ 28.342.657,23** em rubricas compatíveis com contratação, o equivalente a **39,34%** de todo o núcleo.

Como se trata de arranjo institucional de serviços e não de uma compra convencional de mercadoria, foi calculada uma **sensibilidade**, não uma exclusão substantiva:

Sem a Fundação:
- denominador: **R$ 43.696.833,95**;
- CNPJ local exato ativo: **35,26%**;
- presença local ampliada: **58,57%**;
- externo sem footprint local: **41,43%**.

A diferença entre 74,87% no núcleo integral e 58,57% sem a Fundação mostra que a leitura agregada é fortemente dependente de um único arranjo institucional.

## 4. Sensibilidade sem rubricas genéricas de serviços PJ

As duas variantes de “outros serviços de terceiros — pessoa jurídica” somam **R$ 51.040.784,58** e têm presença local ampliada de aproximadamente **91,22%**. Esse bloco é responsável pela maior parte da aparente ancoragem local do núcleo.

Ao retirar apenas essas rubricas genéricas e manter materiais, bens para distribuição, equipamentos, obras, TIC, consultoria e passagens:

- denominador: **R$ 20.998.706,60**;
- CNPJ local exato ativo: **23,63%**;
- presença local ampliada: **35,12%**;
- externo sem footprint ativo local: **64,88%**.

Esta sensibilidade não afirma que serviços devam ser excluídos. Ela mostra que **o padrão territorial de serviços difere substancialmente do padrão territorial das demais compras/contratações**.

## 5. Bens, materiais e equipamentos

Somando somente:
- material de consumo;
- material/bem/serviço para distribuição gratuita;
- equipamentos e material permanente;

o valor pago é **R$ 16.762.852,35**.

Distribuição territorial:
- local exato ativo: **24,94%**;
- presença local ampliada: **25,90%**;
- credores sem footprint ativo local: **74,09%**.

Este é, até o momento, o sinal mais direto de exposição externa nas aquisições de bens da administração municipal.

Ainda assim, **74,09% não é taxa de vazamento**: fornecedores externos podem utilizar trabalho/subcontratação local e fornecedores locais podem revender produtos produzidos fora.

## 6. Diferença por rubrica

A heterogeneidade é muito elevada:

- serviços PJ genéricos: presença local ampliada ≈ **91,22%**;
- material de consumo: ≈ **36,05%**;
- material/bem/serviço para distribuição gratuita: **12,53%**;
- equipamentos e material permanente: ≈ **14,00%**;
- obras e instalações: ≈ **91,75%**;
- TIC: ≈ **33,63%**;
- consultoria: **10,26%**;
- passagens/locomoção: **14,13%**.

Consequentemente, uma taxa única de “compras locais” esconderia mecanismos econômicos distintos.

## 7. Diagnóstico

**Dado observado/calculado:** a despesa municipal compatível com compras/contratações combina um circuito de serviços fortemente ancorado em organizações com presença local e aquisições de bens/equipamentos predominantemente direcionadas a credores sem estabelecimento ativo em São Borja.

**Interpretação:** a hipótese territorial de conversão/recirculação ganha evidência empírica no setor público, mas de forma seletiva por categoria. O principal ponto de perda de captura local aparece nas compras de bens, materiais, equipamentos, TIC, consultoria e passagens; obras e serviços institucionais apresentam desenho diferente.

**Não concluir:** que 25,13%, 41,43%, 64,88% ou 74,09% sejam taxas finais de vazamento da economia municipal. São indicadores de geografia cadastral da primeira rodada de pagamento em recortes distintos.

## 8. Implicação para o modelo territorial

A evidência permite substituir a hipótese genérica “o setor público pode comprar fora” por uma formulação mais precisa:

> A administração municipal injeta recursos relevantes na economia, mas a capacidade de retenção da primeira rodada é desigual. Serviços e algumas obras apresentam forte presença local, enquanto compras de bens, materiais e equipamentos mostram elevada exposição a fornecedores sem footprint ativo no município. A conversão territorial do gasto público depende, portanto, da composição da despesa e das cadeias subsequentes dos fornecedores.

