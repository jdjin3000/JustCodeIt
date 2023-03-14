class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort() # for the smallest lexical order
        answer = []

        def dfs(current_state, remained_tickets):
            if len(answer) == len(tickets) + 1:
                return
            
            answer.append(current_state)

            for ticket in remained_tickets:
                departure, arrival = ticket

                if departure == current_state:
                    next_ticket = remained_tickets[:]
                    next_ticket.remove(ticket)

                    dfs(arrival, next_ticket)

                    if len(answer) != len(tickets) + 1:
                        answer.pop()
        
        dfs("JFK", tickets)

        return answer