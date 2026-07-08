from collections import Counter


class TrendAnalysis:

    def __init__(self, tickets):

        self.tickets = tickets

    def category_distribution(self):

        categories = [

            t.get("category", "Unknown")

            for t in self.tickets

        ]

        return dict(Counter(categories))

    def priority_distribution(self):

        priorities = [

            t.get("priority", "Unknown")

            for t in self.tickets

        ]

        return dict(Counter(priorities))

    def country_distribution(self):

        countries = [

            t.get("country", "Unknown")

            for t in self.tickets

        ]

        return dict(Counter(countries))

    def daily_ticket_trend(self):

        daily = Counter()

        for ticket in self.tickets:

            created = ticket.get("created_at")

            if created:

                day = created[:10]

                daily[day] += 1

        return dict(daily)