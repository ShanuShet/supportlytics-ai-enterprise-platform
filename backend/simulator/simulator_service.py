from backend.simulator.traffic_engine import TrafficEngine


class SimulatorService:

    def __init__(self):

        self.engine = TrafficEngine()

    def start(self, count=50):

        tickets = self.engine.start(count)

        return {

            "status": "running",

            "generated_tickets": len(tickets),

            "tickets": tickets

        }

    def stop(self):

        self.engine.stop()

        return {

            "status": "stopped"

        }