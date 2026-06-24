from qos.sli import calculate_sli

from qos.slo import SLO, evaluate_slo


class ReliabilityAnalyzer:


    def analyze(self, records):


        sli = calculate_sli(records)


        slo = SLO()


        evaluation = evaluate_slo(

            sli,

            slo

        )


        return {

            "sli": sli,

            "evaluation": evaluation

        }