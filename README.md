# Juliana Rodrigues Ramos — landing page demonstrativa

Proposta de presença digital para a psicóloga Juliana Rodrigues Ramos, CRP 09/010877, inspirada na linguagem visual de HalanaMaranhaPsiLp. Site estático em HTML, CSS e JavaScript, sem dependências de build.

## Prévia e validação

- Prévia: `python3 -m http.server 4174 --bind 127.0.0.1`
- Verificação da estrutura: `python3 scripts/check_site.py`
- Sintaxe JavaScript: `node --check script.js`

Os arquivos usam caminhos relativos para funcionar no GitHub Pages em uma subpasta. O menu móvel fecha por link, clique externo ou Escape. A página usa links reais de WhatsApp, sem formulário de envio simulado. O aviso de conceito e a diretiva `noindex` devem ser revisados quando a profissional aprovar a publicação oficial.

## Git e publicação

Repositório novo em PlannoCorp. Base inicial para as branches: `main` → `deploy` → `homolog`, como no projeto anterior. Alterações em `homolog`, PR para `deploy`. O usuário faz o merge, salvo autorização específica para este PR. GitHub Pages publica a raiz de `deploy`, sem CNAME ou domínio da Halana.

## Pesquisa

As fontes e divergências identificadas estão em [docs/RESEARCH.md](docs/RESEARCH.md). A fotografia foi obtida do perfil público da profissional no Linktree e integrada sem alterar sua aparência; o enquadramento circular é feito com CSS.
