class ScenarioGenerator:

    @staticmethod
    def office_morning():

        return {

            "scenario": "Office Morning Rush",

            "tickets_per_minute": 20

        }

    @staticmethod
    def vpn_outage():

        return {

            "scenario": "VPN Gateway Failure",

            "tickets_per_minute": 100

        }

    @staticmethod
    def phishing_attack():

        return {

            "scenario": "Security Incident",

            "tickets_per_minute": 50

        }