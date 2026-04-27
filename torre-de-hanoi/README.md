# Torre de Hanói

Simulação interativa da Torre de Hanói com interface gráfica no navegador.

## Funcionalidades

- **2 a 8 discos** ajustáveis via slider
- **Resolução automática** com animação (algoritmo recursivo)
- **Passo a passo** — avança um movimento por vez
- **Modo manual** — clique e arraste os discos entre as hastes (funciona no celular também)
- Contador de movimentos e progresso em relação ao mínimo teórico (2ⁿ − 1)
- Responsivo para mobile

## Como usar

Abra o `index.html` no navegador — não precisa de servidor, build ou dependências.

## Publicar no GitHub Pages

1. Crie um repositório no GitHub
2. Faça upload do `index.html`
3. Vá em **Settings → Pages**
4. Em **Source**, selecione `main` e a pasta `/root`
5. Clique em **Save**

O link ficará disponível em:
```
https://<seu-usuario>.github.io/<nome-do-repositorio>/
```

## Algoritmo

A solução usa recursão clássica:

```
hanoi(n, origem, destino, auxiliar):
  se n == 1:
    mover disco de origem para destino
  senão:
    hanoi(n-1, origem, auxiliar, destino)
    mover disco de origem para destino
    hanoi(n-1, auxiliar, destino, origem)
```

O número mínimo de movimentos para `n` discos é sempre **2ⁿ − 1**.
