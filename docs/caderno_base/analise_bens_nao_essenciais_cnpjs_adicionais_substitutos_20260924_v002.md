# Bens não essenciais — CNPJs adicionais, substitutos e candidatos — v002 — 24/09/2026

## 1. Atualização

A versão v002 incorpora os resultados do lote 19 de reconciliação P0.

O universo externo aos 103 CNPJs originais passou de **26 para 31 CNPJs únicos**.

Foram acrescentados:

- `43.839.616/0001-63` — MB Lojas — operador atual confirmado da marca;
- `35.686.566/0001-01` — Loja It Girls — operador atual confirmado da marca;
- `46.083.011/0001-83` — Excêntrica — candidato corrente forte, ainda sem vínculo explícito da marca;
- `37.106.058/0001-24` — Top 20 — operador atual confirmado da marca;
- `00.664.113/0001-91` — Rilu Tecidos — continuidade candidata da operação Rilu.

O CNPJ `00.776.574/1709-06` da Americanas, já presente na v001, foi promovido de substituto pendente para **substituto operacional confirmado**, com base na licença municipal e em bases cadastrais correntes.

## 2. Classificação atual

A matriz contém:

- 11 `ADICIONAL_RAIZ`;
- 5 `IDENTIFICADO_LINHA_SEM_CNPJ`;
- 3 `OPERADOR_ATUAL_MARCA_CONFIRMADO`;
- 2 `CANDIDATO_FORTE_LINHA_SEM_CNPJ`;
- e 10 registros distribuídos entre correção de duplicidade, candidatos, histórico, homônimo, sucessor e substituto operacional confirmado.

Essas categorias são **classificações técnicas do SBMI**, não categorias oficiais da Receita Federal.

## 3. Regra de uso

A matriz continua sendo uma camada de controle.

- operador atual confirmado pode ser usado no futuro cenário-base exploratório;
- CNPJ adicional de raiz continua dependendo da função física;
- candidato corrente/continuidade candidata permanece fora do denominador canônico até reconciliação;
- registros históricos não entram como oferta corrente.

## 4. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- nenhuma métrica de oferta ou concentração foi recalculada.

## 5. Artefato

`docs/data_sources/bens_nao_essenciais_cnpjs_adicionais_substitutos_candidatos_20260924_v002.csv`
