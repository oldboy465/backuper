<div align="center">

<!-- Banner Animado em SVG / CSS Puro -->
<svg width="100%" height="220" viewBox="0 0 800 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="50%" stop-color="#161b22" />
      <stop offset="100%" stop-color="#0d1117" />
    </linearGradient>
    
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#818cf8" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <style>
      .glow-title {
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
        font-weight: 800;
        font-size: 42px;
        fill: url(#accentGrad);
        letter-spacing: 2px;
      }
      .subtitle {
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
        font-size: 14px;
        fill: #8b949e;
        letter-spacing: 1px;
      }
      .node-pulse {
        animation: pulse 2.5s infinite ease-in-out;
      }
      .stream-particle {
        animation: flowParticle 3s infinite linear;
      }
      .particle-delayed {
        animation: flowParticle 3s infinite linear;
        animation-delay: 1.5s;
      }
      .box-hover {
        animation: floatBox 3.5s infinite ease-in-out;
      }
      @keyframes flowParticle {
        0% { transform: translateX(0); opacity: 0; }
        15% { opacity: 1; }
        85% { opacity: 1; }
        100% { transform: translateX(260px); opacity: 0; }
      }
      @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.08); opacity: 1; filter: drop-shadow(0 0 10px #38bdf8); }
      }
      @keyframes floatBox {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-8px); }
      }
    </style>
  </defs>

  <!-- Background Card -->
  <rect width="800" height="220" rx="16" fill="url(#bgGrad)" stroke="#30363d" stroke-width="1.5" />

  <!-- Título e Subtítulo -->
  <text x="400" y="55" text-anchor="middle" class="glow-title">⚡ BACKUPER ⚡</text>
  <text x="400" y="82" text-anchor="middle" class="subtitle">AUTOMATED GUI DIRECTORY ARCHIVER & ORGANIZER</text>

  <!-- Animação do Fluxo de Arquivos para Pasta de Backup -->
  <g transform="translate(140, 110)">
    <!-- Origem (Arquivos Soltos) -->
    <g class="box-hover">
      <rect x="0" y="10" width="130" height="65" rx="10" fill="#21262d" stroke="#38bdf8" stroke-width="1.5" />
      <text x="65" y="38" text-anchor="middle" fill="#f0f6fc" font-size="12" font-weight="600" font-family="sans-serif">Root Folder</text>
      <text x="65" y="56" text-anchor="middle" fill="#7ee787" font-size="11" font-family="monospace">*.pdf, *.txt...</text>
    </g>

    <!-- Linha de Fluxo -->
    <line x1="140" y1="42" x2="380" y2="42" stroke="#30363d" stroke-width="3" stroke-dasharray="6,6" />

    <!-- Partículas em Movimento (Arquivos sendo transferidos) -->
    <g transform="translate(140, 42)">
      <circle class="stream-particle" cx="0" cy="0" r="5" fill="#38bdf8" filter="url(#glow)" />
      <circle class="particle-delayed" cx="0" cy="0" r="5" fill="#c084fc" filter="url(#glow)" />
    </g>

    <!-- Destino (Pasta de Backup Datada) -->
    <g transform="translate(390, 0)" class="box-hover" style="animation-delay: -1.75s;">
      <rect x="0" y="10" width="150" height="65" rx="10" fill="#1f242c" stroke="#818cf8" stroke-width="2" />
      <rect x="15" y="0" width="50" height="15" rx="4" fill="#818cf8" />
      <text x="75" y="38" text-anchor="middle" fill="#f0f6fc" font-size="12" font-weight="700" font-family="sans-serif">backup DD-MM-YYYY</text>
      <text x="75" y="56" text-anchor="middle" fill="#a5d6ff" font-size="10" font-family="monospace">[safe & isolated]</text>
    </g>
  </g>
</svg>

<br/>

<!-- Badges Estilizadas -->
[![Python Version](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-blueviolet?style=for-the-badge&logo=linux&logoColor=white)](#)
[![Interface](https://img.shields.io/badge/GUI-Tkinter%20Native-00e676?style=for-the-badge)](#)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Lib-orange?style=for-the-badge)](#)
[![GitHub license](https://img.shields.io/github/license/oldboy465/backuper?style=for-the-badge)](LICENSE)

<br/>

**Organize e isole arquivos instantaneamente com um seletor visual nativo e rotulagem cronológica automática.**

</div>

---

## 🌊 Visão Geral

O **Backuper** é um utilitário ultraleve em Python projetado para resolver a desordem em pastas de trabalho, diretórios de downloads e repositórios locais. 

Ao rodar o script:
1. Uma **janela nativa do sistema** é exibida para seleção da pasta desejada.
2. O sistema gera automaticamente uma subpasta carimbada no formato: `backup dd-mm-yyyy`.
3. Todos os arquivos soltos do diretório são **movidos atomicamente** para dentro da nova pasta, mantendo subpastas intactas e protegendo a integridade dos seus dados.

---

## 🎬 Como Funciona (Motion Workflow)
