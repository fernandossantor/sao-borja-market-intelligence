# Observatório do Comércio Fecomércio-RS — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Produtor:** Instituto Fecomércio-RS de Pesquisas (IFEP-RS)  
**Plataforma:** https://observatorio.fecomercio-rs.org.br/page/home

## Finalidade no SBMI

Usar o Observatório como fonte complementar e de validação cruzada para indicadores empresariais e setoriais, preservando a prioridade das fontes primárias quando estas já forem utilizadas diretamente pelo projeto.

## Conteúdo confirmado

Materiais públicos do lançamento descrevem dados sobre:
- empresas/estabelecimentos;
- emprego/trabalho;
- receitas;
- despesas;
- segmentação regional;
- segmentação por atividade econômica.

Também são divulgados indicadores próprios do IFEP-RS, incluindo rotatividade, concentração territorial e tempo de vida/atividade das empresas.

## Origem dos dados

A plataforma possui seção “Fonte dos dados”, que deve ser tratada como referência para mapear a proveniência de cada indicador.

Nesta v001, foram confirmadas externamente como fontes utilizadas pelo Observatório:
- Receita Federal;
- Ministério do Trabalho.

A lista detalhada da seção “Fonte dos dados” ainda não foi transcrita nesta auditoria, porque a aplicação é carregada dinamicamente e essa camada não ficou disponível no rastreamento textual automatizado. Não inferir outras bases sem validação direta na plataforma.

## Regra de integração

1. Se o Observatório reproduzir/transformar uma fonte primária já canonizada no SBMI, manter a fonte primária como referência principal.
2. Se o indicador for próprio do IFEP-RS, registrar:
   - nome do indicador;
   - definição;
   - fórmula/metodologia;
   - periodicidade;
   - geografia;
   - fonte(s) de entrada;
   - limitações.
3. Não comparar automaticamente indicadores que usem conceitos diferentes de estabelecimento, empresa, emprego, receita ou despesa.
4. Recortes municipais e regionais só serão incorporados depois de verificação explícita dos filtros da plataforma.

## Próxima auditoria específica

Transcrever a seção “Fonte dos dados” e produzir uma matriz:

`indicador | fonte_original | produtor | periodicidade | menor_geografia | unidade | transformação_IFEP | uso_SB​​MI`

Depois, testar explicitamente:
- São Borja;
- Fronteira Oeste/região comparável, quando houver;
- Rio Grande do Sul.
