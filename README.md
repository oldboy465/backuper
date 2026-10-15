<div align="center">

# 📦 BACKUPER

### *Organização instantânea e isolamento cronológico de arquivos com GUI nativa*

<!-- Animação Motion Oficial de Backup & Sync de Dados -->
<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHIyb2s4ejBmcTRvMmQ1MnJleWpkaGNsbnYycHFkMmF1MWJ2ajBhNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oKIPnAiaMCws8nOsE/giphy.gif" width="480" alt="Backup Motion Animation" />

<br/>

<!-- Badges Dinâmicas -->
[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter%20Native-00e676?style=for-the-badge)](#)
[![OS](https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-blueviolet?style=for-the-badge&logo=linux&logoColor=white)](#)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20External-orange?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

<br/>

<!-- Efeito Digitação Animado -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=16&duration=2800&pause=1000&color=38BDF8&center=true&vCenter=true&width=550&lines=Selecione+uma+pasta+com+1+clique;Cria+subpasta+com+data+autom%C3%A1tica;Move+todos+os+arquivos+com+seguran%C3%A7a;Preserva+suas+subpastas+intactas!" alt="Typing SVG" />
</a>

</div>

---

## ⚡ Como Funciona

O **Backuper** foi criado para acabar com a bagunça em pastas de downloads, projetos ou diretórios de trabalho com apenas 1 clique:

1. **Interface Nativa**: Abre uma janela do seu sistema operacional (`Tkinter`) para você escolher a pasta.
2. **Carimbo de Data Automático**: Cria uma pasta no padrão `backup DD-MM-YYYY` no mesmo local.
3. **Isolamento Inteligente**: Move todos os arquivos soltos da raiz para a nova pasta de backup, sem tocar em subpastas já existentes.

---

## 🔄 Fluxo de Movimentação

```text
📁 Pasta Selecionada/
│
├── 📄 documento.pdf   ───┐
├── 📊 planilha.xlsx   ────┼──►  📁 backup 15-10-2026/
├── 🖼️ imagem.png      ───┘        ├── 📄 documento.pdf
│                                  ├── 📊 planilha.xlsx
└── 📁 projetos_antigos/           └── 🖼️ imagem.png
    └── (permanece intacta)
