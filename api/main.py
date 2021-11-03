import pandas as pd
from fastapi import FastAPI

app = FastAPI()

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua-and-Barbuda', 'Egypt', 'Argentina',
             'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
             'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia-and-Herzegovina', 'Botswana', 'Brazil', 'Brunei',
             'Bulgaria', 'Burkina-Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cabo-Verde',
             'Central-African-Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo-Republic-of-the',
             'Costa-Rica', "Cote-d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Korea-North',
             'Congo-Democratic-Republic-of-the', 'Denmark', 'Djibouti', 'Dominica', 'Dominican-Republic', 'Ecuador',
             'El-Salvador', 'Equatorial-Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia',
             'Micronesia-Federated-States-of', 'Fiji', 'Finland', 'France', 'Gabon', 'Georgia', 'Germany', 'Ghana',
             'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
             'Hong-Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Iran', 'Israel', 'Italy',
             'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos',
             'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau',
             'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall-Islands', 'Mauritania',
             'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Burma',
             'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New-Zealand', 'Nicaragua', 'Niger', 'Nigeria',
             'North-Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua-New-Guinea', 'Paraguay', 'Peru',
             'Philippines', 'Poland', 'Portugal', 'Qatar', 'Venezuela', 'Korea-South', 'Yemen', 'Romania', 'Russia',
             'Rwanda', 'Saint-Kitts-and-Nevis', 'Saint-Lucia', 'Saint-Vincent-and-the-Grenadines', 'Samoa',
             'San-Marino', 'Sao-Tome-and-Principe', 'Saudi-Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra-Leone',
             'Singapore', 'Slovakia', 'Slovenia', 'Solomon-Islands', 'Somalia', 'South-Africa', 'South-Sudan', 'Spain',
             'Sri-Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania',
             'Thailand', 'Bahamas-The', 'Gambia-The', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad-and-Tobago', 'Tunisia',
             'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United-Arab-Emirates', 'United-Kingdom',
             'United-States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vietnam', 'West-Bank', 'Mauritania', 'Zambia',
             'Zimbabwe']

fields = ['country_comparison_infant_mortality_rate', 'crude_oil_production', 'exports',
          'broadband_fixed_subscriptions', 'budget_surplus_deficit',
          'carbon_dioxide_emissions_from_consumption_of_energy', 'country_comparison_airports',
          'country_comparison_area', 'country_comparison_birth_rate',
          'country_comparison_children_under_the_age_of_5_years_underweight', 'country_comparison_death_rate',
          'country_comparison_education_expenditures', 'country_comparison_hiv_aids_adult_prevalence_rate',
          'country_comparison_hiv_aids_deaths', 'country_comparison_hiv_aids_people_living_with_hiv_aids',
          'gdp_per_capita', 'gdp_real_growth_rate', 'gross_national_saving', 'imports',
          'industrial_production_growth_rate', 'inflation_rate', 'internet_users', 'labor_force',
          'natural_gas_consumption', 'natural_gas_exports', 'natural_gas_imports', 'natural_gas_production',
          'natural_gas_proved_reserves', 'public_debt', 'refined_petroleum_products_consumption',
          'refined_petroleum_products_exports', 'refined_petroleum_products_imports',
          'refined_petroleum_products_production', 'reserves_of_foreign_exchange_and_gold', 'taxes_and_other_revenues',
          'telephones_fixed_lines', 'telephones_mobile_cellular', 'unemployment_rate', 'crude_oil_proved_reserves',
          'current_account_balance', 'debt_external', 'electricity_consumption', 'electricity_exports',
          'electricity_from_fossil_fuels', 'electricity_from_hydroelectric_plants', 'electricity_from_nuclear_fuels',
          'electricity_from_other_renewable_sources', 'electricity_imports',
          'electricity_installed_generating_capacity', 'electricity_production',
          'country_comparison_life_expectancy_at_birth', 'country_comparison_maternal_mortality_rate',
          'country_comparison_median_age', 'country_comparison_merchant_marine',
          'country_comparison_military_expenditures', 'country_comparison_net_migration_rate',
          'country_comparison_obesity_adult_prevalence_rate', 'country_comparison_population',
          'country_comparison_population_growth_rate', 'country_comparison_railways', 'country_comparison_roadways',
          'country_comparison_total_fertility_rate', 'country_comparison_unemployment_youth_ages_15_24',
          'country_comparison_waterways', 'crude_oil_exports', 'crude_oil_imports']

df = pd.read_csv("./cia-factbook.csv")


@app.get("/")
async def root():
    try:
        return {f"Made by @woosal1337"}

    except Exception as e:
        return {f"{e} has happened!"}


@app.get("/country")
async def all_countries():
    try:
        return countries

    except Exception as e:
        return {f"{e} has happened!"}


@app.get("/field")
async def all_fields():
    try:
        return fields

    except Exception as e:
        return {f"{e} has happened!"}


@app.get("/country/{country}")
async def read_item(country: str):
    try:

        if country not in countries:
            return {
                f"{country} is not in the list! Go to `/country' to find the full list of all the available countries!"}

        res = {}

        for i in df.columns[1:]:
            column_value = float(df[df['country'] == f'{country}'][f'{i}'])

            if pd.isnull(column_value):
                res[i] = "NAN"
            else:
                res[i] = column_value

        return res

    except Exception as e:
        return {f"{e} has happened!"}


@app.get("/field/{field}")
async def read_item(field: str):
    try:

        if field not in fields:
            return {
                f"{field} is not in the list! Go to `/field' to find the full list of all the available fields!"}

        a = ["NAN" if pd.isnull(i) else i for i in df[f"{field}"]]

        return dict(zip(countries, a))

    except Exception as e:
        return {f"{e} has happened!"}
