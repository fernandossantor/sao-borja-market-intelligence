# Radar do Mercado — crosswalk de grupos NCM para os cadernos SBMI — v001

**Data:** 2026-09-26  
**Fonte taxonômica:** Receita Estadual do RS — Radar do Mercado — dimensão `d_ncms.grupo_afinidade_final`  
**Universo taxonômico auditado:** **110 grupos de afinidade distintos**  
**Geografia dos valores do Radar:** Rio Grande do Sul; **nenhum valor estadual é atribuído a São Borja**.  
**Finalidade:** orientar a taxonomia do pedido agregado `São Borja × NCM × valor` e separar perímetro principal, ampliado, adjacente e excluído.

## 1. Regra de uso

Este crosswalk classifica grupos de produto, não faturamento. Ele não transforma valores do Radar em valores de São Borja, não mede market share, não substitui a POF na demanda residente, não atribui vendas a empresas e não autoriza somar grupos com sobreposição de NCM.

O Radar é usado como **fonte de taxonomia e estrutura estadual de mercado**. A monetização municipal depende de extração fiscal agregada específica.

## 2. Fontes de escopo dos cadernos

A classificação foi confrontada com os POM 2026 já incorporados ao projeto:

- **Bens Essenciais:** supermercados, atacados, mercados/minimercados, padarias/confeitarias, açougues e fruteiras; mix inclui alimentação, bebidas e limpeza. O perímetro monetário canônico permanece **alimentação no domicílio**.
- **Saúde/Higiene/Cuidados Pessoais:** farmácias/drogarias, perfumarias, cosméticos/dermocosméticos, suplementação, artigos médicos/ortopédicos e ótica compatível com o estudo.
- **Bens Não Essenciais:** vestuário, calçados, móveis, eletrodomésticos, decoração e outros bens discricionários; pet/agro é fronteira que exige controle de uso final.
- **Serviços:** oficinas, salões/barbearias, lavanderias, clínicas/consultórios, reparos e outros serviços; NCM só é relevante para mercadorias complementares.
- **Alimentação Fora do Lar:** restaurantes, lanchonetes, pizzarias, cafeterias, bares, sorveterias e delivery. Para dimensão do mercado, **CNAE 56/transação do estabelecimento é preferível a NCM dos insumos**.

## 3. Estados do crosswalk

- **CORE:** aderente ao perímetro principal atual;
- **EXPANDED:** pertence ao escopo amplo do caderno, mas não à cesta POF atualmente calculada;
- **ADJACENT:** relacionado, com risco de sobreposição ou de medir mercadoria complementar;
- **REVIEW:** amplo/ambíguo; requer NCM4/NCM8;
- **EXCLUDE:** fora do perímetro prioritário.

Prioridade: ALTA = necessária ao primeiro denominador; MÉDIA = expansão útil; BAIXA = revisão/exclusão salvo nova pergunta.

## 4. Resumo

- grupos auditados: **110**;
- prioridade ALTA: **43**;
- prioridade MÉDIA: **17**;
- prioridade BAIXA: **50**;
- grupos fora do perímetro por padrão: **46**.

- Bens Essenciais | ADJACENT: 3
- Bens Essenciais | CORE: 28
- Bens Não Essenciais | ADJACENT: 5
- Bens Não Essenciais | CORE: 5
- Bens Não Essenciais | EXPANDED: 10
- Bens Não Essenciais | REVIEW: 4
- Fora do perímetro prioritário | EXCLUDE: 46
- Saúde/Higiene/Cuidados Pessoais | ADJACENT: 1
- Saúde/Higiene/Cuidados Pessoais | CORE: 3
- Saúde/Higiene/Cuidados Pessoais | EXPANDED: 2
- Saúde/Higiene/Cuidados Pessoais | REVIEW: 1
- Serviços | ADJACENT: 2

## 5. Crosswalk completo

| Grupo de afinidade Radar | Setor principal SBMI | Módulo | Status | Relação POF | Prioridade | Justificativa |
|---|---|---|---|---|---|---|
| Acessórios Pessoais e Artigos de Uso Pessoal | Bens Não Essenciais | Acessórios pessoais | REVIEW | parcial | MÉDIA | Grupo amplo com possível sobreposição com higiene/cuidados pessoais; necessita NCM8. |
| Adubos e Fertilizantes | Bens Não Essenciais | Pet/agro — fronteira de escopo | REVIEW | não | BAIXA | Contexto pet/agro aparece no POM, mas grupos são amplos e misturam consumo final e insumo produtivo; não incluir sem NCM e uso final. |
| Aeronaves e Espaço | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Alumínio e Suas Obras | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Animais Vivos e Genética | Bens Não Essenciais | Pet/agro — fronteira de escopo | REVIEW | não | BAIXA | Contexto pet/agro aparece no POM, mas grupos são amplos e misturam consumo final e insumo produtivo; não incluir sem NCM e uso final. |
| Aparelhos Telefônicos | Bens Não Essenciais | Eletrônicos de consumo | EXPANDED | não direto | ALTA | Bens discricionários próximos ao escopo eletroeletrônico; não incluídos automaticamente na cesta POF atual. |
| Armas e Munições | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Artefatos de Metal Diversos | Bens Não Essenciais | Utilidades domésticas / bens duráveis | ADJACENT | não | MÉDIA | Pode conter utilidades domésticas e itens industriais; NCM8 é necessário para evitar inclusão indevida. |
| Açúcares, Sacarídeos e Produtos de Confeitaria (sem cacau) | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Bebidas Alcoólicas | Bens Essenciais | Alimentação/bebidas — perímetro ampliado | ADJACENT | parcial | MÉDIA | Relacionado ao mix alimentar, mas não entra automaticamente no núcleo monetário canônico sem validar correspondência POF e uso final. |
| Bebidas Não Alcoólicas (Exceto Sucos) | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Biodiesel | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Borracha e Suas Obras (Exceto Pneumáticos) | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Brinquedos, Jogos e Artigos de Lazer | Bens Não Essenciais | Discricionários / lazer / decoração | EXPANDED | não | MÉDIA | Bens discricionários coerentes com o conceito amplo do caderno, fora dos três módulos monetários atuais. |
| Cabos e Fios | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Cacau e Preparações | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Café | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Calçados | Bens Não Essenciais | Vestuário e calçados | CORE | parcial/alta | ALTA | Escopo explícito do POM; complementar ao módulo POF Vestuário. |
| Carnes Preparadas (Defumadas/Salgadas) | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Carnes de Bovinos | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Carnes de Espécies Exóticas/Diversas e Subprodutos | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Carnes de Frango | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Carnes de Outras Aves (Exceto Frango) | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Carnes de Ovinos e Caprinos | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Carnes de Suínos | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Cereais e Grãos (exceto soja) | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Chás e Especiarias | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Combustíveis e Derivados de Petróleo | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Componentes Elétricos e Eletrônicos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Conservas de Frutas e Hortícolas | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Couros e Suas Obras | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Eletrodomésticos (Linha Branca + Portáteis) | Bens Não Essenciais | Eletrodomésticos | CORE | sim/alta | ALTA | Correspondência direta com o módulo POF Eletrodomésticos. |
| Eletrônicos de Consumo – Comunicação/Imagem | Bens Não Essenciais | Eletrônicos de consumo | EXPANDED | não direto | ALTA | Bens discricionários próximos ao escopo eletroeletrônico; não incluídos automaticamente na cesta POF atual. |
| Eletrônicos de Consumo – Informática/TIC | Bens Não Essenciais | Eletrônicos de consumo | EXPANDED | não direto | ALTA | Bens discricionários próximos ao escopo eletroeletrônico; não incluídos automaticamente na cesta POF atual. |
| Eletrônicos de Consumo – Áudio/Vídeo | Bens Não Essenciais | Eletrônicos de consumo | EXPANDED | não direto | ALTA | Bens discricionários próximos ao escopo eletroeletrônico; não incluídos automaticamente na cesta POF atual. |
| Embarcações e Estruturas Flutuantes | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Energia Elétrica | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Erva-mate | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Etanol e Álcool Etílico | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Explosivos e Pirotecnia | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Farinha, Malte e Preparações de Cereais | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Feltros, Passamanarias, Têxteis Técnicos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Ferramentas e Cutelaria (Metais Comuns) | Bens Não Essenciais | Utilidades domésticas / bens duráveis | ADJACENT | não | MÉDIA | Pode conter utilidades domésticas e itens industriais; NCM8 é necessário para evitar inclusão indevida. |
| Fibras Sintéticas/Descontínuas – Têxteis | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Filamentos Sintéticos – Têxteis Técnicos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Frutas e Hortícolas | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Instrumentos Musicais | Bens Não Essenciais | Discricionários / lazer / decoração | EXPANDED | não | MÉDIA | Bens discricionários coerentes com o conceito amplo do caderno, fora dos três módulos monetários atuais. |
| Instrumentos Médicos | Saúde/Higiene/Cuidados Pessoais | Artigos médicos/ortopédicos | EXPANDED | não | ALTA | O POM inclui artigos médicos e ortopédicos; módulo fora da DR POF atual. |
| Joias, Bijuterias, Metais Preciosos e Relógios | Bens Não Essenciais | Discricionários / lazer / decoração | EXPANDED | não | MÉDIA | Bens discricionários coerentes com o conceito amplo do caderno, fora dos três módulos monetários atuais. |
| Laticínios | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Madeira e Cortiça - Produtos e Obras | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Massas e Panificação | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Material Ferroviário e Contêineres | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Medicamentos | Saúde/Higiene/Cuidados Pessoais | Remédios/farmacêuticos | CORE | sim/alta | ALTA | Correspondência direta com o módulo de remédios e o escopo farmacêutico; auditar sobreposição entre grupos antes de somar. |
| Mel e Outros Produtos Comestíveis de Origem Animal | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Metais Não Ferrosos e Suas Obras (NCMs dos Caps. 74, 75, 78, 79, 80, 81) | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Minerais e Materiais de Mineração (Não Metálicos) | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Minérios e Subprodutos da Metalurgia (NCMs do Cap. 26) | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Mobiliário e Iluminação | Bens Não Essenciais | Móveis e decoração | CORE | sim/parcial | ALTA | Correspondência direta com móveis e próxima à arena de decoração. |
| Motocicletas | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Máquinas e Equipamentos Industriais | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Máquinas e Implementos Agrícolas | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Objetos de Arte e Coleções | Bens Não Essenciais | Discricionários / lazer / decoração | EXPANDED | não | MÉDIA | Bens discricionários coerentes com o conceito amplo do caderno, fora dos três módulos monetários atuais. |
| Obras de Espartaria e Cestaria | Bens Não Essenciais | Decoração e utilidades | EXPANDED | não | MÉDIA | Possível arena de decoração/utilidades; requer confirmação de escopo comercial local. |
| Obras de Ferro ou Aço | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Outras Fibras Têxteis Vegetais | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Outros | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Ovos | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Papel e Papelão | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Pasta Química e Pasta Mecânica | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Perfumaria e Cosméticos | Saúde/Higiene/Cuidados Pessoais | Higiene, beleza e cosméticos | CORE | sim/parcial | ALTA | Escopo explícito do POM e próximo ao módulo POF Higiene e Cuidados Pessoais. |
| Pescados e Frutos do Mar | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Pescados e Frutos do Mar - Preparações e Conservas | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Peças e Acessórios Automotivos | Serviços | Oficinas — bens complementares | ADJACENT | não | MÉDIA | Relacionados a oficinas do caderno de Serviços, mas são mercadorias; não substituem NFS-e da prestação. |
| Plantas Vivas e Floricultura | Bens Não Essenciais | Decoração e utilidades | EXPANDED | não | MÉDIA | Possível arena de decoração/utilidades; requer confirmação de escopo comercial local. |
| Plásticos e Suas Obras | Bens Não Essenciais | Utilidades domésticas / bens duráveis | ADJACENT | não | MÉDIA | Pode conter utilidades domésticas e itens industriais; NCM8 é necessário para evitar inclusão indevida. |
| Pneumáticos, Câmaras e Protetores | Serviços | Oficinas — bens complementares | ADJACENT | não | MÉDIA | Relacionados a oficinas do caderno de Serviços, mas são mercadorias; não substituem NFS-e da prestação. |
| Preparações Alimentícias Diversas (Molhos, Condimentos, etc) | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Preparações de Carne | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Preparações, Suplementos e Complementos alimentares | Saúde/Higiene/Cuidados Pessoais | Suplementação | EXPANDED | não direto | ALTA | Escopo explícito da pesquisa POM, fora da cesta-núcleo POF Higiene + Remédios. |
| Produtos Cerâmicos, Porcelana e Refratários | Bens Não Essenciais | Utilidades domésticas / bens duráveis | ADJACENT | não | MÉDIA | Pode conter utilidades domésticas e itens industriais; NCM8 é necessário para evitar inclusão indevida. |
| Produtos Editoriais, Impressos e Materiais Gráficos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Produtos Farmacêuticos | Saúde/Higiene/Cuidados Pessoais | Remédios/farmacêuticos | CORE | sim/alta | ALTA | Correspondência direta com o módulo de remédios e o escopo farmacêutico; auditar sobreposição entre grupos antes de somar. |
| Produtos Fotográficos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Produtos Minerais: Pedra, Cimento, Gesso, Amianto e Abrasivos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Produtos Químicos Diversos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Produtos de Origem Animal (Não Alimentares) | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Químicos Inorgânicos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Químicos Orgânicos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Resíduos para Alimentação Animal | Bens Não Essenciais | Pet/agro — fronteira de escopo | REVIEW | não | BAIXA | Contexto pet/agro aparece no POM, mas grupos são amplos e misturam consumo final e insumo produtivo; não incluir sem NCM e uso final. |
| Sabões e Preparações de Limpeza, Ceras e Pastas | Bens Essenciais | Limpeza doméstica | ADJACENT | não no núcleo atual | ALTA | O POM inclui limpeza, mas o benchmark monetário atual está restrito à alimentação no domicílio para evitar sobreposição. |
| Siderurgia – Ferro e Aço | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Soja, Oleaginosas e Sementes | Bens Essenciais | Alimentação/bebidas — perímetro ampliado | ADJACENT | parcial | MÉDIA | Relacionado ao mix alimentar, mas não entra automaticamente no núcleo monetário canônico sem validar correspondência POF e uso final. |
| Sucos e Bebidas à Base de Frutas/Vegetais | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Tabaco e Sucedâneos | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Tecidos Impregnados/Revestidos/Laminados | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Tecidos Sintéticos (Inclusive Malhas) | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Tintas, Pigmentos e Corantes | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Toucinho e Gorduras Não Fundidas | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Tratores | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Têxteis Naturais (Algodão, Lã, Seda e Afins) | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Vacinas e Soros | Saúde/Higiene/Cuidados Pessoais | Imunobiológicos | ADJACENT | não | BAIXA | Relacionado à saúde, mas não representa varejo privado típico; pode envolver fornecimento institucional e serviços. |
| Vestuário Tecido (Plano) | Bens Não Essenciais | Vestuário | CORE | sim/alta | ALTA | Correspondência direta com POF Vestuário e escopo POM. |
| Vestuário de Malha | Bens Não Essenciais | Vestuário | CORE | sim/alta | ALTA | Correspondência direta com POF Vestuário e escopo POM. |
| Veículos Comerciais (Caminhões e Carga) e Ônibus | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Veículos Leves e de Passageiros | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Vidro e Suas Obras | Bens Não Essenciais | Utilidades domésticas / bens duráveis | ADJACENT | não | MÉDIA | Pode conter utilidades domésticas e itens industriais; NCM8 é necessário para evitar inclusão indevida. |
| Óleos Brutos de Petróleo | Fora do perímetro prioritário | — | EXCLUDE | não | BAIXA | Grupo fora dos mercados de consumo priorizados ou predominantemente insumo/capital fora do escopo corrente. |
| Óleos e Gorduras Vegetais/animais | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | Compatível com o núcleo alimentar comprado para consumo no domicílio; NCM separa produto do CNAE do emissor. |
| Óptica, Instrumentos e Aparelhos de Precisão | Saúde/Higiene/Cuidados Pessoais | Óptica / artigos de saúde | REVIEW | não | MÉDIA | O POM inclui óticas, mas o grupo Radar é mais amplo; requer filtragem NCM. |

## 6. Decisões por setor

### Bens Essenciais
Priorizar grupos alimentares CORE. Limpeza e categorias limítrofes ficam separadas para não inflar o benchmark canônico de alimentação no domicílio.

### Saúde/Higiene
Priorizar Medicamentos, Produtos Farmacêuticos, Perfumaria e Cosméticos, Suplementos, Instrumentos Médicos e NCMs selecionados de Óptica. A coexistência de “Medicamentos” e “Produtos Farmacêuticos” exige auditoria de NCM8 antes de qualquer soma.

### Bens Não Essenciais
Primeiro núcleo: Vestuário de malha, Vestuário tecido, Calçados, Mobiliário e Iluminação e Eletrodomésticos. Segunda camada: eletrônicos, decoração, acessórios e lazer. Pet/agro fica em revisão.

### Serviços
NCM é complementar para operações mistas. O denominador principal continua NFS-e/CFS-e por item de serviço.

### Alimentação Fora do Lar
Não dimensionar AFL pela soma de NCMs alimentares vendidos no município. O primeiro recorte fiscal adequado continua CNAE 56/transação do estabelecimento.

## 7. Especificação recomendada

Solicitar:

`ano-mês × município emissor (4318002) × modelo NFC-e × NCM8/NCM4 × valor × quantidade × nº contribuintes da célula × indicador de supressão`.

Se a Receita puder fornecer `grupo_afinidade_final` do Radar, ele pode ser incluído como dimensão derivada. Caso contrário, o SBMI fará o crosswalk localmente a partir de NCM.

## 8. Catálogo NCM8 completo

A primeira consulta detalhada atingiu o limite público de **10.000 linhas** e cobriu **92 dos 110 grupos de afinidade**.

Para eliminar a truncagem sem alterar o modelo público, foi criada uma segunda extração reprodutível:

1. consulta independente do domínio completo de grupos;
2. identificação dos **18 grupos ausentes** na janela inicial;
3. consulta individual de cada grupo ausente;
4. recomposição e deduplicação por `grupo_afinidade_final × NCM8 × descrição`.

Resultado final auditado:

- grupos de afinidade: **110**;
- linhas NCM8/grupo: **11.765**;
- grupos ausentes após recomposição: **0**;
- NCM8 inválidos após normalização: **0**.

Natureza: **CATÁLOGO TAXONÔMICO OBSERVADO NO MODELO PÚBLICO DO RADAR**.

Esse catálogo não contém faturamento municipal e não transforma valores estaduais em valores de São Borja. Sua utilidade é fornecer uma taxonomia íntegra para:

- especificar pedidos de `São Borja × NCM × valor`;
- filtrar grupos amplos por NCM8 quando necessário;
- auditar sobreposição entre grupos como Medicamentos e Produtos Farmacêuticos;
- construir módulos de produto coerentes com os cadernos.

## 9. Rastreabilidade

### Extração inicial e domínio de grupos

Workflow: `.github/workflows/radar-mercado-ncm-taxonomy-v1.yml`

Execução validada:
- run: `36266655049`;
- commit: `3d2b1606b7d9c1b436c94f2ae167d1c3ea6778e1`;
- artifact: `10913519416`;
- digest: `sha256:0361697f8094b0408bca759dc584536c4ed3940186d501beee3baa52e50eec11`.

Google Drive:
- `SBMI_Radar_Mercado_taxonomia_NCM_v001.zip`;
- ID: `1QA5tVqZvUKXVPTuzbcIEzbK2UtF5t4x1`.

### Catálogo completo

Workflow: `.github/workflows/radar-mercado-ncm-taxonomy-complete-v1.yml`

Execução:
- run: `36267773156`;
- commit: `ae8282d8c47f770f0dabc01b638e1029da8d2edd`;
- artifact: `10914542081`;
- digest: `sha256:ace7428be2e1b4cdc8c47f8a41eef63da11094b066feaf8a578fa7b158f1d5e3`.

Google Drive:
- `SBMI_Radar_Mercado_taxonomia_NCM_completa_v001.zip`;
- ID: `1hXk6FCqM4nf3gMwPD5mm-UEoyXfsitlz`.

## 10. Decisão

O universo taxonômico NCM8 do Radar utilizado pelo SBMI está **canonizado para esta etapa**: 110 grupos e 11.765 associações grupo × NCM8.

Isso **não desbloqueia market share por si só**. A próxima fronteira empírica continua sendo obter valores agregados de São Borja por CNAE/NCM.

Nenhum CNPJ, loja, vínculo, remuneração ou participação regional será usado para ratear o envelope municipal.

O catálogo completo passa a ser a base preferencial para desenhar:
- o pedido `São Borja × NCM × valor` à Receita Estadual;
- filtros NCM8 para grupos classificados como REVIEW/ADJACENT;
- checagens de sobreposição entre módulos.
