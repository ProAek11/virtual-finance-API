"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_yf_profile_calendar": {
        "url": "quote/{ticker}",
        "response": {
            "Value": {
                "Earnings Date": 1618790400000,
                "Earnings Average": 1.63,
                "Earnings Low": 1.39,
                "Earnings High": 1.82,
                "Revenue Average": 17377200000,
                "Revenue Low": 17108000000,
                "Revenue High": 17607300000,
            }
        },
    },
    "_yf_profile_recommendations": {
        "url": "quote/{ticker}",
        "response": {
            "Firm": {
                "1578917505000": "Evercore ISI Group",
                "1579261087000": "Morgan Stanley",
                "1579698302000": "Citigroup",
                "1579701598000": "Cantor Fitzgerald",
                "1579703271000": "Morgan Stanley",
                "1580755983000": "Edward Jones",
                "1584973665000": "Nomura",
                "1585163241000": "Morgan Stanley",
                "1586872308000": "Wells Fargo",
                "1586953551000": "Credit Suisse",
                "1586959964000": "Stifel",
                "1587472015000": "Morgan Stanley",
                "1587479348000": "Wedbush",
                "1587481869000": "UBS",
                "1587572973000": "Citigroup",
                "1595337378000": "Credit Suisse",
                "1595337540000": "Morgan Stanley",
                "1595423859000": "Argus Research",
                "1602245772000": "Morgan Stanley",
                "1603210621000": "BMO Capital",
            },
            "To Grade": {
                "1578917505000": "In-Line",
                "1579261087000": "Equal-Weight",
                "1579698302000": "Neutral",
                "1579701598000": "Neutral",
                "1579703271000": "Equal-Weight",
                "1580755983000": "Buy",
                "1584973665000": "Buy",
                "1585163241000": "Equal-Weight",
                "1586872308000": "Equal-Weight",
                "1586953551000": "Outperform",
                "1586959964000": "Buy",
                "1587472015000": "Equal-Weight",
                "1587479348000": "Neutral",
                "1587481869000": "Neutral",
                "1587572973000": "Neutral",
                "1595337378000": "Outperform",
                "1595337540000": "Equal-Weight",
                "1595423859000": "Buy",
                "1602245772000": "Equal-Weight",
                "1603210621000": "Market Perform",
            },
            "From Grade": {
                "1578917505000": "Outperform",
                "1579261087000": "Overweight",
                "1579698302000": "",
                "1579701598000": "",
                "1579703271000": "",
                "1580755983000": "Hold",
                "1584973665000": "",
                "1585163241000": "",
                "1586872308000": "",
                "1586953551000": "",
                "1586959964000": "",
                "1587472015000": "",
                "1587479348000": "",
                "1587481869000": "",
                "1587572973000": "",
                "1595337378000": "",
                "1595337540000": "",
                "1595423859000": "Hold",
                "1602245772000": "",
                "1603210621000": "",
            },
            "Action": {
                "1578917505000": "down",
                "1579261087000": "down",
                "1579698302000": "main",
                "1579701598000": "main",
                "1579703271000": "main",
                "1580755983000": "up",
                "1584973665000": "main",
                "1585163241000": "main",
                "1586872308000": "main",
                "1586953551000": "main",
                "1586959964000": "main",
                "1587472015000": "main",
                "1587479348000": "main",
                "1587481869000": "main",
                "1587572973000": "main",
                "1595337378000": "main",
                "1595337540000": "main",
                "1595423859000": "up",
                "1602245772000": "main",
                "1603210621000": "main",
            },
        },
    },
    "_yf_profile_sustainability": {
        "url": "quote/{ticker}",
        "response": {
            "Value": {
                "palmOil": False,
                "controversialWeapons": False,
                "gambling": False,
                "socialScore": 10.08,
                "nuclear": False,
                "furLeather": False,
                "alcoholic": False,
                "gmo": False,
                "catholic": False,
                "socialPercentile": None,
                "peerCount": 103,
                "governanceScore": 7.39,
                "environmentPercentile": None,
                "animalTesting": False,
                "tobacco": False,
                "totalEsg": 17.88,
                "highestControversy": 2,
                "esgPerformance": "UNDER_PERF",
                "coal": False,
                "pesticides": False,
                "adult": False,
                "percentile": 14.92,
                "peerGroup": "Software & Services",
                "smallArms": False,
                "environmentScore": 0.41,
                "governancePercentile": None,
                "militaryContract": False,
            }
        },
    },
    "_yf_profile_info": {
        "url": "quote/{ticker}",
        "response": {
            "zip": "10504",
            "sector": "Technology",
            "fullTimeEmployees": 345900,
            "city": "Armonk",
            "phone": "914 499 1900",
            "state": "NY",
            "country": "United States",
            "companyOfficers": [],
            "website": "http://www.ibm.com",
            "maxAge": 1,
            "address1": "One New Orchard Road",
            "industry": "Information Technology Services",
            "previousClose": 128.9,
            "regularMarketOpen": 128.5,
            "twoHundredDayAverage": 122.19059,
            "trailingAnnualDividendYield": 0.05050427,
            "payoutRatio": 1.0619999,
            "volume24Hr": None,
            "regularMarketDayHigh": 130.715,
            "navPrice": None,
            "averageDailyVolume10Day": 5328433,
            "totalAssets": None,
            "regularMarketPreviousClose": 128.9,
            "fiftyDayAverage": 122.95,
            "trailingAnnualDividendRate": 6.51,
            "open": 128.5,
            "toCurrency": None,
        },
    },
    "_yf_holders_major": {
        "url": "quote/{ticker}/holders",
        "response": {
            "0": {"0": "0.13%", "1": "58.58%", "2": "58.66%", "3": "2561"},
            "1": {
                "0": "% of Shares Held by All Insider",
                "1": "% of Shares Held by Institutions",
                "2": "% of Float Held by Institutions",
                "3": "Number of Institutions Holding Shares",
            },
        },
    },
    "_yf_holders_mutualfund": {"url": "quote/{ticker}/holders", "response": {}},
    "_yf_holders_institutional": {"url": "quote/{ticker}/holders", "response": {}},
    "_yf_financials_earnings": {
        "url": "quote/{ticker}/financials",
        "response": {
            "yearly": {
                "Revenue": {
                    "2017": 79139000000,
                    "2018": 79591000000,
                    "2019": 77147000000,
                    "2020": 73621000000,
                },
                "Earnings": {
                    "2017": 5753000000,
                    "2018": 8728000000,
                    "2019": 9431000000,
                    "2020": 5590000000,
                },
            },
            "quarterly": {
                "Revenue": {
                    "1Q2020": 17571000000,
                    "2Q2020": 18121000000,
                    "3Q2020": 17561000000,
                    "4Q2020": 20368000000,
                },
                "Earnings": {
                    "1Q2020": 1175000000,
                    "2Q2020": 1361000000,
                    "3Q2020": 1698000000,
                    "4Q2020": 1356000000,
                },
            },
        },
    },
    "_yf_financials_balancesheet": {"url": "quote/{ticker}/financials", "response": {}},
    "_yf_financials_cashflow": {"url": "quote/{ticker}/financials", "response": {}},
    "_yf_financials_financials": {"url": "quote/{ticker}/financials", "response": {}},
    "_yf_options_options": {
        "url": "v7/finance/options{ticker}",
        "response": (
            "2021-03-26",
            "2021-04-01",
            "2021-04-09",
            "2021-04-16",
            "2021-04-23",
            "2021-04-30",
            "2021-05-21",
            "2021-06-18",
            "2021-07-16",
            "2021-09-17",
            "2021-10-15",
            "2022-01-21",
            "2023-01-20",
        ),
    },
    "_yf_options_optionchain": {"url": "v7/finance/options{ticker}", "response": {}},
    "_yf_history_IBM": {
        "url": "v8/finance/chart{ticker}",
        "params": {"range": "max", "interval": "1d", "events": "div,splits"},
        "response": {},
    },
}
