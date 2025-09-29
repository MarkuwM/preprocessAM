import pandas as pd

#credit-data
credit_df = pd.read_csv("credit-data.csv")

#As colunas income, age e loan estavam em formato incorreto (strings com pontos extras), foram convertidas para valores numéricos válidos (float)
for col in ["income", "age", "loan"]:
    credit_df[col] = credit_df[col].astype(str).str.replace(".", "", regex=False).astype(float)

#Todos os NA foram substituídos pela média da respectiva coluna 
credit_df.fillna(credit_df.mean(numeric_only=True), inplace=True)

credit_df.to_csv("credit-data-tratado.csv", index=False)

#census
census_df = pd.read_csv("census.csv")

#O dataset utilizava " ?" para indicar ausência de valor. Estes foram convertidos para NA
census_df.replace(" ?", pd.NA, inplace=True)

for col in census_df.columns:
    if census_df[col].dtype == "object":
      #Para atributos categóricos, foram preenchidos com a moda
        census_df[col].fillna(census_df[col].mode()[0], inplace=True)
    else:
      #Para atributos numéricos, foram preenchidos com a mediana
        census_df[col].fillna(census_df[col].median(), inplace=True)

census_df.to_csv("census-tratado.csv", index=False)

print("Arquivos tratados salvos com sucesso!")
