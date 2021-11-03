# 👽 CIA Factbook API Docs

### Available Options

```
/country
/country/{country_name}
/field
/field/{field_name}
```

### `/country`
##### Usage: [https://cia-factbook.herokuapp.com/country](https://cia-factbook.herokuapp.com/country)
##### Returns:
```
[
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua-and-Barbuda",
    "Egypt",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    ...
    "United-States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vietnam",
    "West-Bank",
    "Mauritania",
    "Zambia",
    "Zimbabwe"
]
```

### `country/{country_name}`
##### Usage: [https://cia-factbook.herokuapp.com/country/Azerbaijan](https://cia-factbook.herokuapp.com/country/Azerbaijan)
##### Returns:
```
{
    "country_comparison_infant_mortality_rate": 21.3,
    "crude_oil_production": 798000.0,
    "exports": 15150000000.0,
    "broadband_fixed_subscriptions": 1890913.0,
    "budget_surplus_deficit": -1.6,
    "carbon_dioxide_emissions_from_consumption_of_energy": 35600000.0,
    "country_comparison_airports": 23.0,
    "country_comparison_area": 86600.0,
    "country_comparison_birth_rate": 14.5,
    "country_comparison_children_under_the_age_of_5_years_underweight": 4.9,
    ...
    "country_comparison_roadways": 24981.0,
    "country_comparison_total_fertility_rate": 1.88,
    "country_comparison_unemployment_youth_ages_15_24": 13.4,
    "country_comparison_waterways": "NAN",
    "crude_oil_exports": 718800.0,
    "crude_oil_imports": 0.0
}
```

### `/field`
##### Usage: [https://cia-factbook.herokuapp.com/field](https://cia-factbook.herokuapp.com/field)
##### Returns:
```
[
    "country_comparison_infant_mortality_rate",
    "crude_oil_production",
    "exports",
    "broadband_fixed_subscriptions",
    "budget_surplus_deficit",
    "carbon_dioxide_emissions_from_consumption_of_energy",
    "country_comparison_airports",
    "country_comparison_area",
    "country_comparison_birth_rate",
    "country_comparison_children_under_the_age_of_5_years_underweight",
    ...
    "country_comparison_roadways",
    "country_comparison_total_fertility_rate",
    "country_comparison_unemployment_youth_ages_15_24",
    "country_comparison_waterways",
    "crude_oil_exports",
    "crude_oil_imports"
]
```

### `/field/exports`
##### Usage: [https://cia-factbook.herokuapp.com/field/exports](https://cia-factbook.herokuapp.com/field/exports)
##### Returns:
```
{
    "Afghanistan": 784000000.0,
    "Albania": "NAN",
    "Algeria": 900700000.0,
    "Andorra": 34370000000.0,
    "Angola": 428000000.0,
    "Antigua-and-Barbuda": 78710000.0,
    "Egypt": 33070000000.0,
    "Argentina": 7900000.0,
    "Armenia": "NAN",
    "Australia": 86700000.0,
    "Austria": 82985000000.0,
    "Azerbaijan": 2361000000.0,
    ...
    "Uruguay": 27500000.0,
    "Uzbekistan": 3827000000.0,
    "Vanuatu": 15600000.0,
    "Vietnam": 221100000000.0,
    "West-Bank": 2362000000.0,
    "Zambia": 564800000.0,
    "Zimbabwe": 1085000000.0
}
```

### License
MIT