
# LP3 IFSP

Repositório para organizar os códigos da disciplina Linguagem de Programação 3..

## Intruções Lab de Informática

Ao chegar no laboratório:

Configurar o usuário local do git

```bash 
git config --global user.name "Seu nome"
git config --global user.email "seuemail@email.com"
```

Fazer o clone do se repositório no GitHub

```bash
git clone https://github.com/ca12loss/lp3-ifsp.git
```

Abrir a repo no VSCode 
```bash
code lp3-ifsp
```

Criar um token para realizar os pushs
Settings -> Developer Settings -> Personal access tokens -> Tokens (classic)
Generate new token, selecionar a opção Generate new token classic, marcar a opção scope repo

### Antes de sair do Laboratório 
1-Remover as configurações de usuário do git local
```bash
git config --global --unset user.name
git config --global --unset user.email
```

2-Deletar o token no GitHub

3-Deslogar do GitHub