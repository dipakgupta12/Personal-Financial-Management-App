from rest_framework import views
from rest_framework.response import Response


class MonthlyExpensesView(views.APIView):

    def post(self, request, format=None):
        transaction_list = []
        transaction_dict = {}

        # Get all historical transactions.
        transactions = self.request.data["transactions"]
        total_recurrent_expenses = 0

        # Append all transaction['details'] to list.
        for transaction in transactions:
            transaction_data = {
                transaction["details"]: {
                    "afterAmount": transaction["afterAmount"],
                    "beforeAmount": transaction["beforeAmount"],
                    "amount": transaction["amount"],
                    "currency": transaction["currency"],
                    "description": transaction["description"],
                    "details": transaction["details"],
                    "type": transaction["type"],
                }
            }
            transaction_list.append(transaction_data)

        '''
        Filter transactions and count recurrent order
        and add to transaction_dict.
        '''
        for i in transaction_list:
            if transaction_list.count(i) > 1:
                for key in i:
                    if key not in transaction_dict:
                        total_recurrent_expenses += i[key][
                            "amount"
                        ] * transaction_list.count(i)
                        i[key].update(
                            {
                                "recurrent_count": transaction_list.count(i),
                                "recurrent_amount": i[key]["amount"] * transaction_list.count(i),
                            }
                        )
                        transaction_dict.update(i)

        # Return all recurrent transactions and total of recurret transactions.
        recurrent_expenses = {
            "Monthly Recurrent Transactions": transaction_dict.values(),
            "Monthly Fixed Recurrent Expenses": round(total_recurrent_expenses, 2),
        }
        return Response(recurrent_expenses)
