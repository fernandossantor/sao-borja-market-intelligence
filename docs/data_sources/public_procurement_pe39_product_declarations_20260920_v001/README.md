# PE39/2026 — declarações de modelo/marca: vencedor × participante local

Fonte: Ata Final oficial do PE39/2026.

O arquivo winner_local_product_declarations.csv preserva, para cada item prioritário:
- o campo combinado Modelo + Marca/Fabricante da proposta inicial do participante local;
- o mesmo campo do arrematante final, quando houve vencedor;
- valores iniciais e posição/valor final.

O campo declaracao_modelo_marca_raw é intencionalmente não separado.
A extração PDF não fornece fronteira de coluna estável entre Modelo e Marca/Fabricante,
portanto qualquer separação automática criaria informação não observada.

contains_corfio mede somente a ocorrência textual de CORFIO no campo declarado.
Não comprova fabricante, fornecedor upstream, estoque, autenticidade, equivalência técnica
ou produto efetivamente entregue.

O item 7 não possui linha WINNER porque o item fracassou.

Governança: Caderno-Base v028 permanece read-only; PR #41 permanece aberto, draft e sem merge.
