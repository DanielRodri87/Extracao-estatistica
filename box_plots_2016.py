import pandas as pd
import matplotlib.pyplot as plt

# Definir opção para exibir todas as colunas
pd.set_option('display.max_columns', None)

# Ler os arquivos de entrada especificando a codificação e ignorando linhas com problemas
caminho_plan1 = r'C:/Users/danie/OneDrive/Documentos/UFPI-2024.1/ESTATÍSTICA/PYTHON/BoxPlot-Trabalho/dados_2016.CSV'

# Função para filtrar os dados e calcular a soma das raças
def filtrar_e_calcular_somas(df, cursos_selecionados):
    df_filtrado = df[df['NO_CURSO'].isin(cursos_selecionados)]
    df_filtrado = df_filtrado[(df_filtrado['QT_ING_BRANCA'] > 0) & (df_filtrado['QT_ING_PRETA'] > 0) & 
                              (df_filtrado['QT_ING_PARDA'] > 0) & (df_filtrado['QT_ING_AMARELA'] > 0) & 
                              (df_filtrado['QT_ING_INDIGENA'] > 0)]
    df_filtrado['Soma_Racas'] = df_filtrado[['QT_ING_BRANCA', 'QT_ING_PRETA', 'QT_ING_PARDA', 
                                              'QT_ING_AMARELA', 'QT_ING_INDIGENA']].sum(axis=1)
    return df_filtrado

# Ler os dados para a área de Exatas
df_exatas = pd.read_csv(caminho_plan1, sep=';', encoding='latin-1')
cursos_selecionados_exatas = ['GESTÃO DE SISTEMAS DE INFORMAÇÃO', 'GESTÃO DA TECNOLOGIA DA INFORMAÇÃO', 
                               'GESTÃO FINANCEIRA', 'CIÊNCIAS CONTÁBEIS', 'ANÁLISE E DESENVOLVIMENTO DE SISTEMAS', 
                               'SISTEMAS PARA INTERNET', 'SISTEMAS DE INFORMAÇÃO']
df_exatas = filtrar_e_calcular_somas(df_exatas, cursos_selecionados_exatas)

# Ler os dados para a área de Humanas
df_humanas = pd.read_csv(caminho_plan1, sep=';', encoding='latin-1')
cursos_selecionados_humanas = ['ADMINISTRAÇÃO', 'GESTÃO DE RECURSOS HUMANOS', 'DIREITO', 'HISTÓRIA', 
                                'LETRAS - PORTUGUÊS', 'PEDAGOGIA', 'SERVIÇO SOCIAL']
df_humanas = filtrar_e_calcular_somas(df_humanas, cursos_selecionados_humanas)

# Ler os dados para a área de Saúde
df_saude = pd.read_csv(caminho_plan1, sep=';', encoding='latin-1')
cursos_selecionados_saude = ['ENFERMAGEM', 'MEDICINA', 'NUTRIÇÃO', 'PSICOLOGIA', 'FISIOTERAPIA', 
                             'GESTÃO DE SERVIÇOS DE SAÚDE', 'ODONTOLOGIA']
df_saude = filtrar_e_calcular_somas(df_saude, cursos_selecionados_saude)

# Preparar os dados para o boxplot
dados_exatas = [df_exatas['QT_ING_BRANCA'], df_exatas['QT_ING_PRETA'], df_exatas['QT_ING_PARDA'], 
                df_exatas['QT_ING_AMARELA'], df_exatas['QT_ING_INDIGENA']]
dados_humanas = [df_humanas['QT_ING_BRANCA'], df_humanas['QT_ING_PRETA'], df_humanas['QT_ING_PARDA'], 
                 df_humanas['QT_ING_AMARELA'], df_humanas['QT_ING_INDIGENA']]
dados_saude = [df_saude['QT_ING_BRANCA'], df_saude['QT_ING_PRETA'], df_saude['QT_ING_PARDA'], 
               df_saude['QT_ING_AMARELA'], df_saude['QT_ING_INDIGENA']]
labels = ['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena']

# Plotar os boxplots para Exatas
# Plotar os boxplots para Exatas
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.boxplot(dados_exatas, patch_artist=True, showfliers=False, labels=labels,
            medianprops=dict(color='black'))  # Definindo a cor da mediana como preta
plt.title('Exatas')
plt.ylabel('Quantidade de Alunos')
plt.ylim(0, 251)

# Plotar os boxplots para Humanas
plt.subplot(1, 3, 2)
plt.boxplot(dados_humanas, patch_artist=True, showfliers=False, labels=labels,
            medianprops=dict(color='black'))  # Definindo a cor da mediana como preta
plt.title('Humanas')
plt.ylabel('Quantidade de Alunos')
plt.ylim(0, 251)

# Plotar os boxplots para Saúde
plt.subplot(1, 3, 3)
plt.boxplot(dados_saude, patch_artist=True, showfliers=False, labels=labels,
            medianprops=dict(color='black'))  # Definindo a cor da mediana como preta
plt.title('Saúde')
plt.ylabel('Quantidade de Alunos')
plt.ylim(0, 251)

# Ajustar layout
plt.tight_layout()

# Exibir os boxplots
plt.show()



# Ajustar layout
plt.tight_layout()

# Exibir os boxplots
plt.show()
