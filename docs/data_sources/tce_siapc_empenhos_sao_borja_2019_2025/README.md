# TCE-RS/SIAPC — empenhos por credor — Prefeitura de São Borja — 2019–2025

**Fonte observada:** Tribunal de Contas do Estado do Rio Grande do Sul — Dados Abertos SIAPC.
**Órgão:** PM DE SÃO BORJA, código TCE-RS 58000.
**Período:** exercícios 2019–2025.
**Unidade:** R$ correntes quando a coluna de pagamento é mapeada sem ambiguidade.

A rota oficial de Despesa Orçamentária por Empenhos inclui operações de empenho, liquidação e pagamento e campos de credor, inclusive CPF/CNPJ, conforme a documentação do TCE-RS. O workflow usa exclusivamente os arquivos por órgão para evitar o download dos arquivos estaduais anuais de grande volume.

Os arquivos brutos e dados pessoais de credores pessoa física não são persistidos no Git. A camada persistida contém apenas manifesto de fonte/hashes, inventário de schema e agregados anuais. Qualquer classificação territorial futura de fornecedores deve usar apenas CNPJs e permanecer separada de CPF.

**Limitação:** SIAPC é fonte administrativa remetida pelos jurisdicionados; o próprio TCE-RS informa que esses dados de origem não foram analisados pelo Tribunal. Comparações com SICONFI exigem conciliação conceitual e temporal antes de uso analítico.
