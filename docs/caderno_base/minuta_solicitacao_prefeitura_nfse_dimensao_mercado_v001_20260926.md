# Minuta — solicitação à Prefeitura de São Borja — NFS-e/CFS-e agregada — v001

**Data:** 2026-09-26  
**Destinatário recomendado:** Secretaria Municipal de Fazenda — ISSQN  
**Contato público identificado no portal:** `iss@saoborja.rs.gov.br`  
**Projeto:** São Borja — Inteligência Mercadológica  
**Finalidade:** dimensão de mercado de Serviços em formato exclusivamente agregado.

## Assunto sugerido

**Solicitação acadêmica de dados agregados de NFS-e/CFS-e para análise econômica de São Borja**

## Texto sugerido

Prezados(as),

Estou desenvolvendo um projeto acadêmico de inteligência mercadológica territorial de São Borja e gostaria de consultar a possibilidade de acesso a **dados agregados e anonimizados** do sistema municipal de NFS-e/CFS-e.

A pesquisa não necessita de notas individuais, CNPJ/CPF, nomes de prestadores ou tomadores, endereços, chaves de acesso ou qualquer informação protegida individualmente. O objetivo é apenas dimensionar, em nível agregado, a atividade formal de alguns submercados de serviços no município.

A estrutura mínima desejada, para o período de janeiro de 2023 até a última competência fechada disponível, seria:

`competência | código de tributação/item de serviço | valor bruto dos serviços | quantidade de documentos | situação do documento`.

Se tecnicamente disponível, seriam muito úteis também:
- CNAE do prestador;
- município do destinatário/tomador;
- município/local da prestação;
- base de cálculo do ISS;
- valor do ISS;
- quantidade de prestadores distintos em cada célula.

O layout técnico atualmente publicado pelo sistema documenta campos como competência, código de tributação nacional/municipal, local da prestação e município do destinatário. Entretanto, tenho plena ciência de que a disponibilidade e a completude histórica desses campos podem ter mudado entre 2023 e 2026.

Por isso, caso seja possível fornecer a base agregada, solicito também indicação de:
- desde quando cada dimensão possui cobertura confiável;
- tratamento de notas canceladas/substituídas;
- eventuais mudanças de layout/metodologia;
- regra de supressão estatística utilizada.

A agregação pode ser realizada no nível que a Secretaria considerar necessário para preservar o sigilo fiscal. Células com poucos prestadores podem ser suprimidas ou agregadas a categoria superior.

Uma chave analítica preferencial seria:

`competência × código tributação × município do destinatário × local da prestação × situação`.

Mas, se essa estrutura for muito detalhada, uma primeira entrega apenas de:

`competência × código tributação × valor bruto × quantidade de notas`

já seria extremamente útil.

O objetivo é produzir indicadores acadêmicos agregados sobre dimensão e composição dos mercados de serviços de São Borja. Não se pretende identificar ou comparar contribuintes individualmente.

Caso a extração não possa ser fornecida, uma orientação sobre **quais agregações/relatórios já existem no sistema** ou quais campos podem ser disponibilizados também será suficiente para adequar o estudo.

Agradeço pela atenção e fico à disposição para encaminhar uma especificação técnica mais detalhada.

Atenciosamente,

[Nome]  
[Instituição / vínculo acadêmico]  
[E-mail]  
[Telefone, se desejado]

## Anexo recomendado

`nfse_sao_borja_especificacao_dados_mercado_v001_20260926.md`

## Controle metodológico

Mesmo que os dados sejam obtidos:
- valor de NFS-e será tratado como faturamento fiscal/documentado, não como renda disponível ou valor adicionado;
- município do destinatário não será automaticamente tratado como residência do consumidor;
- nenhum market share empresarial será calculado sem numerador compatível fornecido pela própria empresa e mesmo perímetro fiscal.
