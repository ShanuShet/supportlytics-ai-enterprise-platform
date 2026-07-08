import time

from backend.simulator.ticket_generator import TicketGenerator


class TrafficEngine:

    def __init__(self):

        self.running = False

    def start(self, count=10):

        self.running = True

        generated = []

        for _ in range(count):

            if not self.running:
                break

            generated.append(

                TicketGenerator.generate()

            )

            time.sleep(0.2)

        return generated

    def stop(self):

        self.running = False