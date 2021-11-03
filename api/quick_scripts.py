import pandas as pd

df = pd.read_csv("./cia-factbook.csv")

# for i in df.columns[1:]:
#     print(f"{float(df[df['country'] == 'Azerbaijan'][f'{i}'])}")
#

# country = "Azerbaijan"

# res = {i: float(df[df['country'] == f'{country}'][f'{i}']) for i in df.columns[1:]}

# res = {}
#
# for i in df.columns[1:]:
#     column_value = float(df[df['country'] == f'{country}'][f'{i}'])
#
#     if pd.isnull(column_value):
#         res[i] = "NAN"
#     else:
#         res[i] = column_value
#
# print(type(res['country_comparison_waterways']))


print([i for i in df.columns[1:]])






# field = "exports"
# a = ["NAN" if pd.isnull(i) else i for i in df[f"{field}"]]
# b = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua-and-Barbuda', 'Egypt', 'Argentina',
#      'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
#      'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia-and-Herzegovina', 'Botswana', 'Brazil', 'Brunei',
#      'Bulgaria', 'Burkina-Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cabo-Verde',
#      'Central-African-Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo-Republic-of-the',
#      'Costa-Rica', "Cote-d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Korea-North',
#      'Congo-Democratic-Republic-of-the', 'Denmark', 'Djibouti', 'Dominica', 'Dominican-Republic', 'Ecuador',
#      'El-Salvador', 'Equatorial-Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia',
#      'Micronesia-Federated-States-of', 'Fiji', 'Finland', 'France', 'Gabon', 'Georgia', 'Germany', 'Ghana',
#      'Greece', 'Greenland', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
#      'Hong-Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Iran', 'Israel', 'Italy',
#      'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos',
#      'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau',
#      'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall-Islands', 'Mauritania',
#      'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Burma',
#      'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New-Zealand', 'Nicaragua', 'Niger', 'Nigeria',
#      'North-Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua-New-Guinea', 'Paraguay', 'Peru',
#      'Philippines', 'Poland', 'Portugal', 'Qatar', 'Venezuela', 'Korea-South', 'Yemen', 'Romania', 'Russia',
#      'Rwanda', 'Saint-Kitts-and-Nevis', 'Saint-Lucia', 'Saint-Vincent-and-the-Grenadines', 'Samoa',
#      'San-Marino', 'Sao-Tome-and-Principe', 'Saudi-Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra-Leone',
#      'Singapore', 'Slovakia', 'Slovenia', 'Solomon-Islands', 'Somalia', 'South-Africa', 'South-Sudan', 'Spain',
#      'Sri-Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania',
#      'Thailand', 'Bahamas-The', 'Gambia-The', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad-and-Tobago', 'Tunisia',
#      'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United-Arab-Emirates', 'United-Kingdom',
#      'United-States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vietnam', 'West-Bank', 'Mauritania', 'Zambia',
#      'Zimbabwe']
#
# print(dict(zip(a, b)))
