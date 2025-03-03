Aqui mostro quais textos serão utilizados nos commits do Git e qual sua finalidade.

Textos de referência:
1. https://www.conventionalcommits.org/en/v1.0.0/
2. https://medium.com/linkapi-solutions/conventional-commits-pattern-3778d1a1e657
3. https://github.com/iuricode/padroes-de-commits
4. https://dev.to/renatoadorno/padroes-de-commits-commit-patterns-41co

| Texto | Finalidade | Exemplo |
| ----- | ---------- | ------- |
| file | Atualização  documental que não tem haver diretamente com o código | file: acrescentado o arquivo docs\desing_patter_commits.md |
| feat | Criação de um novo componente ou recursos no código | feat: criado histograma do numero de vendas no vendas.py e vendas.ipynb |
| fix | Um bug que estava acontecendo e consegui resolver | fix: integração do streamlit com o plotly_express no vendas.py |
| doc | Criação da documentação do código. Pode ser concatenada com qualquer outro texto utilizado no commit. | feat doc: arquivo src\visualisation\dashboard_vendedores.py |
| refactor | Reestruturação do código para melhorar seu entendimento | refactor: código do mapa de restaurantes com melhor entendimento. |
| style | Alterações que não afetam o significado do código, provavelmente relacionadas à formatação do código, como espaço em branco, falta de ponto e vírgula e assim por diante | style: limpeza no arquivo src\app\app_init.py |
| update | Atualiza um componente ou recurso existente para melhorar algo nele | update: dashboard dos atendentes conforme v5.3.0 |
| remove | remove arquivos seja de qualquer natureza | remove doc: src\visualisation\dashboard_vendedores.py |