from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
)

OUTPUT = "notebook_specs.pdf"

# Colors
DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#0f3460")
LIGHT_BG = HexColor("#f0f0f5")
WHITE = HexColor("#ffffff")
GRAY = HexColor("#666666")

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    topMargin=40,
    bottomMargin=40,
    leftMargin=50,
    rightMargin=50,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "DocTitle", parent=styles["Title"],
    fontSize=26, textColor=DARK, spaceAfter=4, alignment=TA_CENTER,
)
subtitle_style = ParagraphStyle(
    "DocSubtitle", parent=styles["Normal"],
    fontSize=11, textColor=GRAY, alignment=TA_CENTER, spaceAfter=16,
)
section_style = ParagraphStyle(
    "Section", parent=styles["Heading2"],
    fontSize=14, textColor=ACCENT, spaceBefore=18, spaceAfter=8,
)
normal_style = ParagraphStyle(
    "Body", parent=styles["Normal"],
    fontSize=10, leading=14, textColor=DARK,
)
label_style = ParagraphStyle(
    "Label", parent=styles["Normal"],
    fontSize=10, leading=14, textColor=DARK, fontName="Helvetica-Bold",
)
value_style = ParagraphStyle(
    "Value", parent=styles["Normal"],
    fontSize=10, leading=14, textColor=HexColor("#333333"),
)

def make_table(data):
    rows = []
    for label, value in data:
        rows.append([
            Paragraph(label, label_style),
            Paragraph(value, value_style),
        ])
    t = Table(rows, colWidths=[150, 310])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, HexColor("#dddddd")),
        ("BACKGROUND", (0, 0), (-1, -1), WHITE),
    ]))
    return t

def hr():
    return HRFlowable(width="100%", thickness=1, color=HexColor("#cccccc"),
                       spaceAfter=6, spaceBefore=6)

story = []

# Header
story.append(Spacer(1, 10))
story.append(Paragraph("ASUS N46VM", title_style))
story.append(Paragraph("Especificacoes de Hardware e Software para Engenharia de Software", subtitle_style))
story.append(Paragraph("Gerado em 17/02/2026", subtitle_style))
story.append(hr())

# System
story.append(Paragraph("Sistema Operacional", section_style))
story.append(make_table([
    ("Distribuicao", "Linux Mint 22.3"),
    ("Kernel", "6.17.0-14-generic"),
    ("Arquitetura", "x86_64 (64-bit)"),
    ("Hostname", "alexandre-N46VM"),
    ("Fabricante", "ASUSTeK COMPUTER INC."),
    ("Modelo", "N46VM"),
    ("Firmware", "N46VM.404 (08/2012)"),
]))

# CPU
story.append(Paragraph("Processador (CPU)", section_style))
story.append(make_table([
    ("Modelo", "Intel Core i7-3610QM @ 2.30 GHz"),
    ("Geracao", "3a Geracao (Ivy Bridge)"),
    ("Nucleos / Threads", "4 nucleos / 8 threads"),
    ("Frequencia Max.", "3.30 GHz (Turbo Boost)"),
    ("Cache L2", "1 MiB (4 instancias)"),
    ("Cache L3", "6 MiB"),
    ("Virtualizacao", "Intel VT-x (suportada)"),
    ("Instrucoes", "SSE 4.1, SSE 4.2, AVX, AES-NI"),
]))

# RAM
story.append(Paragraph("Memoria RAM", section_style))
story.append(make_table([
    ("Total", "7.6 GiB (~8 GB)"),
    ("Swap", "2.0 GiB"),
    ("Observacao", "Suficiente para dev web e mobile; limitado para Docker pesado ou VMs simultaneas"),
]))

# Storage
story.append(Paragraph("Armazenamento", section_style))
story.append(make_table([
    ("Disco", "Samsung ST1000LM024 HN-M101MBB"),
    ("Tipo", "HDD (disco mecanico)"),
    ("Capacidade", "931.5 GB (~1 TB)"),
    ("Recomendacao", "Upgrade para SSD SATA melhora drasticamente tempos de build e IDE"),
]))

# GPU
story.append(Paragraph("Placa de Video (GPU)", section_style))
story.append(make_table([
    ("GPU Integrada", "Intel HD Graphics 4000 (3a Gen)"),
    ("GPU Dedicada", "NVIDIA GeForce GT 630M"),
    ("Configuracao", "Optimus (hibrido Intel + NVIDIA)"),
]))

# Display
story.append(Paragraph("Display e Saidas de Video", section_style))
story.append(make_table([
    ("Tela", '14" 1366x768 (HD) - LVDS'),
    ("Saida Externa", "VGA-1 (disponivel)"),
]))

# Network
story.append(Paragraph("Rede", section_style))
story.append(make_table([
    ("Wi-Fi", "Qualcomm Atheros AR9485"),
    ("Ethernet", "Porta RJ-45 integrada"),
    ("Status Wi-Fi", "Conectado (sinal: 70/100)"),
]))

# Battery
story.append(Paragraph("Bateria", section_style))
story.append(make_table([
    ("Fabricante", "ASUSTeK"),
    ("Tecnologia", "Litio-Ion (Li-ion)"),
    ("Capacidade Original", "57.2 Wh"),
    ("Capacidade Atual", "22.9 Wh (40.1% de saude)"),
    ("Estado", "Carregando (89%)"),
    ("Observacao", "Bateria degradada; recomenda-se uso na tomada para sessoes longas"),
]))

# Dev Tools
story.append(Paragraph("Ferramentas de Desenvolvimento", section_style))
story.append(make_table([
    ("Python", "3.12.3"),
    ("Node.js", "18.19.1"),
    ("Git", "2.43.0"),
    ("Java (OpenJDK)", "17.0.18"),
    ("GCC", "13.3.0"),
    ("Claude Code", "Instalado e funcional"),
]))

# Evaluation
story.append(Paragraph("Avaliacao para Engenharia de Software", section_style))
story.append(Spacer(1, 4))

eval_items = [
    "<b>Pontos Fortes:</b> CPU i7 quad-core com HT, 8 GB RAM, bom ecossistema de ferramentas instalado, Linux Mint estavel e leve.",
    "<b>Limitacoes:</b> HDD mecanico (gargalo principal), 8 GB RAM pode limitar containers Docker, bateria degradada, tela HD 768p.",
    "<b>Recomendacoes de Upgrade:</b> (1) SSD SATA de 240/480 GB - maior impacto; (2) Segundo modulo RAM para 16 GB se o slot estiver livre; (3) Bateria nova se precisar de mobilidade.",
    "<b>Ideal Para:</b> Desenvolvimento web (frontend/backend), scripts Python, APIs REST, projetos Java/Spring, Git workflows.",
    "<b>Limitado Para:</b> Builds Android Studio pesados, multiplos containers Docker, machine learning com datasets grandes.",
]
for item in eval_items:
    story.append(Paragraph(item, normal_style))
    story.append(Spacer(1, 6))

doc.build(story)
print(f"PDF criado: {OUTPUT}")
