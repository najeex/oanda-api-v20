"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""
responses = {
    "_v3_accounts_accountID_trades": {
        "url": "v3/accounts/{accountID}/trades",
        "params": {
            "instrument": "DE30_EUR,EUR_USD"
        },
        "response": {
            "trades": [
                {
                    "financing": "0.0000",
                    "openTime": "2016-10-28T14:28:05.231759081Z",
                    "price": "10678.3",
                    "unrealizedPL": "25.0000",
                    "realizedPL": "0.0000",
                    "instrument": "DE30_EUR",
                    "state": "OPEN",
                    "initialUnits": "10",
                    "currentUnits": "10",
                    "id": "2315"
                },
                {
                    "financing": "0.0000",
                    "openTime": "2016-10-28T14:27:19.011002322Z",
                    "price": "1.09448",
                    "unrealizedPL": "-0.0933",
                    "realizedPL": "0.0000",
                    "instrument": "EUR_USD",
                    "state": "OPEN",
                    "initialUnits": "100",
                    "currentUnits": "100",
                    "id": "2313"
                }
            ],
            "lastTransactionID": "2315"
        }
    },
    "_v3_accounts_accountID_opentrades": {
        "url": "v3/accounts/{accountID}/openTrades",
        "response": {
            "trades": [
                {
                    "financing": "0.0000",
                    "openTime": "2016-10-28T14:28:05.231759081Z",
                    "price": "10678.3",
                    "unrealizedPL": "136.0000",
                    "realizedPL": "0.0000",
                    "instrument": "DE30_EUR",
                    "state": "OPEN",
                    "initialUnits": "10",
                    "currentUnits": "10",
                    "id": "2315"
                }
            ],
            "lastTransactionID": "2317"
        }
    },
    "_v3_account_accountID_trades_details": {
        # tradeID 2315
        "url": "v3/accounts/{accountID}/trades/{tradeID}",
        "response": {
            "lastTransactionID": "2317",
            "trade": {
                "financing": "0.0000",
                "openTime": "2016-10-28T14:28:05.231759081Z",
                "price": "10678.3",
                "unrealizedPL": "226.0000",
                "realizedPL": "0.0000",
                "instrument": "DE30_EUR",
                "state": "OPEN",
                "initialUnits": "10",
                "currentUnits": "10",
                "id": "2315"
            }
        }
    }
}
