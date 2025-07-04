#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Teste para verificar se o sistema consegue analisar múltiplas portarias corretamente
"""

from portaria_analyzer import PortariaAnalyzer

def testar_multiplas_portarias():
    """Testa a análise de múltiplas portarias"""
    
    # Texto com múltiplas portarias
    texto_completo = """PORTARIA, Nº 5.149, DE 24 DE JUNHO DE 2025
A COORDENADORA DE PROCESSOS MIGRATÓRIOS, no uso da competência delegada pela Portaria nº 623 de 13 de novembro de 2020, publicada no Diário Oficial da União, de 17 de novembro de 2020, RESOLVE:

CONCEDER a nacionalidade brasileira, por naturalização, às pessoas abaixo relacionadas, nos termos do art. 12, II, "a", da Constituição Federal de 1988, e em conformidade com o art. 65 da Lei nº 13.445, de 24 de maio de 2017, regulamentada pelo Decreto nº 9.199/2017, de 20 de novembro de 2020, a fim de que possam gozar dos direitos outorgados pela Constituição e leis do Brasil:
 
AKEEM AKINOLA APENA - V005786-X, natural da Nigéria, nascido(a) em 5 de maio de 1965, filho(a) de Raheem Apena e de Safurat Apena, residente no estado de São Paulo (Processo nº 235881.0499242/2024);
ALENA ASTAKHOVA - F811397-J, natural da Rússia, nascida em 19 de dezembro de 1992, filha de Yurii Ermolaev e de Svetlana Ermolaeva, residente no estado de São Paulo (Processo 235881.0519913/2024);

As pessoas referidas nesta Portaria deverão comparecer perante a Justiça Eleitoral para o devido cadastramento, nos termos do art. 231 do Decreto nº 9.199/2017, que regulamenta a Lei nº 13.445/2017.

SANDRA MARIA MENDES ADJAFRE SINDEAUX
Coordenadora de Processos Migratórios

DEPARTAMENTO DE MIGRAÇOES
PORTARIA, Nº 5.150, DE 24 DE JUNHO DE 2025

A COORDENADORA DE PROCESSOS MIGRATÓRIOS, no uso da competência delegada pela Portaria nº 623 de 13 de novembro de 2020, publicada no Diário Oficial da União, de 17 de novembro de 2020, RESOLVE:
 
CONCEDER a nacionalidade brasileira, por naturalização, às pessoas abaixo relacionadas, nos termos do art. 12, II, "b", da Constituição Federal de 1988, e em conformidade com o art. 67 da Lei nº 13.445, de 24 de maio de 2017, regulamentada pelo Decreto nº 9.199/2017, de 20 de novembro de 2020, a fim de que possam gozar dos direitos outorgados pela Constituição e leis do Brasil:
 
PABLO CESAR LEHMANN ALBORNOZ - V278540-V, natural da Colômbia, nascido em 28 de março de 1974, filho de Fabricio Lehmann Gonzalez e de Gloria Isabel Albornoz Montilla, residente no Estado do Rio Grande do Sul (Processo 235881.0570932/2024);

As pessoas referidas nesta Portaria deverão comparecer perante a Justiça Eleitoral para o devido cadastramento, nos termos do art. 231 do Decreto nº 9.199/2017, que regulamenta a Lei nº 13.445/2017.

SANDRA MARIA MENDES ADJAFRE SINDEAUX
Coordenadora de Processos Migratórios

DEPARTAMENTO DE MIGRAÇOES
PORTARIA, Nº 5.151, DE 24 DE JUNHO DE 2025

A COORDENADORA DE PROCESSOS MIGRATÓRIOS, no uso da competência delegada pela Portaria nº 623 de 13 de novembro de 2020, publicada no Diário Oficial da União, de 17 de novembro de 2020: RESOLVE:

CONCEDER a nacionalidade brasileira, por Naturalização Provisória, às pessoas abaixo relacionadas, nos termos do art. 12, inciso II, alínea "a", da Constituição Federal de 1988, e em conformidade com o art. 70 da Lei nº 13.445, de 24 de maio de 2017, regulamentada pelo Decreto nº 9.199/2017, de 20 de novembro de 2020, a fim de que possa gozar dos direitos outorgados pela Constituição e leis do Brasil, até 2 (dois) anos após atingir a maioridade, nos termos do Parágrafo único do referido artigo:
 
ARAMIDE NGOZI AKINTOLA - F988304-5, natural da Nigéria, nascida em 14 de julho de 2015, filha de Oluwadare Akintola e de Ijeoma Akintola, residente no estado de São Paulo (Processo 235881.0512924/2024);
ATAHUALPA ABRAHAM YAQUIRA - F742007-5, natural da Argentina, nascido em 20 de outubro de 2020, filho de Mariano Yaquira e de Maria Paola Joffre Rosales, residente no estado de Santa Catarina (Processo 235881.0566628/2024);

SANDRA MARIA MENDES ADJAFRE SINDEAUX
Coordenadora de Processos Migratórios"""

    print("="*60)
    print("🧪 TESTE DE MÚLTIPLAS PORTARIAS")
    print("="*60)
    
    # Inicializar analisador
    analyzer = PortariaAnalyzer()
    
    print("\n📋 Analisando texto com múltiplas portarias...")
    print(f"Tamanho do texto: {len(texto_completo)} caracteres")
    
    # Analisar múltiplas portarias
    resultados, arquivos_excel = analyzer.analisar_multiplas_portarias(texto_completo, gerar_excel=False)
    
    print(f"\n✅ Análise concluída!")
    print(f"📊 Total de portarias encontradas: {len(resultados)}")
    
    total_pessoas = 0
    total_erros = 0
    
    for i, resultado in enumerate(resultados, 1):
        dados = resultado['dados_portaria']
        erros = resultado['erros']
        
        print(f"\n--- PORTARIA {i} ---")
        print(f"Número: {dados['numero']}")
        print(f"Data: {dados['data']}")
        print(f"Tipo: {dados['tipo']}")
        print(f"Pessoas: {len(dados['pessoas'])}")
        print(f"Erros: {len(erros)}")
        
        total_pessoas += len(dados['pessoas'])
        total_erros += len(erros)
        
        # Mostrar algumas pessoas
        for j, pessoa in enumerate(dados['pessoas'][:3], 1):
            print(f"  {j}. {pessoa['nome']} - {pessoa['pais']}")
        
        if len(dados['pessoas']) > 3:
            print(f"  ... e mais {len(dados['pessoas']) - 3} pessoas")
    
    print(f"\n📈 RESUMO FINAL:")
    print(f"Total de portarias: {len(resultados)}")
    print(f"Total de pessoas: {total_pessoas}")
    print(f"Total de erros: {total_erros}")
    
    # Verificar se todas as portarias foram capturadas
    portarias_esperadas = ['5.149', '5.150', '5.151']
    portarias_encontradas = [r['dados_portaria']['numero'].replace('Nº ', '').replace('.', '') for r in resultados]
    
    print(f"\n🔍 VERIFICAÇÃO:")
    print(f"Portarias esperadas: {portarias_esperadas}")
    print(f"Portarias encontradas: {portarias_encontradas}")
    
    if len(resultados) == 3:
        print("✅ SUCESSO: Todas as 3 portarias foram capturadas!")
    else:
        print(f"❌ PROBLEMA: Esperava 3 portarias, mas encontrou {len(resultados)}")
    
    return resultados

if __name__ == "__main__":
    testar_multiplas_portarias() 